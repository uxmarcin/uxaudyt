/* Ekipaż – aplikacja (vanilla JS, bez zależności)
 * Widoki routowane hashem: #/  #/z/ID  #/dodaj  #/ekipy  #/e/ID  #/ranking  #/ja  #/g/ID  #/start  #/odzyskaj  #/plan  #/zasady
 * Dane użytkownika wstawiane wyłącznie przez textContent (h()). */
(() => {
'use strict';

/* ------------------------------------------------------------ słowniki */
const API = 'api.php';
const ACT = {
  heist:    { l: 'Napady',          i: '💰', d: 'Przygotówki i finały' },
  contact:  { l: 'Misje',           i: '📞', d: 'Kontakty i zlecenia' },
  race:     { l: 'Wyścigi',         i: '🏁', d: 'Tor, ulica, rajdy' },
  business: { l: 'Biznes i grind',  i: '📦', d: 'Dostawy, sprzedaż' },
  freeroam: { l: 'Free roam',       i: '🌴', d: 'Luźne jeżdżenie' },
  pvp:      { l: 'PvP',             i: '🎯', d: 'Deathmatche, tryby' },
  rp:       { l: 'Roleplay',        i: '🎭', d: 'Klimat i fabuła' },
  cars:     { l: 'Auta i zloty',    i: '🚗', d: 'Tuning, meety, zdjęcia' },
};
const ACT_GEN = { heist: 'napadu', contact: 'misji', race: 'wyścigów', business: 'grindu biznesu', freeroam: 'free roamu', pvp: 'PvP', rp: 'roleplayu', cars: 'zlotu aut' };
const TIMES = { morning: 'Rano', afternoon: 'Popołudnie', evening: 'Wieczór', night: 'Noc' };
const TIME_I = { morning: '☕', afternoon: '🌤️', evening: '🌆', night: '🌙' };
const STYLES = { chill: 'Na luzie', balanced: 'Rzetelnie', tryhard: 'Na wynik' };
const STYLE_D = { chill: 'Bez spiny, śmiech na czacie', balanced: 'Gramy porządnie, ale bez krzyku', tryhard: 'Elite, rekordy, zero błędów' };
const PLAT = { ps5: 'PS5', xbox: 'XSX', pc: 'PC' };
const PLAT_L = { ps5: 'PlayStation 5', xbox: 'Xbox Series', pc: 'PC' };
const PLAT_CLS = { ps5: 'ps', xbox: 'xbox', pc: 'pc' };
const AVATARS = ['#D81B6A', '#3B82F6', '#D97706', '#7C3AED', '#059669', '#DC2626', '#4F46E5', '#64748B', '#EA580C', '#0D9488', '#65A30D', '#C026D3'];
const CREW_COLORS = ['#2A2A36', '#D81B6A', '#D97706', '#7C3AED', '#059669', '#DC2626'];
const FEATURES = [
  { id: 'map',        t: 'Interaktywna mapa',       d: 'Mapa Leonidy z miejscówkami, sklepami i znajdźkami – gdy tylko świat zostanie rozpracowany.' },
  { id: 'checklist',  t: 'Lista postępu na 100%',   d: 'Odhaczasz zadania i znajdźki, a postęp trzyma się Twojego profilu.' },
  { id: 'guides',     t: 'Poradniki po polsku',      d: 'Krótkie, konkretne przejścia napadów i sposoby na kasę – bez lania wody.' },
  { id: 'photo',      t: 'Konkurs na zdjęcia',       d: 'Cotygodniowy temat, głosowanie społeczności i nagrody od partnerów.' },
  { id: 'events',     t: 'Wydarzenia ekip',          d: 'Zloty, turnieje wyścigowe i wspólne noce napadów z zapisami.' },
  { id: 'discordbot', t: 'Bot na Discorda',          d: 'Nowe zlecenia prosto na kanał Twojego serwera, z przyciskiem „Wchodzę”.' },
];
/* Przykładowe zlecenia – szablony pokazywane, gdy tablica jest prawie pusta. Nie są prawdziwymi ogłoszeniami. */
const SAMPLES = [
  { activity: 'heist', title: 'Finał napadu – brakuje 2 osób', platform: 'ps5', slots: 4, inMin: 20, style: 'balanced', mic: true, details: 'Przygotówki zrobione, wchodzimy prosto w finał. Podział po równo.' },
  { activity: 'race', title: 'Nocne wyścigi uliczne', platform: 'ps5', slots: 6, inMin: 90, style: 'chill', mic: false, details: 'Czyste jazdy, bez taranowania. Kto wygra, wybiera kolejną trasę.' },
  { activity: 'business', title: 'Sprzedaż towaru – potrzebna obstawa', platform: 'xbox', slots: 3, inMin: 45, style: 'balanced', mic: true, details: 'Trzy dostawy przez miasto. Ty jedziesz, ja pilnuję tyłów.' },
  { activity: 'heist', title: 'Przygotówki od zera, spokojnie', platform: 'pc', slots: 4, inMin: 180, style: 'chill', mic: false, details: 'Dla nowych w napadach – wszystko tłumaczę po drodze.' },
  { activity: 'cars', title: 'Zlot aut na parkingu przy plaży', platform: 'ps5', slots: 8, inMin: 240, style: 'chill', mic: false, details: 'Przyjeżdżajcie czystymi furami, robimy zdjęcia o zachodzie.' },
  { activity: 'pvp', title: 'Deathmatch drużynowy na wieczór', platform: 'pc', slots: 8, inMin: 120, style: 'tryhard', mic: true, details: 'Dwie drużyny po czterech, gramy do trzech wygranych.' },
];
function useSample(x) {
  S.draft = { title: x.title, activity: x.activity, platform: (S.me && S.me.platform) || x.platform, slots: x.slots, when: x.inMin <= 120 ? [5, 15, 30, 60, 120].reduce((a, b) => Math.abs(b - x.inMin) < Math.abs(a - x.inMin) ? b : a) : 120, style: x.style, mic: x.mic, details: x.details };
  location.hash = '#/dodaj';
}
function sampleCard(x, i) {
  const a = ACT[x.activity];
  const job = { slots: x.slots, taken: 1 };
  const startAt = now() + x.inMin * 60;
  return h('article', { class: 'ek-job ek-job--sample ek-rise', '--i': i, role: 'button', tabindex: '0', 'aria-label': 'Przykład: ' + x.title + '. Kliknij, żeby wystawić podobne zlecenie.', onclick: () => useSample(x), onkeydown: e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); useSample(x); } } },
    h('span', { class: 'ek-sticker ek-sticker--teal ek-job__mine' }, 'Przykład'),
    h('div', { class: 'ek-job__head' }, h('div', null, h('div', { class: 'ek-job__activity' }, a.i + ' ' + a.l), h('h3', { class: 'ek-job__title' }, x.title))),
    h('div', { class: 'ek-job__host' }, avatar({ nick: 'Ty', avatar: (S.me && S.me.avatar) || 0 }, 'sm', false), h('b', null, S.me ? S.me.nick : 'Twój nick'), h('span', { class: 'ek-meta' }, '· gospodarz')),
    h('div', { class: 'ek-job__meta' }, platTag(x.platform), h('span', { class: 'ek-badge' }, STYLES[x.style]), x.mic ? h('span', { class: 'ek-badge ek-badge--mic' }, '🎙 Mikrofon') : null),
    h('p', { class: 'ek-job__note' }, x.details),
    h('div', { class: 'ek-job__foot' }, slots(job), h('span', { class: 'ek-cd-wrap' }, h('span', { class: 'ek-countdown__label' }, 'Start za'), h('span', { class: 'ek-countdown' }, x.inMin < 60 ? x.inMin + ' min' : Math.round(x.inMin / 60) + ' h')),
      h('span', { class: 'ek-btn ek-btn--secondary ek-btn--sm' }, 'Wystaw podobne')));
}
function samplesSection(list) {
  const f = S.filters;
  let items = SAMPLES.filter(x => (!f.platform || x.platform === f.platform) && (!f.activity || x.activity === f.activity));
  if (!items.length) items = SAMPLES;
  return h('section', { class: 'ek-samples' },
    h('div', { class: 'ek-samples__head' }, h('h3', { class: 'ek-h3' }, list.length ? 'Brakuje czegoś? Wystaw podobne' : 'Tak wyglądają zlecenia'),
      h('p', { class: 'ek-meta' }, 'To przykłady, nie prawdziwe ogłoszenia. Kliknij kartę, a formularz wypełni się sam – zmienisz tylko to, co chcesz.')),
    h('div', { class: 'ek-grid' }, items.slice(0, list.length ? 3 : 6).map(sampleCard)));
}
const REPORT_REASONS = { spam: 'Spam lub reklama', scam: 'Oszustwo / wyłudzenie', toxic: 'Toksyczne zachowanie', cheats: 'Cheaty, modmenu, handel kontami', other: 'Coś innego' };

/* ------------------------------------------------------------ stan */
function store() {}
store.get = k => { try { return localStorage.getItem(k); } catch (e) { return null; } };
store.set = (k, v) => { try { v == null ? localStorage.removeItem(k) : localStorage.setItem(k, v); } catch (e) {} };

const S = {
  token: store.get('ek_token'),
  me: null, meData: null,
  stats: null, jobs: [], jobsLoaded: false, offline: false,
  filters: { platform: store.get('ek_f_platform') || '', activity: '', when: '', style: '', open: false },
  lbPeriod: 'week', lbPlatform: '', lbTab: 'players',
  meTab: 'inbox', draft: null,
};

/* ------------------------------------------------------------ narzędzia */

function h(tag, attrs, ...kids) {
  const el = document.createElement(tag);
  if (attrs) for (const [k, v] of Object.entries(attrs)) {
    if (v == null || v === false) continue;
    if (k === 'class') el.className = v;
    else if (k === 'style' && typeof v === 'object') Object.assign(el.style, v);
    else if (k.startsWith('on') && typeof v === 'function') el.addEventListener(k.slice(2), v);
    else if (k === 'dataset') Object.assign(el.dataset, v);
    else if (k.startsWith('--')) el.style.setProperty(k, v);
    else el.setAttribute(k, v === true ? '' : v);
  }
  for (const c of kids.flat(Infinity)) {
    if (c == null || c === false) continue;
    el.append(c instanceof Node ? c : document.createTextNode(String(c)));
  }
  return el;
}
const svgNS = 'http://www.w3.org/2000/svg';
function icon(name, size = 18) {
  const P = {
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    share: '<path d="M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7M16 6l-4-4-4 4M12 2v14"/>',
    flag: '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
    mic: '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    check: '<path d="M5 12l5 5L20 7"/>',
    x: '<path d="M6 6l12 12M18 6L6 18"/>',
    copy: '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a1 1 0 0 1 1-1h10"/>',
    arrow: '<path d="M15 18l-6-6 6-6"/>',
    lock: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    radio: '<path d="M4 10h16v10H4zM8 10l9-6"/><circle cx="9" cy="15" r="2"/><path d="M14 14h3M14 17h3"/>',
    pin: '<path d="M12 21s-6-5.3-6-11a6 6 0 0 1 12 0c0 5.7-6 11-6 11z"/><circle cx="12" cy="10" r="2.2"/>',
    star: '<path d="M12 2.8l2.8 6 6.6.6-5 4.4 1.5 6.5L12 17l-5.9 3.3 1.5-6.5-5-4.4 6.6-.6z"/>',
    discord: '<path d="M8 8c2.6-1 5.4-1 8 0M7.5 16c2.8 1.2 6.2 1.2 9 0M6 7.5C4.6 10 4 12.7 4.2 15.6 5.6 17 7 17.8 8.5 18.3l1-1.8M18 7.5c1.4 2.5 2 5.2 1.8 8.1-1.4 1.4-2.8 2.2-4.3 2.7l-1-1.8"/><circle cx="9.5" cy="12.5" r="1"/><circle cx="14.5" cy="12.5" r="1"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    logout: '<path d="M15 4h4a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-4M10 16l-4-4 4-4M6 12h10"/>',
  };
  const s = document.createElementNS(svgNS, 'svg');
  s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('width', size); s.setAttribute('height', size);
  s.setAttribute('fill', 'none'); s.setAttribute('stroke', 'currentColor'); s.setAttribute('stroke-width', '2');
  s.setAttribute('stroke-linecap', 'round'); s.setAttribute('stroke-linejoin', 'round'); s.setAttribute('aria-hidden', 'true');
  s.innerHTML = P[name] || '';
  return s;
}
const $ = (sel, root = document) => root.querySelector(sel);
const now = () => Math.floor(Date.now() / 1000);
const pad = n => String(n).padStart(2, '0');
function hhmm(ts) { const d = new Date(ts * 1000); return pad(d.getHours()) + ':' + pad(d.getMinutes()); }
function dayLabel(ts) {
  const d = new Date(ts * 1000), t = new Date();
  const diff = Math.round((new Date(d.toDateString()) - new Date(t.toDateString())) / 86400000);
  if (diff === 0) return 'dziś';
  if (diff === 1) return 'jutro';
  if (diff === -1) return 'wczoraj';
  return d.toLocaleDateString('pl-PL', { weekday: 'short', day: 'numeric', month: 'short' });
}
function ago(ts) {
  const s = Math.max(1, now() - ts);
  if (s < 60) return 'przed chwilą';
  const m = Math.round(s / 60); if (m < 60) return m + ' min temu';
  const hh = Math.round(m / 60); if (hh < 24) return hh + ' godz. temu';
  const d = Math.round(hh / 24); return d === 1 ? 'wczoraj' : d + ' dni temu';
}
function countdown(ts) {
  const s = ts - now();
  if (s <= 0) { const m = Math.floor(-s / 60); return { t: m < 1 ? 'TERAZ' : 'TRWA ' + m + ' MIN', cls: 'is-started', label: 'Wystartowało' }; }
  const hh = Math.floor(s / 3600), mm = Math.floor((s % 3600) / 60), ss = s % 60;
  if (s > 86400) return { t: dayLabel(ts).toUpperCase() + ' ' + hhmm(ts), cls: '', label: 'Start' };
  return { t: (hh ? pad(hh) + ':' : '') + pad(mm) + ':' + pad(ss), cls: s < 1800 ? 'is-urgent' : '', label: 'Start za' };
}
function plural(n, one, few, many) { const n10 = n % 10, n100 = n % 100; return n === 1 ? one : (n10 >= 2 && n10 <= 4 && (n100 < 12 || n100 > 14)) ? few : many; }
function initials(nick) { const p = String(nick || '?').replace(/[_\-.]/g, ' ').trim().split(/\s+/); return ((p[0] || '?')[0] + (p[1] ? p[1][0] : (p[0][1] || ''))).toUpperCase(); }

function avatar(p, size = '', status = true) {
  const a = h('span', { class: 'ek-avatar' + (size ? ' ek-avatar--' + size : ''), style: { background: AVATARS[(p && p.avatar) || 0] }, 'aria-hidden': 'true' }, initials(p && p.nick));
  if (status && p && p.online) a.append(h('span', { class: 'ek-avatar__status is-online' }));
  return a;
}
function wanted(stars, size = 'sm', value) {
  const w = h('span', { class: 'ek-wanted ek-wanted--' + size, role: 'img', 'aria-label': 'Respekt: ' + stars + ' z 5 gwiazdek' });
  for (let i = 1; i <= 5; i++) w.append(h('i', { class: 'ek-wanted__star' + (i <= stars ? ' is-on' : '') }));
  if (value != null) w.append(h('span', { class: 'ek-wanted__value' }, value));
  return w;
}
function platTag(p) { return h('span', { class: 'ek-platform ek-platform--' + PLAT_CLS[p], title: PLAT_L[p] }, PLAT[p] || p); }
function playerLink(p) { return h('a', { href: '#/g/' + p.id, class: 'ek-person__name' }, p.nick); }

/* ------------------------------------------------------------ API */
async function api(action, { method = 'GET', body, params } = {}) {
  const qs = new URLSearchParams({ a: action, ...(params || {}) });
  const headers = {};
  if (S.token) headers['X-Ekipaz-Token'] = S.token;
  if (body) headers['Content-Type'] = 'application/json';
  let res;
  try {
    res = await fetch(API + '?' + qs.toString(), { method: body ? 'POST' : method, headers, body: body ? JSON.stringify(body) : undefined, credentials: 'same-origin' });
  } catch (e) {
    S.offline = true; throw { message: 'Nie dobiliśmy do serwera. Sprawdź sieć i spróbuj jeszcze raz.', error: 'network' };
  }
  let data = null;
  try { data = await res.json(); } catch (e) { data = null; }
  if (!data) { S.offline = true; throw { message: 'Serwer odpowiedział nieczytelnie. Spróbuj za chwilę.', error: 'server' }; }
  S.offline = false;
  if (!res.ok || data.ok === false) {
    if (data.error === 'unauthorized' && S.token) { setToken(null); }
    throw data;
  }
  return data;
}
function setToken(t) { S.token = t; store.set('ek_token', t); if (!t) { S.me = null; S.meData = null; } }

