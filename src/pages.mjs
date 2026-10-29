// Lista stron: adres, typ szablonu i propsy komponentów (wyciągnięte z Framera)
import fs from 'node:fs';
const P = JSON.parse(fs.readFileSync(new URL('./props.json', import.meta.url), 'utf8'));
const one = (k, part) => (P[k][part] || [])[0];
const v7 = (key, path) => ({ key, path, kind: 'v7', props: { main: one(key, 'main'), footer: one(key, 'footer'), sheet: one(key, 'sheet'), cookie: one(key, 'cookie'), fx: one(key, 'fx') } });
const legal = (key, title) => ({ key, path: '/' + key, kind: 'legal', title, props: { legal: one(key, 'legal'), cookie: one(key, 'cookie'), fx: one(key, 'fx') } });
const checkout = (key) => ({ key, path: '/' + key, kind: 'checkout', noindex: true, title: key === 'zamowienie' ? 'Zamówienie audytu · uxaudyt.pl' : 'Zamówienie · uxaudyt.pl', props: { checkout: one(key, 'checkout'), cookie: one(key, 'cookie'), fx: one(key, 'fx') } });
export const pages = [
  v7('index', '/'),
  { key: 'przykladowy-raport', path: '/przykladowy-raport', kind: 'raport', title: 'Przykładowy raport z audytu UX · uxaudyt.pl', props: { raport: one('przykladowy-raport', 'raport'), cookie: one('przykladowy-raport', 'cookie'), fx: one('przykladowy-raport', 'fx') } },
  legal('regulamin', 'Regulamin · uxaudyt.pl'),
  legal('polityka-prywatnosci', 'Polityka prywatności · uxaudyt.pl'),
  ...['audyt-sklepu-internetowego', 'audyt-strony-internetowej', 'audyt-sklepu-z-opieka', 'wdrozenie-poprawek'].map((k) => v7(k, '/' + k)),
  legal('polityka-cookies'),
  ...['audyt-ux', 'porzucone-koszyki', 'audyt-ux-prestashop', 'audyt-ux-a-audyt-seo', 'niska-konwersja-sklepu', 'karta-produktu-checklista',
    'ux-sklepu-mobilnego', 'audyt-ux-woocommerce', 'audyt-ux-shopify', 'jak-sprawdzic-ux-sklepu', 'darmowy-audyt-sklepu'].map((k) => v7(k, '/' + k)),
  checkout('zamowienie'),
  checkout('zamowienie-plan'),
];
