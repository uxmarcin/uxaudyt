// Build: render stron do statycznego HTML (SSR) + bundle JS do hydracji
// Uruchom: node build.mjs   → wynik w public/
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const esbuild = require(process.env.ESBUILD || 'esbuild');
const { renderToString } = await import('react-dom/server');
const { jsx } = await import('react/jsx-runtime');

const ROOT = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.join(ROOT, 'public');
const SITE = 'https://www.uxaudyt.pl';
const props = JSON.parse(fs.readFileSync(path.join(ROOT, 'src/props.json'), 'utf8'));
const meta = JSON.parse(fs.readFileSync(path.join(ROOT, 'src/meta.json'), 'utf8'));
const { pages } = await import('./src/pages.mjs');

// 1) bundle klienta
const kinds = [...new Set(pages.map((p) => p.kind))];
const res = await esbuild.build({
  entryPoints: Object.fromEntries(kinds.map((k) => [k, path.join(ROOT, `src/apps/${k}.client.mjs`)])),
  bundle: true, minify: true, format: 'esm', splitting: true, target: ['es2020'],
  outdir: path.join(OUT, 'js'), entryNames: '[name]-[hash]', chunkNames: 'c-[hash]',
  define: { 'process.env.NODE_ENV': '"production"' }, legalComments: 'none', metafile: true,
  nodePaths: [path.join(ROOT, 'node_modules')],
  // W przeglądarce Preact zamiast Reacta (ten sam kod, ~20x mniejszy)
  alias: process.env.NO_PREACT ? {} : {
    'react/jsx-runtime': 'preact/jsx-runtime', 'react-dom/client': 'preact/compat/client',
    'react-dom': 'preact/compat', react: 'preact/compat',
  },
});
for (const f of fs.readdirSync(path.join(OUT, 'js'))) {
  const full = path.join(OUT, 'js', f);
  if (!Object.keys(res.metafile.outputs).some((o) => path.resolve(o) === full)) fs.unlinkSync(full);
}
const entryFile = Object.fromEntries(Object.entries(res.metafile.outputs)
  .filter(([, o]) => o.entryPoint).map(([f, o]) => [path.basename(o.entryPoint).replace('.client.mjs', ''), '/js/' + path.basename(f)]));

// 2) render HTML
const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
const css = fs.readFileSync(path.join(ROOT, 'src/base.css'), 'utf8').replace(/\s*\n\s*/g, '');
const apps = {};
for (const k of kinds) apps[k] = (await import(`./src/apps/${k}.mjs`)).default;

for (const p of pages) {
  const m = meta[p.key] || {};
  const pr = { ...p.props };
  const html = renderToString(jsx(apps[p.kind], pr));
  const title = p.title || m.title;
  const desc = p.description ?? m.description;
  const url = SITE + p.path;
  const img = SITE + (m.og_image || '/img/L7tYwRG1Z2LDw2rf7ooJXDB5gU.png');
  const doc = `<!doctype html>
<html lang="pl" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
${desc ? `<meta name="description" content="${esc(desc)}">\n` : ''}<link rel="canonical" href="${url}">
<meta name="robots" content="${p.noindex ? 'noindex' : 'max-image-preview:large'}">
<meta property="og:type" content="website">
<meta property="og:url" content="${url}">
<meta property="og:title" content="${esc(title)}">
${desc ? `<meta property="og:description" content="${esc(desc)}">\n` : ''}<meta property="og:image" content="${img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(title)}">
${desc ? `<meta name="twitter:description" content="${esc(desc)}">\n` : ''}<meta name="twitter:image" content="${img}">
<link rel="icon" href="/img/lxp74g8xQ3bEUK1mzOApyn7OfL4.png">
<link rel="apple-touch-icon" href="/img/asygCqAesPc10LtTCSyR5UEIJE.png">
<link rel="preload" href="/fonts/fr/_Xmz-HUzqDCFdgfMsYiV_F7wfS-Bs_d_QF5bwkEU4HTy.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts/fonts.css">
<style>${css}</style>
<link rel="modulepreload" href="${entryFile[p.kind]}">
</head>
<body class="k-${p.kind}">
<div id="app">${html}</div>
<script type="application/json" id="ux-props">${JSON.stringify(pr).replace(/</g, '\\u003c')}</script>
<script type="module" src="${entryFile[p.kind]}"></script>
</body>
</html>
`;
  const file = p.path === '/' ? 'index.html' : p.path.slice(1) + '.html';
  fs.writeFileSync(path.join(OUT, file), doc);
  console.log('✓', p.path.padEnd(30), (doc.length / 1024).toFixed(0) + ' KB');
}

fs.copyFileSync(path.join(ROOT, 'src/404.html'), path.join(OUT, '404.html'));

// 3) sitemap
const today = new Date().toISOString().slice(0, 10);
fs.writeFileSync(path.join(OUT, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.filter((p) => !p.noindex && p.sitemap !== false).map((p) => `  <url><loc>${SITE}${p.path}</loc><lastmod>${today}</lastmod></url>`).join('\n')}
</urlset>
`);
for (const [f, o] of Object.entries(res.metafile.outputs)) console.log('  js', path.basename(f), (o.bytes / 1024).toFixed(0) + ' KB');
