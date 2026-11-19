/* Ekipaż – service worker: powiadomienia push (wiadomości bez treści – treść pobieramy z API) */
const DB = 'ekipaz', STORE = 'kv';
function idbGet(key) {
  return new Promise(res => {
    try {
      const r = indexedDB.open(DB, 1);
      r.onupgradeneeded = () => r.result.createObjectStore(STORE);
      r.onsuccess = () => { try { const tx = r.result.transaction(STORE, 'readonly').objectStore(STORE).get(key); tx.onsuccess = () => res(tx.result || null); tx.onerror = () => res(null); } catch (e) { res(null); } };
      r.onerror = () => res(null);
    } catch (e) { res(null); }
  });
}
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('push', event => {
  event.waitUntil((async () => {
    let title = 'Ekipaż', body = 'Masz nowe powiadomienie.', url = '#/', count = 0;
    try {
      const token = await idbGet('token');
      if (token) {
        const r = await fetch('api.php?a=notifs.latest', { headers: { 'X-Ekipaz-Token': token }, cache: 'no-store' });
        const d = await r.json();
        if (d && d.ok && d.item) { title = d.item.title; body = d.item.body; url = d.item.url || '#/'; count = d.unread; }
      }
    } catch (e) {}
    if (self.navigator && self.navigator.setAppBadge && count) { try { await self.navigator.setAppBadge(count); } catch (e) {} }
    await self.registration.showNotification(title, { body, tag: 'ekipaz-' + url, renotify: true, icon: 'icon-192.png', badge: 'badge-96.png', data: { url } });
  })());
});
self.addEventListener('notificationclick', event => {
  event.notification.close();
  const target = new URL((event.notification.data && event.notification.data.url) || '#/', self.registration.scope).href;
  event.waitUntil((async () => {
    const all = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
    for (const c of all) { if (c.url.startsWith(self.registration.scope)) { await c.focus(); try { await c.navigate(target); } catch (e) { c.postMessage({ go: target }); } return; } }
    await self.clients.openWindow(target);
  })());
});
