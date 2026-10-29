// Przykładowy raport
import { jsx, jsxs } from 'react/jsx-runtime';
import { init as initRaport, Raport } from '../c/Raport.mjs';
import { n as initCookie, t as Cookie } from '../c/CookieConsent.mjs';
import { a as initFx, i as Fx } from '../c/shared-lib.mjs';
initRaport(); initCookie(); initFx();
export default function App({ raport, cookie, fx }) {
  return jsxs('div', { className: 'ux-page', children: [jsx(Raport, raport), jsx(Cookie, cookie), jsx(Fx, fx)] });
}