/* ------------------------------------------------------------ toast / sheet */
function toast(title, body = '', kind = 'success') {
  const ic = { success: 'check', danger: 'x', cash: 'star', info: 'radio' }[kind] || 'radio';
  const t = h('div', { class: 'ek-toast ek-toast--' + kind, role: 'status' },
    h('span', { class: 'ek-toast__icon' }, icon(ic, 18)),
    h('div', null, h('div', { class: 'ek-toast__from' }, ({ danger: 'Problem', cash: 'Respekt', info: 'Info' }[kind] || 'Wiadomość') + ' · teraz'), h('div', { class: 'ek-toast__title' }, title), body ? h('div', { class: 'ek-toast__body' }, body) : null),
    h('button', { class: 'ek-btn ek-btn--ghost ek-btn--icon ek-btn--sm', 'aria-label': 'Zamknij', onclick: () => close() }, icon('x', 16)));
  const host = $('#toasts'); host.append(t);
  while (host.children.length > 3) host.firstChild.remove();
  let gone = false;
  function close() { if (gone) return; gone = true; t.classList.add('is-leaving'); setTimeout(() => t.remove(), 220); }
  setTimeout(close, kind === 'danger' ? 6000 : 4200);
}
let sheetReturn = null;
function openSheet(title, content, foot) {
  const sh = $('#sheet'), bd = $('#backdrop');
  sheetReturn = document.activeElement;
  sh.replaceChildren(
    h('div', { class: 'ek-sheet__head' }, h('h2', { class: 'ek-sheet__title', id: 'sheetTitle' }, title),
      h('button', { class: 'ek-btn ek-btn--ghost ek-btn--icon', 'aria-label': 'Zamknij', onclick: closeSheet }, icon('x', 20))),
    content, foot ? h('div', { class: 'ek-sheet__foot' }, foot) : null);
  sh.hidden = false;
  requestAnimationFrame(() => { sh.classList.add('is-open'); bd.classList.add('is-open'); const f = sh.querySelector('input,select,textarea,button:not([aria-label="Zamknij"])'); (f || sh).focus({ preventScroll: true }); });
}
function closeSheet() {
  const sh = $('#sheet'), bd = $('#backdrop');
  sh.classList.remove('is-open'); bd.classList.remove('is-open');
  setTimeout(() => { sh.hidden = true; sh.replaceChildren(); }, 320);
  if (sheetReturn && sheetReturn.focus) sheetReturn.focus({ preventScroll: true });
}
$('#backdrop').addEventListener('click', closeSheet);
document.addEventListener('keydown', e => {
  const sh = $('#sheet');
  if (sh.hidden) return;
  if (e.key === 'Escape') closeSheet();
  if (e.key === 'Tab') {
    const f = [...sh.querySelectorAll('a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])')].filter(x => x.offsetParent !== null);
    if (!f.length) return;
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  }
});

