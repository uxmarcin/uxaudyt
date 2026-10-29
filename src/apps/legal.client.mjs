import { jsx } from 'react/jsx-runtime';
import { hydrateRoot } from 'react-dom/client';
import App from './legal.mjs';
const el = document.getElementById('app');
const props = JSON.parse(document.getElementById('ux-props').textContent);
hydrateRoot(el, jsx(App, props));
