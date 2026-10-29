// Test interakcji (bez wysyłania formularzy na zewnątrz)
const { chromium } = require('playwright');
const base = process.argv[2] || 'http://127.0.0.1:8090';
const S = process.argv[3];
(async () => {
  const b = await chromium.launch(); const log = (...a) => console.log(...a);
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  await ctx.route(/make\.com|formspree\.io|stripe\.com/, r => { log('  [zablokowano wysyłkę]', r.request().method(), r.request().url().slice(0, 60)); r.fulfill({ status: 200, contentType: 'application/json', body: '{"ok":true}' }); });
  const pg = await ctx.newPage(); const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto(base + '/', { waitUntil: 'networkidle' });
  log('cookie banner:', await pg.isVisible('.uxcc'));
  await pg.click('.uxcc-w'); log('po akceptacji:', await pg.isVisible('.uxcc'), await pg.evaluate(() => localStorage.getItem('uxaudyt-consent')));
  await pg.hover('.v7nav-dd button'); await pg.waitForTimeout(400); log('mega menu open:', await pg.evaluate(() => document.querySelector('.v7mega').classList.contains('open')));
  await pg.screenshot({ path: S + '/i-mega.png' });
  await pg.mouse.move(700, 600); await pg.waitForTimeout(500);
  // FAQ
  const q = pg.locator('.v7-qb').nth(2); await q.scrollIntoViewIfNeeded(); await q.click(); await pg.waitForTimeout(300);
  log('FAQ #3 open:', await pg.locator('.v7-q').nth(2).evaluate(e => e.classList.contains('open')));
  // kalkulator
  const inp = pg.locator('#policz .v7-in').first(); await inp.scrollIntoViewIfNeeded(); await inp.fill('20000'); await pg.waitForTimeout(900);
  log('kalkulator:', (await pg.locator('#policz .v7-resv').innerText()).replace(/\s+/g, ' '));
  // przełącznik wdrożenia
  await pg.locator('.v7-sw').scrollIntoViewIfNeeded(); await pg.click('.v7-sw'); await pg.waitForTimeout(300);
  log('wdrożenie on:', await pg.locator('.v7-impl').evaluate(e => e.classList.contains('on')), await pg.locator('#cennik a.v7-btn').first().getAttribute('href'));
  // arkusz #ocena
  await pg.evaluate(() => scrollTo(0, 0)); await pg.hover('.v7nav-dd button'); await pg.waitForTimeout(300);
  await pg.click('.v7mega-card'); await pg.waitForTimeout(600);
  log('arkusz ocena:', await pg.isVisible('.uxs-panel'), await pg.locator('#uxs-title').innerText());
  await pg.fill('.uxs-panel input[name=name]', 'Test'); await pg.fill('.uxs-panel input[name=email]', 'test@example.com');
  await pg.fill('.uxs-panel input[name=shop]', 'https://example.com'); await pg.selectOption('.uxs-panel select', { index: 1 });
  await pg.screenshot({ path: S + '/i-sheet.png' });
  await pg.click('.uxs-panel button[type=submit]'); await pg.waitForTimeout(800);
  log('po wysłaniu:', (await pg.locator('.uxs-panel').innerText()).slice(0, 60).replace(/\s+/g, ' '));
  await pg.keyboard.press('Escape'); await pg.waitForTimeout(500); log('arkusz zamknięty:', !(await pg.isVisible('.uxs-panel')));
  // checklista
  const em = pg.locator('#checklista .v7-email'); await em.scrollIntoViewIfNeeded(); await em.fill('test@example.com'); await pg.click('#checklista button[type=submit]'); await pg.waitForTimeout(800);
  log('checklista:', (await pg.locator('#checklista').innerText()).includes('Gotowe'));
  // mobile menu
  const m = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true }); const mp = await m.newPage();
  await mp.goto(base + '/', { waitUntil: 'networkidle' }); await mp.click('.v7nav-in .v7nav-burger'); await mp.waitForTimeout(600);
  log('menu mobilne:', await mp.evaluate(() => document.querySelector('.v7menu').classList.contains('open')));
  await mp.click('.v7m-main .v7m-row'); await mp.waitForTimeout(500); log('podmenu usługi:', await mp.evaluate(() => document.querySelector('.v7m-track').classList.contains('sub')));
  await mp.screenshot({ path: S + '/i-menu.png' });
  // checkout
  const c = await ctx.newPage(); c.on('pageerror', e => errs.push(e.message));
  await c.goto(base + '/zamowienie?pakiet=strona', { waitUntil: 'networkidle' });
  log('checkout pakiet z URL:', (await c.locator('.uxc-opt.is-on').innerText()).split('\n')[0]);
  await c.click('.uxc-cta'); await c.waitForTimeout(500); log('walidacja błędów:', await c.locator('.uxc-errtxt').count());
  await c.fill('input[data-f=url]', 'example.com'); await c.fill('input[data-f=name]', 'Jan Test'); await c.fill('input[data-f=email]', 'jan@example.com');
  await c.click('[data-f=terms]'); 
  const [nav] = await Promise.all([c.waitForRequest(r => /stripe\.com/.test(r.url()), { timeout: 5000 }).catch(() => null), c.click('.uxc-cta')]);
  log('przekierowanie do Stripe:', nav ? nav.url().replace(/prefilled_email=[^&]+/, 'prefilled_email=…').slice(0, 110) : 'BRAK');
  // raport
  const r = await ctx.newPage(); await r.goto(base + '/przykladowy-raport', { waitUntil: 'networkidle' });
  const before = await r.locator('.uxr-item').count(); await r.locator('.uxr-pill').nth(1).click(); await r.waitForTimeout(600);
  log('raport filtr:', before, '→', await r.locator('.uxr-item:visible').count());
  log('błędy JS:', errs.length ? errs : 'brak');
  await b.close();
})();
