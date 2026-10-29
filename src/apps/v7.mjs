// Strony V7: główna, usługi, poradniki
import { jsx, jsxs } from 'react/jsx-runtime';
import { a as Sheet, i as initFooter, n as initMain, o as initSheet, r as Footer, t as Main } from '../c/V7Home.mjs';
import { n as initCookie, t as Cookie } from '../c/CookieConsent.mjs';
import { a as initFx, i as Fx } from '../c/shared-lib.mjs';
initMain(); initFooter(); initSheet(); initCookie(); initFx();
export default function App({ main, footer, sheet, cookie, fx }) {
  return jsxs('div', { className: 'ux-page', children: [
    jsx(Main, main), jsx(Footer, footer), jsx(Sheet, sheet), jsx(Cookie, cookie), jsx(Fx, fx),
  ] });
}
