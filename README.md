# uxaudyt.pl

Strona przeniesiona z Framera na własny hosting (cyber_Folks, domena `uxaudyt.pl`).

## Jak to działa

- `src/c/` — komponenty strony (React): `V7Home` (strona główna, usługi, poradniki, stopka, formularze w nakładce),
  `Checkout` (zamówienie + Stripe), `LegalPage` (regulamin, polityki), `Raport` (przykładowy raport),
  `CookieConsent`, `shared-lib` (logo, efekty hover), `Icons`.
- `src/fw/` — małe adaptery zastępujące API Framera i Reacta (komponenty działają bez Framera).
- `src/pages.mjs` + `src/props.json` — lista stron i ich ustawienia (FAQ, linki płatności, adresy formularzy).
- `src/meta.json` — tytuły, opisy i adresy kanoniczne (SEO 1:1 z Framera).
- `build.mjs` — renderuje każdą stronę do statycznego HTML (treść widoczna dla Google bez JS)
  i buduje skrypty w `public/js/`, które ożywiają interakcje (menu, kalkulator, formularze, FAQ).
- `public/` — gotowa strona. To ten katalog trafia na serwer.

## Zmiany

```bash
npm install         # raz
npm run build       # przebudowuje public/
npm run dev         # podgląd: http://127.0.0.1:8090
```

Commit + push na `main` → GitHub Actions wysyła `public/` przez FTPS do `domains/uxaudyt.pl/public_html/`.

## Integracje (bez zmian względem Framera)

- Formularze „Bezpłatna ocena” / „Wycena wdrożenia” → Formspree + Make.com (e-maile automatyczne).
- Checklista → Make.com.
- Zamówienia → Stripe Payment Links (BLIK, Przelewy24, karta), powiadomienia → Formspree + Make.com.
- Analityka: brak (baner cookies gotowy na GA/Clarity — wpisz ID w `src/props.json`, pola `gaId` / `clarityId`).