/* ------------------------------------------------------------ wspólne komponenty */
function chip(label, pressed, onclick, extra = '') {
  return h('button', { type: 'button', class: 'ek-chip ' + extra, 'aria-pressed': pressed ? 'true' : 'false', onclick }, label);
}
function field(label, input, hint) {
  const id = input.id || ('f' + Math.random().toString(36).slice(2, 8)); input.id = id;
  return h('div', { class: 'ek-field' }, h('label', { class: 'ek-label', for: id }, label), input, hint ? h('div', { class: 'ek-hint' }, hint) : null);
}
function fieldError(input, msg) {
  const f = input.closest('.ek-field'); if (!f) return;
  const hint = f.querySelector('.ek-hint') || f.appendChild(h('div', { class: 'ek-hint' }));
  if (hint.dataset.orig == null) hint.dataset.orig = hint.textContent;
  f.classList.toggle('is-invalid', !!msg);
  hint.textContent = msg || hint.dataset.orig;
  if (msg) { input.setAttribute('aria-invalid', 'true'); input.focus(); } else input.removeAttribute('aria-invalid');
}
const PL_MAP = { ą: 'a', ć: 'c', ę: 'e', ł: 'l', ń: 'n', ó: 'o', ś: 's', ź: 'z', ż: 'z' };
function discordNormalize(v) { return String(v || '').toLowerCase().replace(/[ąćęłńóśźż]/g, c => PL_MAP[c]).replace(/^@/, '').replace(/\s+/g, ''); }
const DISCORD_RE = /^(?:[a-z0-9_.]{2,32}|[^\s#@:]{2,32}#\d{4})$/;
function discordInput(value, onValue) {
  const inp = h('input', { class: 'ek-input', maxlength: 40, value: value || '', placeholder: 'np. krolnapadow', autocapitalize: 'none', autocomplete: 'off', spellcheck: 'false' });
  let hadPl = false;
  inp.addEventListener('input', () => {
    const raw = inp.value, norm = discordNormalize(raw);
    if (/[ąćęłńóśźż]/i.test(raw)) hadPl = true;
    if (!norm) hadPl = false;
    if (norm !== raw) { const pos = inp.selectionStart; inp.value = norm; try { inp.setSelectionRange(pos, pos); } catch (e) {} }
    const f = inp.closest('.ek-field'), hint = f && f.querySelector('.ek-hint');
    if (hint) { if (hint.dataset.orig == null) hint.dataset.orig = hint.textContent; f.classList.remove('is-invalid');
      hint.textContent = hadPl ? 'Discord nie używa polskich znaków, więc zapisujemy to jako „' + norm + '”. Sprawdź, czy tak brzmi Twoja nazwa w Discordzie.' : hint.dataset.orig;
      hint.classList.toggle('ek-hint--fix', hadPl); }
    onValue(inp.value);
  });
  return inp;
}
function groupLabel(text) { return h('div', { class: 'ek-label' }, text); }
function toggle(label, checked, onchange) {
  const inp = h('input', { type: 'checkbox', checked: checked ? true : null, onchange: e => onchange(e.target.checked) });
  return h('label', { class: 'ek-toggle' }, inp, h('span', { class: 'ek-toggle__track' }), h('span', null, label));
}
function empty(title, text, cta, art = 'radio') {
  return h('div', { class: 'ek-empty' }, h('div', { class: 'ek-empty__art' }, icon(art, 120)), h('h3', { class: 'ek-empty__title' }, title), h('p', { class: 'ek-empty__text' }, text), cta || null);
}
function sectionHead(title, aside) { return h('div', { class: 'ek-section-head' }, h('h2', { class: 'ek-h2' }, title), aside || null); }
function pageHead(kicker, title, lead, back) {
  return h('div', { class: 'ek-page-head' },
    back ? h('a', { class: 'ek-back', href: back }, icon('arrow', 16), 'Wróć') : null,
    h('div', { class: 'ek-kicker' }, kicker), h('h1', { class: 'ek-h1' }, title), lead ? h('p', { class: 'ek-lead' }, lead) : null);
}
function needProfile(next) {
  if (S.token) return false;
  store.set('ek_next', next || location.hash);
  location.hash = '#/start';
  return true;
}
function errMsg(e) { return (e && e.message) || 'Coś poszło nie tak. Spróbuj jeszcze raz.'; }
async function share(title, path) {
  const url = location.href.split('#')[0] + path;
  try { if (navigator.share) { await navigator.share({ title, text: title + ' – wbijaj na Ekipaż', url }); return; } } catch (e) { if (e && e.name === 'AbortError') return; }
  try { await navigator.clipboard.writeText(url); toast('Link skopiowany', 'Wklej go na swój serwer albo do znajomych.'); }
  catch (e) { openSheet('Udostępnij', h('div', { class: 'ek-stack' }, h('p', null, 'Skopiuj ten link:'), h('input', { class: 'ek-input', value: url, readonly: true, onfocus: ev => ev.target.select() }))); }
}
async function copy(text, what) {
  try { await navigator.clipboard.writeText(text); toast(what + ' skopiowany', text); } catch (e) { toast('Skopiuj ręcznie', text, 'info'); }
}
function reportSheet(type, id) {
  let reason = 'spam';
  const box = h('div', { class: 'ek-chips ek-chips--wrap' });
  const draw = () => box.replaceChildren(...Object.entries(REPORT_REASONS).map(([k, l]) => chip(l, reason === k, () => { reason = k; draw(); })));
  draw();
  openSheet('Zgłoś nadużycie', h('div', { class: 'ek-stack' }, h('p', { class: 'ek-meta' }, 'Zgłoszenia są anonimowe dla innych graczy. Trzy niezależne zgłoszenia automatycznie ukrywają zlecenie do czasu sprawdzenia.'), box),
    [h('button', { class: 'ek-btn ek-btn--ghost', onclick: closeSheet }, 'Anuluj'),
     h('button', { class: 'ek-btn ek-btn--danger', onclick: async () => {
       try { await api('report', { body: { type, id, reason } }); closeSheet(); toast('Dziękujemy za zgłoszenie', 'Moderacja sprawdzi je najszybciej, jak to możliwe.'); } catch (e) { toast('Nie wysłano zgłoszenia', errMsg(e), 'danger'); }
     } }, 'Wyślij zgłoszenie')]);
}

/* ------------------------------------------------------------ karta zlecenia */
function slots(job) {
  const wrap = h('span', { class: 'ek-slots' + (job.slots > 5 ? ' ek-slots--many' : ''), role: 'img', 'aria-label': 'Skład ' + job.taken + ' z ' + job.slots });
  for (let i = 0; i < job.slots; i++) wrap.append(h('span', { class: 'ek-slot' + (i === 0 ? ' is-host is-filled' : i < job.taken ? ' is-filled' : '') }, i === 0 ? '★' : i < job.taken ? '✓' : ''));
  wrap.append(h('span', { class: 'ek-slots__label' }, h('b', null, job.taken), '/' + job.slots));
  return wrap;
}
function cdEl(ts) {
  const c = countdown(ts);
  return h('span', { class: 'ek-cd-wrap' }, h('span', { class: 'ek-countdown__label', 'data-cdl': ts }, c.label), h('span', { class: 'ek-countdown ' + c.cls, 'data-cd': ts }, c.t));
}
function jobCard(job, i = 0) {
  const s = job.startAt - now();
  const live = job.status === 'open' && s < 1800;
  const soon = job.status === 'open' && !live && s < 7200;
  const mine = job.myStatus === 'owner';
  const a = ACT[job.activity] || ACT.heist;
  const card = h('article', { class: 'ek-job ek-rise' + (live ? ' is-live' : '') + (job.status === 'full' ? ' is-full' : '') + (job.status === 'closed' ? ' is-closed' : '') + (mine ? ' is-mine' : ''), '--i': Math.min(i, 12) },
    i % 3 === 1 ? h('span', { class: 'ek-pin ek-pin--teal' }) : i % 3 === 2 ? h('span', { class: 'ek-pin' }) : h('span', { class: 'ek-tape' }),
    mine ? h('span', { class: 'ek-sticker ek-sticker--pink ek-job__mine' }, 'Twoje') : null,
    h('div', { class: 'ek-job__head' },
      h('div', null, h('div', { class: 'ek-job__activity' }, a.i + ' ' + a.l), h('h3', { class: 'ek-job__title' }, h('a', { href: '#/z/' + job.id }, job.title))),
      live ? h('span', { class: 'ek-live' }, s <= 0 ? 'Trwa' : 'Na żywo') : soon ? h('span', { class: 'ek-live ek-live--soon' }, 'Wkrótce') : null),
    job.owner ? h('div', { class: 'ek-job__host' }, avatar(job.owner, 'sm'), h('a', { href: '#/g/' + job.owner.id }, h('b', null, job.owner.nick)), wanted(job.owner.stars, 'sm')) : null,
    h('div', { class: 'ek-job__meta' }, platTag(job.platform), h('span', { class: 'ek-badge' }, STYLES[job.style]), job.micRequired ? h('span', { class: 'ek-badge ek-badge--mic' }, '🎙 Mikrofon') : null,
      job.myStatus === 'accepted' ? h('span', { class: 'ek-badge ek-badge--gold' }, 'Jesteś w składzie') : job.myStatus === 'pending' ? h('span', { class: 'ek-badge' }, 'Zgłoszenie wysłane') : null),
    job.details ? h('p', { class: 'ek-job__note' }, job.details.length > 90 ? job.details.slice(0, 88) + '…' : job.details) : null,
    h('div', { class: 'ek-job__foot' }, slots(job), cdEl(job.startAt),
      job.status === 'open' && !job.myStatus ? h('button', { class: 'ek-btn ek-btn--primary ek-btn--sm', onclick: e => { e.stopPropagation(); joinJob(job); } }, 'Wchodzę') : null),
    h('span', { class: 'ek-job__stamp' }, h('span', { class: 'ek-stamp' }, 'Pełny skład')));
  return card;
}
function skeletonCards(n = 3) {
  return Array.from({ length: n }, () => h('div', { class: 'ek-job ek-job--skeleton', 'aria-hidden': 'true' },
    h('div', { class: 'ek-skeleton', style: { width: '30%' } }), h('div', { class: 'ek-skeleton', style: { width: '80%', height: '26px' } }),
    h('div', { class: 'ek-skeleton', style: { width: '50%' } }), h('div', { class: 'ek-skeleton', style: { width: '100%', height: '30px', marginTop: 'auto' } })));
}

async function joinJob(job) {
  if (needProfile('#/z/' + job.id)) return;
  if (S.me && S.me.platform !== job.platform) { toast('Inna platforma', 'To zlecenie jest na ' + PLAT_L[job.platform] + ', a Twój profil na ' + PLAT_L[S.me.platform] + '.', 'danger'); return; }
  const msg = h('input', { class: 'ek-input', maxlength: 160, placeholder: 'np. Mam Kosatkę, lvl 120, mogę od razu' });
  openSheet('Zgłoszenie do składu', h('div', { class: 'ek-stack' },
    h('p', { class: 'ek-meta' }, 'Gospodarz zobaczy Twój profil i oceny. Po akceptacji wyświetlimy Ci jego Discorda.'),
    field('Krótka wiadomość (opcjonalnie)', msg)),
    [h('button', { class: 'ek-btn ek-btn--ghost', onclick: closeSheet }, 'Anuluj'),
     h('button', { class: 'ek-btn ek-btn--primary', onclick: async ev => {
       ev.target.disabled = true;
       try { await api('job.join', { body: { id: job.id, msg: msg.value } }); closeSheet(); toast('Zgłoszenie wysłane', 'Status zobaczysz w zleceniu i w swoim profilu.'); refreshJobs(); if (route().name === 'job') render(); }
       catch (e) { ev.target.disabled = false; toast('Nie udało się', errMsg(e), 'danger'); }
     } }, 'Wyślij zgłoszenie')]);
}

/* ------------------------------------------------------------ TABLICA */
function heroSkyline() {
  const w = h('div', { class: 'ek-hero__skyline', 'aria-hidden': 'true' });
  w.innerHTML = '<svg viewBox="0 0 400 120" preserveAspectRatio="xMidYMax slice" fill="currentColor"><path d="M0 120V92h18V78h10v-8h8v8h14v14h12V60h6v-6h10v6h6v32h16V84h22V70h4V58h6v12h6v14h18V96h14V74l10-8 10 8v22h12V80h20V64h8v16h18v14h16V70h6V52h4v18h8v22h14V86h20v34z"/><path d="M70 120c2-22 4-42 10-62l3 1c-5 20-7 40-8 61z"/><path d="M82 58c-10-6-24-6-34 2 12-2 22 0 30 5zM82 58c-4-10-14-16-26-16 10 4 17 10 22 18zM82 58c4-10 14-15 26-14-10 3-17 8-22 16zM82 58c10-4 22-2 30 6-10-3-20-2-28 1zM82 58c-2 8-8 14-16 18 8-6 12-12 13-19z"/><path d="M318 120c-1-30 1-56 8-80l3 1c-6 24-8 50-7 79z"/><path d="M327 40c-12-7-28-6-40 3 14-3 26-1 36 5zM327 40c-5-12-17-19-31-18 12 4 21 11 27 21zM327 40c5-12 17-18 31-16-12 3-21 9-27 19zM327 40c12-5 26-2 35 8-12-4-24-3-33 1zM327 40c1 10 7 17 15 22-9-4-15-11-17-21z"/></svg>';
  return w;
}
function ticker() {
  const feed = (S.stats && S.stats.feed) || [];
  const items = feed.length ? feed.map(feedItem) : [
    h('span', { class: 'ek-ticker__item' }, h('time', null, hhmm(now())), h('span', { class: 'ek-ticker__code' }, '10-8'), 'Nasłuch włączony. Pierwsze zlecenie może być Twoje.'),
    h('span', { class: 'ek-ticker__item' }, h('span', { class: 'ek-ticker__code' }, 'INFO'), 'Na start działamy w obecnym GTA Online – profile i respekt przechodzą dalej.'),
  ];
  const track = h('div', { class: 'ek-ticker__track' }, items, h('span', { 'aria-hidden': 'true', style: { display: 'contents' } }, items.map(n => { const c = n.cloneNode(true); c.setAttribute('aria-hidden', 'true'); return c; })));
  return h('div', { class: 'ek-ticker', '--_speed': Math.max(30, items.length * 7) + 's', role: 'region', 'aria-label': 'Nasłuch – ostatnie zdarzenia' },
    h('span', { class: 'ek-ticker__label' }, 'Nasłuch'), h('div', { class: 'ek-ticker__viewport', tabindex: '0' }, track));
}
function feedItem(e) {
  const code = { job: '10-31', accept: '10-4', vouch: '10-99', crew: 'CREW', crewjoin: 'CREW', join: 'NEW' }[e.type] || 'INFO';
  const text = {
    job: [h('b', null, e.nick), ' szuka ludzi: ', e.title],
    accept: [h('b', null, e.nick), ' wchodzi w skład: ', e.title],
    vouch: [h('b', null, e.nick), ' dostaje respekt od ', e.from],
    crew: [h('b', null, e.nick), ' zakłada ekipę ', e.crew],
    crewjoin: [h('b', null, e.nick), ' dołącza do ekipy ', e.crew],
    join: ['Nowy gracz na mieście: ', h('b', null, e.nick)],
  }[e.type] || [''];
  return h('span', { class: 'ek-ticker__item' }, h('time', null, hhmm(e.created)), h('span', { class: 'ek-ticker__code' }, code), ...text);
}
function quickMatch() {
  const f = S.filters;
  const sel = (opts, val, cls, on, label) => {
    const s = h('select', { class: 'ek-quickmatch__slot ' + cls, 'aria-label': label, onchange: e => on(e.target.value) }, opts.map(([v, l]) => h('option', { value: v, selected: v === val ? true : null }, l)));
    return s;
  };
  const result = h('p', { class: 'ek-quickmatch__result', 'aria-live': 'polite' });
  const run = () => {
    const list = filteredJobs().filter(j => j.status === 'open' && !j.myStatus);
    if (list.length) {
      result.replaceChildren('Mamy ', h('b', null, list.length + ' ' + plural(list.length, 'zlecenie', 'zlecenia', 'zleceń')), ' pod Ciebie. Najbliższe startuje o ', h('b', null, hhmm(list[0].startAt)), '.');
      const el = document.getElementById('jobs');
      if (el) el.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    } else {
      result.replaceChildren('Nikt jeszcze nie szuka takiej ekipy. ', h('a', { href: '#/dodaj', onclick: () => { S.draft = { activity: f.activity || 'heist', platform: f.platform || (S.me && S.me.platform) || 'ps5', when: f.when === 'now' ? 15 : 60 }; } }, 'Wystaw to zlecenie jako pierwszy →'));
    }
  };
  const presets = [
    ['Napad dziś wieczorem', { activity: 'heist', when: 'today' }], ['Wyścigi teraz', { activity: 'race', when: 'now' }],
    ['Grind biznesu na luzie', { activity: 'business', style: 'chill' }], ['Free roam bez spiny', { activity: 'freeroam', style: 'chill' }],
  ];
  return h('section', { class: 'ek-container' },
    h('div', { class: 'ek-quickmatch' },
      h('p', { class: 'ek-quickmatch__lead' }, 'Szybkie dopasowanie'),
      h('div', { class: 'ek-quickmatch__sentence' }, 'Szukam',
        sel([['', 'czegokolwiek'], ...Object.entries(ACT_GEN)], f.activity, '', v => { f.activity = v; renderBoardList(); }, 'Aktywność'),
        'na',
        sel([['', 'każdej platformie'], ...Object.entries(PLAT_L).map(([k, v]) => [k, k === 'pc' ? 'PC' : v])], f.platform, 'ek-quickmatch__slot--teal', v => { f.platform = v; store.set('ek_f_platform', v); renderBoardList(); }, 'Platforma'),
        sel([['', 'kiedykolwiek'], ['now', 'w ciągu godziny'], ['today', 'dzisiaj']], f.when, '', v => { f.when = v; renderBoardList(); }, 'Kiedy')),
      h('div', { class: 'ek-quickmatch__actions' }, h('button', { class: 'ek-btn ek-btn--primary', onclick: run }, 'Dopasuj ekipę'), h('a', { class: 'ek-btn ek-btn--secondary', href: '#/dodaj' }, 'Wystaw zlecenie')),
      h('div', { class: 'ek-chips ek-quickmatch__presets' }, presets.map(([l, p]) => h('button', { class: 'ek-chip', type: 'button', onclick: () => { Object.assign(f, { activity: '', when: '', style: '' }, p); render(); setTimeout(run, 50); } }, l))),
      result));
}
function filteredJobs() {
  const f = S.filters, t = now();
  return S.jobs.filter(j =>
    (!f.platform || j.platform === f.platform) && (!f.activity || j.activity === f.activity) && (!f.style || j.style === f.style) &&
    (!f.open || j.status === 'open') &&
    (f.when !== 'now' || j.startAt < t + 3600) &&
    (f.when !== 'today' || new Date(j.startAt * 1000).toDateString() === new Date().toDateString()));
}
function filterBar() {
  const f = S.filters;
  const row1 = h('div', { class: 'ek-chips', role: 'group', 'aria-label': 'Platforma' },
    chip('Wszystkie', !f.platform, () => { f.platform = ''; store.set('ek_f_platform', ''); renderBoardList(); }),
    ...Object.keys(PLAT).map(p => chip(PLAT_L[p], f.platform === p, () => { f.platform = f.platform === p ? '' : p; store.set('ek_f_platform', f.platform); renderBoardList(); }, p === 'pc' ? '' : 'ek-chip--' + PLAT_CLS[p] + (f.platform === p ? ' is-selected' : ''))),
    chip('Tylko wolne miejsca', f.open, () => { f.open = !f.open; renderBoardList(); }));
  const row2 = h('div', { class: 'ek-chips', role: 'group', 'aria-label': 'Aktywność' },
    ...Object.entries(ACT).map(([k, v]) => {
      const n = S.jobs.filter(j => j.activity === k && j.status !== 'closed').length;
      return h('button', { type: 'button', class: 'ek-chip', 'aria-pressed': f.activity === k ? 'true' : 'false', onclick: () => { f.activity = f.activity === k ? '' : k; renderBoardList(); } }, v.i + ' ' + v.l, n ? h('span', { class: 'ek-chip__count' }, n) : null);
    }),
    ...Object.entries(STYLES).map(([k, v]) => chip(v, f.style === k, () => { f.style = f.style === k ? '' : k; renderBoardList(); })));
  return h('div', { class: 'ek-filterbar', id: 'filterbar' }, row1, row2);
}
function renderBoardList() {
  const host = document.getElementById('boardList'); if (!host) return;
  const fb = document.getElementById('filterbar'); if (fb) fb.replaceWith(filterBar());
  document.querySelectorAll('.ek-cat').forEach(b => { const k = [...b.classList].find(c => c.startsWith('ek-cat--')); if (k) b.setAttribute('aria-pressed', S.filters.activity === k.slice(8) ? 'true' : 'false'); });
  const qm = document.querySelector('.ek-quickmatch'); // utrzymaj selecty w zgodzie z filtrami
  if (qm) { const sels = qm.querySelectorAll('select'); if (sels[0]) sels[0].value = S.filters.activity; if (sels[1]) sels[1].value = S.filters.platform; if (sels[2]) sels[2].value = S.filters.when; }
  if (!S.jobsLoaded) { host.replaceChildren(h('div', { class: 'ek-grid' }, skeletonCards(3))); return; }
  const list = filteredJobs();
  const cnt = document.getElementById('jobCount'); if (cnt) cnt.textContent = list.length + ' ' + plural(list.length, 'zlecenie', 'zlecenia', 'zleceń');
  if (!list.length) {
    const anyJobs = S.jobs.length > 0;
    host.replaceChildren(samplesSection(list), h('div', { style: { height: '24px' } }), empty(anyJobs ? 'Brak zleceń dla tych filtrów' : 'Tablica czeka na pierwsze zlecenie',
      anyJobs ? 'Zmień filtry albo wystaw własne zlecenie – trafi na górę tablicy.' : 'Wystaw je w minutę. Zobaczą je wszyscy, którzy właśnie szukają składu.',
      h('div', { class: 'ek-row', style: { justifyContent: 'center' } },
        h('a', { class: 'ek-btn ek-btn--primary', href: '#/dodaj' }, 'Wystaw zlecenie'),
        anyJobs ? h('button', { class: 'ek-btn ek-btn--ghost', onclick: () => { Object.assign(S.filters, { platform: '', activity: '', when: '', style: '', open: false }); store.set('ek_f_platform', ''); render(); } }, 'Wyczyść filtry') : null)));
    return;
  }
  host.replaceChildren(...[h('div', { class: 'ek-grid' }, list.map(jobCard)), list.length < 4 ? samplesSection(list) : null].filter(Boolean));
}
function goFilter(patch) {
  Object.assign(S.filters, { activity: '', when: '', style: '', open: false }, patch);
  if (route().name !== 'board') { location.hash = '#/'; setTimeout(() => scrollToJobs(), 400); return; }
  renderBoardList(); scrollToJobs();
}
function scrollToJobs() { const el = document.getElementById('jobs'); if (el) el.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }
const CAT_ART = { heist: '💰', contact: '📞', race: '🏁', business: '📦', freeroam: '🌴', pvp: '🎯', rp: '🎭', cars: '🚗' };
function welcomeCard() {
  const st = S.stats || {};
  const me = S.me;
  const inbox = S.meData ? S.meData.inbox.length : 0;
  return h('section', { class: 'ek-welcome' },
    h('div', { class: 'ek-welcome__art', 'aria-hidden': 'true' }, h('div', { class: 'ek-hero__sun' }), heroSkyline()),
    h('div', { class: 'ek-welcome__body' },
      h('div', { class: 'ek-kicker' }, 'GTA Online · PS5 · Xbox · PC'),
      me ? h('h1', { class: 'ek-welcome__title' }, 'Cześć, ', h('span', { class: 'ek-sunset-text' }, me.nick + '.'), h('br'), 'Co dziś gramy?')
         : h('h1', { class: 'ek-welcome__title' }, 'Ekipa, która ', h('span', { class: 'ek-sunset-text' }, 'dowiezie finał.')),
      h('p', { class: 'ek-welcome__sub' }, me
        ? (inbox ? inbox + ' ' + plural(inbox, 'gracz czeka', 'graczy czeka', 'graczy czeka') + ' na Twoją decyzję. Sprawdź ich oceny i skompletuj skład.' : 'Wystaw zlecenie z godziną startu albo dołącz do składu, który właśnie zbiera ludzi.')
        : 'Wystaw zlecenie z godziną startu albo dołącz do cudzego. Każdy gracz ma oceny od ludzi, z którymi grał – zanim kogoś przyjmiesz, wiesz, czy dowozi, czy wychodzi w połowie.'),
      h('div', { class: 'ek-welcome__ctas' },
        me ? h('a', { class: 'ek-btn ek-btn--grad ek-btn--lg', href: '#/dodaj' }, icon('plus'), 'Wystaw zlecenie')
           : h('a', { class: 'ek-btn ek-btn--grad ek-btn--lg', href: '#/start' }, 'Załóż darmowy profil'),
        me && inbox ? h('a', { class: 'ek-btn ek-btn--glass ek-btn--lg', href: '#/ja' }, 'Zgłoszenia', h('span', { class: 'ek-dot-inline' }, inbox))
           : h('button', { class: 'ek-btn ek-btn--glass ek-btn--lg', onclick: scrollToJobs }, 'Zobacz zlecenia')),
      h('div', { class: 'ek-welcome__stats' },
        h('span', { class: 'ek-pillstat' }, h('i', { class: 'ek-pillstat__dot' }), h('b', null, st.online ?? '–'), ' online'),
        h('span', { class: 'ek-pillstat' }, h('b', null, st.jobs ?? '–'), ' ' + plural(st.jobs || 0, 'zlecenie', 'zlecenia', 'zleceń')),
        h('span', { class: 'ek-pillstat' }, h('b', null, st.crews ?? '–'), ' ' + plural(st.crews || 0, 'ekipa', 'ekipy', 'ekip')))),
    !me ? h('p', { class: 'ek-welcome__note' }, h('b', null, 'GTA VI Online nie ma jeszcze daty premiery. '), 'Do tego czasu gramy w obecne GTA Online – profil i oceny zostaną z Tobą, gdy ruszy nowa odsłona.') : null);
}
function bigCards() {
  const n = S.jobs.filter(j => j.status === 'open').length;
  return h('section', { class: 'ek-bigcards' },
    h('a', { class: 'ek-bigcard ek-bigcard--jobs', href: '#jobs', onclick: e => { e.preventDefault(); scrollToJobs(); } },
      h('span', { class: 'ek-bigcard__title' }, 'Zlecenia'), h('span', { class: 'ek-bigcard__meta' }, n + ' ' + plural(n, 'otwarte', 'otwarte', 'otwartych')), h('span', { class: 'ek-bigcard__art', 'aria-hidden': 'true' }, '💰')),
    h('a', { class: 'ek-bigcard ek-bigcard--crews', href: '#/ekipy' },
      h('span', { class: 'ek-bigcard__title' }, 'Ekipy'), h('span', { class: 'ek-bigcard__meta' }, (S.stats && S.stats.crews || 0) + ' ' + plural((S.stats && S.stats.crews) || 0, 'ekipa', 'ekipy', 'ekip')), h('span', { class: 'ek-bigcard__art', 'aria-hidden': 'true' }, '🕶️')));
}
function promoBanners() {
  const cnt = a => S.jobs.filter(j => j.activity === a && j.status === 'open').length;
  const B = [
    { cls: 'heist', k: 'Finały i przygotówki', t: ['Napady', 'na wieczór'], d: cnt('heist') ? cnt('heist') + ' ' + plural(cnt('heist'), 'skład szuka ludzi', 'składy szukają ludzi', 'składów szuka ludzi') : 'Zbierz skład na dzisiejszy wieczór', art: '💰', on: () => goFilter({ activity: 'heist', when: 'today' }) },
    { cls: 'race', k: 'Wyścigi', t: ['Czyste', 'lobby'], d: cnt('race') ? cnt('race') + ' ' + plural(cnt('race'), 'lobby zbiera', 'lobby zbierają', 'lobby zbiera') + ' kierowców' : 'Bez taranowania i ragequitów', art: '🏎️', on: () => goFilter({ activity: 'race' }) },
    { cls: 'rank', k: 'Ranking tygodnia', t: ['Najlepiej', 'oceniani'], d: 'Zobacz, z kim warto grać', art: '🏆', on: () => { location.hash = '#/ranking'; } },
  ];
  return h('section', { class: 'ek-promos', 'aria-label': 'Wyróżnione' }, B.map(b => h('button', { type: 'button', class: 'ek-promo ek-promo--' + b.cls, onclick: b.on },
    h('span', { class: 'ek-promo__k' }, b.k), h('span', { class: 'ek-promo__t' }, b.t[0], h('br'), b.t[1]), h('span', { class: 'ek-promo__d' }, b.d), h('span', { class: 'ek-promo__art', 'aria-hidden': 'true' }, b.art))));
}
function liveStrip() {
  const feed = ((S.stats && S.stats.feed) || []).slice(0, 12);
  const items = feed.length ? feed.map(e => {
    const t = { job: ['szuka ludzi', e.title], accept: ['wchodzi w skład', e.title], vouch: ['dostaje respekt', 'od ' + e.from], crew: ['zakłada ekipę', e.crew], crewjoin: ['dołącza do ekipy', e.crew] }[e.type] || ['', ''];
    const href = e.jobId ? '#/z/' + e.jobId : e.crewId ? '#/e/' + e.crewId : null;
    return h(href ? 'a' : 'div', { class: 'ek-livechip', href },
      h('span', { class: 'ek-livechip__ic', 'aria-hidden': 'true' }, ({ job: '📣', accept: '🤝', vouch: '⭐', crew: '🕶️', crewjoin: '🕶️' })[e.type] || '•'),
      h('span', { class: 'ek-livechip__txt' }, h('b', null, e.nick), ' ' + t[0], h('span', { class: 'ek-livechip__sub' }, t[1] + ' · ' + hhmm(e.created))));
  }) : [h('div', { class: 'ek-livechip' }, h('span', { class: 'ek-livechip__ic' }, '📻'), h('span', { class: 'ek-livechip__txt' }, h('b', null, 'Na razie spokojnie'), h('span', { class: 'ek-livechip__sub' }, 'Nowe zlecenia i składy pojawią się tutaj')))];
  return h('section', { class: 'ek-livestrip', 'aria-label': 'Ostatnia aktywność' },
    h('div', { class: 'ek-livestrip__badge' }, h('span', { class: 'ek-livestrip__wave', 'aria-hidden': 'true' }, '((•))'), 'Na', h('br'), 'żywo'),
    h('div', { class: 'ek-livestrip__track' }, items));
}
function catTiles() {
  const f = S.filters;
  return h('section', { class: 'ek-cats-wrap' },
    h('div', { class: 'ek-section-head' }, h('h2', { class: 'ek-h2' }, 'Co dziś gramy?'), f.activity ? h('button', { class: 'ek-btn ek-btn--ghost ek-btn--sm', onclick: () => goFilter({}) }, 'Pokaż wszystko') : null),
    h('div', { class: 'ek-cats', role: 'group', 'aria-label': 'Kategorie' }, Object.entries(ACT).map(([k, v]) => {
      const n = S.jobs.filter(j => j.activity === k && j.status !== 'closed').length;
      return h('button', { type: 'button', class: 'ek-cat ek-cat--' + k, 'aria-pressed': f.activity === k ? 'true' : 'false', onclick: () => goFilter({ activity: f.activity === k ? '' : k }) },
        h('span', { class: 'ek-cat__count' }, n ? n + ' ' + plural(n, 'zlecenie', 'zlecenia', 'zleceń') : 'Brak zleceń'),
        h('span', { class: 'ek-cat__art', 'aria-hidden': 'true' }, CAT_ART[k]),
        h('span', { class: 'ek-cat__label' }, v.l));
    })));
}
function viewBoard() {
  const firstVisit = !S.token;
  const liveJobs = S.jobs.filter(j => j.status === 'open' && j.startAt - now() < 1800).slice(0, 8);
  return [
    h('div', { class: 'ek-container ek-board-top' }, welcomeCard(), bigCards(), promoBanners(), liveStrip(), catTiles()),
    quickMatch(),
    liveJobs.length ? h('section', { class: 'ek-container ek-section', style: { paddingBottom: 0 } },
      sectionHead('Start w ciągu 30 minut', h('span', { class: 'ek-live' }, 'Na żywo')),
      h('div', { class: 'ek-live-strip' }, liveJobs.map(jobCard))) : null,
    h('section', { class: 'ek-container ek-section', id: 'jobs' },
      sectionHead('Tablica zleceń', h('span', { class: 'ek-count', id: 'jobCount' })),
      filterBar(),
      S.offline ? h('div', { class: 'ek-banner' }, icon('radio'), S.jobs.length ? 'Brak połączenia z serwerem. Pokazujemy ostatnie znane zlecenia.' : 'Brak połączenia z serwerem. Spróbuj odświeżyć za chwilę.') : null,
      h('div', { id: 'boardList' })),
    firstVisit ? h('section', { class: 'ek-container ek-section' },
      sectionHead('Jak to działa'),
      h('div', { class: 'ek-steps3' },
        h('div', { class: 'ek-step3' }, h('h3', { class: 'ek-h3' }, 'Wystaw zlecenie'), h('p', null, 'Wybierasz aktywność, platformę, godzinę startu i liczbę miejsc. Zajmuje to mniej niż minutę.')),
        h('div', { class: 'ek-step3' }, h('h3', { class: 'ek-h3' }, 'Wybierz skład'), h('p', null, 'Przy każdym zgłoszeniu widzisz oceny i liczbę rozegranych robót. Decydujesz Ty, a Twój Discord zobaczą tylko przyjęci.')),
        h('div', { class: 'ek-step3' }, h('h3', { class: 'ek-h3' }, 'Oceń po grze'), h('p', null, 'Po robocie dajesz +1 tym, którzy dowieźli. Oceny dają tylko gracze ze wspólnego składu, więc nie da się ich kupić ani nabić.')))) : null,
  ];
}

/* ------------------------------------------------------------ sidebar i panel na żywo (desktop) */
function renderSide() {
  const side = $('#side'); if (!side) return;
  const r = route();
  const link = (href, ic, label, key, extra) => h('a', { class: 'ek-side__link', href, 'aria-current': key === r.name ? 'page' : null }, h('span', { class: 'ek-side__ic', 'aria-hidden': 'true' }, ic), label, extra || null);
  const n = S.meData ? S.meData.inbox.length + S.meData.mates.length : 0;
  side.replaceChildren(h('div', { class: 'ek-side__inner' },
    h('div', { class: 'ek-side__switch' }, h('a', { href: '#/', 'aria-current': ['board', 'job', 'add'].includes(r.name) ? 'page' : null }, 'Zlecenia'), h('a', { href: '#/ekipy', 'aria-current': ['crews', 'crew'].includes(r.name) ? 'page' : null }, 'Ekipy')),
    h('a', { class: 'ek-btn ek-btn--grad ek-btn--block', href: S.token ? '#/dodaj' : '#/start' }, icon('plus', 16), S.token ? 'Wystaw zlecenie' : 'Załóż profil'),
    h('nav', { class: 'ek-side__group', 'aria-label': 'Menu' },
      link('#/', '🗂️', 'Tablica', 'board'), link('#/ranking', '🏆', 'Ranking', 'ranking'), link('#/ja', '🪪', 'Moja kartoteka', 'me', n ? h('span', { class: 'ek-dot-inline' }, n) : null), link('#/plan', '🧭', 'Co budujemy', 'plan')),
    h('div', { class: 'ek-side__label' }, 'Kategorie'),
    h('div', { class: 'ek-side__group' }, Object.entries(ACT).map(([k, v]) => {
      const c = S.jobs.filter(j => j.activity === k && j.status !== 'closed').length;
      return h('button', { type: 'button', class: 'ek-side__link', 'aria-pressed': S.filters.activity === k && r.name === 'board' ? 'true' : 'false', onclick: () => { goFilter({ activity: S.filters.activity === k ? '' : k }); renderSide(); } },
        h('span', { class: 'ek-side__ic', 'aria-hidden': 'true' }, v.i), v.l, c ? h('span', { class: 'ek-side__count' }, c) : null);
    })),
    h('div', { class: 'ek-side__foot' }, h('a', { href: '#/zasady' }, 'Zasady i prywatność'), h('a', { href: '#/odzyskaj' }, 'Odzyskaj profil'))));
}
async function refreshRailTop() {
  try { const d = await api('leaderboard', { params: { period: 'week' } }); S.lbTop = d.players.slice(0, 3); } catch (e) {}
  renderRail();
}
function renderRail() {
  const rail = $('#rail'); if (!rail) return;
  const feed = ((S.stats && S.stats.feed) || []).slice(0, 14);
  const top = S.lbTop || [];
  rail.replaceChildren(h('div', { class: 'ek-rail__inner' },
    h('div', { class: 'ek-rail__head' }, h('span', { class: 'ek-live' }, 'Nasłuch'), h('span', { class: 'ek-meta' }, 'Ostatnia aktywność graczy')),
    h('a', { class: 'ek-railtop', href: '#/ranking' },
      h('div', { class: 'ek-railtop__head' }, h('span', null, '🏆 Ranking tygodnia'), h('span', { 'aria-hidden': 'true' }, '›')),
      top.length ? h('ol', { class: 'ek-railtop__list' }, top.map((p, i) => h('li', null, h('span', { class: 'ek-medal ek-medal--' + (i + 1) }, i + 1), h('span', { class: 'ek-railtop__nick' }, p.nick), h('span', { class: 'ek-lb__score' }, '+' + p.score))))
        : h('p', { class: 'ek-meta', style: { margin: 0 } }, 'Pierwsze oceny pojawią się po pierwszych wspólnych grach.')),
    h('div', { class: 'ek-rail__feed' }, feed.length ? feed.map(e => {
      const t = { job: 'szuka ludzi: ' + e.title, accept: 'wchodzi w skład: ' + e.title, vouch: 'dostaje respekt od ' + e.from, crew: 'zakłada ekipę ' + e.crew, crewjoin: 'dołącza do ekipy ' + e.crew }[e.type] || '';
      const href = e.jobId ? '#/z/' + e.jobId : e.crewId ? '#/e/' + e.crewId : null;
      return h(href ? 'a' : 'div', { class: 'ek-msg', href }, h('div', { class: 'ek-msg__top' }, h('b', null, e.nick), h('time', null, hhmm(e.created))), h('div', { class: 'ek-msg__bubble' }, t));
    }) : h('div', { class: 'ek-msg' }, h('div', { class: 'ek-msg__bubble' }, 'Tu zobaczysz nowe zlecenia, przyjęcia do składów i oceny – na bieżąco.'))),
    h('a', { class: 'ek-btn ek-btn--grad ek-btn--block', href: S.token ? '#/dodaj' : '#/start' }, S.token ? 'Wystaw zlecenie' : 'Załóż profil')));
}

/* ------------------------------------------------------------ SZCZEGÓŁY ZLECENIA */
async function viewJob(id) {
  let job;
  try { job = (await api('job', { params: { id } })).job; }
  catch (e) { return [h('div', { class: 'ek-container' }, pageHead('Zlecenie', 'Zlecenie wygasło', null, '#/'), empty('Tego zlecenia już nie ma', errMsg(e), h('a', { class: 'ek-btn ek-btn--primary', href: '#/' }, 'Wróć na tablicę')))]; }
  const a = ACT[job.activity] || ACT.heist;
  const isOwner = job.myStatus === 'owner';
  const inCrew = isOwner || job.myStatus === 'accepted';
  const c = countdown(job.startAt);
  document.title = job.title + ' – Ekipaż';

  const members = h('ul', { class: 'ek-crewlist' },
    job.owner ? h('li', { class: 'ek-person' }, avatar(job.owner), h('div', null, playerLink(job.owner), h('span', { class: 'ek-person__sub' }, 'Gospodarz · ' + job.owner.jobsDone + ' ' + plural(job.owner.jobsDone, 'robota', 'roboty', 'robót'))), wanted(job.owner.stars)) : null,
    job.members.map(m => h('li', { class: 'ek-person' }, avatar(m), h('div', null, playerLink(m), h('span', { class: 'ek-person__sub' }, 'W składzie')), wanted(m.stars))),
    Array.from({ length: Math.max(0, job.slots - job.taken) }, () => h('li', { class: 'ek-person is-empty' }, h('span', { class: 'ek-slot' }), h('span', null, 'Wolne miejsce'), h('span'))));

  let contactBox = null;
  if (inCrew && !isOwner && job.owner && job.owner.contact) {
    contactBox = h('div', { class: 'ek-stack' }, h('div', { class: 'ek-label' }, 'Discord gospodarza'), h('button', { class: 'ek-contact', onclick: () => copy(job.owner.contact, 'Discord') }, icon('discord'), job.owner.contact, icon('copy', 14)));
  } else if (!inCrew) {
    contactBox = h('p', { class: 'ek-lock-note' }, icon('lock', 16), 'Discord gospodarza zobaczysz po przyjęciu do składu.');
  }

  let requestsBox = null;
  if (isOwner) {
    const reqs = job.requests || [];
    const pending = reqs.filter(r => r.status === 'pending');
    const accepted = reqs.filter(r => r.status === 'accepted');
    requestsBox = h('section', { class: 'ek-card ek-stack' },
      h('div', { class: 'ek-section-head', style: { marginBottom: 0 } }, h('h2', { class: 'ek-h3' }, 'Zgłoszenia'), h('span', { class: 'ek-count' }, pending.length + ' oczekuje')),
      pending.length ? h('ul', { class: 'ek-crewlist' }, pending.map(r => requestRow(r, job))) :
        h('p', { class: 'ek-meta' }, 'Brak zgłoszeń. Udostępnij link na swoim serwerze Discord albo w grupie – tak najszybciej zbierzesz skład.'),
      accepted.length ? [h('div', { class: 'ek-label' }, 'Kontakty składu'), h('ul', { class: 'ek-crewlist' }, accepted.map(r => h('li', { class: 'ek-person' }, avatar(r.player), h('div', null, playerLink(r.player), h('span', { class: 'ek-person__sub' }, 'Discord')), h('button', { class: 'ek-contact', onclick: () => copy(r.player.contact, 'Discord') }, r.player.contact))))] : null);
  }

  let cta;
  if (job.status === 'closed') cta = [h('span', { class: 'ek-meta', style: { flex: 1 } }, 'Zlecenie zamknięte.'), h('a', { class: 'ek-btn ek-btn--secondary', href: '#/' }, 'Inne zlecenia')];
  else if (isOwner) cta = [h('button', { class: 'ek-btn ek-btn--cash', onclick: () => share(job.title, '#/z/' + job.id) }, icon('share'), 'Udostępnij link'),
    h('button', { class: 'ek-btn ek-btn--ghost', onclick: () => confirmSheet(job.startAt <= now() ? 'Zakończyć robotę?' : 'Odwołać zlecenie?', job.startAt <= now() ? 'Zlecenie zniknie z tablicy, a skład dostanie zaliczoną robotę.' : 'Zlecenie zniknie z tablicy, a zgłoszenia przepadną.', 'Tak, zamykam', async () => { try { await api('job.close', { body: { id: job.id } }); toast('Zlecenie zamknięte', job.startAt <= now() ? 'Robota zaliczona całemu składowi. Możecie teraz wystawić sobie oceny.' : 'Zniknęło z tablicy.'); refreshJobs(); refreshMe(); render(); } catch (e) { toast('Nie udało się', errMsg(e), 'danger'); } }) }, job.startAt <= now() ? 'Zakończ' : 'Odwołaj')];
  else if (job.myStatus === 'accepted') cta = [h('span', { class: 'ek-stamp ek-stamp--ok is-stamping', style: { fontSize: '1rem' } }, 'W składzie'), h('button', { class: 'ek-btn ek-btn--secondary', onclick: () => share(job.title, '#/z/' + job.id) }, icon('share'), 'Udostępnij'),
    h('button', { class: 'ek-btn ek-btn--ghost', onclick: () => leave(job) }, 'Rezygnuję')];
  else if (job.myStatus === 'pending') cta = [h('span', { class: 'ek-meta', style: { flex: 1 } }, 'Zgłoszenie wysłane. Czekasz na decyzję gospodarza.'), h('button', { class: 'ek-btn ek-btn--ghost', onclick: () => leave(job) }, 'Wycofaj')];
  else if (job.myStatus === 'declined') cta = [h('span', { class: 'ek-meta', style: { flex: 1 } }, 'Gospodarz wybrał inny skład. Sprawdź pozostałe zlecenia.'), h('a', { class: 'ek-btn ek-btn--secondary', href: '#/' }, 'Szukaj dalej')];
  else if (job.status === 'full') cta = [h('span', { class: 'ek-meta', style: { flex: 1 } }, 'Skład jest kompletny.'), h('a', { class: 'ek-btn ek-btn--secondary', href: '#/' }, 'Inne zlecenia')];
  else cta = [h('button', { class: 'ek-btn ek-btn--primary ek-btn--lg', onclick: () => joinJob(job) }, 'Wchodzę'), h('button', { class: 'ek-btn ek-btn--secondary ek-btn--icon', 'aria-label': 'Udostępnij', onclick: () => share(job.title, '#/z/' + job.id) }, icon('share'))];

  return [h('div', { class: 'ek-container' },
    h('div', { class: 'ek-page-head', style: { paddingBottom: 0 } }, h('a', { class: 'ek-back', href: '#/' }, icon('arrow', 16), 'Tablica')),
    h('div', { class: 'ek-detail' },
      h('div', null,
        h('article', { class: 'ek-detail__poster ek-halftone' },
          job.status === 'full' ? h('span', { class: 'ek-detail__stamp' }, h('span', { class: 'ek-stamp is-stamping' }, 'Pełny skład')) : null,
          h('div', { class: 'ek-row' }, h('span', { class: 'ek-job__activity' }, a.i + ' ' + a.l), platTag(job.platform), job.status === 'open' && job.startAt - now() < 1800 ? h('span', { class: 'ek-live' }, 'Na żywo') : null),
          h('h1', { class: 'ek-display' }, job.title),
          h('div', { class: 'ek-detail__grid' },
            h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value', 'data-cd': job.startAt }, c.t), h('span', { class: 'ek-stat__label', 'data-cdl': job.startAt }, c.label)),
            h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, hhmm(job.startAt)), h('span', { class: 'ek-stat__label' }, dayLabel(job.startAt))),
            h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, job.taken + '/' + job.slots), h('span', { class: 'ek-stat__label' }, 'Skład'))),
          h('div', { class: 'ek-job__meta' }, h('span', { class: 'ek-badge' }, STYLES[job.style]), job.micRequired ? h('span', { class: 'ek-badge ek-badge--mic' }, '🎙 Mikrofon wymagany') : h('span', { class: 'ek-badge' }, 'Mikrofon mile widziany'), h('span', { class: 'ek-badge' }, 'Wystawione ' + ago(job.created))),
          job.details ? h('p', { class: 'ek-job__note', style: { marginTop: '16px', whiteSpace: 'pre-line' } }, job.details) : null),
        h('div', { class: 'ek-detail__cta' }, cta)),
      h('div', { class: 'ek-stack' },
        h('section', { class: 'ek-card ek-stack' }, h('h2', { class: 'ek-h3' }, 'Skład'), slots(job), members, contactBox),
        requestsBox,
        !isOwner ? h('button', { class: 'ek-btn ek-btn--ghost ek-btn--sm', onclick: () => reportSheet('job', job.id) }, icon('flag', 16), 'Zgłoś zlecenie') : null)))];
}
function requestRow(r, job) {
  const decide = async (d, btn) => {
    btn.disabled = true;
    try { await api('request.decide', { body: { id: r.id, decision: d } }); toast(d === 'accept' ? r.player.nick + ' w składzie' : 'Zgłoszenie odrzucone', d === 'accept' ? 'Discord gracza znajdziesz teraz w szczegółach zlecenia.' : 'Gracz dostanie informację.', d === 'accept' ? 'success' : 'info'); refreshMe(); refreshJobs(); render(); }
    catch (e) { btn.disabled = false; toast('Nie udało się', errMsg(e), 'danger'); }
  };
  return h('li', { class: 'ek-person ek-person--req' }, avatar(r.player),
    h('div', null, playerLink(r.player), h('span', { class: 'ek-person__sub' }, [!job && r.jobTitle ? r.jobTitle : null, STYLES[r.player.style], r.player.mic ? 'z mikrofonem' : 'bez mikrofonu', r.player.jobsDone + ' ' + plural(r.player.jobsDone, 'robota', 'roboty', 'robót'), ago(r.created)].filter(Boolean).join(' · '))),
    h('div', { class: 'ek-person__actions' }, wanted(r.player.stars),
      h('button', { class: 'ek-btn ek-btn--secondary ek-btn--sm', onclick: e => decide('accept', e.currentTarget) }, 'Przyjmij'),
      h('button', { class: 'ek-btn ek-btn--ghost ek-btn--sm', 'aria-label': 'Odrzuć ' + r.player.nick, onclick: e => decide('decline', e.currentTarget) }, 'Odrzuć')),
    r.msg ? h('p', { class: 'ek-person__msg' }, '„' + r.msg + '”') : null);
}
function confirmSheet(title, text, yes, fn) {
  openSheet(title, h('p', null, text), [h('button', { class: 'ek-btn ek-btn--ghost', onclick: closeSheet }, 'Nie'), h('button', { class: 'ek-btn ek-btn--danger', onclick: async () => { closeSheet(); await fn(); } }, yes)]);
}
function leave(job) { confirmSheet('Na pewno?', job.myStatus === 'accepted' ? 'Zwolnisz swoje miejsce w składzie. Gospodarz zobaczy je jako wolne.' : 'Wycofasz zgłoszenie do tej roboty.', 'Tak, rezygnuję', () => doLeave(job)); }
async function doLeave(job) {
  try { await api('job.leave', { body: { id: job.id } }); toast('Wycofano', 'Miejsce wraca do puli.'); refreshJobs(); render(); } catch (e) { toast('Nie udało się', errMsg(e), 'danger'); }
}

