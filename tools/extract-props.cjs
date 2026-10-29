// Jednorazowe: wyciąga propsy komponentów z plików stron Framera (uxsrc/pages/*.js)
const fs = require('fs'), path = require('path');
const acorn = require('/opt/node-tools/node_modules/acorn');
const walk = require('/opt/npm-tools/node_modules/acorn-walk');
const dir = process.argv[2], out = {};
const val = (n) => {
  if (n.type === 'Literal') return n.value;
  if (n.type === 'TemplateLiteral' && n.expressions.length === 0) return n.quasis.map(q => q.value.cooked).join('');
  if (n.type === 'UnaryExpression' && n.operator === '!' && n.argument.type === 'Literal') return !n.argument.value;
  if (n.type === 'UnaryExpression' && n.operator === '-' && n.argument.type === 'Literal') return -n.argument.value;
  return undefined;
};
const kinds = { page: 'main', showChecklist: 'footer', hoverFx: 'fx', gaId: 'cookie', payLinkA: 'checkout', ctaTitle: 'raport' };
for (const f of fs.readdirSync(dir)) {
  const src = fs.readFileSync(path.join(dir, f), 'utf8');
  let ast; try { ast = acorn.parse(src, { ecmaVersion: 'latest', sourceType: 'module' }); } catch (e) { console.error(f, e.message); continue; }
  const res = {};
  walk.simple(ast, { ObjectExpression(o) {
    const keys = o.properties.filter(p => p.key).map(p => p.key.name || p.key.value);
    let kind = Object.keys(kinds).find(k => keys.includes(k)) ? kinds[Object.keys(kinds).find(k => keys.includes(k))] : null;
    if (!kind && keys.includes('endpoint') && keys.includes('id') && keys.length <= 6) kind = 'sheet';
    if (!kind && keys.includes('doc')) kind = 'legal';
    if (!kind && keys.includes('kind') && keys.includes('id')) kind = 'legal';
    if (!kind) return;
    const obj = {};
    for (const p of o.properties) { if (!p.key) continue; const k = p.key.name || p.key.value; const v = val(p.value); if (v !== undefined && !['id','height','width','layoutId'].includes(k)) obj[k] = v; }
    if (Object.keys(obj).length) (res[kind] = res[kind] || []).push(obj);
  }});
  out[f.replace('.js', '')] = res;
}
fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
for (const [p, r] of Object.entries(out)) console.log(p, Object.fromEntries(Object.entries(r).map(([k, v]) => [k, v.length])));
