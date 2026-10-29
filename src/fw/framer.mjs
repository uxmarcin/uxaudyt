// Adapter: minimalne zamienniki API Framera (bez Framera)
const init = () => {};
export const RenderTarget = { canvas: 'CANVAS', preview: 'PREVIEW', export: 'EXPORT', thumbnail: 'THUMBNAIL', current: () => 'PREVIEW' };
const addPropertyControls = () => {};
const ControlType = new Proxy({}, { get: (_, k) => String(k) });
export { init as A, RenderTarget as d, addPropertyControls as m, ControlType as r };