/* ------------------------------------------------------------ DODAJ ZLECENIE */
function viewAdd() {
  if (needProfile('#/dodaj')) return [];
  const me = S.me || {};
  const d = Object.assign({ title: '', activity: (me.activities && me.activities[0]) || 'heist', platform: me.platform || 'ps5', slots: 4, when: 30, custom: '', style: me.style || 'balanced', mic: false, details: '' }, S.draft || {});
  S.draft = null;
  const TITLE_IDEAS = {
    heist: ['Finał napadu – brakuje 2 osób', 'Przygotówki od zera, spokojnie', 'Elite challenge, tylko ogarnięci'],
    contact: ['Misje kontaktowe na kasę', 'Seria misji, potem free roam'],
    race: ['Nocne wyścigi uliczne', 'Lobby wyścigowe – czyste jazdy'],
    business: ['Sprzedaż towaru – potrzebna obstawa', 'Wspólny grind biznesów'],
    freeroam: ['Luźne jeżdżenie po mieście', 'Free roam i zdjęcia o zachodzie'],
    pvp: ['Deathmatch drużynowy', 'Tryby PvP na wieczór'],
    rp: ['Wieczór roleplay – policja vs ekipa', 'Klimatyczne RP bez trollowania'],
    cars: ['Zlot aut na parkingu przy plaży', 'Sesja zdjęciowa aut'],
  };
  const msg = h('p', { class: 'ek-formmsg', 'aria-live': 'polite' });
  const titleIn = h('input', { class: 'ek-input', maxlength: 60, required: true, value: d.title, placeholder: 'np. Finał napadu – brakuje 2 osób', oninput: e => { d.title = e.target.value; } });
  const ideas = h('div', { class: 'ek-chips' });
  const drawIdeas = () => ideas.replaceChildren(...(TITLE_IDEAS[d.activity] || []).map(t => h('button', { type: 'button', class: 'ek-chip', onclick: () => { d.title = t; titleIn.value = t; titleIn.focus(); } }, t)));
  const actTiles = h('div', { class: 'ek-tiles ek-tiles--4', role: 'group', 'aria-label': 'Aktywność' });
  const drawAct = () => actTiles.replaceChildren(...Object.entries(ACT).map(([k, v]) => h('button', { type: 'button', class: 'ek-tile', 'aria-pressed': d.activity === k ? 'true' : 'false', onclick: () => { d.activity = k; drawAct(); drawIdeas(); } },
    h('span', { class: 'ek-tile__icon', 'aria-hidden': 'true' }, v.i), h('span', { class: 'ek-tile__title' }, v.l), h('span', { class: 'ek-tile__desc' }, v.d))));
  const platRow = h('div', { class: 'ek-chips', role: 'group', 'aria-label': 'Platforma' });
  const drawPlat = () => platRow.replaceChildren(...Object.keys(PLAT).map(p => chip(PLAT_L[p], d.platform === p, () => { d.platform = p; drawPlat(); }, p !== 'pc' ? 'ek-chip--' + PLAT_CLS[p] + (d.platform === p ? ' is-selected' : '') : '')));
  const customIn = h('input', { class: 'ek-input', type: 'datetime-local', value: d.custom, onchange: e => { d.custom = e.target.value; d.when = 'custom'; drawWhen(); } });
  const whenRow = h('div', { class: 'ek-chips ek-chips--wrap', role: 'group', 'aria-label': 'Start' });
  const drawWhen = () => { whenRow.replaceChildren(...[[5, 'Za 5 min'], [15, 'Za 15 min'], [30, 'Za 30 min'], [60, 'Za godzinę'], [120, 'Za 2 godziny'], ['custom', 'Inny termin']].map(([v, l]) => chip(l, d.when === v, () => { d.when = v; drawWhen(); if (v === 'custom') customIn.focus(); }))); customIn.parentElement && (customIn.closest('.ek-field').hidden = d.when !== 'custom'); };
  const slotsOut = h('output', { 'aria-live': 'polite' }, d.slots);
  const stepper = h('div', { class: 'ek-stepper' },
    h('button', { type: 'button', class: 'ek-btn ek-btn--icon', 'aria-label': 'Mniej miejsc', onclick: () => { d.slots = Math.max(2, d.slots - 1); slotsOut.textContent = d.slots; } }, '−'), slotsOut,
    h('button', { type: 'button', class: 'ek-btn ek-btn--icon', 'aria-label': 'Więcej miejsc', onclick: () => { d.slots = Math.min(8, d.slots + 1); slotsOut.textContent = d.slots; } }, '+'),
    h('span', { class: 'ek-meta' }, 'z Tobą włącznie'));
  const styleRow = h('div', { class: 'ek-chips ek-chips--wrap', role: 'group', 'aria-label': 'Styl' });
  const drawStyle = () => styleRow.replaceChildren(...Object.entries(STYLES).map(([k, v]) => chip(v, d.style === k, () => { d.style = k; drawStyle(); })));
  const details = h('textarea', { class: 'ek-textarea', maxlength: 400, placeholder: 'Co konkretnie robimy, czego wymagasz, jaki masz sprzęt w grze. Bez numerów telefonów i linków do płatnych usług.', oninput: e => { d.details = e.target.value; } }, d.details);
  drawAct(); drawIdeas(); drawPlat(); drawStyle();

  const submit = async e => {
    e.preventDefault();
    let startAt;
    if (d.when === 'custom') { const t = Date.parse(d.custom); if (!t) { msg.textContent = 'Wybierz datę i godzinę startu.'; return; } startAt = Math.floor(t / 1000); if (startAt < now()) { msg.textContent = 'Ten termin już minął. Wybierz godzinę w przyszłości.'; return; } }
    else startAt = now() + d.when * 60;
    fieldError(titleIn, '');
    if ((d.title || '').trim().length < 4) { fieldError(titleIn, 'Nazwa zlecenia musi mieć co najmniej 4 znaki.'); return; }
    const btn = e.submitter || $('button[type=submit]', e.target); btn.disabled = true; msg.textContent = '';
    try {
      const r = await api('job.create', { body: { title: d.title.trim(), activity: d.activity, platform: d.platform, slots: d.slots, startAt, style: d.style, micRequired: d.mic, details: d.details } });
      toast('Zlecenie opublikowane', 'Udostępnij link na Discordzie – tak najszybciej zbierzesz skład.', 'cash');
      refreshJobs(); location.hash = '#/z/' + r.job.id;
    } catch (err) { btn.disabled = false; msg.textContent = errMsg(err); }
  };
  const form = h('form', { class: 'ek-form', novalidate: true, onsubmit: submit },
    h('div', { class: 'ek-stack' }, groupLabel('Co robimy'), actTiles),
    h('div', { class: 'ek-stack' }, field('Nazwa zlecenia', titleIn, 'Krótko i konkretnie. Najlepiej działają nazwy z celem i brakującym składem.'), ideas),
    h('div', { class: 'ek-form__row' },
      h('div', { class: 'ek-stack' }, groupLabel('Platforma'), platRow),
      h('div', { class: 'ek-stack' }, groupLabel('Ile osób w składzie'), stepper)),
    h('div', { class: 'ek-stack' }, groupLabel('Start'), whenRow, field('Data i godzina', customIn)),
    h('div', { class: 'ek-form__row' },
      h('div', { class: 'ek-stack' }, groupLabel('Styl gry'), styleRow),
      h('div', { class: 'ek-stack' }, groupLabel('Wymagania'), toggle('Mikrofon obowiązkowy', d.mic, v => { d.mic = v; }))),
    field('Szczegóły (opcjonalnie)', details),
    msg,
    h('div', { class: 'ek-row' }, h('button', { class: 'ek-btn ek-btn--primary ek-btn--lg', type: 'submit' }, 'Wystaw zlecenie'), h('a', { class: 'ek-btn ek-btn--ghost', href: '#/' }, 'Anuluj')));
  setTimeout(drawWhen, 0);
  return [h('div', { class: 'ek-container' },
    pageHead('Nowe zlecenie', 'Wystaw zlecenie', 'Podaj aktywność, godzinę startu i liczbę miejsc. Zlecenie znika z tablicy dwie godziny po starcie.', '#/'),
    h('div', { class: 'ek-panel' }, form))];
}

