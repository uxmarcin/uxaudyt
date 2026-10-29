import { t as e } from "../fw/rolldown-runtime.mjs";
import { A as t, C as n, S as r, T as i, g as a, k as o, l as s, o as c, p as l, s as u, v as d, y as f } from "../fw/react.mjs";
import { A as _, d as E, m as D, r as k } from "../fw/framer.mjs";
import { n as re, t as ie } from "./shared-lib.mjs";
import { n as F, t as ae } from "./Icons.mjs";
function ce(e) {
  let [t, n] = a(1440);
  return (
    i(() => {
      let t = e.current;
      if (!t || typeof ResizeObserver > `u`) return;
      let r = new ResizeObserver((e) => n(e[0].contentRect.width));
      return (
        r.observe(t),
        n(t.getBoundingClientRect().width),
        () => r.disconnect()
      );
    }, []),
    t
  );
}
function le() {
  let e = f(null),
    [t, n] = a(!1);
  return (
    d(() => {
      let t = e.current;
      if (!t || typeof IntersectionObserver > `u`) {
        n(!0);
        return;
      }
      let r = new IntersectionObserver(
        (e) => {
          e.some((e) => e.isIntersecting) && (n(!0), r.disconnect());
        },
        { threshold: 0.2 },
      );
      return (r.observe(t), () => r.disconnect());
    }, []),
    [e, t]
  );
}
function I({ icon: e, label: t, children: n }) {
  return s(`div`, {
    style: { display: `flex`, alignItems: `flex-start`, gap: 14 },
    children: [
      c(`span`, {
        style: {
          flex: `none`,
          width: 28,
          height: 28,
          borderRadius: 3,
          background: `#F5F5F5`,
          display: `grid`,
          placeItems: `center`,
          marginTop: 1,
        },
        children: c(F, { name: e, size: 15, color: V.ink, strokeWidth: 2.25 }),
      }),
      s(`div`, {
        style: {
          display: `flex`,
          flexDirection: `column`,
          gap: 2,
          minWidth: 0,
        },
        children: [
          c(`span`, {
            style: {
              fontFamily: B,
              fontSize: 11,
              letterSpacing: `.08em`,
              textTransform: `uppercase`,
              color: `#6B6B6B`,
            },
            children: t,
          }),
          c(`span`, {
            style: {
              fontFamily: z,
              fontSize: 17,
              lineHeight: 1.45,
              color: V.ink,
            },
            children: n,
          }),
        ],
      }),
    ],
  });
}
function L({ children: e, dark: t = !1, phone: n, style: r }) {
  return c(`div`, {
    "data-uxfx": `skip`,
    style: {
      background: t ? V.ink : V.surface,
      color: t ? `#fff` : V.ink,
      borderRadius: 4,
      border: t ? `none` : `1px solid ` + V.line,
      padding: n ? 26 : 40,
      ...r,
    },
    children: e,
  });
}
function ue({ f: e, n: t, phone: n, canvas: r }) {
  let [i, a] = le();
  return c(`div`, {
    ref: i,
    className: `uxr-item` + (a || r ? ` uxr-on` : ``),
    style: { display: `flex` },
    children: s(L, {
      phone: n,
      style: { flex: 1, display: `flex`, flexDirection: `column` },
      children: [
        s(`div`, {
          style: {
            display: `flex`,
            alignItems: `center`,
            justifyContent: `space-between`,
            gap: 12,
          },
          children: [
            s(`span`, {
              style: {
                fontFamily: B,
                fontSize: 12,
                letterSpacing: `.08em`,
                textTransform: `uppercase`,
                color: V.ink3,
              },
              children: [
                s(`span`, {
                  style: { color: V.primary },
                  children: [`[`, String(t).padStart(2, `0`), `]`],
                }),
                `  `,
                e.area,
              ],
            }),
            s(`span`, {
              style: {
                display: `inline-flex`,
                alignItems: `center`,
                gap: 7,
                height: 32,
                padding: `0 12px`,
                borderRadius: 3,
                background: U(e.sev),
                fontFamily: B,
                fontWeight: 500,
                fontSize: 11,
                letterSpacing: `.08em`,
                textTransform: `uppercase`,
                color: `#FFFFFF`,
                whiteSpace: `nowrap`,
              },
              children: [
                c(`span`, {
                  style: {
                    width: 6,
                    height: 6,
                    borderRadius: `50%`,
                    background: `#FFFFFF`,
                  },
                }),
                e.sev,
              ],
            }),
          ],
        }),
        c(`h3`, {
          style: {
            margin: n ? `20px 0 0` : `28px 0 0`,
            fontFamily: z,
            fontWeight: 300,
            fontSize: n ? 24 : 28,
            lineHeight: 1.2,
            letterSpacing: `-0.02em`,
            color: V.ink,
          },
          children: e.title,
        }),
        c(`p`, {
          style: {
            margin: `16px 0 0`,
            fontFamily: z,
            fontSize: n ? 16 : 18,
            lineHeight: 1.6,
            color: V.ink2,
          },
          children: e.why,
        }),
        c(`div`, {
          style: {
            height: 1,
            background: V.line,
            margin: n ? `24px 0` : `28px 0`,
          },
        }),
        s(`div`, {
          style: { display: `flex`, flexDirection: `column`, gap: 18 },
          children: [
            c(I, {
              icon: `x`,
              label: `Teraz`,
              children: c(`span`, {
                className: `uxr-strike`,
                style: { color: V.bad },
                children: e.now,
              }),
            }),
            c(I, {
              icon: `check`,
              label: `Po poprawce`,
              children: c(`span`, {
                style: { color: V.ok, fontWeight: 500 },
                children: e.fix,
              }),
            }),
            c(I, { icon: `clock`, label: `Wdrożenie`, children: W(e.hours) }),
          ],
        }),
      ],
    }),
  });
}
function R(e) {
  let {
      label: t,
      shop: n,
      scope: r,
      note: i,
      ctaTitle: o,
      ctaText: l,
      ctaLabel: u,
      ctaHref: d,
      homeHref: p,
    } = e,
    m = f(null),
    h = ce(m),
    g = h < 600,
    _ = h >= 1e3,
    v = E.current() === E.canvas,
    [y, b] = a(`all`),
    x = H.filter((e) => y === `all` || e.sev === y),
    S = (e) => H.filter((t) => t.sev === e).length,
    C = H.reduce((e, t) => e + t.hours, 0),
    w = Math.round(C / 8),
    T = (e, t, n = `#FFFFFF`) =>
      s(`div`, {
        style: { display: `flex`, alignItems: `baseline`, gap: 8 },
        children: [
          c(`span`, {
            style: {
              fontFamily: z,
              fontWeight: 300,
              fontSize: g ? 44 : 64,
              lineHeight: 1,
              letterSpacing: `-0.04em`,
              color: n,
            },
            children: e,
          }),
          c(`span`, {
            style: {
              fontFamily: B,
              fontSize: 11,
              letterSpacing: `.08em`,
              textTransform: `uppercase`,
              color: `#8A8A8A`,
            },
            children: t,
          }),
        ],
      });
  return s(`div`, {
    ref: m,
    className: `uxr`,
    style: {
      width: `100%`,
      minHeight: `100vh`,
      background: V.page,
      fontFamily: z,
      padding: g ? `16px 16px 64px` : `40px 40px 112px`,
    },
    children: [
      c(`style`, { dangerouslySetInnerHTML: { __html: de } }),
      s(`div`, {
        style: {
          maxWidth: 1120,
          margin: `0 auto`,
          display: `flex`,
          flexDirection: `column`,
          gap: g ? 12 : 20,
        },
        children: [
          s(`div`, {
            className: `uxr-noprint`,
            style: {
              display: `flex`,
              justifyContent: `space-between`,
              alignItems: `center`,
              padding: `0 8px 4px`,
            },
            children: [
              s(`a`, {
                href: p,
                className: `uxr-back`,
                children: [
                  c(F, { name: `arrow-left`, size: 16 }),
                  ` Wróć na stronę`,
                ],
              }),
              s(`span`, {
                style: {
                  display: `inline-flex`,
                  alignItems: `center`,
                  gap: 8,
                  fontFamily: B,
                  fontSize: 12,
                  letterSpacing: `.07em`,
                  textTransform: `uppercase`,
                  color: `#6B6B6B`,
                },
                children: [
                  c(`span`, {
                    style: {
                      width: 6,
                      height: 6,
                      borderRadius: `50%`,
                      background: V.primary,
                    },
                  }),
                  i,
                ],
              }),
            ],
          }),
          s(L, {
            dark: !0,
            phone: g,
            children: [
              s(`div`, {
                style: {
                  display: `flex`,
                  justifyContent: `space-between`,
                  alignItems: `center`,
                  gap: 16,
                },
                children: [
                  c(re, { height: g ? 26 : 30, ink: `#FFFFFF`, shadow: !1 }),
                  s(`span`, {
                    style: {
                      fontFamily: B,
                      fontSize: 12,
                      letterSpacing: `.08em`,
                      textTransform: `uppercase`,
                      color: `#9A9A9A`,
                    },
                    children: [
                      `[ `,
                      c(`span`, { style: { color: V.primary }, children: `●` }),
                      ` `,
                      t,
                      ` ]`,
                    ],
                  }),
                ],
              }),
              s(`h1`, {
                style: {
                  margin: g ? `28px 0 0` : `40px 0 0`,
                  fontFamily: z,
                  fontWeight: 300,
                  fontSize: g ? 34 : 56,
                  lineHeight: 1.06,
                  letterSpacing: `-0.035em`,
                  color: `#FFFFFF`,
                },
                children: [
                  `Przykładowy raport z audytu UX sklepu`,
                  c(`span`, {
                    style: {
                      display: `block`,
                      marginTop: 12,
                      fontSize: `0.5em`,
                      lineHeight: 1.2,
                      letterSpacing: `-0.02em`,
                      color: `#8A8A8A`,
                    },
                    children: n,
                  }),
                ],
              }),
              c(`p`, {
                style: {
                  margin: `16px 0 0`,
                  maxWidth: 720,
                  fontFamily: z,
                  fontSize: g ? 16 : 18,
                  lineHeight: 1.6,
                  color: `#BDBDBD`,
                },
                children: r,
              }),
              c(`div`, {
                style: {
                  height: 1,
                  background: `#2E2E2E`,
                  margin: g ? `28px 0` : `36px 0`,
                },
              }),
              s(`div`, {
                style: {
                  display: `grid`,
                  gridTemplateColumns: g ? `1fr 1fr` : `repeat(4, auto)`,
                  justifyContent: `space-between`,
                  rowGap: 20,
                  columnGap: 24,
                },
                children: [
                  T(S(`Krytyczny`), `krytyczne`, V.primary),
                  T(S(`Ważny`), `ważne`, `#E8A33C`),
                  T(S(`Drobny`), `drobne`),
                  T(w, w === 1 ? `dzień wdrożenia` : `dni wdrożenia`),
                ],
              }),
            ],
          }),
          s(`div`, {
            style: {
              display: `flex`,
              flexDirection: g ? `column` : `row`,
              alignItems: g ? `flex-start` : `center`,
              flexWrap: `wrap`,
              justifyContent: `space-between`,
              gap: 14,
              padding: g ? `20px 8px 4px` : `28px 8px 8px`,
            },
            children: [
              s(`h2`, {
                style: {
                  margin: 0,
                  fontFamily: z,
                  fontWeight: 300,
                  fontSize: g ? 28 : 40,
                  letterSpacing: `-0.03em`,
                  color: V.ink,
                },
                children: [
                  `Do poprawy `,
                  c(`span`, {
                    style: { color: `#9A9A9A` },
                    children: `od najważniejszych`,
                  }),
                ],
              }),
              c(`div`, {
                className: `uxr-noprint`,
                role: `radiogroup`,
                "aria-label": `Filtruj według wagi`,
                style: { display: `flex`, flexWrap: `wrap`, gap: 6 },
                children: [
                  [`all`, `Wszystkie`],
                  [`Krytyczny`, `Krytyczne`],
                  [`Ważny`, `Ważne`],
                  [`Drobny`, `Drobne`],
                ].map(([e, t]) =>
                  c(
                    `button`,
                    {
                      type: `button`,
                      role: `radio`,
                      "aria-checked": y === e,
                      "data-uxfx": `skip`,
                      className: `uxr-pill` + (y === e ? ` is-on` : ``),
                      onClick: () => b(e),
                      children: t,
                    },
                    e,
                  ),
                ),
              }),
            ],
          }),
          c(`div`, {
            style: {
              display: `grid`,
              gridTemplateColumns: _ ? `1fr 1fr` : `1fr`,
              gap: g ? 12 : 20,
            },
            children: x.map((e) =>
              c(
                ue,
                { f: e, n: H.indexOf(e) + 1, phone: g, canvas: v },
                e.title,
              ),
            ),
          }),
          s(L, {
            dark: !0,
            phone: g,
            style: {
              marginTop: g ? 8 : 12,
              display: `flex`,
              flexDirection: _ ? `row` : `column`,
              alignItems: _ ? `center` : `flex-start`,
              justifyContent: `space-between`,
              gap: 28,
            },
            children: [
              s(`div`, {
                style: {
                  display: `flex`,
                  flexDirection: `column`,
                  gap: 10,
                  maxWidth: 560,
                },
                children: [
                  c(`h2`, {
                    style: {
                      margin: 0,
                      fontFamily: z,
                      fontWeight: 300,
                      fontSize: g ? 28 : 40,
                      lineHeight: 1.1,
                      letterSpacing: `-0.03em`,
                      color: `#FFFFFF`,
                    },
                    children: o,
                  }),
                  c(`p`, {
                    style: {
                      margin: 0,
                      fontFamily: z,
                      fontSize: g ? 16 : 18,
                      lineHeight: 1.6,
                      color: `#B4B4B4`,
                    },
                    children: l,
                  }),
                ],
              }),
              s(`a`, {
                href: d,
                className: `uxr-cta`,
                style: {
                  background: `#FFFFFF`,
                  color: V.ink,
                  width: g ? `100%` : `auto`,
                  height: 60,
                  padding: `0 30px`,
                },
                children: [u, ` `, c(F, { name: `arrow-right`, size: 18 })],
              }),
            ],
          }),
        ],
      }),
    ],
  });
}
var z,
  B,
  V,
  H,
  de,
  U,
  W,
  G,
  fe = e(() => {
    (u(),
      n(),
      _(),
      ae(),
      ie(),
      (z = `"Figtree", "Figtree Placeholder", system-ui, sans-serif`),
      (B = `"Figtree", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif`),
      (V = {
        ink: `#0D0D0D`,
        ink2: `#5D5D5D`,
        ink3: `#6E6E6E`,
        line: `#EAEAEA`,
        page: `#FFFFFF`,
        box: `#F7F7F7`,
        surface: `#FFFFFF`,
        primary: `#FF5A1F`,
        bad: `#DC3709`,
        warn: `#B26A00`,
        ok: `#1E9E5A`,
      }),
      (H = [
        {
          sev: `Krytyczny`,
          area: `Karta produktu`,
          title: `Próg darmowej dostawy ukryty w stopce`,
          why: `Krem za 119 zł nie podpowiada, że do darmowej dostawy brakuje 41 zł. Klient nie dokłada drugiego produktu.`,
          now: `Informacja tylko w stopce`,
          fix: `„Brakuje 41 zł do darmowej dostawy” przy cenie`,
          hours: 2,
          img: `/img/MmYgYaxSDCvaaIwC7VSHWlGDIM.jpg`,
        },
        {
          sev: `Krytyczny`,
          area: `Koszyk`,
          title: `Koszt dostawy dopiero w ostatnim kroku`,
          why: `W koszyku widać „dostawa od 0 zł”. Prawdziwa kwota pojawia się przy płatności, czyli w najgorszym możliwym momencie.`,
          now: `Kwota dostawy w kroku 3`,
          fix: `Koszt dostawy wyliczony już w koszyku`,
          hours: 4,
          icon: `truck`,
        },
        {
          sev: `Ważny`,
          area: `Mobile`,
          title: `Przycisk „Dodaj do koszyka” jest za nisko`,
          why: `Na telefonie przycisk jest półtora ekranu niżej, pod galerią i wariantami.`,
          now: `Przycisk nisko na stronie`,
          fix: `Przyklejony przycisk na dole ekranu`,
          hours: 3,
          icon: `phone`,
        },
        {
          sev: `Ważny`,
          area: `Karta produktu`,
          title: `Pojemność i skład schowane w zakładkach`,
          why: `Przy kosmetykach to pierwsze pytania klienta. Odpowiedź jest w trzeciej zakładce.`,
          now: `Skład w zakładce nr 3`,
          fix: `Pojemność i 3 kluczowe składniki pod nazwą`,
          hours: 2,
          icon: `list`,
        },
        {
          sev: `Ważny`,
          area: `Checkout`,
          title: `Wymuszone zakładanie konta`,
          why: `Przed płatnością trzeba się zarejestrować. To jeden z najczęstszych powodów porzucenia zakupu.`,
          now: `Rejestracja przed płatnością`,
          fix: `Zakup jako gość, konto po zakupie`,
          hours: 8,
          icon: `user`,
        },
        {
          sev: `Drobny`,
          area: `Kategoria`,
          title: `Filtry ukryte pod ikoną`,
          why: `Ikona lejka bez podpisu. Na telefonie mało kto ją zauważa.`,
          now: `Sama ikona`,
          fix: `Przycisk „Filtruj (3)”`,
          hours: 1,
          icon: `filter`,
        },
        {
          sev: `Drobny`,
          area: `Strona główna`,
          title: `Slider zamiast bestsellerów`,
          why: `Pięć slajdów z hasłami zajmuje cały pierwszy ekran i nie pokazuje żadnego produktu.`,
          now: `5 slajdów z hasłami`,
          fix: `Siatka 8 bestsellerów z ceną`,
          hours: 3,
          icon: `grid`,
        },
      ]),
      (de = `

.uxr *{box-sizing:border-box}
.uxr-item{opacity:0;transform:translateY(12px);transition:opacity .6s cubic-bezier(.2,.8,.2,1),transform .6s cubic-bezier(.2,.8,.2,1)}
.uxr-item.uxr-on{opacity:1;transform:none}
.uxr-strike{position:relative}
.uxr-strike::after{content:"";position:absolute;left:0;right:0;top:55%;height:1.5px;background:#DC3709;transform:scaleX(0);transform-origin:left;transition:transform .6s cubic-bezier(.65,0,.35,1) .2s}
.uxr-on .uxr-strike::after{transform:scaleX(1)}
.uxr-pill{height:36px;padding:0 14px;border-radius:999px;border:1px solid #DADADA;background:#FFFFFF;font:400 12px/1 ${B};letter-spacing:.07em;text-transform:uppercase;color:#0D0D0D;cursor:pointer;display:inline-flex;align-items:center;gap:7px;transition:background-color .2s ease,color .2s ease,border-color .2s ease}
@media (hover:hover){.uxr-pill:hover{border-color:rgba(13,13,13,.3)}}
.uxr-pill.is-on{background:#0D0D0D;border-color:#0D0D0D;color:#FFFFFF}
.uxr-pill:focus-visible,.uxr-cta:focus-visible{outline:2px solid #FF5A1F;outline-offset:3px}
.uxr-cta{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:56px;padding:0 26px;border-radius:999px;background:#0D0D0D;color:#FFFFFF;text-decoration:none;font:500 16px/1 ${z};white-space:nowrap;transition:background .3s ease,color .3s ease,transform .3s ease}
.uxr-cta:hover{background:#FF5A1F!important;color:#fff!important;transform:translateY(-2px)}
.uxr-cta svg{transition:transform .35s ease}.uxr-cta:hover svg{transform:translateX(5px)}
.uxr-back{display:inline-flex;align-items:center;gap:8px;font:400 12px/1.4 ${B};letter-spacing:.07em;text-transform:uppercase;color:#6B6B6B;text-decoration:none}
.uxr-back:hover{color:#0D0D0D}
@media print{.uxr{background:#fff!important}.uxr-noprint{display:none!important}.uxr-item{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.uxr-item{opacity:1;transform:none;transition:none}.uxr-strike::after{transition:none;transform:scaleX(1)}}
`),
      (U = (e) =>
        e === `Krytyczny` ? V.bad : e === `Ważny` ? V.warn : V.ink3),
      (W = (e) =>
        e < 8
          ? e + ` h`
          : Math.round(e / 8) === 1
            ? `1 dzień`
            : Math.round(e / 8) + ` dni`),
      (G = (e, t, n = !1) => ({
        type: k.String,
        title: e,
        defaultValue: t,
        displayTextArea: n,
      })),
      D(R, {
        label: G(`Etykieta`, `Raport UX · przykład`),
        shop: G(`Sklep`, `Sklep z kosmetykami naturalnymi`),
        scope: G(
          `Zakres`,
          `Cała ścieżka zakupu na desktopie oraz urządzeniach mobilnych: strona główna, kategoria, karta produktu, koszyk i płatność.`,
          !0,
        ),
        note: G(`Notka`, `Przykład poglądowy`),
        ctaTitle: G(`CTA tytuł`, `Sprawdzę tak samo Twój sklep.`),
        ctaText: G(
          `CTA opis`,
          `Otrzymasz go w 5 dni roboczych, razem z makietami poprawek. Jeśli nie znajdę nic, co wpływa na sprzedaż, oddam Ci pieniądze.`,
          !0,
        ),
        ctaLabel: G(`Przycisk`, `Zamów audyt sklepu`),
        ctaHref: G(`Link`, `/zamowienie`),
        homeHref: G(`Strona główna`, `/`),
      }));
  });

export { fe as init, R as Raport };
