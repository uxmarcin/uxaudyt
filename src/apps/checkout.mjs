// Zamówienie (checkout)
import { jsx, jsxs } from 'react/jsx-runtime';
import { n as initCheckout, t as Checkout } from '../c/Checkout.mjs';
import { n as initCookie, t as Cookie } from '../c/CookieConsent.mjs';
import { a as initFx, i as Fx } from '../c/shared-lib.mjs';
initCheckout(); initCookie(); initFx();
export default function App({ checkout, cookie, fx }) {
  return jsxs('div', { className: 'ux-page', children: [jsx(Checkout, checkout), jsx(Cookie, cookie), jsx(Fx, fx)] });
}