/* ------------------------------------------------------------ ONBOARDING */
function viewStart() {
  if (S.token) { location.hash = '#/ja'; return []; }
  const d = { platform: '', activities: [], times: [], style: 'balanced', mic: true, nick: '', contact: '', avatar: Math.floor(Math.random() * 12), bio: '' };
  let step = 1;
  const wrap = h('div', { class: 'ek-panel' });
  const draw = () => {
    const steps = h('div', { class: 'ek-onboard__steps', 'aria-hidden': 'true' }, [1, 2, 3, 4].map(i => h('span', { class: 'ek-onboard__step' + (i < step ? ' is-done' : i === step ? ' is-current' : '') })));
    const counter = h('span', { class: 'ek-onboard__counter' }, 'Krok ' + step + ' z 4');
    let body, next, canNext = true;
    if (step === 1) {
      body = [h('h2', { class: 'ek-h2' }, 'Na czym grasz?'), h('p', { class: 'ek-meta' }, 'Pokażemy Ci zlecenia z Twojej platformy. Zmienisz to w każdej chwili.'),
        h('div', { class: 'ek-tiles', role: 'group', 'aria-label': 'Platforma' }, Object.keys(PLAT).map(p => h('button', { type: 'button', class: 'ek-tile', 'aria-pressed': d.platform === p ? 'true' : 'false', onclick: () => { d.platform = p; step = 2; draw(); } },
          h('span', { class: 'ek-tile__icon' }, p === 'pc' ? '🖥️' : '🎮'), h('span', { class: 'ek-tile__title' }, PLAT_L[p]), h('span', { class: 'ek-tile__desc' }, p === 'pc' ? 'GTA Online na PC' : 'Konsola nowej generacji'))))];
      canNext = !!d.platform;
    } else if (step === 2) {
      body = [h('h2', { class: 'ek-h2' }, 'Co lubisz robić?'), h('p', { class: 'ek-meta' }, 'Zaznacz wszystko, co Cię kręci. Dopasujemy zlecenia i ekipy.'),
        h('div', { class: 'ek-tiles ek-tiles--4', role: 'group', 'aria-label': 'Aktywności' }, Object.entries(ACT).map(([k, v]) => h('button', { type: 'button', class: 'ek-tile', 'aria-pressed': d.activities.includes(k) ? 'true' : 'false', onclick: () => { d.activities = d.activities.includes(k) ? d.activities.filter(x => x !== k) : [...d.activities, k]; draw(); } },
          h('span', { class: 'ek-tile__icon' }, v.i), h('span', { class: 'ek-tile__title' }, v.l), h('span', { class: 'ek-tile__desc' }, v.d)))),
        h('div', { class: 'ek-onboard__counter' }, d.activities.length + ' zaznaczone')];
      canNext = d.activities.length > 0;
    } else if (step === 3) {
      body = [h('h2', { class: 'ek-h2' }, 'Kiedy i jak grasz?'),
        h('div', { class: 'ek-tiles ek-tiles--4', role: 'group', 'aria-label': 'Pory gry' }, Object.entries(TIMES).map(([k, v]) => h('button', { type: 'button', class: 'ek-tile', 'aria-pressed': d.times.includes(k) ? 'true' : 'false', onclick: () => { d.times = d.times.includes(k) ? d.times.filter(x => x !== k) : [...d.times, k]; draw(); } },
          h('span', { class: 'ek-tile__icon' }, TIME_I[k]), h('span', { class: 'ek-tile__title' }, v)))),
        h('div', { class: 'ek-label', style: { marginTop: '8px' } }, 'Styl'),
        h('div', { class: 'ek-tiles', role: 'group', 'aria-label': 'Styl gry' }, Object.entries(STYLES).map(([k, v]) => h('button', { type: 'button', class: 'ek-tile', 'aria-pressed': d.style === k ? 'true' : 'false', onclick: () => { d.style = k; draw(); } },
          h('span', { class: 'ek-tile__title' }, v), h('span', { class: 'ek-tile__desc' }, STYLE_D[k])))),
        toggle('Mam mikrofon', d.mic, v => { d.mic = v; })];
      canNext = d.times.length > 0;
    } else {
      const msg = h('p', { class: 'ek-formmsg', 'aria-live': 'polite' });
      const nick = h('input', { class: 'ek-input', maxlength: 24, value: d.nick, autocomplete: 'nickname', placeholder: 'Twój nick z gry', oninput: e => { d.nick = e.target.value; } });
      const contact = discordInput(d.contact, v => { d.contact = v; });
      const hp = h('input', { class: 'ek-hp', tabindex: '-1', autocomplete: 'off', name: 'website', 'aria-hidden': 'true' });
      const avs = h('div', { class: 'ek-avatars', role: 'group', 'aria-label': 'Kolor avatara' });
      const drawAv = () => avs.replaceChildren(...AVATARS.map((_, i) => h('button', { type: 'button', class: 'ek-avatar-pick', 'aria-label': 'Avatar ' + (i + 1), 'aria-pressed': d.avatar === i ? 'true' : 'false', onclick: () => { d.avatar = i; drawAv(); } }, avatar({ nick: d.nick || 'EK', avatar: i }, '', false))));
      drawAv();
      nick.addEventListener('input', drawAv);
      const submit = async e => {
        e.preventDefault(); msg.textContent = '';
        fieldError(nick, ''); fieldError(contact, '');
        if (d.nick.trim().length < 3) { fieldError(nick, 'Nick musi mieć co najmniej 3 znaki.'); return; }
        if (!/^[A-Za-z0-9ĄĆĘŁŃÓŚŹŻąćęłńóśźż_\-. ]+$/.test(d.nick.trim())) { fieldError(nick, 'Nick może zawierać litery, cyfry, spację oraz _ - .'); return; }
        if (!DISCORD_RE.test(d.contact.trim())) { fieldError(contact, 'Wpisz nazwę użytkownika Discord: małe litery, cyfry, kropka lub podkreślnik, np. krolnapadow.'); return; }
        const btn = e.submitter; if (btn) btn.disabled = true;
        try {
          const r = await api('register', { body: { ...d, nick: d.nick.trim(), contact: d.contact.trim(), website: hp.value } });
          setToken(r.token); S.me = r.me;
          showRecovery(r.recovery, true);
        } catch (err) {
          if (btn) btn.disabled = false;
          const m = errMsg(err);
          if (/Discord/i.test(m)) fieldError(contact, m); else if (/nick/i.test(m)) fieldError(nick, m); else msg.textContent = m;
        }
      };
      body = [h('h2', { class: 'ek-h2' }, 'Twój profil'), h('p', { class: 'ek-meta' }, 'Bez maila i hasła. Na koniec dostaniesz kod odzyskiwania – zapisz go.'),
        h('form', { class: 'ek-form', onsubmit: submit, novalidate: true },
          field('Nick', nick, '3–24 znaki. Użyj nicku z gry, żeby skład mógł Cię znaleźć.'),
          field('Discord', contact, 'Nazwa użytkownika, np. krolnapadow. Widzą ją tylko ludzie przyjęci do wspólnego składu.'),
          h('div', { class: 'ek-stack' }, groupLabel('Kolor avatara'), avs), hp, msg,
          h('div', { class: 'ek-row' }, h('button', { class: 'ek-btn ek-btn--ghost', type: 'button', onclick: () => { step = 3; draw(); } }, 'Wstecz'), h('button', { class: 'ek-btn ek-btn--primary ek-btn--lg', type: 'submit' }, 'Załóż profil')),
          h('p', { class: 'ek-meta' }, 'Zakładając profil, akceptujesz ', h('a', { href: '#/zasady' }, 'zasady'), '. Serwis dla osób 16+.'))];
      canNext = false;
    }
    next = step < 4 ? h('div', { class: 'ek-row', style: { justifyContent: 'space-between' } },
      step > 1 ? h('button', { class: 'ek-btn ek-btn--ghost', onclick: () => { step--; draw(); } }, 'Wstecz') : h('a', { class: 'ek-btn ek-btn--ghost', href: '#/odzyskaj' }, 'Mam już profil'),
      h('button', { class: 'ek-btn ek-btn--primary', disabled: canNext ? null : true, onclick: () => { step++; draw(); } }, 'Dalej')) : null;
    wrap.replaceChildren(h('div', { class: 'ek-onboard' }, h('div', { class: 'ek-row', style: { justifyContent: 'space-between' } }, counter), steps, body, next));
    const firstBtn = wrap.querySelector('h2'); if (firstBtn) { firstBtn.tabIndex = -1; firstBtn.focus({ preventScroll: true }); }
  };
  draw();
  return [h('div', { class: 'ek-container', style: { maxWidth: '760px' } }, pageHead('Pierwsze wejście', 'Załóż profil gracza', 'Cztery krótkie kroki, bez maila i hasła. Potem od razu wystawiasz zlecenie albo dołączasz do składu.'), wrap)];
}
function showRecovery(code, fresh) {
  const next = store.get('ek_next'); store.set('ek_next', null);
  openSheet(fresh ? 'Profil gotowy' : 'Kod odzyskiwania',
    h('div', { class: 'ek-stack' },
      h('p', null, 'To jedyny klucz do Twojego profilu. Zapisz go w bezpiecznym miejscu – nie pokażemy go ponownie. Przyda się na nowym urządzeniu albo po wyczyszczeniu przeglądarki.'),
      h('div', { class: 'ek-recovery' }, h('div', { class: 'ek-label' }, 'Nick: ' + (S.me ? S.me.nick : '')), h('div', { class: 'ek-recovery__code' }, code),
        h('button', { class: 'ek-btn ek-btn--cash ek-btn--sm', onclick: () => copy((S.me ? S.me.nick : '') + ' / ' + code, 'Kod') }, icon('copy', 16), 'Kopiuj kod'))),
    [h('button', { class: 'ek-btn ek-btn--primary', onclick: () => { closeSheet(); location.hash = next || '#/dodaj'; } }, 'Kod zapisany')]);
  refreshMe();
}
function viewRecover() {
  const msg = h('p', { class: 'ek-formmsg', 'aria-live': 'polite' });
  const nick = h('input', { class: 'ek-input', maxlength: 24, placeholder: 'Twój nick' });
  const code = h('input', { class: 'ek-input ek-mono', maxlength: 20, placeholder: 'XXXX-XXXX-XXXX', autocomplete: 'one-time-code' });
  const submit = async e => {
    e.preventDefault(); msg.textContent = '';
    try { const r = await api('recover', { body: { nick: nick.value.trim(), code: code.value.trim() } }); setToken(r.token); S.me = r.me; toast('Jesteś z powrotem', 'Profil ' + r.me.nick + ' odzyskany.'); refreshMe(); location.hash = '#/ja'; }
    catch (err) { msg.textContent = errMsg(err); }
  };
  return [h('div', { class: 'ek-container', style: { maxWidth: '640px' } }, pageHead('Odzyskiwanie', 'Odzyskaj profil', 'Wpisz nick i kod odzyskiwania z dnia założenia profilu.'),
    h('div', { class: 'ek-panel' }, h('form', { class: 'ek-form', onsubmit: submit }, field('Nick', nick), field('Kod odzyskiwania', code), msg,
      h('div', { class: 'ek-row' }, h('button', { class: 'ek-btn ek-btn--primary', type: 'submit' }, 'Odzyskaj profil'), h('a', { class: 'ek-btn ek-btn--ghost', href: '#/start' }, 'Załóż nowy')))))];
}

