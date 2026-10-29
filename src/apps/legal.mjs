// Regulamin i polityki
import { jsx, jsxs } from 'react/jsx-runtime';
import { n as initLegal, t as Legal } from '../c/LegalPage.mjs';
import { n as initCookie, t as Cookie } from '../c/CookieConsent.mjs';
import { a as initFx, i as Fx } from '../c/shared-lib.mjs';
initLegal(); initCookie(); initFx();
export default function App({ legal, cookie, fx }) {
  return jsxs('div', { className: 'ux-page', children: [jsx(Legal, legal), jsx(Cookie, cookie), jsx(Fx, fx)] });
}