/* ------------------------------------------------------------ PROFIL (rap sheet) */
function rapSheet(p, extra = {}) {
  const caseNo = 'EKP-' + String(Math.abs([...p.id].reduce((a, c) => (a * 31 + c.charCodeAt(0)) | 0, 7)) % 10000).padStart(4, '0');
  const nextAt = [1, 4, 10, 20, 40, 40][p.stars];
  const prevAt = [0, 1, 4, 10, 20, 40][p.stars];
  const progress = p.stars >= 5 ? 100 : Math.round(((p.rep - prevAt) / Math.max(1, nextAt - prevAt)) * 100);
  const since = new Date(p.created * 1000).toLocaleDateString('pl-PL', { day: 'numeric', month: 'long', year: 'numeric' });
  return h('article', { class: 'ek-rapsheet' },
    h('div', { class: 'ek-rapsheet__band' }),
    h('div', { class: 'ek-rapsheet__header' },
      h('div', { class: 'ek-rapsheet__mug' }, avatar(p, 'lg'), h('span', { class: 'ek-rapsheet__plate' }, caseNo)),
      h('div', null,
        h('div', { class: 'ek-rapsheet__case' }, 'Kartoteka · od ' + since),
        h('h1', { class: 'ek-rapsheet__name' }, p.nick),
        wanted(p.stars, 'lg'),
        h('div', { class: 'ek-meta', style: { marginTop: '6px' } }, p.online ? '● Online' : 'Widziany ' + ago(p.lastSeen)),
        extra.crew ? h('a', { class: 'ek-rapsheet__crew', href: '#/e/' + extra.crew.id }, '[' + extra.crew.tag + '] ' + extra.crew.name) : null,
        p.rep >= 10 ? h('div', null, h('span', { class: 'ek-rapsheet__stamp' }, h('span', { class: 'ek-stamp ek-stamp--ok' }, 'Zaufany'))) : null)),
    h('div', { class: 'ek-rapsheet__stats' },
      h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, p.rep), h('span', { class: 'ek-stat__label' }, 'Respekt')),
      h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, p.jobsDone), h('span', { class: 'ek-stat__label' }, 'Roboty')),
      h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, extra.hosted ?? '–'), h('span', { class: 'ek-stat__label' }, 'Wystawione'))),
    h('div', { class: 'ek-rapsheet__section ek-stack' },
      h('div', { class: 'ek-row', style: { justifyContent: 'space-between' } }, h('span', { class: 'ek-label' }, p.stars >= 5 ? 'Maksymalny poziom zaufania' : 'Do kolejnej gwiazdki'), h('span', { class: 'ek-mono ek-meta' }, p.stars >= 5 ? '★★★★★' : p.rep + '/' + nextAt)),
      h('div', { class: 'ek-progress' }, h('div', { class: 'ek-progress__bar', '--_v': progress + '%' }))),
    h('div', { class: 'ek-rapsheet__section' },
      h('dl', { class: 'ek-rapsheet__dl' },
        h('dt', null, 'Platforma'), h('dd', null, PLAT_L[p.platform]),
        h('dt', null, 'Robi'), h('dd', null, p.activities.length ? p.activities.map(a => ACT[a] ? ACT[a].l : a).join(', ') : '—'),
        h('dt', null, 'Gra'), h('dd', null, p.times.length ? p.times.map(t => TIMES[t]).join(', ') : '—'),
        h('dt', null, 'Styl'), h('dd', null, STYLES[p.style]),
        h('dt', null, 'Mikrofon'), h('dd', null, p.mic ? 'Tak' : 'Nie'))),
    p.bio ? h('div', { class: 'ek-rapsheet__section' }, h('p', { class: 'ek-rapsheet__bio' }, p.bio)) : null,
    extra.cta ? h('div', { class: 'ek-rapsheet__cta' }, extra.cta) : null);
}
async function viewPlayer(id) {
  if (S.me && S.me.id === id) { location.hash = '#/ja'; return []; }
  let d;
  try { d = await api('player', { params: { id } }); }
  catch (e) { return [h('div', { class: 'ek-container' }, pageHead('Kartoteka', 'Nie ma takiego gracza', null, '#/'), empty('Profil niedostępny', errMsg(e)))]; }
  const p = d.player;
  document.title = p.nick + ' – kartoteka – Ekipaż';
  const theirJobs = S.jobs.filter(j => j.owner && j.owner.id === p.id && j.status !== 'closed');
  return [h('div', { class: 'ek-container' },
    h('div', { class: 'ek-page-head', style: { paddingBottom: '16px' } }, h('a', { class: 'ek-back', href: '#/' }, icon('arrow', 16), 'Wróć')),
    h('div', { class: 'ek-profile' },
      rapSheet(p, { crew: d.crew, hosted: d.hosted, cta: [
        h('button', { class: 'ek-btn ek-btn--secondary', onclick: () => share(p.nick + ' na Ekipażu', '#/g/' + p.id) }, icon('share'), 'Udostępnij'),
        h('button', { class: 'ek-btn ek-btn--ghost ek-btn--icon', 'aria-label': 'Zgłoś gracza', onclick: () => reportSheet('player', p.id) }, icon('flag'))] }),
      h('div', { class: 'ek-stack' },
        sectionHead('Aktywne zlecenia'),
        theirJobs.length ? h('div', { class: 'ek-grid' }, theirJobs.map(jobCard)) : h('p', { class: 'ek-meta' }, 'Teraz nic nie wystawia. Zajrzyj później albo zaproś do swojego zlecenia.'),
        sectionHead('Respekt od'),
        d.vouchers.length ? h('ul', { class: 'ek-crewlist' }, d.vouchers.map(v => h('li', { class: 'ek-person' }, avatar(v), h('div', null, playerLink(v), h('span', { class: 'ek-person__sub' }, PLAT[v.platform])), wanted(v.stars)))) :
          h('p', { class: 'ek-meta' }, 'Jeszcze nikt nie dał respektu. Pierwsza wspólna robota to zmieni.'))))];
}

/* ------------------------------------------------------------ JA */
async function viewMe() {
  if (needProfile('#/ja')) return [];
  try { await refreshMe(); } catch (e) {}
  const M = S.meData;
  if (!M) return [h('div', { class: 'ek-container' }, pageHead('Twój profil', 'Nie wczytaliśmy profilu', null), empty('Brak połączenia', 'Spróbuj odświeżyć stronę za chwilę.'))];
  const me = M.me;
  document.title = 'Mój profil – Ekipaż';
  const tabs = [
    ['inbox', 'Zgłoszenia', M.inbox.length], ['mates', 'Respekt do dania', M.mates.length], ['jobs', 'Moje zlecenia', M.jobs.length],
    ['joined', 'Gdzie wchodzę', M.joined.length], ['edit', 'Edytuj profil', 0],
  ];
  const panel = h('div');
  const tabBar = h('div', { class: 'ek-tabs', role: 'tablist' });
  const draw = () => {
    tabBar.replaceChildren(...tabs.map(([k, l, n]) => h('button', { class: 'ek-tab', role: 'tab', 'aria-selected': S.meTab === k ? 'true' : 'false', onclick: () => { S.meTab = k; draw(); } }, l, n ? h('span', { class: k === 'inbox' || k === 'mates' ? 'ek-dot-inline' : 'ek-chip__count', style: { marginLeft: '6px' } }, n) : null)));
    let content;
    if (S.meTab === 'inbox') {
      content = M.inbox.length ? h('ul', { class: 'ek-crewlist' }, M.inbox.map(r => requestRow(r, null))) :
        empty('Brak nowych zgłoszeń', M.jobs.length ? 'Udostępnij link do zlecenia na Discordzie albo w grupie – tak najszybciej zbierzesz skład.' : 'Wystaw zlecenie. Zgłoszenia graczy pojawią się tutaj.', h('a', { class: 'ek-btn ek-btn--primary', href: '#/dodaj' }, 'Wystaw zlecenie'));
    } else if (S.meTab === 'mates') {
      content = M.mates.length ? h('div', { class: 'ek-stack' }, h('p', { class: 'ek-meta' }, 'Gracze z Twoich składów z ostatnich 48 godzin. Daj +1 tym, którzy dowieźli – to ich reputacja na kolejne zlecenia.'),
        h('ul', { class: 'ek-crewlist' }, M.mates.map(m => h('li', { class: 'ek-person' }, avatar(m.player), h('div', null, playerLink(m.player), h('span', { class: 'ek-person__sub' }, m.jobTitle)),
          h('button', { class: 'ek-btn ek-btn--cash ek-btn--sm', onclick: async ev => {
            const btn = ev.currentTarget; btn.disabled = true;
            try { await api('vouch', { body: { to: m.player.id, jobId: m.jobId } }); toast('Czysta robota +1', m.player.nick + ' dostaje respekt.', 'cash'); await refreshMe(); draw(); }
            catch (e) { btn.disabled = false; toast('Nie udało się', errMsg(e), 'danger'); }
          } }, '★ Czysta robota +1'))))) :
        empty('Brak graczy do oceny', 'Oceniasz osoby ze wspólnego składu, od 15 minut do 48 godzin po starcie zlecenia.', null, 'star');
    } else if (S.meTab === 'jobs' || S.meTab === 'joined') {
      const list = S.meTab === 'jobs' ? M.jobs : M.joined;
      content = list.length ? h('div', { class: 'ek-grid' }, list.map(jobCard)) :
        empty(S.meTab === 'jobs' ? 'Brak Twoich zleceń' : 'Nigdzie nie wchodzisz', S.meTab === 'jobs' ? 'Twoje aktywne zlecenia pojawią się tutaj.' : 'Zgłoś się do zlecenia z tablicy – status zobaczysz tutaj.', h('a', { class: 'ek-btn ek-btn--primary', href: S.meTab === 'jobs' ? '#/dodaj' : '#/' }, S.meTab === 'jobs' ? 'Wystaw zlecenie' : 'Przeglądaj tablicę'));
    } else {
      content = editProfile(me);
    }
    panel.replaceChildren(content);
  };
  draw();
  return [h('div', { class: 'ek-container' },
    h('div', { class: 'ek-page-head', style: { paddingBottom: '16px' } }, h('div', { class: 'ek-kicker' }, 'Twoja kartoteka')),
    h('div', { class: 'ek-profile ek-profile--me' },
      rapSheet(me, { crew: M.crew, hosted: M.hosted, cta: [
        h('button', { class: 'ek-btn ek-btn--primary', onclick: () => share('Moja kartoteka na Ekipażu', '#/g/' + me.id) }, icon('share'), 'Udostępnij profil'),
        h('button', { class: 'ek-btn ek-btn--ghost ek-btn--icon', 'aria-label': 'Wyloguj', onclick: logout }, icon('logout'))] }),
      h('div', null, tabBar, panel)))];
}
function editProfile(me) {
  const d = { platform: me.platform, activities: [...me.activities], times: [...me.times], style: me.style, mic: me.mic, contact: me.contact || '', bio: me.bio || '', avatar: me.avatar };
  const msg = h('p', { class: 'ek-formmsg', 'aria-live': 'polite' });
  const plat = h('div', { class: 'ek-chips ek-chips--wrap' }), acts = h('div', { class: 'ek-chips ek-chips--wrap' }), times = h('div', { class: 'ek-chips ek-chips--wrap' }), styles = h('div', { class: 'ek-chips ek-chips--wrap' }), avs = h('div', { class: 'ek-avatars' });
  const redraw = () => {
    plat.replaceChildren(...Object.keys(PLAT).map(p => chip(PLAT_L[p], d.platform === p, () => { d.platform = p; redraw(); })));
    acts.replaceChildren(...Object.entries(ACT).map(([k, v]) => chip(v.i + ' ' + v.l, d.activities.includes(k), () => { d.activities = d.activities.includes(k) ? d.activities.filter(x => x !== k) : [...d.activities, k]; redraw(); })));
    times.replaceChildren(...Object.entries(TIMES).map(([k, v]) => chip(v, d.times.includes(k), () => { d.times = d.times.includes(k) ? d.times.filter(x => x !== k) : [...d.times, k]; redraw(); })));
    styles.replaceChildren(...Object.entries(STYLES).map(([k, v]) => chip(v, d.style === k, () => { d.style = k; redraw(); })));
    avs.replaceChildren(...AVATARS.map((_, i) => h('button', { type: 'button', class: 'ek-avatar-pick', 'aria-label': 'Avatar ' + (i + 1), 'aria-pressed': d.avatar === i ? 'true' : 'false', onclick: () => { d.avatar = i; redraw(); } }, avatar({ nick: me.nick, avatar: i }, '', false))));
  };
  redraw();
  const contact = discordInput(d.contact, v => { d.contact = v; });
  const bio = h('textarea', { class: 'ek-textarea', maxlength: 280, placeholder: 'Kilka słów: co masz w grze, jak grasz, czego szukasz.', oninput: e => { d.bio = e.target.value; } }, d.bio);
  return h('form', { class: 'ek-form', onsubmit: async e => {
    e.preventDefault(); msg.className = 'ek-formmsg'; msg.textContent = ''; fieldError(contact, '');
    if (!DISCORD_RE.test(d.contact.trim())) { fieldError(contact, 'Wpisz nazwę użytkownika Discord: małe litery, cyfry, kropka lub podkreślnik.'); return; }
    try { const r = await api('profile.update', { body: d }); S.me = r.me; msg.className = 'ek-formmsg is-ok'; msg.textContent = 'Zapisane. Kartoteka zaktualizowana.'; toast('Profil zapisany'); refreshMe().then(() => { if (route().name === 'me') render(); }); }
    catch (err) { msg.textContent = errMsg(err); }
  } },
    h('div', { class: 'ek-stack' }, groupLabel('Avatar'), avs),
    h('div', { class: 'ek-stack' }, groupLabel('Platforma'), plat),
    h('div', { class: 'ek-stack' }, groupLabel('Co robisz'), acts),
    h('div', { class: 'ek-stack' }, groupLabel('Kiedy grasz'), times),
    h('div', { class: 'ek-stack' }, groupLabel('Styl'), styles),
    toggle('Mam mikrofon', d.mic, v => { d.mic = v; }),
    field('Discord', contact, 'Nazwa użytkownika z Discorda. Widzą ją tylko gracze z Twoich składów.'),
    field('O mnie', bio),
    msg,
    h('div', { class: 'ek-row' }, h('button', { class: 'ek-btn ek-btn--primary', type: 'submit' }, 'Zapisz zmiany'),
      h('button', { class: 'ek-btn ek-btn--ghost', type: 'button', onclick: logout }, icon('logout', 16), 'Wyloguj z tego urządzenia')),
    h('p', { class: 'ek-meta' }, 'Wylogowanie usuwa klucz z tej przeglądarki. Wrócisz kodem odzyskiwania z pierwszego logowania.'));
}
function logout() {
  openSheet('Wylogować?', h('p', null, 'Do profilu wrócisz tylko z kodem odzyskiwania. Masz go zapisanego?'),
    [h('button', { class: 'ek-btn ek-btn--ghost', onclick: closeSheet }, 'Zostaję'), h('button', { class: 'ek-btn ek-btn--danger', onclick: async () => { try { await api('logout', { body: {} }); } catch (e) {} setToken(null); closeSheet(); toast('Wylogowano', 'Wrócisz kodem odzyskiwania.', 'info'); location.hash = '#/'; renderChrome(); } }, 'Wyloguj')]);
}

/* ------------------------------------------------------------ EKIPY */
function crewCard(c) {
  return h('article', { class: 'ek-crew ek-crew--c' + c.color },
    h('div', { class: 'ek-crew__emblem', 'aria-hidden': 'true' }, c.tag),
    h('div', null, h('h3', { class: 'ek-crew__name' }, h('a', { href: '#/e/' + c.id }, c.name)), h('div', { class: 'ek-row' }, h('span', { class: 'ek-crew__tag' }, '[' + c.tag + ']'), platTag(c.platform), h('span', { class: 'ek-badge' }, (ACT[c.focus] || ACT.heist).l))),
    c.details ? h('p', { class: 'ek-crew__desc' }, c.details.length > 120 ? c.details.slice(0, 118) + '…' : c.details) : null,
    h('div', { class: 'ek-crew__foot' },
      h('div', { class: 'ek-crew__members' }, c.members.slice(0, 5).map(m => avatar(m, '', false)), h('span', { class: 'ek-crew__count' }, c.count + ' ' + plural(c.count, 'członek', 'członków', 'członków') + ' · ★ ' + c.rep)),
      c.mine ? h('span', { class: 'ek-badge ek-badge--gold' }, 'Twoja ekipa') : c.recruiting ? h('button', { class: 'ek-btn ek-btn--secondary ek-btn--sm', onclick: e => { e.stopPropagation(); joinCrew(c); } }, 'Dołącz') : h('span', { class: 'ek-crew__lock' }, '🔒 Rekrutacja zamknięta')));
}
async function joinCrew(c) {
  if (needProfile('#/e/' + c.id)) return;
  try { await api('crew.join', { body: { id: c.id } }); toast('Witaj w ' + c.name, 'Jesteś teraz częścią ekipy [' + c.tag + '].', 'cash'); await refreshMe(); render(); }
  catch (e) { toast('Nie udało się', errMsg(e), 'danger'); }
}
async function viewCrews() {
  let crews = [];
  const plat = S.filters.platform;
  try { crews = (await api('crews', { params: plat ? { platform: plat } : {} })).crews; } catch (e) { return [h('div', { class: 'ek-container' }, pageHead('Ekipy', 'Ekipy', null), empty('Brak połączenia', errMsg(e)))]; }
  const myCrew = S.meData && S.meData.crew;
  return [h('div', { class: 'ek-container' },
    pageHead('Stałe składy', 'Ekipy', 'Gracie regularnie w tym samym gronie? Załóż ekipę z własnym tagiem, budujcie wspólną reputację i rekrutujcie nowych graczy.'),
    h('div', { class: 'ek-row', style: { marginBottom: '16px', justifyContent: 'space-between' } },
      h('div', { class: 'ek-chips' }, chip('Wszystkie', !plat, () => { S.filters.platform = ''; store.set('ek_f_platform', ''); render(); }), ...Object.keys(PLAT).map(p => chip(PLAT_L[p], plat === p, () => { S.filters.platform = p; store.set('ek_f_platform', p); render(); }))),
      myCrew ? h('a', { class: 'ek-btn ek-btn--secondary', href: '#/e/' + myCrew.id }, 'Moja ekipa') : h('button', { class: 'ek-btn ek-btn--primary', onclick: createCrew }, icon('plus'), 'Załóż ekipę')),
    crews.length ? h('div', { class: 'ek-grid' }, crews.map(crewCard)) :
      empty('Nie ma jeszcze żadnej ekipy', 'Załóż pierwszą. Dostaniesz własny tag, wspólny ranking i stronę rekrutacyjną dla nowych graczy.', myCrew ? null : h('button', { class: 'ek-btn ek-btn--primary', onclick: createCrew }, 'Załóż ekipę')))];
}
function createCrew() {
  if (needProfile('#/ekipy')) return;
  const d = { name: '', tag: '', details: '', platform: (S.me && S.me.platform) || 'ps5', focus: 'heist', recruiting: true, color: 1 };
  const msg = h('p', { class: 'ek-formmsg', 'aria-live': 'polite' });
  const name = h('input', { class: 'ek-input', maxlength: 28, placeholder: 'np. Nocna Zmiana', oninput: e => { d.name = e.target.value; if (!tag.dataset.touched) { tag.value = d.name.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[łŁ]/g, m => m === 'ł' ? 'l' : 'L').replace(/[^A-Za-z0-9 ]/g, '').split(/\s+/).map(w => w[0] || '').join('').slice(0, 4).toUpperCase(); d.tag = tag.value; } } });
  const tag = h('input', { class: 'ek-input ek-mono', maxlength: 4, placeholder: 'NZ', oninput: e => { e.target.dataset.touched = '1'; e.target.value = e.target.value.toUpperCase().replace(/[^A-Z0-9]/g, ''); d.tag = e.target.value; } });
  const det = h('textarea', { class: 'ek-textarea', maxlength: 300, placeholder: 'Czym się zajmujecie, kiedy gracie, kogo szukacie.', oninput: e => { d.details = e.target.value; } });
  const focus = h('select', { class: 'ek-select', onchange: e => { d.focus = e.target.value; } }, Object.entries(ACT).map(([k, v]) => h('option', { value: k }, v.l)));
  const plat = h('select', { class: 'ek-select', onchange: e => { d.platform = e.target.value; } }, Object.keys(PLAT).map(p => h('option', { value: p, selected: d.platform === p ? true : null }, PLAT_L[p])));
  const sw = h('div', { class: 'ek-swatches', role: 'group', 'aria-label': 'Kolor ekipy' });
  const drawSw = () => sw.replaceChildren(...CREW_COLORS.map((c, i) => h('button', { type: 'button', class: 'ek-swatch', style: { background: c }, 'aria-label': 'Kolor ' + (i + 1), 'aria-pressed': d.color === i ? 'true' : 'false', onclick: () => { d.color = i; drawSw(); } })));
  drawSw();
  openSheet('Nowa ekipa', h('form', { class: 'ek-form', id: 'crewForm', onsubmit: async e => {
    e.preventDefault(); msg.textContent = '';
    try { const r = await api('crew.create', { body: d }); closeSheet(); toast('Ekipa założona', '[' + r.crew.tag + '] ' + r.crew.name + ' – czas na rekrutację.', 'cash'); await refreshMe(); location.hash = '#/e/' + r.crew.id; }
    catch (err) { msg.textContent = errMsg(err); }
  } }, h('div', { class: 'ek-form__row' }, field('Nazwa', name), field('Tag (2–4 znaki)', tag)), h('div', { class: 'ek-form__row' }, field('Specjalizacja', focus), field('Platforma', plat)),
    field('Opis', det), h('div', { class: 'ek-stack' }, groupLabel('Kolor'), sw), toggle('Otwarta rekrutacja', true, v => { d.recruiting = v; }), msg),
    [h('button', { class: 'ek-btn ek-btn--ghost', type: 'button', onclick: closeSheet }, 'Anuluj'), h('button', { class: 'ek-btn ek-btn--primary', type: 'submit', form: 'crewForm' }, 'Załóż ekipę')]);
}
async function viewCrew(id) {
  let c;
  try { c = (await api('crew', { params: { id } })).crew; } catch (e) { return [h('div', { class: 'ek-container' }, pageHead('Ekipa', 'Nie ma takiej ekipy', null, '#/ekipy'), empty('Ekipa została rozwiązana', errMsg(e)))]; }
  document.title = c.name + ' – ekipa – Ekipaż';
  const isBoss = S.me && c.ownerId === S.me.id;
  const myCrew = S.meData && S.meData.crew;
  let actions;
  if (c.mine) actions = [h('button', { class: 'ek-btn ek-btn--cash', onclick: () => share('Dołącz do ' + c.name, '#/e/' + c.id) }, icon('share'), 'Zaproś ludzi'),
    isBoss ? h('button', { class: 'ek-btn ek-btn--secondary', onclick: async () => { try { await api('crew.update', { body: { details: c.details, recruiting: !c.recruiting } }); toast(c.recruiting ? 'Rekrutacja zamknięta' : 'Rekrutacja otwarta'); render(); } catch (e) { toast('Nie udało się', errMsg(e), 'danger'); } } }, c.recruiting ? 'Zamknij rekrutację' : 'Otwórz rekrutację') : null,
    h('button', { class: 'ek-btn ek-btn--ghost', onclick: () => openSheet('Odejść z ekipy?', h('p', null, isBoss ? 'Jesteś szefem. Władzę przejmie członek z najwyższym respektem, a jeśli nikogo nie ma – ekipa zostanie rozwiązana.' : 'Zawsze możesz wrócić, jeśli rekrutacja będzie otwarta.'),
      [h('button', { class: 'ek-btn ek-btn--ghost', onclick: closeSheet }, 'Zostaję'), h('button', { class: 'ek-btn ek-btn--danger', onclick: async () => { try { await api('crew.leave', { body: {} }); closeSheet(); toast('Nie jesteś już w ekipie', 'Drzwi zostają otwarte, jeśli rekrutacja ruszy.', 'info'); await refreshMe(); location.hash = '#/ekipy'; } catch (e) { toast('Nie udało się', errMsg(e), 'danger'); } } }, 'Odchodzę')]) }, 'Odejdź')];
  else if (c.recruiting && !myCrew) actions = [h('button', { class: 'ek-btn ek-btn--primary ek-btn--lg', onclick: () => joinCrew(c) }, 'Dołącz do ekipy'), h('button', { class: 'ek-btn ek-btn--secondary ek-btn--icon', 'aria-label': 'Udostępnij', onclick: () => share(c.name, '#/e/' + c.id) }, icon('share'))];
  else actions = [h('span', { class: 'ek-meta', style: { flex: 1 } }, myCrew ? 'Jesteś już w innej ekipie.' : 'Rekrutacja zamknięta.'), h('button', { class: 'ek-btn ek-btn--ghost ek-btn--icon', 'aria-label': 'Zgłoś ekipę', onclick: () => reportSheet('crew', c.id) }, icon('flag'))];
  return [h('div', { class: 'ek-container' },
    h('div', { class: 'ek-page-head', style: { paddingBottom: 0 } }, h('a', { class: 'ek-back', href: '#/ekipy' }, icon('arrow', 16), 'Ekipy')),
    h('div', { class: 'ek-detail' },
      h('div', null,
        h('article', { class: 'ek-detail__poster ek-halftone ek-crew--c' + c.color, style: { '--_crew': CREW_COLORS[c.color] } },
          h('div', { class: 'ek-row' }, h('div', { class: 'ek-crew__emblem' }, c.tag), h('div', null, h('div', { class: 'ek-kicker' }, 'Ekipa · ' + (ACT[c.focus] || ACT.heist).l), platTag(c.platform))),
          h('h1', { class: 'ek-display' }, c.name),
          h('div', { class: 'ek-detail__grid' },
            h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, c.count), h('span', { class: 'ek-stat__label' }, 'Członkowie')),
            h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, c.rep), h('span', { class: 'ek-stat__label' }, 'Respekt')),
            h('div', { class: 'ek-stat' }, h('span', { class: 'ek-stat__value' }, c.recruiting ? 'TAK' : 'NIE'), h('span', { class: 'ek-stat__label' }, 'Rekrutacja'))),
          c.details ? h('p', { class: 'ek-lead', style: { whiteSpace: 'pre-line' } }, c.details) : null),
        h('div', { class: 'ek-detail__cta' }, actions)),
      h('section', { class: 'ek-card ek-stack' }, h('h2', { class: 'ek-h3' }, 'Skład ekipy'),
        h('ul', { class: 'ek-crewlist' }, c.members.map(m => h('li', { class: 'ek-person' }, avatar(m), h('div', null, playerLink(m), h('span', { class: 'ek-person__sub' }, m.role === 'boss' ? 'Szef' : 'Członek')), wanted(m.stars)))))))];
}

/* ------------------------------------------------------------ RANKING */
async function viewRanking() {
  let d;
  try { d = await api('leaderboard', { params: { period: S.lbPeriod, ...(S.lbPlatform ? { platform: S.lbPlatform } : {}) } }); }
  catch (e) { return [h('div', { class: 'ek-container' }, pageHead('Ranking', 'Najbardziej zaufani', null), empty('Brak połączenia', errMsg(e)))]; }
  const seg = (opts, val, set) => h('div', { class: 'ek-segmented', role: 'group' }, opts.map(([k, l]) => h('button', { class: 'ek-segmented__btn', 'aria-pressed': val === k ? 'true' : 'false', onclick: () => { set(k); render(); } }, l)));
  let list;
  if (S.lbTab === 'players') {
    const rows = d.players;
    const meIdx = S.me ? rows.findIndex(r => r.id === S.me.id) : -1;
    list = rows.length ? h('ol', { class: 'ek-lb' }, rows.map((p, i) => h('li', null, h('a', { class: 'ek-lb__row' + (i < 3 ? ' is-top' : '') + (i === meIdx ? ' is-me' : ''), href: '#/g/' + p.id },
        i < 3 ? h('span', { class: 'ek-medal ek-medal--' + (i + 1) }, i + 1) : h('span', { class: 'ek-lb__rank' }, i + 1),
        avatar(p), h('span', { style: { minWidth: 0 } }, h('span', { class: 'ek-lb__name' }, p.nick), h('span', { class: 'ek-lb__sub' }, PLAT[p.platform] + ' · ' + wantedText(p.stars))),
        h('span', { class: 'ek-lb__score' }, '+' + p.score)))),
        S.me && meIdx === -1 ? h('li', null, h('div', { class: 'ek-lb__row is-me is-pinned' }, h('span', { class: 'ek-lb__rank' }, '–'), avatar(S.me), h('span', null, h('span', { class: 'ek-lb__name' }, S.me.nick), h('span', { class: 'ek-lb__sub' }, 'Jeszcze bez respektu w tym okresie')), h('span', { class: 'ek-lb__score' }, '0'))) : null) :
      empty('Ranking ruszy po pierwszych grach', 'Oceny pojawiają się po wspólnych robotach. Wystaw zlecenie, zagraj z ekipą i zdobądź pierwsze +1.', h('a', { class: 'ek-btn ek-btn--primary', href: '#/dodaj' }, 'Wystaw zlecenie'), 'star');
  } else {
    list = d.crews.length ? h('ol', { class: 'ek-lb' }, d.crews.map((c, i) => h('li', null, h('a', { class: 'ek-lb__row' + (i < 3 ? ' is-top' : ''), href: '#/e/' + c.id },
      i < 3 ? h('span', { class: 'ek-medal ek-medal--' + (i + 1) }, i + 1) : h('span', { class: 'ek-lb__rank' }, i + 1),
      h('span', { class: 'ek-avatar', style: { background: CREW_COLORS[c.color] } }, c.tag.slice(0, 2)),
      h('span', { style: { minWidth: 0 } }, h('span', { class: 'ek-lb__name' }, c.name), h('span', { class: 'ek-lb__sub' }, '[' + c.tag + '] · ' + c.count + ' ' + plural(c.count, 'członek', 'członków', 'członków'))),
      h('span', { class: 'ek-lb__score' }, '★ ' + c.score))))) : empty('Brak ekip w rankingu', 'Załóż ekipę i zbierajcie respekt razem.', h('a', { class: 'ek-btn ek-btn--primary', href: '#/ekipy' }, 'Zobacz ekipy'), 'star');
  }
  return [h('div', { class: 'ek-container', style: { maxWidth: '820px' } },
    pageHead('Ranking', S.lbTab === 'players' ? (S.lbPeriod === 'week' ? 'Najlepiej oceniani w tym tygodniu' : S.lbPeriod === 'month' ? 'Najlepiej oceniani w tym miesiącu' : 'Najlepiej oceniani od startu') : 'Najmocniejsze ekipy', 'Liczą się wyłącznie oceny od graczy ze wspólnych składów. Nie da się ich kupić ani nabić samemu.'),
    h('div', { class: 'ek-lb-head' },
      seg([['players', 'Gracze'], ['crews', 'Ekipy']], S.lbTab, v => { S.lbTab = v; }),
      S.lbTab === 'players' ? seg([['week', 'Tydzień'], ['month', 'Miesiąc'], ['all', 'Zawsze']], S.lbPeriod, v => { S.lbPeriod = v; }) : null),
    S.lbTab === 'players' ? h('div', { class: 'ek-chips', style: { marginBottom: '16px' } }, chip('Wszystkie platformy', !S.lbPlatform, () => { S.lbPlatform = ''; render(); }), ...Object.keys(PLAT).map(p => chip(PLAT_L[p], S.lbPlatform === p, () => { S.lbPlatform = p; render(); }))) : null,
    list)];
}
function wantedText(n) { return n ? '★'.repeat(n) : 'bez gwiazdek'; }

/* ------------------------------------------------------------ PLAN / ZASADY / ADMIN */
async function viewPlan() {
  let v = { counts: {}, mine: [] };
  try { v = await api('votes'); } catch (e) {}
  const max = Math.max(1, ...Object.values(v.counts));
  const mine = new Set(v.mine);
  return [h('div', { class: 'ek-container' },
    pageHead('Roadmapa', 'Co budujemy dalej', 'Zagłosuj na funkcje, których potrzebujesz. Najczęściej wybierane wdrażamy jako pierwsze.'),
    h('div', { class: 'ek-roadmap' }, FEATURES.map(f => {
      const n = v.counts[f.id] || 0, on = mine.has(f.id);
      return h('article', { class: 'ek-feature' }, h('h3', { class: 'ek-feature__title' }, f.t), h('p', null, f.d),
        h('div', { class: 'ek-feature__bar' }, h('i', { '--_v': Math.round(n / max * 100) + '%' })),
        h('div', { class: 'ek-feature__foot' }, h('span', { class: 'ek-meta ek-mono' }, n + ' ' + plural(n, 'głos', 'głosy', 'głosów')),
          h('button', { class: 'ek-btn ek-btn--sm ' + (on ? 'ek-btn--cash' : 'ek-btn--secondary'), 'aria-pressed': on ? 'true' : 'false', onclick: async () => {
            if (needProfile('#/plan')) return;
            try { await api('vote', { body: { feature: f.id, on: !on } }); render(); } catch (e) { toast('Nie udało się', errMsg(e), 'danger'); }
          } }, on ? '✓ Chcę to' : 'Chcę to')));
    })))];
}
function viewRules() {
  const li = t => h('li', null, t);
  return [h('div', { class: 'ek-container' }, pageHead('Zasady', 'Zasady', 'Kilka reguł, które trzymają poziom tablicy. Pilnujemy ich bez wyjątków.'),
    h('div', { class: 'ek-prose' },
      h('h2', { class: 'ek-h3' }, 'Gramy czysto'),
      h('ul', null, li('Zero cheatów, modmenu, handlu kontami, walutą z gry i „money dropów”. Za to od razu ban.'), li('Zero oszustw – obiecujesz udział w łupie, to dzielisz.'), li('Szanujemy się na czacie. Toksyczność zgłaszaj przyciskiem z flagą.'), li('Respekt dajesz tylko za prawdziwą, wspólną grę. Farmienie respektu = reset kartoteki.')),
      h('h2', { class: 'ek-h3' }, 'Moderacja'),
      h('p', null, 'Trzy niezależne zgłoszenia automatycznie zdejmują zlecenie z tablicy do czasu sprawdzenia. Moderacja może zablokować profil, który łamie zasady.'),
      h('h2', { class: 'ek-h3' }, 'Prywatność'),
      h('ul', null, li('Nie zbieramy maili ani haseł. Profil to nick, preferencje i Discord.'), li('Discord widzą tylko osoby przyjęte do wspólnego składu.'), li('Do ochrony przed spamem przechowujemy skrót (hash) adresu IP przez maksymalnie 24 godziny.'), li('Klucz do profilu trzymamy w Twojej przeglądarce. W bazie leży tylko jego skrót.'), li('Chcesz usunąć profil? Napisz do administratora serwisu.')),
      h('h2', { class: 'ek-h3' }, 'Dla kogo'),
      h('p', null, 'Ekipaż jest dla osób, które ukończyły 16 lat. To niezależny projekt fanowski, niezwiązany z Rockstar Games ani Take-Two Interactive.')))];
}
async function viewAdmin() {
  let key = ''; try { key = sessionStorage.getItem('ek_admin') || ''; } catch (e) {}
  const keyIn = h('input', { class: 'ek-input', type: 'password', value: key, placeholder: 'Klucz admina z data/config.php', autocomplete: 'off' });
  const out = h('div', { class: 'ek-stack' });
  const call = async (a, body) => {
    const r = await fetch(API + '?a=' + a, { method: body ? 'POST' : 'GET', headers: { 'X-Ekipaz-Admin': keyIn.value, ...(body ? { 'Content-Type': 'application/json' } : {}) }, body: body ? JSON.stringify(body) : undefined }).then(x => x.json()).catch(() => null);
    if (!r || !r.ok) throw r || { message: 'Brak połączenia.' };
    return r;
  };
  const act = async (a, body, msg) => { try { await call(a, body); toast(msg); load(); } catch (e) { toast('Nie udało się', errMsg(e), 'danger'); } };
  const load = async () => {
    try { sessionStorage.setItem('ek_admin', keyIn.value); } catch (e) {}
    try {
      const r = await call('admin.reports');
      out.replaceChildren(r.reports.length ? h('ul', { class: 'ek-crewlist' }, r.reports.map(rep => h('li', { class: 'ek-person ek-person--req' }, h('span', { class: 'ek-badge' }, rep.target_type), h('div', null,
        h('a', { class: 'ek-person__name', href: rep.target_type === 'job' ? '#/z/' + rep.target_id : rep.target_type === 'crew' ? '#/e/' + rep.target_id : '#/g/' + rep.target_id }, rep.target_id),
        h('span', { class: 'ek-person__sub' }, REPORT_REASONS[rep.reason] + ' · ' + ago(rep.created))), h('span'),
        h('div', { class: 'ek-person__actions' },
          rep.target_type === 'job' ? h('button', { class: 'ek-btn ek-btn--secondary ek-btn--sm', onclick: () => act('admin.unhide', { id: rep.target_id }, 'Zlecenie przywrócone') }, 'Przywróć zlecenie') : null,
          rep.target_type === 'player' ? h('button', { class: 'ek-btn ek-btn--danger ek-btn--sm', onclick: () => act('admin.ban', { id: rep.target_id }, 'Gracz zablokowany') }, 'Zablokuj gracza') : null,
          h('button', { class: 'ek-btn ek-btn--ghost ek-btn--sm', onclick: () => act('admin.resolve', { rid: rep.id }, 'Zgłoszenie zamknięte') }, 'Bez akcji'))))) : h('p', { class: 'ek-meta' }, 'Brak otwartych zgłoszeń. Spokojna noc na mieście.'));
    } catch (e) { out.replaceChildren(h('p', { class: 'ek-formmsg' }, errMsg(e))); }
  };
  if (key) setTimeout(load, 0);
  return [h('div', { class: 'ek-container', style: { maxWidth: '760px' } }, pageHead('Moderacja', 'Panel moderatora', 'Klucz trzymamy tylko do zamknięcia karty.'), h('div', { class: 'ek-panel ek-stack' }, field('Klucz', keyIn), h('button', { class: 'ek-btn ek-btn--primary', onclick: load }, 'Pokaż zgłoszenia'), out))];
}

/* ------------------------------------------------------------ odświeżanie danych */
async function refreshJobs() {
  try {
    const [j, s] = await Promise.all([api('jobs'), api('stats')]);
    S.jobs = j.jobs; S.stats = s; S.jobsLoaded = true;
    store.set('ek_cache', JSON.stringify({ jobs: S.jobs, stats: S.stats, t: now() }));
  } catch (e) {
    if (!S.jobsLoaded) {
      try { const c = JSON.parse(store.get('ek_cache') || 'null'); if (c) { S.jobs = c.jobs; S.stats = c.stats; } } catch (x) {}
      S.jobsLoaded = true;
    }
  }
  if (route().name === 'board') renderBoardList();
  renderSide(); renderRail();
}
async function refreshMe() {
  if (!S.token) { S.meData = null; renderChrome(); return; }
  try {
    const prev = S.meData ? S.meData.inbox.length : null;
    S.meData = await api('me'); S.me = S.meData.me;
    if (prev !== null && S.meData.inbox.length > prev) toast('Ktoś puka do składu', S.meData.inbox[0].player.nick + ' chce wejść w: ' + S.meData.inbox[0].jobTitle, 'info');
  } catch (e) {}
  renderChrome();
}

/* ------------------------------------------------------------ chrome i router */
function renderChrome() {
  renderSide(); renderRail();
  const r = route();
  const navKey = { board: 'board', job: 'board', crews: 'crews', crew: 'crews', ranking: 'ranking', me: 'me', player: '', add: 'add', plan: 'plan' }[r.name] || '';
  document.querySelectorAll('[data-nav]').forEach(a => { if (a.dataset.nav === navKey) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
  const n = S.meData ? S.meData.inbox.length + S.meData.mates.length : 0;
  const dot = $('#navDot'); dot.hidden = !n; dot.textContent = n > 9 ? '9+' : n;
  const act = $('#topActions');
  act.replaceChildren(
    h('a', { class: 'ek-btn ek-btn--primary ek-btn--sm ek-topbar__cta', href: '#/dodaj' }, icon('plus', 16), 'Wystaw zlecenie'),
    S.me ? h('a', { class: 'ek-topbar__me', href: '#/ja', 'aria-label': 'Mój profil' + (n ? ', ' + n + ' powiadomień' : '') }, avatar(S.me, 'sm'), h('span', null, S.me.nick), n ? h('span', { class: 'ek-dot-inline' }, n) : null)
      : h('a', { class: 'ek-btn ek-btn--secondary ek-btn--sm', href: '#/start' }, 'Załóż profil'));
}
function route() {
  const hsh = location.hash.replace(/^#\/?/, '');
  const [a, b] = hsh.split('/');
  const map = { '': 'board', z: 'job', dodaj: 'add', start: 'start', odzyskaj: 'recover', ja: 'me', g: 'player', ekipy: 'crews', e: 'crew', ranking: 'ranking', plan: 'plan', zasady: 'rules', admin: 'admin' };
  return { name: map[a] || 'board', id: b ? decodeURIComponent(b).replace(/[^A-Za-z0-9]/g, '') : '' };
}
let renderSeq = 0, quietRender = false;
async function render() {
  const r = route(), seq = ++renderSeq;
  if (location.hash === '#jobs') return;
  document.title = 'Ekipaż – znajdź ekipę do GTA Online';
  renderChrome();
  const view = $('#view');
  const views = { board: () => viewBoard(), job: () => viewJob(r.id), add: viewAdd, start: viewStart, recover: viewRecover, me: viewMe, player: () => viewPlayer(r.id), crews: viewCrews, crew: () => viewCrew(r.id), ranking: viewRanking, plan: viewPlan, rules: viewRules, admin: viewAdmin };
  let nodes;
  const slow = setTimeout(() => { if (seq === renderSeq && !quietRender) view.replaceChildren(h('div', { class: 'ek-container ek-section' }, h('div', { class: 'ek-grid' }, skeletonCards(3)))); }, 250);
  try { nodes = await (views[r.name] || viewBoard)(); } catch (e) { console.error(e); nodes = [h('div', { class: 'ek-container' }, empty('Coś się wysypało', 'Odśwież stronę. Jeśli problem wraca – daj znać moderacji.'))]; }
  clearTimeout(slow);
  if (seq !== renderSeq) return;
  view.replaceChildren(...[].concat(nodes).filter(Boolean));
  if (r.name === 'board') renderBoardList();
}
let lastRoute = '';
window.addEventListener('hashchange', () => {
  if (location.hash === '#jobs') return;
  const key = route().name + route().id;
  if (!$('#sheet').hidden) closeSheet();
  render().then(() => { if (key !== lastRoute) { window.scrollTo(0, 0); $('#view').focus({ preventScroll: true }); } lastRoute = key; });
});

/* odliczanie – raz na sekundę, tylko textContent */
setInterval(() => {
  document.querySelectorAll('[data-cd]').forEach(el => { const c = countdown(+el.dataset.cd); if (el.textContent !== c.t) el.textContent = c.t; if (el.classList.contains('ek-countdown')) { el.classList.toggle('is-urgent', c.cls === 'is-urgent'); el.classList.toggle('is-started', c.cls === 'is-started'); } });
  document.querySelectorAll('[data-cdl]').forEach(el => { const c = countdown(+el.dataset.cdl); if (el.textContent !== c.label) el.textContent = c.label; });
}, 1000);

/* odświeżanie w tle (tylko gdy karta widoczna) */
setInterval(() => { if (document.visibilityState === 'visible') { refreshJobs(); refreshMe(); } }, 25000);
/* widok zlecenia odświeża się sam co 10 s (status zgłoszenia, skład, kontakt) – bez utraty fokusu w formularzu */
let lastJobSig = '';
setInterval(async () => {
  const r = route();
  if (r.name !== 'job' || document.visibilityState !== 'visible' || !$('#sheet').hidden) return;
  try {
    const j = (await api('job', { params: { id: r.id } })).job;
    const sig = JSON.stringify([j.status, j.taken, j.myStatus, (j.requests || []).map(x => x.id + x.status), j.owner && j.owner.contact]);
    if (lastJobSig && sig !== lastJobSig) {
      if (j.myStatus === 'accepted') toast('Jesteś w składzie', 'Discord gospodarza znajdziesz w szczegółach zlecenia.', 'cash');
      quietRender = true; await render(); quietRender = false;
    }
    lastJobSig = sig;
  } catch (e) {}
}, 10000);
window.addEventListener('hashchange', () => { lastJobSig = ''; });
document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') { refreshJobs(); refreshMe(); } });

/* start */
lastRoute = route().name + route().id;
render();
refreshJobs().then(() => { if (route().name === 'board') render(); });
refreshRailTop(); setInterval(() => { if (document.visibilityState === 'visible') refreshRailTop(); }, 60000);
refreshMe();
})();
