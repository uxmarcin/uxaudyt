#!/usr/bin/env python3
"""Zmiany treści uxaudyt.pl, listopad 2026 (copy + SEO + 3 nowe poradniki + llms.txt).

Uruchom z katalogu repo:  python3 tools/copy-patch-2026-11.py   (potem: npm run build)
Skrypt jest idempotentny: każda zamiana sprawdza, czy stary literał występuje dokładnie tyle razy,
ile powinien; jeśli już jest nowy tekst, pomija. Przy niezgodności przerywa bez zapisu plików.
Nie zmienia regulaminu/polityk (LegalPage.mjs), cen ani logiki płatności.
Źródła: copy/ux-copy-core.md, ux-copy-guides.md, ux-llms.txt, poprawki z ux-review.md
i rozstrzygnięcie właściciela z BRIEF.md (3.11.2026).
"""
import json, os, sys, copy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.loads('''{
"ops": [
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Płacisz za każde wejście. Sprawdzę, dlaczego klienci wychodzą bez zakupu i co poprawić najpierw. Każdy sklep przechodzę osobiście, na desktopie oraz urządzeniach mobilnych.",
"new": "Płacisz za ruch, z reklam albo z SEO. Sprawdzę osobiście, na komputerze i telefonie, dlaczego klienci wychodzą bez zakupu i co poprawić najpierw. Cenę i termin znasz przed zamówieniem.",
"count": 1,
"id": "H-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Tyle czekasz na raport",
"new": "roboczych od zaksięgowania płatności",
"count": 1,
"id": "H-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Zwrotu, jeśli nic nie znajdę",
"new": "Zwrotu na zasadach gwarancji",
"count": 1,
"id": "H-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`PrestaShop`,`Oficjalny partner`]];return",
"new": "[`PrestaShop`,`Expert`]];return",
"count": 1,
"id": "H-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "koszyków klienci sklepów internetowych porzucają przed zakupem",
"new": "koszyków klienci porzucają przed zakupem. To średnia z 50 badań zebranych przez Baymard Institute.",
"count": 1,
"id": "P-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "o tyle może wzrosnąć konwersja, gdy uprościsz zamówienie",
"new": "o tyle, według Baymard Institute, przeciętny duży sklep może podnieść konwersję, poprawiając proces zamówienia",
"count": 1,
"id": "P-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Przykład: przy tych samych odwiedzinach do kasy trafia ",
"new": "Przykładowe wyliczenie: przy tych samych odwiedzinach i konwersji wyższej o 35% do kasy trafia ",
"count": 1,
"id": "P-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": ", badania checkoutu w e-commerce",
"new": ", zestawienie badań porzuceń koszyka (aktualizacja: wrzesień 2025). Wzrost o 35% dotyczy dużych sklepów z USA i UE i samego procesu zamówienia.",
"count": 1,
"id": "P-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[02] Policz zysk",
"new": "[02] Policz przychód",
"count": 1,
"id": "K-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": ", zyskam:",
"new": ", mój miesięczny przychód będzie wyższy o:",
"count": 1,
"id": "K-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Kliknij liczby i wpisz dane swojego sklepu",
"new": "Kliknij liczby i wpisz dane swojego sklepu. 15% to tylko przykładowe założenie.",
"count": 1,
"id": "K-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Możesz zyskać",
"new": "Dodatkowy przychód",
"count": 1,
"id": "K-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "więcej przychodu miesięcznie.",
"new": "miesięcznie, przed odjęciem kosztów.",
"count": 1,
"id": "K-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Po poprawkach",
"new": "Przy wyższej konwersji",
"count": 1,
"id": "K-7"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Przykładowe wyliczenie, nie obietnica. Wynik zależy od branży, ruchu i tego, co wdrożysz.",
"new": "Przykładowe wyliczenie, nie obietnica. To przychód przed odjęciem kosztów. Wynik zależy od branży, ruchu i tego, co wdrożysz.",
"count": 1,
"id": "K-6"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "b?` Audyt sklepu za `+L(t)+` zł netto zwraca się `+b+`.`:``",
"new": "b?` Dodatkowy przychód zrówna się z ceną audytu (`+L(t)+` zł netto) `+b+`.`:``",
"count": 1,
"id": "K-8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Tak jak klient: od wejścia z reklamy aż po płatność, na desktopie oraz urządzeniach mobilnych.",
"new": "Tak jak klient: od pierwszego wejścia aż po płatność, na komputerze i telefonie.",
"count": 1,
"id": "J-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "W 5 dni roboczych. Problemy układam od najważniejszych i przy każdym podaję gotową poprawkę.",
"new": "W 5 dni roboczych od zaksięgowania płatności, jako PDF. Problemy układam od najważniejszych i przy każdym podaję gotową poprawkę.",
"count": 1,
"id": "J-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "d(`span`,{children:`Jak to działa`})})}),d(`div`,{className:`v7-mono v7-muted`",
"new": "d(`span`,{children:`Jak wygląda audyt UX`})})}),d(`div`,{className:`v7-mono v7-muted`",
"count": 1,
"id": "J-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Zamów audyt UX",
"new": "Cennik audytu UX",
"count": 1,
"id": "C-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[06] Cennik",
"new": "[06] Stała cena, płacisz raz",
"count": 1,
"id": "C-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Oferta, nawigacja i wezwania do działania",
"new": "Oferta, nawigacja, przyciski i kontakt",
"count": 1,
"id": "C-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Cała ścieżka zakupu na desktopie oraz urządzeniach mobilnych",
"new": "Cała ścieżka zakupu na komputerze i telefonie",
"count": 1,
"id": "C-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Problemy uporządkowane od najważniejszych",
"new": "Problemy od najważniejszych, z poprawką przy każdym",
"count": 1,
"id": "C-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Dla sklepów, które chcą przejść od raportu do efektów pod moją opieką.",
"new": "Dla sklepów bez projektanta UX, które chcą pomocy przy wdrożeniu. Dopłacasz 1500 zł netto do audytu sklepu.",
"count": 1,
"id": "C-7"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Warsztat z omówieniem raportu",
"new": "Warsztat online z Tobą i Twoim zespołem",
"count": 1,
"id": "C-8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`30 dni wsparcia przy wdrożeniu`,`Ponowne sprawdzenie sklepu po zmianach`],cta:",
"new": "`30 dni wsparcia e-mailem przy wdrożeniu`,`Ponowne sprawdzenie sklepu po zmianach`],cta:",
"count": 1,
"id": "C-9"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Polecany",
"new": "Najpełniejszy",
"count": 2,
"id": "C-10"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "d(`em`,{children:`Przygotuję wycenę po napisaniu raportu UX`})",
"new": "d(`em`,{children:`wycena po raporcie`})",
"count": 1,
"id": "C-11"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Świetnie. Przygotuję wycenę po napisaniu raportu UX, gdy będzie wiadomo, co jest do zrobienia. Wycena jest bez zobowiązań: sam decydujesz, co wdrażamy.",
"new": "Zaznaczone. Wycenę wdrożenia przygotuję po raporcie, gdy będzie wiadomo, co jest do zrobienia. Jest bez zobowiązań, a cena audytu się nie zmienia.",
"count": 1,
"id": "C-12"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Zaprojektuję poprawki w Figmie i wdrożę je na Twojej platformie albo razem z Twoim developerem. Przygotuję wycenę po napisaniu raportu UX.",
"new": "Chcesz, żebym wdrożył poprawki? Zaprojektuję je w Figmie i wdrożę na Twojej platformie albo poprowadzę Twojego developera. Wycenę przygotuję po raporcie.",
"count": 1,
"id": "C-13"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Uczciwa gwarancja.",
"new": "Gwarancja zwrotu.",
"count": 1,
"id": "C-14"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": " Jeśli nie znajdę nic, co realnie wpływa na sprzedaż, albo nie dostarczę raportu w terminie, zwrócę całą kwotę.",
"new": " Zwrócę całą kwotę, jeśli raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w terminie, chyba że opóźnienie wynika z niedostępności Twojego sklepu. Wystarczy e-mail w ciągu 14 dni od terminu raportu albo od jego otrzymania.",
"count": 1,
"id": "C-15"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Od ponad 15 lat projektuję strony",
"new": "Od 13 lat projektuję produkty cyfrowe,",
"count": 1,
"id": "O-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": " i sklepy, które sprzedają.",
"new": "dziś także sklepy i strony.",
"count": 1,
"id": "O-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Widziałem wiele razy, jak drobne zmiany w karcie produktu czy w checkoucie przekładają się na realną sprzedaż.",
"new": "Projektowałem złożone systemy B2B dla budownictwa, logistyki i medycyny. Uczyłem się tam usuwać zbędne kroki. W sklepie każdy taki krok może kosztować zamówienie, więc szukam ich w pierwszej kolejności.",
"count": 1,
"id": "O-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`15+`,`lat w UX/UI`]",
"new": "[`13`,`lat projektowania produktów`]",
"count": 1,
"id": "O-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "children:`Oficjalny partner`}):null]},e.n))",
"new": "children:`PrestaShop Expert`}):null]},e.n))",
"count": 1,
"id": "O-6"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Przykłady z analiz",
"new": "Tak opisuję problemy",
"count": 1,
"id": "E-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "prawdziwych sklepów.",
"new": "w raporcie.",
"count": 1,
"id": "E-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[05] Co znajduję w audycie",
"new": "[05] Przykłady poglądowe",
"count": 1,
"id": "E-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "W pełnym raporcie każdy przykład ma zrzut ekranu, wyjaśnienie i makietę poprawki.",
"new": "Przykłady są poglądowe, uogólnione z typowych błędów w sklepach. W Twoim raporcie każdy problem ma zrzut ekranu z Twojego sklepu, wyjaśnienie i konkretną poprawkę.",
"count": 1,
"id": "E-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Fragment analizy: ",
"new": "Przykład poglądowy: ",
"count": 2,
"id": "E-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`Przykładowy raport`,`PDF`,e.report]",
"new": "[`Przykładowy raport`,`Zobacz online`,e.report]",
"count": 1,
"id": "M-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`PrestaShop`,`Oficjalny partner`,`/audyt-ux-prestashop`]",
"new": "[`PrestaShop`,`PrestaShop Expert`,`/audyt-ux-prestashop`]",
"count": 1,
"id": "M-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Raport z poprawkami w 5 dni roboczych",
"new": "Stała cena, raport PDF w 5 dni roboczych",
"count": 1,
"id": "M-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Wyślij adres sklepu lub strony. Sprawdzę, czy pełny audyt ma u Ciebie sens.",
"new": "Wyślij adres sklepu lub strony. Odpiszę e-mailem, czy pełny audyt ma u Ciebie sens.",
"count": 1,
"id": "M-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`Shopify, WooCommerce, Shoper, IdoSell`,``,e.about]",
"new": "[`Shopify`,`Poradnik`,`/audyt-ux-shopify`],[`WooCommerce`,`Poradnik`,`/audyt-ux-woocommerce`],[`Shoper`,`Poradnik`,`/audyt-ux-shoper`]",
"count": 1,
"id": "M-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "\\\\xA0 Oficjalny partner PrestaShop",
"new": "\\\\xA0 PrestaShop Expert",
"count": 1,
"id": "F-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`sklepów internetowych`]",
"new": "`sklepów i stron www`]",
"count": 1,
"id": "F-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": " Marcin Bednarz Creative Vision · NIP 7952514299",
"new": " Marcin Bednarz Creative Vision · ul. Pańska 13A/1, 35-213 Rzeszów · NIP 7952514299",
"count": 1,
"id": "F-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Realizacja: ",
"new": "Usługa studia ",
"count": 1,
"id": "F-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Checklista UX koszyka",
"new": "Checklista koszyka i zamówienia",
"count": 2,
"id": "L-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Podaj adres sklepu albo strony. Osobiście sprawdzę, czy audyt ma u Ciebie sens. Jeśli coś zatrzymuje klientów, wskażę gdzie.",
"new": "Podaj adres sklepu albo strony. Przejrzę go osobiście i odpiszę e-mailem, czy pełny audyt ma u Ciebie sens. Jeśli coś zatrzymuje klientów, wskażę gdzie.",
"count": 1,
"id": "W-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Przejrzę stronę osobiście i odpiszę na podany e-mail, zwykle w ciągu 1–2 dni roboczych.",
"new": "Przejrzę sklep lub stronę osobiście i odpiszę na podany e-mail, zwykle w ciągu 2 dni roboczych.",
"count": 1,
"id": "W-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Napisz w kilku zdaniach, co chcesz poprawić. Jeśli nie masz jeszcze audytu, zaczniemy od niego. Przygotuję wycenę po napisaniu raportu UX, bez zobowiązań.",
"new": "Napisz w kilku zdaniach, co chcesz poprawić. Jeśli nie masz jeszcze audytu, zaczniemy od niego. Masz raport od innej firmy? Wspomnij o nim, porozmawiamy. Wycena jest bez zobowiązań.",
"count": 1,
"id": "W-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Wyślij zapytanie",
"new": "Poproś o wycenę",
"count": 1,
"id": "W-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Zapytaj o wdrożenie poprawek",
"new": "Wycena wdrożenia poprawek",
"count": 1,
"id": "W-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "typeof l==`string`?l.replace(/dostajesz/g,`otrzymasz`):l",
"new": "l",
"count": 2,
"id": "runtime-replace"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Przejdę Twój sklep tak jak klient: od wejścia na stronę aż po płatność, na desktopie oraz urządzeniach mobilnych. Jeśli gdzieś po drodze klienci rezygnują, pokażę Ci gdzie i co poprawić najpierw, żeby sprzedawać więcej.",
"new": "Przejdę Twój sklep tak jak klient, od wejścia na stronę po płatność, na komputerze i telefonie. Pokażę, gdzie klienci rezygnują i co poprawić najpierw. Raport otrzymasz w 5 dni roboczych od zaksięgowania płatności.",
"count": 1,
"id": "S-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Raport PDF z listą problemów, od tych, które najbardziej wpływają na sprzedaż",
"new": "Raport PDF: problemy od tych, które najbardziej wpływają na sprzedaż",
"count": 1,
"id": "S-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Przy każdym problemie zrzut ekranu, wyjaśnienie i konkretną poprawkę",
"new": "Przy każdym problemie zrzut ekranu, wyjaśnienie i konkretna poprawka",
"count": 1,
"id": "S-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "3 makiety poprawek dla najważniejszych problemów",
"new": "Prawo do swobodnego korzystania z raportu: przekażesz go developerowi lub agencji",
"count": 1,
"id": "S-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Rozmowę o raporcie, na której odpowiem na wszystkie pytania",
"new": "Rozmowa o raporcie, na której odpowiem na Twoje pytania",
"count": 2,
"id": "S-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Większość ruchu to urządzenia mobilne. Sprawdzam całą ścieżkę zakupu na urządzeniach mobilnych.",
"new": "Całą ścieżkę zakupu sprawdzam osobno na telefonie: przyciski, formularze, filtry i płatność.",
"count": 1,
"id": "S-6"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`Checkout i płatność`,",
"new": "[`Zamówienie i płatność`,",
"count": 1,
"id": "S-7"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Tak jak klient: od reklamy po płatność, na desktopie oraz urządzeniach mobilnych.",
"new": "Tak jak klient: od wejścia na stronę po płatność, na komputerze i telefonie.",
"count": 1,
"id": "S-8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "W 5 dni roboczych, z poprawkami od najważniejszych.",
"new": "W 5 dni roboczych od zaksięgowania płatności, z poprawkami od najważniejszych.",
"count": 2,
"id": "S-9"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Pracuję z PrestaShop, Shopify, WooCommerce, Shoper, IdoSell, Magento i innymi platformami. Dostęp do panelu sklepu nie jest potrzebny.",
"new": "Pracuję z PrestaShop (status PrestaShop Expert), Shopify, WooCommerce, Shoper, IdoSell, Magento i innymi platformami. Wystarczy mi adres sklepu, dostęp do panelu nie jest potrzebny.",
"count": 2,
"id": "S-10"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "d(`span`,{children:`Dla kogo jest`})}),d(`span`,{className:`v7-mask`",
"new": "d(`span`,{children:`Dla kogo jest`})}),` `,d(`span`,{className:`v7-mask`",
"count": 1,
"id": "3.3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Przejdę Twoją stronę tak jak klient, na desktopie oraz urządzeniach mobilnych. Jeśli coś go zatrzymuje, zanim napisze lub zadzwoni, pokażę Ci to i podpowiem, co poprawić najpierw.",
"new": "Przejdę Twoją stronę tak jak klient, na komputerze i telefonie. Pokażę, co go zatrzymuje, zanim napisze lub zadzwoni, i co poprawić najpierw. Platforma nie ma znaczenia: WordPress, Webflow, Wix i inne.",
"count": 1,
"id": "WS-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Raport PDF z listą problemów, od tych, które najbardziej wpływają na liczbę zapytań",
"new": "Raport PDF: problemy od tych, które najbardziej ograniczają liczbę zapytań",
"count": 1,
"id": "WS-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Konkretną poprawkę, którą możesz przekazać developerowi",
"new": "Konkretna poprawka, którą przekażesz developerowi lub wprowadzisz sam",
"count": 1,
"id": "WS-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`Wezwania do działania`,",
"new": "[`Przyciski i kontakt`,",
"count": 1,
"id": "WS-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Czy na urządzeniach mobilnych wszystko jest czytelne, szybkie i łatwe do kliknięcia.",
"new": "Czy na telefonie wszystko jest czytelne, szybkie i łatwe do kliknięcia.",
"count": 1,
"id": "WS-6"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Osobiście, krok po kroku, jak Twój klient.",
"new": "Osobiście, krok po kroku, jak Twój klient, na komputerze i telefonie.",
"count": 1,
"id": "WS-7"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Audyt obejmuje stronę firmową do ok. 20 podstron. Masz większy serwis? Napisz, przygotuję indywidualną wycenę.",
"new": "Audyt obejmuje stronę firmową do ok. 20 podstron. Masz większy serwis? Napisz na kontakt@uxaudyt.pl, przygotuję indywidualną wycenę. Makiety nie są częścią tego pakietu: każdą poprawkę opisuję słowami i pokazuję na zrzucie ekranu.",
"count": 1,
"id": "WS-10"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "h:[`Od raportu`,`do efektów.`]",
"new": "h:[`Raport, makiety`,`i 30 dni wsparcia.`]",
"count": 1,
"id": "OP-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Audyt to dopiero początek. W tym pakiecie zostaję z Tobą, aż poprawki będą wdrożone: omawiamy raport na warsztacie, projektuję makiety wszystkich krytycznych poprawek, przez 30 dni pomagam Tobie i Twojemu developerowi, a na koniec sprawdzam sklep jeszcze raz.",
"new": "Ten pakiet jest dla sklepów, które chcą pomocy także po wysłaniu raportu. Raport omawiamy na warsztacie z Twoim zespołem, projektuję makiety wszystkich krytycznych poprawek, a przez 30 dni od warsztatu odpowiadam e-mailem na pytania Twoje i developera. Po zmianach sprawdzam sklep jeszcze raz. Względem audytu sklepu dopłacasz 1500 zł netto.",
"count": 1,
"id": "OP-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "gets:[`Wszystko z audytu sklepu internetowego`,`Warsztat online",
"new": "gets:[`Wszystko z audytu sklepu: raport PDF w 5 dni roboczych`,`Warsztat online",
"count": 1,
"id": "OP-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Warsztat online z omówieniem raportu, z Tobą i Twoim zespołem",
"new": "Warsztat online z Tobą i Twoim zespołem",
"count": 1,
"id": "OP-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "30 dni wsparcia przy wdrożeniu: odpowiadam na pytania i sprawdzam postępy",
"new": "30 dni wsparcia e-mailem i ponowne sprawdzenie sklepu po zmianach",
"count": 1,
"id": "OP-6"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`,`Ponowne sprawdzenie sklepu po zmianach`],note:",
"new": "`,`Zwrot całej kwoty na zasadach gwarancji, jak w audycie sklepu`],note:",
"count": 1,
"id": "OP-7"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Sklepy, które chcą przejść od raportu do realnych zmian",
"new": "Sklepy, które chcą wdrożyć poprawki z raportu w ciągu najbliższego miesiąca",
"count": 1,
"id": "OP-8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Właściciele, którzy chcą mieć pewność, że poprawki zostaną zrobione dobrze",
"new": "Właściciele, którzy chcą, żeby developer miał kogo zapytać w trakcie zmian",
"count": 1,
"id": "OP-10"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "W 5 dni roboczych, jak w audycie sklepu.",
"new": "W 5 dni roboczych od zaksięgowania płatności, jak w audycie sklepu.",
"count": 1,
"id": "OP-11"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Omawiamy raport i ustalamy kolejność zmian.",
"new": "Umawiamy go zaraz po raporcie. Omawiamy wyniki z Tobą i zespołem i ustalamy kolejność zmian.",
"count": 1,
"id": "OP-12"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Projektuję wszystkie krytyczne poprawki.",
"new": "Projektuję makiety wszystkich krytycznych poprawek, gotowe dla developera.",
"count": 1,
"id": "OP-13"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Pomagam przy wdrożeniu, a na koniec sprawdzam sklep jeszcze raz.",
"new": "Przez 30 dni od warsztatu odpowiadam e-mailem na pytania. W tym czasie możesz zgłosić jedno ponowne sprawdzenie sklepu.",
"count": 1,
"id": "OP-14"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "h1:`Wdrożenie poprawek UX`",
"new": "h1:`Wdrożenie poprawek z audytu UX`",
"count": 1,
"id": "WD-H1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Zaprojektuję poprawki w Figmie i wdrożę je na Twojej platformie albo poprowadzę Twojego developera. Przygotuję wycenę po napisaniu raportu UX, gdy będzie wiadomo, co dokładnie jest do zrobienia.",
"new": "Poprawki zrobi ten, kto je znalazł. Zaprojektuję je w Figmie i wdrożę na Twojej platformie albo poprowadzę Twojego developera. Wycenę przygotuję, gdy będzie wiadomo, co jest do zrobienia, czyli po raporcie.",
"count": 1,
"id": "WD-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "style:{fontSize:11,marginTop:10},children:`Przygotuję wycenę po napisaniu raportu UX`}",
"new": "style:{fontSize:11,marginTop:10},children:`Zależy od liczby i rodzaju poprawek`}",
"count": 1,
"id": "WD-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Wycenę bez zobowiązań, przygotowaną po napisaniu raportu UX",
"new": "Wycena bez zobowiązań, gdy wiadomo, co jest do zrobienia",
"count": 1,
"id": "WD-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Makiety w Figmie dla desktopu oraz urządzeń mobilnych, gotowe do wdrożenia.",
"new": "Makiety w Figmie na komputer i telefon, gotowe do wdrożenia.",
"count": 1,
"id": "WD-7"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "PrestaShop, Shopify, WooCommerce, Shoper, IdoSell i inne.",
"new": "PrestaShop (status PrestaShop Expert), Shopify, WooCommerce, Shoper, IdoSell i inne.",
"count": 1,
"id": "WD-8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Wdrożenie wyceniam po audycie, bo dopiero wtedy wiadomo, co jest do zrobienia. Jeśli masz już raport UX od kogoś innego, też możemy porozmawiać.",
"new": "Wdrożenie wyceniam po audycie, bo dopiero wtedy wiadomo, co jest do zrobienia. Wiele poprawek jest małych: w przykładowym raporcie siedem poprawek to ok. 3 dni pracy. Masz już raport UX od innej firmy? Napisz, porozmawiamy.",
"count": 1,
"id": "WD-9"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "cta:`Zapytaj o wdrożenie`",
"new": "cta:`Poproś o wycenę wdrożenia`",
"count": 1,
"id": "WD-10"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "ctaH:`Twoje poprawki.`",
"new": "ctaH:`Twój plan wdrożenia.`",
"count": 1,
"id": "WD-11"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Zaczynamy od audytu strony albo sklepu.",
"new": "Zaczynamy od audytu strony albo sklepu. Masz raport od innej firmy? Zaczynamy od niego.",
"count": 1,
"id": "WD-12"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Ocena strony internetowej na desktopie oraz urządzeniach mobilnych pod kątem",
"new": "Ocena strony internetowej na komputerze i telefonie pod kątem",
"count": 1,
"id": "schema-strona"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "od wejścia do płatności na desktopie oraz urządzeniach mobilnych. Raport",
"new": "od wejścia do płatności na komputerze i telefonie. Raport",
"count": 1,
"id": "schema-sklep"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Audyt UX sklepu internetowego z konsultacjami i sprawdzeniem wdrożonych poprawek.",
"new": "Audyt UX sklepu internetowego z warsztatem, makietami krytycznych poprawek, 30 dniami wsparcia e-mailem i ponownym sprawdzeniem sklepu.",
"count": 1,
"id": "schema-opieka"
},
{
"op": "rep",
"file": "src/c/Raport.mjs",
"old": "Cała ścieżka zakupu na desktopie oraz urządzeniach mobilnych: strona główna, kategoria, karta produktu, koszyk i płatność.",
"new": "Przykład poglądowy, uogólniony z typowych błędów w sklepach. Zakres taki jak w audycie: cała ścieżka zakupu na komputerze i telefonie, od strony głównej przez kategorię i kartę produktu po koszyk i płatność.",
"count": 1,
"id": "R-1"
},
{
"op": "rep",
"file": "src/c/Raport.mjs",
"old": "Otrzymasz go w 5 dni roboczych, razem z makietami poprawek. Jeśli nie znajdę nic, co wpływa na sprzedaż, oddam Ci pieniądze.",
"new": "Raport otrzymasz w 5 dni roboczych od zaksięgowania płatności. Audyt sklepu kosztuje 2990 zł netto (3677,70 zł brutto). Jeśli raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w terminie, chyba że opóźnienie wynika z niedostępności Twojego sklepu, zwrócę całą kwotę.",
"count": 1,
"id": "R-2"
},
{
"op": "rep",
"file": "src/c/Raport.mjs",
"old": "w === 1 ? `dzień wdrożenia` : `dni wdrożenia`",
"new": "w === 1 ? `dzień pracy na wdrożenie` : `dni pracy na wdrożenie`",
"count": 1,
"id": "R-5/6"
},
{
"op": "rep",
"file": "src/c/Raport.mjs",
"old": "` Wróć na stronę`",
"new": "` Wróć na stronę główną`",
"count": 1,
"id": "R-7"
},
{
"op": "rep",
"file": "src/c/Raport.mjs",
"old": "`Przykładowy raport z audytu UX sklepu`,\\n                  c(`span`, {\\n                    style: {\\n                      display: `block`,",
"new": "`Przykładowy raport z audytu UX sklepu`,\\n                  ` `,\\n                  c(`span`, {\\n                    style: {\\n                      display: `block`,",
"count": 1,
"id": "R-H1-space"
},
{
"op": "rep",
"file": "src/pages.mjs",
"old": "title: 'Przykładowy raport z audytu UX · uxaudyt.pl'",
"new": "title: 'Przykładowy raport z audytu UX sklepu (wzór) | uxaudyt.pl'",
"count": 1,
"id": "7.1-pages"
},
{
"op": "rep",
"file": "src/c/shared-lib.mjs",
"old": "'/przykladowy-raport':'Przykładowy raport z audytu UX · uxaudyt.pl'",
"new": "'/przykladowy-raport':'Przykładowy raport z audytu UX sklepu (wzór) | uxaudyt.pl'",
"count": 1,
"id": "7.1-shared"
},
{
"op": "rep",
"file": "src/c/shared-lib.mjs",
"old": "var D='Audyty UX sklepów internetowych. Konkretne problemy, gotowe poprawki i liczby, które pokazują, ile sklep traci. Oficjalny partner PrestaShop.'",
"new": "var D='Zamów audyt UX sklepu lub strony. Stała cena, raport PDF w 5 dni roboczych od zaksięgowania płatności, gwarancja zwrotu.'",
"count": 1,
"id": "9.1-shared-D"
},
{
"op": "rep",
"file": "src/pages.mjs",
"old": "key === 'zamowienie' ? 'Zamówienie audytu · uxaudyt.pl' : 'Zamówienie · uxaudyt.pl'",
"new": "key === 'zamowienie' ? 'Zamówienie audytu · uxaudyt.pl' : 'Zamówienie audytu z opieką · uxaudyt.pl'",
"count": 1,
"id": "9.1-pages"
},
{
"op": "rep",
"file": "src/c/shared-lib.mjs",
"old": "'/zamowienie-plan':'Zamówienie · uxaudyt.pl'",
"new": "'/zamowienie-plan':'Zamówienie audytu z opieką · uxaudyt.pl'",
"count": 1,
"id": "9.1-shared"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "To zajmie Ci około 2 minut. Raport otrzymasz ${E} od płatności.",
"new": "To zajmie Ci około 2 minut. Raport otrzymasz ${E} od zaksięgowania płatności.",
"count": 1,
"id": "Z-1"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Re(Y?`Zamów audyt strony internetowej`:`Zamów audyt sklepu internetowego`)",
"new": "Re(Y?`Zamów audyt strony internetowej`:Me?`Zamów audyt sklepu z opieką`:`Zamów audyt sklepu internetowego`)",
"count": 1,
"id": "Z-2"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Cała ścieżka zakupu na desktopie oraz urządzeniach mobilnych. Lista problemów od najważniejszych i 3 makiety poprawek.",
"new": "Cała ścieżka zakupu na komputerze i telefonie. Raport PDF z problemami od najważniejszych, poprawka przy każdym i rozmowa o raporcie.",
"count": 1,
"id": "Z-3"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Wszystko z audytu + 60 min omówienia i plan wdrożenia na 30 dni",
"new": "Wszystko z audytu sklepu oraz warsztat online z omówieniem raportu, makiety wszystkich krytycznych poprawek, 30 dni wsparcia e-mailem od warsztatu i jednorazowe ponowne sprawdzenie sklepu.",
"count": 1,
"id": "Z-5"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Strona firmowa do ok. 20 podstron: oferta, przyciski kontaktu, formularze i wersja mobilna.",
"new": "Strona firmowa do ok. 20 podstron: oferta, przyciski kontaktu, formularze i wersja mobilna. Raport PDF i rozmowa o raporcie.",
"count": 2,
"id": "Z-6"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "v:`zwrot, jeśli nic nie znajdę`",
"new": "v:`zwrot całej kwoty na zasadach gwarancji`",
"count": 1,
"id": "Z-8"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Zaprojektuję poprawki w Figmie i wdrożę je na Twojej platformie albo razem z Twoim developerem. Przygotuję wycenę po napisaniu raportu UX.",
"new": "Zaprojektuję poprawki w Figmie i wdrożę je na Twojej platformie albo poprowadzę Twojego developera. Wycenę przygotuję po raporcie, cena audytu się nie zmienia.",
"count": 1,
"id": "Z-9"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "wycenię po raporcie UX",
"new": "wycena po raporcie, bez zobowiązań",
"count": 1,
"id": "Z-10"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Nie udało się wysłać zamówienia. Spróbuj ponownie albo napisz na kontakt@uxaudyt.pl.",
"new": "Nie udało się wysłać zamówienia. Płatność nie została pobrana. Spróbuj ponownie albo napisz na kontakt@uxaudyt.pl.",
"count": 1,
"id": "Z-11"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Zaczynam przechodzić Twój sklep",
"new": "Zaczynam audyt",
"count": 1,
"id": "G-1"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Me?`Raport PDF, a potem umawiamy rozmowę`:`Raport PDF trafia do Twojej skrzynki`",
"new": "Me?`Raport PDF na e-mail, potem umawiamy warsztat`:`Raport PDF na e-mail, potem umawiamy rozmowę`",
"count": 1,
"id": "G-2/G-3"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "Jeśli czegoś potrzebuję, napiszę e-mailem",
"new": "Jeśli czegoś będę potrzebować, napiszę e-mailem",
"count": 1,
"id": "G-4"
},
{
"op": "rep",
"file": "src/c/Checkout.mjs",
"old": "(e.url=`Podaj adres sklepu, np. twojsklep.pl`)",
"new": "(e.url=Y?`Podaj adres strony, np. twojafirma.pl`:`Podaj adres sklepu, np. twojsklep.pl`)",
"count": 1,
"id": "Z-valid"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`Odpowiedź otrzymasz na e-mail, zwykle w ciągu 1–2 dni roboczych, z informacją",
"new": "`Odpowiedź otrzymasz e-mailem, zwykle w ciągu 2 dni roboczych, z informacją",
"count": 1,
"id": "F13-tldr"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "1. **Odpisuję na e-mail**, zwykle w ciągu 1–2 dni roboczych.",
"new": "1. **Odpisuję e-mailem**, zwykle w ciągu 2 dni roboczych.",
"count": 1,
"id": "D-1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "| Zakres | Pierwsze wrażenie i najbardziej widoczne problemy | Cała ścieżka zakupu na desktopie i telefonie",
"new": "| Zakres | Pierwsze wrażenie i najbardziej widoczne problemy | Cała ścieżka zakupu na komputerze i telefonie",
"count": 1,
"id": "D-2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "| Forma | Odpowiedź na e-mail | Raport ze zrzutami ekranu i konkretnymi poprawkami",
"new": "| Forma | Odpowiedź e-mailem | Raport PDF ze zrzutami ekranu i konkretnymi poprawkami",
"count": 1,
"id": "D-3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "| Czas | Zwykle 1–2 dni robocze | 5 dni roboczych",
"new": "| Czas | Zwykle do 2 dni roboczych | 5 dni roboczych od zaksięgowania płatności",
"count": 1,
"id": "D-4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "| Cena | Bezpłatnie | Od 1990 zł netto",
"new": "| Cena | Bezpłatnie | [Od 1990 zł netto](/#cennik)",
"count": 1,
"id": "D-5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Wstępna ocena pomaga zdecydować, czy warto iść dalej. Pełny [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) daje gotową listę zmian do wdrożenia.",
"new": "Wstępna ocena pomaga zdecydować, czy warto iść dalej. Pełny [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) daje gotową listę zmian do wdrożenia, ułożoną od najważniejszych, za stałą cenę i z gwarancją zwrotu.",
"count": 1,
"id": "D-6"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`Przykład z audytu · `",
"new": "`Przykład poglądowy · `",
"count": 1,
"id": "D-7/T1"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Nie. Do wstępnej oceny wystarczy adres sklepu albo strony. Przeglądam ją tak, jak widzi ją klient.",
"new": "Nie. Do wstępnej oceny wystarczy adres sklepu albo strony. Przeglądam ją tak, jak widzi ją klient. Nie potrzebuję też dostępu do Google Analytics.",
"count": 1,
"id": "D-8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`Zwykle 1–2 dni robocze. Odpowiedź otrzymasz",
"new": "`Zwykle do 2 dni roboczych. Odpowiedź otrzymasz",
"count": 1,
"id": "F13-faq"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "d(`div`,{className:`v7-gauth-p`,children:`Oficjalny partner PrestaShop`})",
"new": "d(`div`,{className:`v7-gauth-p`,children:`13 lat projektowania produktów · Creative Vision, PrestaShop Expert`})",
"count": 1,
"id": "T2"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "e===t?d(`em`,{children:`Oficjalny partner`}):null]},t))",
"new": "e===t?d(`em`,{children:`PrestaShop Expert`}):null]},t))",
"count": 1,
"id": "T3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Patrzę na sklep oczami klienta, więc platforma nie ogranicza audytu. Przy PrestaShop podpowiem też konkretne ustawienia i moduły.",
"new": "Patrzę na sklep oczami klienta, więc platforma nie ogranicza audytu. Przy każdej poprawce piszę, czy zmienisz ją w panelu, czy potrzebna będzie wtyczka, aplikacja albo programista.",
"count": 1,
"id": "T4"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "d(`a`,{className:`v7-ul v7-gcta-l`,href:t.report,children:`Zobacz przykładowy raport`})",
"new": "d(`a`,{className:`v7-ul v7-gcta-l`,href:t.report,children:`Zobacz przykładowy raport`}),d(`a`,{className:`v7-ul v7-gcta-l`,href:`/audyt-sklepu-internetowego`,children:`Audyt sklepu: 2990 zł netto, raport w 5 dni roboczych`})",
"count": 1,
"id": "T5"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Audyt UX sklepów internetowych i stron www. Marcin Bednarz, oficjalny partner PrestaShop.",
"new": "Audyt UX sklepów internetowych i stron www. Audyt wykonuje osobiście Marcin Bednarz, projektant UX z 13-letnim doświadczeniem. Studio Creative Vision, PrestaShop Expert.",
"count": 1,
"id": "T6"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "Xe=[`audyt-ux`,`darmowy-audyt-sklepu`,`niska-konwersja-sklepu`,`porzucone-koszyki`,`karta-produktu-checklista`,`ux-sklepu-mobilnego`,`jak-sprawdzic-ux-sklepu`,`audyt-ux-prestashop`,`audyt-ux-woocommerce`,`audyt-ux-shopify`,`audyt-ux-a-audyt-seo`]",
"new": "Xe=[`audyt-ux`,`jak-zwiekszyc-sprzedaz-sklepu`,`checklista-audytu-ux`,`darmowy-audyt-sklepu`,`niska-konwersja-sklepu`,`porzucone-koszyki`,`karta-produktu-checklista`,`ux-sklepu-mobilnego`,`jak-sprawdzic-ux-sklepu`,`audyt-ux-prestashop`,`audyt-ux-woocommerce`,`audyt-ux-shopify`,`audyt-ux-shoper`,`audyt-ux-a-audyt-seo`]",
"count": 1,
"id": "T7"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Audyt UX to sprawdzenie, czy klient bez przeszkód znajdzie na Twojej stronie to, czego szuka, i dokończy zakup albo wyśle zapytanie. W tym poradniku wyjaśniam, co dokładnie obejmuje taki audyt, jak przebiega krok po kroku i ile kosztuje.",
"new": "Audyt UX to ekspercka ocena sklepu lub strony oczami klienta: sprawdzam, gdzie klient się waha, gubi albo rezygnuje, i przy każdym takim miejscu podaję konkretną poprawkę. W uxaudyt.pl audyt strony internetowej kosztuje 1990 zł netto, a sklepu 2990 zł netto. Raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności, a potem omawiamy go na rozmowie.",
"id": "AUX-1"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Audyt sklepu kosztuje od 2990 zł netto, strony firmowej 1990 zł netto, a raport otrzymasz w 5 dni roboczych.",
"new": "Audyt sklepu kosztuje 2990 zł netto, strony firmowej 1990 zł netto. Raport otrzymasz w 5 dni roboczych od zaksięgowania płatności.",
"id": "AUX-2"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "UX (user experience) to doświadczenie użytkownika, czyli wszystko, co klient czuje i robi, korzystając z Twojej strony. Audyt UX polega na przejściu strony oczami klienta i oznaczeniu miejsc, w których może się zawahać, zgubić albo zrezygnować.",
"new": "UX (user experience) to doświadczenie użytkownika, czyli wszystko, co klient czuje i robi, korzystając z Twojej strony. Audyt UX polega na przejściu strony oczami klienta i oznaczeniu miejsc, w których może się zawahać, zgubić albo zrezygnować. Spotkasz też nazwy „audyt użyteczności”, „audyt ekspercki” albo „ocena heurystyczna”. Chodzi o to samo: ekspert ocenia stronę według zasad użyteczności, bez badania z udziałem klientów.",
"id": "AUX-3"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "W sklepie internetowym najważniejsza jest ścieżka zakupu. Sprawdzam ją na desktopie oraz urządzeniach mobilnych:",
"new": "W sklepie internetowym najważniejsza jest ścieżka zakupu. Sprawdzam ją na komputerze i na telefonie:",
"id": "AUX-4"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Audyt strony firmowej skupia się na czymś innym: czy oferta jest jasna, czy klient łatwo znajdzie kontakt i czy formularz nie zniechęca do wysłania zapytania.",
"new": "Audyt strony firmowej skupia się na czymś innym: czy oferta jest jasna, czy klient łatwo znajdzie kontakt i czy formularz nie zniechęca do wysłania zapytania. Szczegóły i cenę znajdziesz na stronie [audytu UX strony internetowej](/audyt-strony-internetowej).",
"id": "AUX-5"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "1. **Zamówienie i krótki brief.** Podajesz adres strony i mówisz, co jest dla Ciebie najważniejsze, np. sprzedaż konkretnej kategorii.",
"new": "1. **Zamówienie i krótka notatka.** Podajesz adres strony i, jeśli chcesz, piszesz, co jest dla Ciebie najważniejsze, np. sprzedaż konkretnej kategorii.",
"id": "AUX-6"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "1. **Raport.** Opisuję każde miejsce do poprawy ze zrzutem ekranu i propozycją zmiany. Raport otrzymasz w 5 dni roboczych.",
"new": "1. **Raport.** Opisuję każde miejsce do poprawy ze zrzutem ekranu i propozycją zmiany. Raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności.",
"id": "AUX-7"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "- osobne spojrzenie na desktop oraz urządzenia mobilne.",
"new": "- osobne spojrzenie na komputer i na telefon.",
"id": "AUX-8"
},
{
"op": "gins",
"key": "audyt-ux",
"after": "::report",
"lines": [
"## Audyt UX a testy z użytkownikami",
"Audyt UX robi ekspert, który przechodzi sklep według zasad użyteczności i dobrych praktyk e-commerce. Testy z użytkownikami polegają na obserwowaniu prawdziwych osób, które wykonują w sklepie konkretne zadania, np. znalezienie i zamówienie produktu.",
"Audyt jest szybszy i tańszy, dlatego zwykle od niego się zaczyna. Testy mają sens później, gdy chcesz sprawdzić wybrane rozwiązanie na klientach albo rozstrzygnąć, która z dwóch wersji jest wygodniejsza."
],
"id": "AUX-9"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "## Ile kosztuje audyt UX",
"new": "## Ile kosztuje audyt UX i od czego zależy cena",
"id": "AUX-10"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "| [Audyt sklepu z opieką](/audyt-sklepu-z-opieka) | 4490 zł | Sklepy, które chcą przejść od raportu do efektów z pomocą przy wdrożeniu",
"new": "| [Audyt sklepu z opieką](/audyt-sklepu-z-opieka) | 4490 zł | Sklepy, które chcą pomocy przy wdrożeniu: warsztat po raporcie i 30 dni wsparcia",
"id": "AUX-11"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Na początek możesz zamówić [bezpłatną wstępną ocenę](/#ocena). To szybkie spojrzenie na Twój sklep, po którym wiesz, czy pełny audyt ma sens.",
"new": "Na początek możesz poprosić o [bezpłatną wstępną ocenę](/darmowy-audyt-sklepu). To szybkie spojrzenie na Twój sklep, po którym wiesz, czy pełny audyt ma sens. Przy mniej niż ok. 50 zamówieniach miesięcznie napiszę wprost, jeśli audyt może się jeszcze nie zwrócić.",
"id": "AUX-12"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "- Klienci często dodają produkty do koszyka, ale nie kończą zakupu. Według [Baymard Institute](https://baymard.com/lists/cart-abandonment-rate) przeciętnie porzucanych jest ok. 70% koszyków. Najczęstsze przyczyny opisuję w poradniku [Porzucone koszyki](/porzucone-koszyki).",
"new": "- Klienci często dodają produkty do koszyka, ale nie kończą zakupu. Według zestawienia 50 badań [Baymard Institute](https://baymard.com/lists/cart-abandonment-rate) (aktualizacja z września 2025) przeciętnie porzucanych jest ok. 70% koszyków. Najczęstsze przyczyny opisuję w poradniku [Porzucone koszyki](/porzucone-koszyki).",
"id": "AUX-13"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Część rzeczy sprawdzisz samodzielnie, przechodząc zakup we własnym sklepie na telefonie i na komputerze. Trudniej jest jednak spojrzeć na własny sklep jak ktoś, kto widzi go pierwszy raz, i ułożyć poprawki od najważniejszych. Do tego przydaje się ktoś z zewnątrz.",
"new": "Część rzeczy sprawdzisz samodzielnie, przechodząc zakup we własnym sklepie na telefonie i na komputerze. Pomoże Ci w tym [scenariusz na 30 minut](/jak-sprawdzic-ux-sklepu) i [checklista audytu UX sklepu](/checklista-audytu-ux) z 25 punktami. Trudniej jest jednak spojrzeć na własny sklep jak ktoś, kto widzi go pierwszy raz, i ułożyć poprawki od najważniejszych. Do tego przydaje się ktoś z zewnątrz.",
"id": "AUX-14"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Raport otrzymasz w 5 dni roboczych od zamówienia.",
"new": "Raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Potem umawiamy rozmowę, na której przechodzimy przez najważniejsze punkty.",
"id": "AUX-15"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Tak. Sprawdzam sklepy na PrestaShop, Shopify, WooCommerce, Shoperze, IdoSell i innych platformach. Jako oficjalny partner PrestaShop najlepiej znam możliwości tej platformy.",
"new": "Tak. Sprawdzam to, co widzi klient, więc audyt działa w sklepie na PrestaShop, Shopify, WooCommerce, Shoperze, IdoSell, Magento i innych platformach. Prowadzę studio Creative Vision ze statusem PrestaShop Expert, więc możliwości PrestaShop znam najlepiej.",
"id": "AUX-16"
},
{
"op": "grep",
"key": "audyt-ux",
"old": "Sprawdzę tak samo Twój sklep. Zacznij od bezpłatnej wstępnej oceny.",
"new": "Audyt sklepu kosztuje 2990 zł netto, a raport otrzymasz w 5 dni roboczych. Nie wiesz, czy to dobry moment? Zacznij od bezpłatnej wstępnej oceny.",
"id": "AUX-18"
},
{
"op": "grep",
"key": "audyt-ux-a-audyt-seo",
"old": "Audyt SEO sprawdza, czy klienci trafią na Twoją stronę z Google. Audyt UX sprawdza, czy po wejściu kupią albo wyślą zapytanie. To dwa różne pytania, a dobra odpowiedź na jedno nie załatwia drugiego.",
"new": "Audyt SEO sprawdza, czy klienci trafią na Twoją stronę z Google, a audyt UX, czy po wejściu kupią albo wyślą zapytanie. Masz ruch, ale mało zamówień? Zacznij od audytu UX. Ruchu prawie nie ma? Zacznij od SEO.",
"id": "SEO-1"
},
{
"op": "grep",
"key": "audyt-ux-a-audyt-seo",
"old": "Masz ruch, ale mało zamówień? Zacznij od UX. Ruchu prawie nie ma? Zacznij od SEO.",
"new": "Więcej ruchu z Google nie pomoże, jeśli nowi klienci trafią w sklepie na te same przeszkody co obecni.",
"id": "SEO-2"
},
{
"op": "grep",
"key": "audyt-ux-a-audyt-seo",
"old": "| Efekty widać | Zwykle zaraz po wdrożeniu poprawek | Zwykle po kilku tygodniach lub miesiącach",
"new": "| Kiedy mierzyć efekt | Od dnia wdrożenia poprawek, na ruchu, który już masz | Zwykle po kilku tygodniach lub miesiącach",
"id": "SEO-3"
},
{
"op": "grep",
"key": "audyt-ux-a-audyt-seo",
"old": "Część poprawek pomaga obu stronom naraz. Szybsze ładowanie, czytelna struktura nagłówków, sensowna nawigacja i wygodna wersja mobilna są ważne zarówno dla klientów, jak i dla Google. Dlatego w audycie UX zwracam uwagę również na te elementy.",
"new": "Część poprawek pomaga obu stronom naraz. Szybsze ładowanie, czytelna struktura nagłówków, sensowna nawigacja i wygodna wersja mobilna są ważne zarówno dla klientów, jak i dla Google. Google potwierdza, że wskaźniki Core Web Vitals są używane przez jego systemy rankingowe, ale najważniejsza pozostaje trafność treści ([Google Search Central](https://developers.google.com/search/docs/appearance/page-experience)). Dlatego w audycie UX zwracam uwagę również na te elementy.",
"id": "SEO-4"
},
{
"op": "grep",
"key": "audyt-ux-a-audyt-seo",
"old": "Ceny audytów SEO zależą od agencji i wielkości sklepu. Audyt UX w uxaudyt.pl ma stałą cenę: 1990 zł netto za [stronę internetową](/audyt-strony-internetowej) i 2990 zł netto za [sklep internetowy](/audyt-sklepu-internetowego). Szczegóły znajdziesz w poradniku [Audyt UX: co to jest, jak wygląda i ile kosztuje](/audyt-ux).",
"new": "Ceny audytów SEO zależą od agencji i wielkości sklepu. Audyt UX w uxaudyt.pl ma stałą cenę: 1990 zł netto za [stronę internetową](/audyt-strony-internetowej) i 2990 zł netto za [sklep internetowy](/audyt-sklepu-internetowego). Raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Szczegóły znajdziesz w poradniku [Audyt UX: co to jest, jak wygląda i ile kosztuje](/audyt-ux), a jeśli nie wiesz, od którego audytu zacząć, poproś o [bezpłatną wstępną ocenę](/darmowy-audyt-sklepu).",
"id": "SEO-6"
},
{
"op": "grep",
"key": "audyt-ux-a-audyt-seo",
"old": "Pośrednio tak. Szybkość strony i wygoda na telefonie są sygnałami, które Google bierze pod uwagę. Głównym efektem dobrego UX jest jednak więcej zamówień z ruchu, który już masz.",
"new": "Pośrednio tak. Google podaje, że jego systemy rankingowe biorą pod uwagę wskaźniki Core Web Vitals, czyli m.in. szybkość i stabilność strony. Najważniejsza pozostaje jednak trafność treści. Głównym celem poprawek UX jest więcej zamówień z ruchu, który już masz.",
"id": "SEO-8"
},
{
"op": "grep",
"key": "audyt-ux-a-audyt-seo",
"old": "Nie wiesz, od którego zacząć? W bezpłatnej wstępnej ocenie podpowiem, czy Twój sklep bardziej potrzebuje poprawek UX.",
"new": "Nie wiesz, od którego zacząć? W bezpłatnej wstępnej ocenie podpowiem, czy Twój sklep bardziej potrzebuje poprawek UX. Pełny audyt sklepu kosztuje 2990 zł netto.",
"id": "SEO-10"
},
{
"op": "grep",
"key": "audyt-ux-prestashop",
"old": "PrestaShop daje dużo możliwości, ale domyślne ustawienia i dodawane latami moduły potrafią utrudnić klientom zakup. Jako oficjalny partner PrestaShop opisuję miejsca, które warto sprawdzić w pierwszej kolejności, i to, jak je poprawić.",
"new": "W sklepie na PrestaShop sprawdź najpierw siedem miejsc: proces zamówienia, pola formularzy i zgody, okno po dodaniu do koszyka, wyszukiwarkę i filtry, kartę produktu, płatności oraz szybkość. Wiele poprawek wprowadzisz ustawieniami i modułami, bez przebudowy sklepu. Prowadzę studio Creative Vision ze statusem PrestaShop Expert, więc przy każdym punkcie podpowiadam, od czego zacząć.",
"id": "PS-1"
},
{
"op": "grep",
"key": "audyt-ux-prestashop",
"old": "Jako oficjalny partner PrestaShop wiem, które poprawki da się wdrożyć szybko.",
"new": "Najszybciej wdrożysz zwykle zakup bez konta, krótszy formularz i uporządkowaną listę płatności.",
"id": "PS-2"
},
{
"op": "grep",
"key": "audyt-ux-prestashop",
"old": "**Co poprawić:** włącz zakup bez konta, pokaż podsumowanie zamówienia na każdym kroku i usuń kroki, których Twój sklep nie potrzebuje.",
"new": "**Co poprawić:** włącz zakup bez konta w ustawieniach zamówień (Parametry sklepu → Ustawienia zamówień, opcja zamówień gości; w [dokumentacji PrestaShop 8](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/order-settings/orders-preferences) to „Enable guest checkout”). Pokaż podsumowanie zamówienia na każdym kroku i usuń kroki, których Twój sklep nie potrzebuje.",
"id": "PS-3"
},
{
"op": "grep",
"key": "audyt-ux-prestashop",
"old": "**Co poprawić:** pokaż w koszyku koszt dostawy i próg darmowej wysyłki, zanim klient przejdzie dalej.",
"new": "**Co poprawić:** na telefonie zostaw w tym oknie jeden wyraźny przycisk przejścia do koszyka, a „kontynuuj zakupy” jako mniej widoczny link. W koszyku pokaż koszt dostawy i próg darmowej wysyłki, zanim klient przejdzie dalej.",
"id": "PS-4"
},
{
"op": "grep",
"key": "audyt-ux-prestashop",
"old": "[Audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje wszystkie powyższe miejsca na desktopie oraz urządzeniach mobilnych. Raport otrzymasz w 5 dni roboczych. Jeśli chcesz, poprawki zaprojektuję i wdrożę w Twoim sklepie w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek).",
"new": "[Audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje wszystkie powyższe miejsca, na komputerze i na telefonie. Kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Do audytu wystarczy adres sklepu, bez dostępu do panelu. Jeśli chcesz, poprawki zaprojektuję i wdrożę w Twoim sklepie w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek).",
"id": "PS-5"
},
{
"op": "grep",
"key": "audyt-ux-prestashop",
"old": "faq:[],cta:`",
"new": "faq:[[`Jak włączyć zakup bez konta w PrestaShop?`,`W panelu wejdź w Parametry sklepu → Ustawienia zamówień i włącz zamówienia gości (w dokumentacji PrestaShop ta opcja nazywa się „Enable guest checkout”). Założenie konta zaproponuj klientowi po zakupie.`],[`Czy do audytu potrzebujesz dostępu do panelu PrestaShop?`,`Nie. Do audytu wystarczy adres sklepu, bo sprawdzam to, co widzi klient. Dostęp do panelu jest potrzebny dopiero wtedy, gdy zlecisz mi wdrożenie poprawek.`],[`Co oznacza status PrestaShop Expert?`,`To status w programie partnerskim PrestaShop (PrestaShop Expert Program). Ma go studio Creative Vision, które prowadzę i w którym projektujemy oraz wdrażamy sklepy na tej platformie.`]],cta:`",
"id": "PS-7"
},
{
"op": "grep",
"key": "audyt-ux-prestashop",
"old": "Sprawdzę Twój sklep na PrestaShop. Zacznij od bezpłatnej wstępnej oceny.",
"new": "Sprawdzę Twój sklep na PrestaShop. Audyt kosztuje 2990 zł netto, a na start możesz poprosić o bezpłatną wstępną ocenę.",
"id": "PS-8"
},
{
"op": "grep",
"key": "audyt-ux-shopify",
"old": "Shopify zdejmuje z właściciela sklepu wiele technicznych problemów, a proces płatności jest tam dopracowany. Mimo to sklepy na Shopify tracą klientów, głównie przed dojściem do płatności. Oto miejsca, które sprawdzam w pierwszej kolejności.",
"new": "W sklepie na Shopify sprawdź najpierw to, co dzieje się przed płatnością: motyw i stronę główną, polskie tłumaczenia, kartę produktu, koszyk, aplikacje oraz lokalne płatności i dostawy. Sam checkout Shopify jest dopracowany, a własne elementy w krokach informacji, dostawy i płatności Shopify pozwala dodawać tylko sklepom na planie Shopify Plus. Dlatego najwięcej poprawek wprowadzisz w motywie i w ustawieniach sklepu.",
"id": "SH-1"
},
{
"op": "grep",
"key": "audyt-ux-shopify",
"old": "Sprawdź polskie tłumaczenia motywu i lokalne metody płatności, bo tu sklepy na Shopify najczęściej tracą zaufanie.",
"new": "Sprawdź polskie tłumaczenia motywu i lokalne metody płatności, bo braki w tych miejscach szybko obniżają zaufanie klienta z Polski.",
"id": "SH-2"
},
{
"op": "grep",
"key": "audyt-ux-shopify",
"old": "Klienci w Polsce oczekują BLIK-a, szybkich przelewów i dostawy do paczkomatu. Jeśli ich nie widzą, część z nich nie dokończy zakupu.",
"new": "Według raportu Gemius „E-commerce w Polsce 2026” z BLIK-a korzystało 67% kupujących online, a z automatów paczkowych w ciągu ostatniego roku 84% ([omówienie raportu w ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/)). Jeśli klient nie widzi tych opcji, łatwo zrezygnuje z zakupu.",
"id": "SH-3"
},
{
"op": "grep",
"key": "audyt-ux-shopify",
"old": "[Audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje całą ścieżkę zakupu na desktopie oraz urządzeniach mobilnych. Raport otrzymasz w 5 dni roboczych. Jeśli chcesz, poprawki zaprojektuję i wdrożę w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek).",
"new": "[Audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje całą ścieżkę zakupu, na komputerze i na telefonie. Kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Do audytu wystarczy adres sklepu. Przy każdej poprawce piszę, czy zmienisz ją w edytorze motywu, czy potrzebna będzie aplikacja albo zmiana w kodzie. Jeśli chcesz, poprawki zaprojektuję i wdrożę w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek).",
"id": "SH-4"
},
{
"op": "grep",
"key": "audyt-ux-shopify",
"old": "Sklepy na innych platformach mają własne typowe problemy. Opisuję je w poradnikach o [PrestaShop](/audyt-ux-prestashop) i [WooCommerce](/audyt-ux-woocommerce).",
"new": "Sklepy na innych platformach mają własne typowe problemy. Opisuję je w poradnikach o [PrestaShop](/audyt-ux-prestashop), [WooCommerce](/audyt-ux-woocommerce) i [Shoperze](/audyt-ux-shoper).",
"id": "SH-5"
},
{
"op": "grep",
"key": "audyt-ux-shopify",
"old": "W standardowych planach proces płatności jest w dużej mierze ustalony przez Shopify, co ma dobre strony: jest sprawdzony i szybki. Dlatego w audycie sklepu na Shopify najwięcej poprawek dotyczy tego, co dzieje się przed płatnością, czyli motywu, karty produktu i koszyka.",
"new": "Tylko częściowo. Własne elementy w krokach informacji, dostawy i płatności Shopify pozwala dodawać wyłącznie sklepom na planie Shopify Plus. Sam checkout jest sprawdzony i szybki, dlatego w audycie sklepu na Shopify najwięcej poprawek dotyczy tego, co dzieje się przed płatnością: motywu, karty produktu i koszyka.",
"id": "SH-7"
},
{
"op": "grep",
"key": "audyt-ux-shopify",
"old": "Sprawdzę Twój sklep na Shopify. Zacznij od bezpłatnej wstępnej oceny.",
"new": "Sprawdzę Twój sklep na Shopify. Pełny audyt kosztuje 2990 zł netto, a na start możesz poprosić o bezpłatną wstępną ocenę.",
"id": "SH-8"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "WooCommerce daje ogromną swobodę, ale ta swoboda ma swoją cenę: każdy sklep to inny motyw i inny zestaw wtyczek, a domyślne ustawienia rzadko są dopasowane do klienta. Oto miejsca, które sprawdzam w sklepach na WooCommerce w pierwszej kolejności.",
"new": "W sklepie na WooCommerce sprawdź najpierw formularz zamówienia, zakup bez konta, koszt dostawy w koszyku, warianty produktów, wtyczki i szybkość, motyw z wyszukiwarką oraz płatności. Każdy sklep na WooCommerce to inny motyw i inny zestaw wtyczek, dlatego zaczynam od tego, co widzi klient. Sposób edycji formularza zależy od tego, czy sklep ma nowy checkout blokowy, czy starszy, oparty na shortcode.",
"id": "WOO-1"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "Zacznij od procesu zamówienia na telefonie, bo tam ucieka najwięcej klientów.",
"new": "Zacznij od procesu zamówienia na telefonie, bo tam zwykle jest najwięcej przeszkód.",
"id": "WOO-2"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "**Co poprawić:** w ustawieniach motywu (Wygląd → Dostosuj → WooCommerce → Zamówienie) możesz ukryć albo oznaczyć jako opcjonalne pola firmy, drugiej linii adresu i telefonu. Pole NIP i fakturę pokaż dopiero wtedy, gdy klient zaznaczy, że jej potrzebuje.",
"new": "**Co poprawić:** ukryj albo oznacz jako opcjonalne pola firmy, drugiej linii adresu i telefonu. W checkoucie blokowym, domyślnym w nowych sklepach z motywem blokowym od WooCommerce 8.3, zrobisz to w edytorze strony zamówienia: zaznacz blok pól zamówienia i w ustawieniach pól adresu wybierz dla każdego z nich „ukryte”, „opcjonalne” albo „wymagane”. W starszym checkoucie opartym na shortcode te same opcje są w Wygląd → Dostosuj → WooCommerce → Zamówienie. Pole NIP i dane do faktury pokaż dopiero wtedy, gdy klient zaznaczy, że potrzebuje faktury.",
"id": "WOO-3"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "**Co poprawić:** w ustawieniach WooCommerce (Ustawienia → Konta i prywatność) włącz składanie zamówień bez konta. Założenie konta zaproponuj na stronie podziękowania.",
"new": "**Co poprawić:** w panelu wejdź w WooCommerce → Ustawienia → Konta i prywatność i włącz zakupy jako gość (w angielskiej wersji: „Enable guest checkout”). W tej samej zakładce pozwolisz klientom założyć konto po złożeniu zamówienia ([dokumentacja WooCommerce](https://woocommerce.com/document/accounts-and-privacy)).",
"id": "WOO-5"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "WooCommerce domyślnie pokazuje warianty jako listy rozwijane. Klient musi kliknąć, żeby zobaczyć opcje, i nie widzi od razu, które są niedostępne.",
"new": "W motywach klasycznych WooCommerce pokazuje warianty jako listy rozwijane. Klient musi kliknąć, żeby zobaczyć opcje, i nie widzi od razu, które są niedostępne.",
"id": "WOO-6"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "**Co poprawić:** pokaż warianty jako przyciski lub próbki kolorów. Wiele motywów ma to wbudowane, w innych wystarczy jedna sprawdzona wtyczka.",
"new": "**Co poprawić:** pokaż warianty jako przyciski lub próbki kolorów. W motywie blokowym przełączysz to w ustawieniach bloku wyboru wariantów, który według [dokumentacji WooCommerce](https://woocommerce.com/document/add-to-cart-options-block/) pokazuje opcje jako przyciski albo listę (blok jest oznaczony jako beta). W motywie klasycznym zwykle wystarczy ustawienie motywu albo jedna sprawdzona wtyczka.",
"id": "WOO-7"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "**Co poprawić:** zrób przegląd wtyczek i usuń nieużywane, włącz pamięć podręczną i optymalizację zdjęć, a wynik sprawdź w PageSpeed Insights dla telefonów, szczególnie na karcie produktu i w koszyku.",
"new": "**Co poprawić:** zrób przegląd wtyczek i usuń nieużywane, włącz pamięć podręczną i optymalizację zdjęć, a wynik sprawdź w [PageSpeed Insights](https://pagespeed.web.dev/) dla telefonów, szczególnie na karcie produktu i w koszyku.",
"id": "WOO-8"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "[Audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje wszystkie powyższe miejsca na desktopie oraz urządzeniach mobilnych. Raport otrzymasz w 5 dni roboczych. Jeśli chcesz, poprawki zaprojektuję i wdrożę w Twoim sklepie w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek).",
"new": "[Audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje wszystkie powyższe miejsca, na komputerze i na telefonie. Kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Przy każdej poprawce piszę, czy zmienisz ją w ustawieniach, czy potrzebna będzie wtyczka albo zmiana w motywie. Jeśli chcesz, poprawki zaprojektuję i wdrożę w Twoim sklepie w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek).",
"id": "WOO-9"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "Część pól, takich jak nazwa firmy, druga linia adresu czy telefon, możesz ukryć albo oznaczyć jako opcjonalne w ustawieniach motywu (Wygląd → Dostosuj → WooCommerce → Zamówienie). Pola, których tam nie ma, zmienisz wtyczką do edycji pól zamówienia albo w kodzie motywu potomnego.",
"new": "To zależy od rodzaju checkoutu. W checkoucie blokowym, domyślnym w nowych sklepach z motywem blokowym od WooCommerce 8.3, otwórz stronę zamówienia w edytorze, zaznacz blok pól zamówienia i ukryj albo oznacz jako opcjonalne pola firmy, drugiej linii adresu i telefonu. W starszym checkoucie opartym na shortcode te same opcje są w Wygląd → Dostosuj → WooCommerce → Zamówienie. Pozostałe pola zmienisz wtyczką albo w kodzie, przy czym w checkoucie blokowym stare filtry pól zamówienia nie działają.",
"id": "WOO-11"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "W panelu WordPressa wejdź w WooCommerce → Ustawienia → Konta i prywatność i zaznacz opcję pozwalającą składać zamówienia bez konta. Założenie konta możesz zaproponować klientowi po zakupie.",
"new": "W panelu WordPressa wejdź w WooCommerce → Ustawienia → Konta i prywatność i włącz zakupy jako gość (w angielskiej wersji: „Enable guest checkout”). W tej samej zakładce pozwolisz klientom założyć konto po złożeniu zamówienia.",
"id": "WOO-12"
},
{
"op": "grep",
"key": "audyt-ux-woocommerce",
"old": "Sprawdzę Twój sklep na WooCommerce. Zacznij od bezpłatnej wstępnej oceny.",
"new": "Sprawdzę Twój sklep na WooCommerce. Pełny audyt kosztuje 2990 zł netto, a na start możesz poprosić o bezpłatną wstępną ocenę.",
"id": "WOO-13"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Klient dodaje produkt do koszyka, a potem zamyka kartę. Według Baymard Institute tak kończy się przeciętnie ok. 70% koszyków w sklepach internetowych. Części tych osób i tak nie planowała kupić. Wiele z nich odpada jednak przez przeszkody, które da się usunąć. Poniżej opisuję 8 najczęstszych i to, jak je naprawić.",
"new": "Klienci porzucają koszyki najczęściej przez zbyt wysokie dodatkowe koszty, wymóg założenia konta, zbyt długi formularz i brak zaufania do sklepu. Według Baymard Institute porzucanych jest przeciętnie ok. 70% koszyków; część tych osób i tak nie planowała kupić, ale wiele odpada przez przeszkody, które da się usunąć. Poniżej 8 najczęstszych przyczyn i poprawka do każdej.",
"id": "PK-1"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Najczęstszy powód porzucenia koszyka to koszt dostawy, który klient poznaje dopiero przy płatności.",
"new": "Najczęstszy powód porzucenia koszyka to zbyt wysokie dodatkowe koszty, głównie dostawa. Pokaż je, zanim klient dojdzie do płatności.",
"id": "PK-2"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Klient widzi cenę produktu, a dodatkowy koszt pojawia się dopiero na końcu. Czuje się zaskoczony i rezygnuje.",
"new": "Klient widzi cenę produktu, a dodatkowy koszt pojawia się dopiero na końcu. Czuje się zaskoczony i rezygnuje. W badaniu Baymard Institute zbyt wysokie dodatkowe koszty (dostawa, podatki, opłaty) wskazało 40% kupujących w USA, którzy porzucili zamówienie z innego powodu niż „tylko oglądam”. W Polsce, według raportu Gemius „E-commerce w Polsce 2026”, ponad połowa kupujących rezygnuje z zakupu, gdy koszt dostawy okazuje się zbyt wysoki.",
"id": "PK-3"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Dla wielu osób konto to dodatkowe hasło i zgody, a chcą tylko kupić jedną rzecz.",
"new": "Dla wielu osób konto to dodatkowe hasło i zgody, a chcą tylko kupić jedną rzecz. W badaniu Baymard ten powód wskazało 18% osób, które porzuciły zamówienie.",
"id": "PK-4"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "**Co zrobić:** usuń pola, których nie potrzebujesz do realizacji zamówienia. Dane do faktury pokaż tylko wtedy, gdy klient zaznaczy, że jej chce.",
"new": "**Co zrobić:** usuń pola, których nie potrzebujesz do realizacji zamówienia. Dane do faktury pokaż tylko wtedy, gdy klient zaznaczy, że jej chce. Punkt odniesienia: według [Baymard](https://baymard.com/blog/checkout-flow-average-form-fields) przeciętny checkout w 2024 roku miał 11,3 pola formularza, a większości sklepów wystarczy 8.",
"id": "PK-5"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Klient, który płaci BLIK-iem, nie będzie szukał karty. Jeśli nie widzi znanej metody, często odchodzi.",
"new": "Klient, który płaci BLIK-iem, nie będzie szukał karty. Według raportu Gemius „E-commerce w Polsce 2026” z BLIK-a korzystało 67% kupujących online, a dla 53% to najczęściej używana metoda płatności. Jeśli klient nie widzi znanej metody, często odchodzi.",
"id": "PK-6"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Nieznany sklep, brak opinii albo danych firmy budzą obawę, czy zamówienie dotrze.",
"new": "Nieznany sklep, brak opinii albo danych firmy budzą obawę, czy zamówienie dotrze. W badaniu Baymard 19% osób zrezygnowało, bo nie ufało stronie na tyle, by podać dane karty.",
"id": "PK-7"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "1. W Google Analytics sprawdź, na którym kroku zamówienia odpada najwięcej osób.",
"new": "1. W Google Analytics 4 sprawdź, na którym kroku zamówienia odpada najwięcej osób.",
"id": "PK-9"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "1. Porównaj swoją ścieżkę zakupu z listą 8 przyczyn powyżej.",
"new": "1. Porównaj swoją ścieżkę zakupu z listą 8 przyczyn powyżej.`,`1. Przejdź [checklistę audytu UX sklepu](/checklista-audytu-ux): 25 punktów od strony głównej po płatność, w tym 9 o koszyku, dostawie i płatności.",
"id": "PK-10"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Jeśli wolisz, żeby zrobił to ktoś z zewnątrz, [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje całą ścieżkę zakupu. Otrzymasz listę poprawek ułożoną od najważniejszych. Więcej o samym audycie przeczytasz w poradniku [Audyt UX: co to jest, jak wygląda i ile kosztuje](/audyt-ux).",
"new": "Jeśli wolisz, żeby zrobił to ktoś z zewnątrz, [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje całą ścieżkę zakupu. Otrzymasz raport w PDF z poprawkami ułożonymi od najważniejszych, w 5 dni roboczych od zaksięgowania płatności. Audyt kosztuje 2990 zł netto. Tak wygląda uwaga o koszcie dostawy w [przykładowym raporcie](/przykladowy-raport), a więcej o samym audycie przeczytasz w poradniku [Audyt UX: co to jest, jak wygląda i ile kosztuje](/audyt-ux).",
"id": "PK-11"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Źródło danych o porzucanych koszykach: [Baymard Institute](https://baymard.com/lists/cart-abandonment-rate).",
"new": "Źródła danych: [Baymard Institute, porzucone koszyki](https://baymard.com/lists/cart-abandonment-rate) (aktualizacja z września 2025), [Baymard Institute, liczba pól w checkoucie](https://baymard.com/blog/checkout-flow-average-form-fields) (2024), raport Gemius „E-commerce w Polsce 2026” w [omówieniu ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/).",
"id": "PK-12"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Przeciętnie ok. 70%, według zestawień Baymard Institute. Zamiast porównywać się ze średnią, sprawdź, na którym kroku Twoi klienci odpadają najczęściej.",
"new": "Przeciętnie ok. 70% (70,22% według zestawienia 50 badań Baymard Institute, aktualizacja z września 2025). Zamiast porównywać się ze średnią, sprawdź, na którym kroku Twoi klienci odpadają najczęściej.",
"id": "PK-13"
},
{
"op": "grep",
"key": "porzucone-koszyki",
"old": "Nie wiesz, która z przyczyn dotyczy Twojego sklepu? Sprawdzę to w bezpłatnej wstępnej ocenie.",
"new": "Nie wiesz, która z przyczyn dotyczy Twojego sklepu? Sprawdzę to w bezpłatnej wstępnej ocenie albo w pełnym audycie sklepu za 2990 zł netto.",
"id": "PK-15"
},
{
"op": "grep",
"key": "niska-konwersja-sklepu",
"old": "Ruch jest, a zamówień mało? To najczęstszy powód, dla którego właściciele sklepów zamawiają u mnie audyt. W tym poradniku pokazuję, jak krok po kroku znaleźć miejsca, w których klienci rezygnują, i które przyczyny sprawdzić w pierwszej kolejności.",
"new": "Niska konwersja to sytuacja, w której ruch w sklepie jest, a zamówień mało. Przyczyną są zwykle przeszkody na ścieżce zakupu: koszt dostawy pokazany za późno, wymuszone konto, słaba karta produktu albo sklep wygodny tylko na komputerze. Najpierw sprawdź w danych, na którym kroku klienci odpadają, a potem przejdź ten krok jak klient.",
"id": "NK-1"
},
{
"op": "grep",
"key": "niska-konwersja-sklepu",
"old": "## Czym jest konwersja i dlaczego nie ma jednej dobrej liczby",
"new": "## Czym jest współczynnik konwersji i dlaczego nie ma jednej dobrej liczby",
"id": "NK-2"
},
{
"op": "grep",
"key": "niska-konwersja-sklepu",
"old": "Porównaj te kroki osobno dla telefonów i komputerów. Bardzo często wersja desktopowa działa poprawnie, a cały problem siedzi w wersji mobilnej.",
"new": "Porównaj te kroki osobno dla telefonów i komputerów. Bardzo często wersja na komputer działa poprawnie, a cały problem siedzi w wersji mobilnej. To ważne, bo według raportu Gemius „E-commerce w Polsce 2026” zakupy na smartfonie finalizuje 58% badanych ([ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/)).",
"id": "NK-3"
},
{
"op": "grep",
"key": "niska-konwersja-sklepu",
"old": "Poniżej przyczyny, które widzę w audytach najczęściej. Ułożyłem je od tych, które zwykle kosztują sklep najwięcej zamówień.",
"new": "Poniżej najczęstsze przyczyny opisywane w badaniach użyteczności e-commerce. Ułożyłem je od tych, które dotyczą klientów najbliżej płatności, bo ci już chcieli kupić.",
"id": "NK-4"
},
{
"op": "grep",
"key": "niska-konwersja-sklepu",
"old": "- Wejdź z Google na produkt, a nie na stronę główną. Tak trafia większość klientów.",
"new": "- Wejdź z Google na produkt, a nie na stronę główną. Tak trafia wielu klientów.",
"id": "NK-5"
},
{
"op": "grep",
"key": "niska-konwersja-sklepu",
"old": "Jeśli dane pokazują problem, ale nie wiesz, co go powoduje, albo poprawki nie przynoszą efektu, [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) pozwoli zobaczyć sklep oczami klienta. Raport otrzymasz w 5 dni roboczych, z poprawkami ułożonymi od najważniejszych. Jeśli chcesz, poprawki zaprojektuję i wdrożę w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek).",
"new": "Jeśli dane pokazują problem, ale nie wiesz, co go powoduje, albo poprawki nie przynoszą efektu, [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) pozwoli zobaczyć sklep oczami klienta. Kosztuje 2990 zł netto, a raport w PDF z poprawkami ułożonymi od najważniejszych otrzymasz w 5 dni roboczych od zaksięgowania płatności. Jeśli chcesz, poprawki zaprojektuję i wdrożę w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek). Nie wiesz, czy audyt ma u Ciebie sens? Zacznij od [bezpłatnej wstępnej oceny](/darmowy-audyt-sklepu).",
"id": "NK-6"
},
{
"op": "grep",
"key": "niska-konwersja-sklepu",
"old": "Sprawdzę, gdzie Twój sklep gubi klientów. Zacznij od bezpłatnej wstępnej oceny.",
"new": "Sprawdzę, gdzie Twój sklep gubi klientów. Zacznij od bezpłatnej wstępnej oceny albo zamów pełny audyt sklepu za 2990 zł netto.",
"id": "NK-9"
},
{
"op": "grep",
"key": "karta-produktu-checklista",
"old": "Na karcie produktu klient podejmuje decyzję o zakupie. Jeśli czegoś na niej brakuje, nie napisze do Ciebie z pytaniem, tylko wróci do Google i kupi u konkurencji. Oto lista, od której zaczynam sprawdzanie każdej karty produktu w audycie.",
"new": "Karta produktu powinna odpowiedzieć na pytania klienta, zanim zacznie ich szukać gdzie indziej: co to jest, ile kosztuje razem z dostawą, kiedy dotrze, który wariant wybrać i czy można to zwrócić. Najważniejsze są zdjęcia, cena z kosztem dostawy, dostępność, czytelne warianty i opinie blisko przycisku zakupu. Poniżej lista 20 punktów, od której zaczynam sprawdzanie każdej karty produktu w audycie.",
"id": "KP-1"
},
{
"op": "grep",
"key": "karta-produktu-checklista",
"old": "Karta produktu ma odpowiedzieć na wszystkie pytania klienta, zanim ten zacznie ich szukać gdzie indziej.",
"new": "Jeśli na karcie produktu czegoś brakuje, klient rzadko pisze z pytaniem. Częściej wraca do wyników wyszukiwania.",
"id": "KP-2"
},
{
"op": "grep",
"key": "karta-produktu-checklista",
"old": "1. **Dostępność i czas wysyłki są przy cenie.** „Wysyłka jutro” działa lepiej niż „dostępny”.",
"new": "1. **Dostępność i czas wysyłki są przy cenie.** „Wysyłka jutro” mówi klientowi więcej niż „dostępny”.",
"id": "KP-3"
},
{
"op": "grep",
"key": "karta-produktu-checklista",
"old": "## Zdjęcia i wideo",
"new": "## Zdjęcia",
"id": "KP-4"
},
{
"op": "gins",
"key": "karta-produktu-checklista",
"after": "1. **Odpowiedzi na typowe pytania**, które klienci zadają Ci mailem lub telefonicznie.",
"lines": [
"## Opis produktu: jak go ułożyć, żeby klient doczytał",
"Klient rzadko czyta opis od góry do dołu. Przewija i szuka odpowiedzi na swoje pytanie, np. o wymiary, skład albo sposób użycia.",
"Dlatego ułóż opis w trzech warstwach: na górze 3–5 najważniejszych korzyści w punktach, niżej krótki akapit o tym, dla kogo jest produkt i jak go używać, na końcu tabela parametrów. Śródtytuły pomagają przeskoczyć do tego, czego klient szuka.",
"Opis skopiowany od producenta klient mógł już widzieć w innych sklepach. Dopisz to, co wyróżnia Twoją ofertę, np. szybszą wysyłkę, doradztwo albo zestaw w lepszej cenie."
],
"id": "KP-5"
},
{
"op": "gins",
"key": "karta-produktu-checklista",
"after": "1. **Przycisk zakupu jest zawsze pod ręką**, np. przyklejony na dole ekranu po przewinięciu.",
"lines": [
"Pozostałe punkty sprawdź na telefonie jeszcze raz, bo tam najłatwiej je przeoczyć. Co jeszcze przeszkadza w zakupie na małym ekranie, opisuję w poradniku [UX sklepu na telefonie](/ux-sklepu-mobilnego)."
],
"id": "KP-6"
},
{
"op": "grep",
"key": "karta-produktu-checklista",
"old": "W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) sprawdzam karty produktu z najważniejszych kategorii, na desktopie oraz urządzeniach mobilnych. Każda uwaga ma zrzut ekranu i konkretną poprawkę. Raport otrzymasz w 5 dni roboczych.",
"new": "W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) sprawdzam karty produktu z najważniejszych kategorii, na komputerze i na telefonie. Każda uwaga ma zrzut ekranu i konkretną poprawkę. Audyt kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności.",
"id": "KP-7"
},
{
"op": "grep",
"key": "karta-produktu-checklista",
"old": "Sprawdzę karty produktu w Twoim sklepie. Zacznij od bezpłatnej wstępnej oceny.",
"new": "Sprawdzę karty produktu w Twoim sklepie. Zacznij od bezpłatnej wstępnej oceny albo zamów audyt sklepu za 2990 zł netto.",
"id": "KP-9"
},
{
"op": "grep",
"key": "ux-sklepu-mobilnego",
"old": "Wersja mobilna to dziś główne wejście do większości sklepów, a jednocześnie miejsce, w którym w audytach znajduję najwięcej problemów. Poniżej przeszkody, które widzę najczęściej, i sposoby, jak je usunąć.",
"new": "Na telefonie zakup psują zwykle okna zasłaniające treść, za małe przyciski, rozbudowane menu, niewygodne filtry, przycisk zakupu znikający po przewinięciu, długi formularz i wolne ładowanie. Warto to sprawdzić, bo według raportu Gemius „E-commerce w Polsce 2026” zakupy na smartfonie finalizuje 58% badanych. Poniżej siedem przeszkód i sposób na każdą.",
"id": "MOB-1"
},
{
"op": "grep",
"key": "ux-sklepu-mobilnego",
"old": "Większość klientów sklepów ogląda je na telefonie, a sklepy wciąż projektuje się i testuje głównie na komputerze.",
"new": "Według Gemius 2026 zakupy na smartfonie finalizuje 58% badanych, a sklepy wciąż często projektuje się i testuje na komputerze.",
"id": "MOB-2"
},
{
"op": "grep",
"key": "ux-sklepu-mobilnego",
"old": "Najwięcej zamówień ucieka przez okna zasłaniające treść, małe przyciski, długie formularze i wolne ładowanie.",
"new": "Zakup na telefonie najczęściej utrudniają okna zasłaniające treść, małe przyciski, długie formularze i wolne ładowanie.",
"id": "MOB-3"
},
{
"op": "grep",
"key": "ux-sklepu-mobilnego",
"old": "**Co poprawić:** przyklej przycisk dodania do koszyka na dole ekranu i sprawdź galerię gestami. Więcej punktów znajdziesz w [checkliście karty produktu](/karta-produktu-checklista).",
"new": "**Co poprawić:** przyklej przycisk dodania do koszyka na dole ekranu i sprawdź galerię gestami. Jak opisuję taki problem w raporcie, zobaczysz w [przykładowym raporcie](/przykladowy-raport). Więcej punktów znajdziesz w [checkliście karty produktu](/karta-produktu-checklista).",
"id": "MOB-4"
},
{
"op": "grep",
"key": "ux-sklepu-mobilnego",
"old": "**Co poprawić:** zmniejsz zdjęcia, ogranicz skrypty zewnętrzne i sprawdź wynik w PageSpeed Insights dla wersji mobilnej. Najważniejsze, żeby szybko ładowały się karta produktu i koszyk.",
"new": "**Co poprawić:** zmniejsz zdjęcia, ogranicz skrypty zewnętrzne i sprawdź wynik w [PageSpeed Insights](https://pagespeed.web.dev/) dla wersji mobilnej. Najważniejsze, żeby szybko ładowały się karta produktu i koszyk.",
"id": "MOB-5"
},
{
"op": "grep",
"key": "ux-sklepu-mobilnego",
"old": "W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) każdą ścieżkę sprawdzam osobno na telefonie i na komputerze. Raport otrzymasz w 5 dni roboczych.",
"new": "W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) każdą ścieżkę sprawdzam osobno na telefonie i na komputerze. Audyt kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Najczęstsze przyczyny rezygnacji w koszyku opisuję w poradniku [Porzucone koszyki](/porzucone-koszyki), a listę 25 punktów do sprawdzenia na telefonie znajdziesz w [checkliście audytu UX sklepu](/checklista-audytu-ux).",
"id": "MOB-6"
},
{
"op": "grep",
"key": "ux-sklepu-mobilnego",
"old": "Sprawdzę, jak Twój sklep działa na telefonie. Zacznij od bezpłatnej wstępnej oceny.",
"new": "Sprawdzę, jak Twój sklep działa na telefonie. Zacznij od bezpłatnej wstępnej oceny albo zamów audyt sklepu za 2990 zł netto.",
"id": "MOB-8"
},
{
"op": "grep",
"key": "jak-sprawdzic-ux-sklepu",
"old": "Nie każdy sklep od razu potrzebuje pełnego audytu. Wiele problemów znajdziesz sam, jeśli przejdziesz zakup tak, jak robi to Twój klient. Poniżej scenariusz, który zajmuje około 30 minut i nie wymaga żadnych płatnych narzędzi.",
"new": "UX sklepu sprawdzisz sam w około 30 minut: weź telefon, wyłącz Wi-Fi, wejdź z Google prosto na produkt i przejdź zakup aż do wyboru płatności, zapisując każdy moment zawahania. Ten scenariusz nie wymaga płatnych narzędzi i pokaże najbardziej widoczne problemy. Poniżej rozpisuję go na pięć etapów, z czasem na każdy.",
"id": "JS-1"
},
{
"op": "grep",
"key": "jak-sprawdzic-ux-sklepu",
"old": "Zapisuj każdy moment zawahania. To lista miejsc do poprawy, ułożona przez samo zachowanie klienta.",
"new": "Zapisuj każdy moment zawahania. Twoje notatki to gotowa lista poprawek.",
"id": "JS-2"
},
{
"op": "grep",
"key": "jak-sprawdzic-ux-sklepu",
"old": "Wpisz w Google nazwę produktu i wejdź do sklepu z wyników, a nie przez stronę główną. Tak trafia większość klientów.",
"new": "Wpisz w Google nazwę produktu i wejdź do sklepu z wyników, a nie przez stronę główną. Tak trafia wielu klientów.",
"id": "JS-3"
},
{
"op": "gins",
"key": "jak-sprawdzic-ux-sklepu",
"after": "Ułóż zapisane problemy według tego, jak blisko płatności się pojawiły. Problem w koszyku zwykle kosztuje więcej zamówień niż problem na stronie głównej, bo dotyczy klientów, którzy już chcieli kupić.",
"lines": [
"Tak wygląda podobna lista w wersji z audytu, z priorytetami i poprawkami: [przykładowy raport z audytu UX](/przykladowy-raport)."
],
"id": "JS-4"
},
{
"op": "gins",
"key": "jak-sprawdzic-ux-sklepu",
"after": "Potem porównaj notatki z danymi z Google Analytics 4 lub Microsoft Clarity. Jeśli krok, w którym Ty miałeś najwięcej wątpliwości, to także ten, na którym odpada najwięcej klientów, wiesz, od czego zacząć. Więcej o czytaniu danych piszę w poradniku [Niska konwersja w sklepie](/niska-konwersja-sklepu).",
"lines": [
"## Lista do odhaczenia",
"Jeśli wolisz pracować z listą, przejdź [checklistę audytu UX sklepu](/checklista-audytu-ux). To 25 pytań od strony głównej po płatność, w tej samej kolejności co ten scenariusz. Przy każdym zapisujesz „tak” albo „nie”."
],
"id": "JS-5"
},
{
"op": "grep",
"key": "jak-sprawdzic-ux-sklepu",
"old": "Jeśli po takim przejściu wciąż nie wiesz, dlaczego klienci nie kupują, albo chcesz mieć pewność, że niczego nie pominąłeś, [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) da Ci pełną listę poprawek ze zrzutami ekranu, ułożoną od najważniejszych. Raport otrzymasz w 5 dni roboczych. Możesz też zacząć od bezpłatnej wstępnej oceny.",
"new": "Jeśli po takim przejściu wciąż nie wiesz, dlaczego klienci nie kupują, albo chcesz mieć pewność, że niczego nie pominąłeś, [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) da Ci pełną listę poprawek ze zrzutami ekranu, ułożoną od najważniejszych. Kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Możesz też zacząć od [bezpłatnej wstępnej oceny](/darmowy-audyt-sklepu).",
"id": "JS-6"
},
{
"op": "grep",
"key": "jak-sprawdzic-ux-sklepu",
"old": "Wolisz, żebym sprawdził sklep za Ciebie? Zacznij od bezpłatnej wstępnej oceny.",
"new": "Wolisz, żebym sprawdził sklep za Ciebie? Zacznij od bezpłatnej wstępnej oceny albo zamów audyt sklepu za 2990 zł netto.",
"id": "JS-7"
},
{
"op": "gins",
"key": "audyt-ux-a-audyt-seo",
"after": "::report",
"lines": [
"## Co z „audytem strony internetowej”?",
"Wiele ofert „audytu strony internetowej” to w praktyce audyty SEO: sprawdzają frazy, indeksowanie, linki i błędy techniczne. Jeśli Twój problem to mało zapytań przy przyzwoitym ruchu, szukaj audytu UX strony. Sprawdza on ofertę, nawigację, przyciski kontaktu i formularz.",
"W uxaudyt.pl [audyt UX strony internetowej](/audyt-strony-internetowej) kosztuje 1990 zł netto i obejmuje strony firmowe do ok. 20 podstron."
],
"id": "SEO-5"
},
{
"op": "gins",
"key": "audyt-ux-a-audyt-seo",
"after": "Ceny audytów SEO zależą od agencji i wielkości sklepu. Audyt UX w uxaudyt.pl ma stałą cenę: 1990 zł netto za [stronę internetową](/audyt-strony-internetowej) i 2990 zł netto za [sklep internetowy](/audyt-sklepu-internetowego). Raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Szczegóły znajdziesz w poradniku [Audyt UX: co to jest, jak wygląda i ile kosztuje](/audyt-ux), a jeśli nie wiesz, od którego audytu zacząć, poproś o [bezpłatną wstępną ocenę](/darmowy-audyt-sklepu).",
"lines": [
"O tym, dlaczego warto poprawić sklep, zanim dołożysz budżet na ruch, piszę w poradniku [Jak zwiększyć sprzedaż w sklepie internetowym](/jak-zwiekszyc-sprzedaz-sklepu)."
],
"id": "SEO-7"
},
{
"op": "gfaq",
"key": "audyt-ux-a-audyt-seo",
"pos": 0,
"q": "Czy dobra pozycja w Google wystarczy, żeby sklep sprzedawał?",
"a": "Nie. Pozycja w Google przyprowadza ludzi do sklepu, ale o zakupie decyduje to, co zobaczą po wejściu: karta produktu, koszt dostawy, formularz zamówienia. Jeśli tam są przeszkody, nowi klienci z Google trafią na te same problemy co obecni.",
"id": "SEO-9"
},
{
"op": "gins",
"key": "audyt-ux-prestashop",
"after": "Najczęstsze powody, dla których klienci nie kończą zakupu, opisuję też w poradniku [Porzucone koszyki](/porzucone-koszyki).",
"lines": [
"Sklepy na PrestaShop projektujemy i wdrażamy też w studiu [Creative Vision](https://creative-vision.pl). Jeśli wolisz najpierw sprawdzić sklep sam, przejdź [checklistę audytu UX sklepu](/checklista-audytu-ux)."
],
"id": "PS-6"
},
{
"op": "gins",
"key": "audyt-ux-shopify",
"after": "::report",
"lines": [
"## Porzucone koszyki na Shopify",
"Jeśli klienci dochodzą do checkoutu i rezygnują, sprawdź najpierw, czy koszt dostawy był widoczny wcześniej: na karcie produktu i w koszyku. W badaniu [Baymard Institute](https://baymard.com/lists/cart-abandonment-rate) zbyt wysokie dodatkowe koszty to najczęstszy powód porzucenia zamówienia (40% kupujących w USA, którzy zrezygnowali z innego powodu niż „tylko oglądam”). Pozostałe przyczyny opisuję w poradniku [Porzucone koszyki](/porzucone-koszyki)."
],
"id": "SH-6"
},
{
"op": "gins",
"key": "audyt-ux-woocommerce",
"after": "**Co poprawić:** ukryj albo oznacz jako opcjonalne pola firmy, drugiej linii adresu i telefonu. W checkoucie blokowym, domyślnym w nowych sklepach z motywem blokowym od WooCommerce 8.3, zrobisz to w edytorze strony zamówienia: zaznacz blok pól zamówienia i w ustawieniach pól adresu wybierz dla każdego z nich „ukryte”, „opcjonalne” albo „wymagane”. W starszym checkoucie opartym na shortcode te same opcje są w Wygląd → Dostosuj → WooCommerce → Zamówienie. Pole NIP i dane do faktury pokaż dopiero wtedy, gdy klient zaznaczy, że potrzebuje faktury.",
"lines": [
"Jak sprawdzić, który checkout masz? Otwórz stronę zamówienia w edytorze WordPressa. Jeśli widzisz bloki zamówienia (pola, dostawa, płatność), masz checkout blokowy. Jeśli w treści jest tylko shortcode woocommerce_checkout, masz starszą wersję. Źródła: [blok Checkout](https://woocommerce.com/document/woocommerce-store-editing/customizing-cart-and-checkout/checkout-block/), [ustawienia checkoutu w Customizerze](https://woocommerce.com/document/woocommerce-customizer/checkout/) i [WooCommerce 8.3](https://developer.woocommerce.com/2023/11/16/woocommerce-8-3-0-released/)."
],
"id": "WOO-4"
},
{
"op": "gins",
"key": "audyt-ux-woocommerce",
"after": "::report",
"lines": [
"## Porzucone koszyki na WooCommerce",
"W sklepach na WooCommerce koszyk często porzucają klienci, którzy dopiero w formularzu poznają koszt dostawy albo trafiają na pola i zgody dodane przez kolejne wtyczki. Zacznij od kroków 1–3 z tej listy, a pozostałe przyczyny znajdziesz w poradniku [Porzucone koszyki](/porzucone-koszyki).",
"Sklep na WordPressie ma często także część firmową: ofertę, blog, stronę kontaktu. Jeśli to ona ma zbierać zapytania, sprawdzi ją [audyt UX strony internetowej](/audyt-strony-internetowej)."
],
"id": "WOO-10"
},
{
"op": "gins",
"key": "porzucone-koszyki",
"after": "::report",
"lines": [
"## Zapobieganie czy odzyskiwanie porzuconych koszyków?",
"Maile przypominające o koszyku i rabaty na powrót pomagają odzyskać część zamówień. Działają jednak dopiero wtedy, gdy klient już odszedł, i nie usuwają przyczyny, przez którą odszedł.",
"Dlatego kolejność ma znaczenie: najpierw usuń przeszkody z listy powyżej, potem ustaw przypomnienia.",
"## Porzucone koszyki na PrestaShop, WooCommerce, Shopify i Shoperze",
"Przyczyny są te same na każdej platformie, różni się miejsce, w którym je poprawisz. Konkretne ustawienia, np. zakup bez konta czy pola formularza, opisuję w poradnikach o [PrestaShop](/audyt-ux-prestashop), [WooCommerce](/audyt-ux-woocommerce), [Shopify](/audyt-ux-shopify) i [Shoperze](/audyt-ux-shoper)."
],
"id": "PK-8"
},
{
"op": "gfaq",
"key": "porzucone-koszyki",
"pos": 1,
"q": "Jak sprawdzić, na którym kroku klienci porzucają koszyk?",
"a": "W Google Analytics 4 zbuduj lejek z kroków: dodanie do koszyka, rozpoczęcie zamówienia, wybór dostawy, płatność i zakup. Krok z największym spadkiem to pierwsze miejsce do sprawdzenia. Nagrania sesji w Microsoft Clarity pokażą, co klienci robili tuż przed wyjściem.",
"id": "PK-14"
},
{
"op": "gins",
"key": "niska-konwersja-sklepu",
"after": "Jeśli dane pokazują problem, ale nie wiesz, co go powoduje, albo poprawki nie przynoszą efektu, [audyt UX sklepu internetowego](/audyt-sklepu-internetowego) pozwoli zobaczyć sklep oczami klienta. Kosztuje 2990 zł netto, a raport w PDF z poprawkami ułożonymi od najważniejszych otrzymasz w 5 dni roboczych od zaksięgowania płatności. Jeśli chcesz, poprawki zaprojektuję i wdrożę w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek). Nie wiesz, czy audyt ma u Ciebie sens? Zacznij od [bezpłatnej wstępnej oceny](/darmowy-audyt-sklepu).",
"lines": [
"Dlaczego warto poprawić sklep, zanim dołożysz budżet na reklamy, wyjaśniam w poradniku [Jak zwiększyć sprzedaż w sklepie internetowym](/jak-zwiekszyc-sprzedaz-sklepu). Listę 25 punktów do samodzielnego sprawdzenia znajdziesz w [checkliście audytu UX sklepu](/checklista-audytu-ux)."
],
"id": "NK-7"
},
{
"op": "gfaq",
"key": "niska-konwersja-sklepu",
"pos": 0,
"q": "Dlaczego sklep internetowy nie sprzedaje, mimo że ma ruch?",
"a": "Najczęściej dlatego, że klienci trafiają na przeszkody między wejściem a płatnością: nie znajdują produktu, nie wiedzą, ile zapłacą za dostawę, muszą zakładać konto albo zniechęca ich formularz. Rzadziej problemem jest sam ruch, np. reklamy przyprowadzają osoby, które nie szukają Twojego produktu. Sprawdź w danych, na którym kroku odpadają klienci, i zacznij od tego miejsca.",
"id": "NK-8"
},
{
"op": "gins",
"key": "karta-produktu-checklista",
"after": "W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) sprawdzam karty produktu z najważniejszych kategorii, na komputerze i na telefonie. Każda uwaga ma zrzut ekranu i konkretną poprawkę. Audyt kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności.",
"lines": [
"Jak wygląda taka uwaga w raporcie, zobaczysz w [przykładowym raporcie](/przykladowy-raport). Karta produktu to tylko jeden etap zakupu: całą ścieżkę, od strony głównej po płatność, obejmuje [checklista audytu UX sklepu](/checklista-audytu-ux). O projektowaniu karty produktu od strony UX piszemy też na blogu [Creative Vision](https://creative-vision.pl/wiedza/ux-karty-produktu)."
],
"id": "KP-8"
},
{
"op": "gins",
"key": "ux-sklepu-mobilnego",
"after": "W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) każdą ścieżkę sprawdzam osobno na telefonie i na komputerze. Audyt kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Najczęstsze przyczyny rezygnacji w koszyku opisuję w poradniku [Porzucone koszyki](/porzucone-koszyki), a listę 25 punktów do sprawdzenia na telefonie znajdziesz w [checkliście audytu UX sklepu](/checklista-audytu-ux).",
"lines": [
"Źródło danych o zakupach na smartfonie: raport Gemius „E-commerce w Polsce 2026” w [omówieniu ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/)."
],
"id": "MOB-7"
},
{
"op": "gfaq",
"key": "audyt-ux",
"pos": "end",
"q": "Co otrzymam po audycie UX?",
"a": "Raport w PDF z listą problemów ułożoną od najważniejszych. Przy każdym problemie jest zrzut ekranu, wyjaśnienie, dlaczego przeszkadza klientom, i konkretna poprawka do przekazania developerowi. W audycie sklepu i strony omawiamy raport na rozmowie, a w pakiecie z opieką na warsztacie online.",
"id": "AUX-17"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Audyt UX`,date:`2026-10-11`",
"new": "crumb:`Audyt UX`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Audyt UX a audyt SEO`,date:`2026-10-11`",
"new": "crumb:`Audyt UX a audyt SEO`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Audyt UX sklepu na PrestaShop`,date:`2026-10-11`",
"new": "crumb:`Audyt UX sklepu na PrestaShop`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Audyt UX sklepu na Shopify`,date:`2026-10-19`",
"new": "crumb:`Audyt UX sklepu na Shopify`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Audyt UX sklepu na WooCommerce`,date:`2026-10-19`",
"new": "crumb:`Audyt UX sklepu na WooCommerce`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Jak sprawdzić UX sklepu`,date:`2026-10-19`",
"new": "crumb:`Jak sprawdzić UX sklepu`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Karta produktu: checklista`,date:`2026-10-19`",
"new": "crumb:`Karta produktu: checklista`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Niska konwersja sklepu`,date:`2026-10-19`",
"new": "crumb:`Niska konwersja sklepu`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`Porzucone koszyki`,date:`2026-10-11`",
"new": "crumb:`Porzucone koszyki`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "crumb:`UX sklepu na telefonie`,date:`2026-10-19`",
"new": "crumb:`UX sklepu na telefonie`,date:`2026-11-03`",
"count": 1,
"id": "T8"
},
{
"op": "gins",
"key": "darmowy-audyt-sklepu",
"after": "Jeśli chcesz najpierw poszukać problemów sam, skorzystaj z poradnika [Jak samodzielnie sprawdzić UX sklepu w 30 minut](/jak-sprawdzic-ux-sklepu).",
"lines": [
"## Co dalej, jeśli ocena wskaże problemy",
"Nic nie musisz kupować. Jeśli zdecydujesz się na audyt, wybierasz jeden z trzech pakietów o stałej cenie:",
"- [Audyt strony internetowej](/audyt-strony-internetowej): 1990 zł netto, strona firmowa do ok. 20 podstron.",
"- [Audyt sklepu internetowego](/audyt-sklepu-internetowego): 2990 zł netto, cała ścieżka zakupu na komputerze i telefonie.",
"- [Audyt sklepu z opieką](/audyt-sklepu-z-opieka): 4490 zł netto, do tego warsztat, makiety wszystkich krytycznych poprawek i 30 dni wsparcia.",
"Raport w każdym pakiecie otrzymasz w 5 dni roboczych od zaksięgowania płatności."
],
"id": "10.3A"
},
{
"op": "gfaq",
"key": "darmowy-audyt-sklepu",
"pos": "end",
"q": "Co się stanie po ocenie?",
"a": "Otrzymasz odpowiedź e-mailem. Jeśli uznam, że pełny audyt nie ma sensu, napiszę to wprost. Jeśli ma, podpowiem, który pakiet pasuje. Decyzja należy do Ciebie.",
"id": "10.3B"
},
{
"op": "newguides",
"objs": [
"\\"jak-zwiekszyc-sprzedaz-sklepu\\":{tldr:[`Sprzedaż to ruch razy konwersja razy wartość zamówienia. Poprawka w sklepie działa na cały ruch, za który już płacisz.`,`Najwięcej klientów odpada blisko płatności: przez wysokie koszty dostawy, wymóg konta i długi formularz.`,`Zacznij od kroku, na którym w Twoich danych odpada najwięcej osób, i zmieniaj jedną rzecz naraz.`],path:`/jak-zwiekszyc-sprzedaz-sklepu`,crumb:`Jak zwiększyć sprzedaż sklepu`,date:`2026-11-03`,title:`Jak zwiększyć sprzedaż w sklepie internetowym: najpierw sklep, potem ruch`,lead:`Sprzedaż w sklepie internetowym zwiększysz na trzy sposoby: większym ruchem, wyższą konwersją albo wyższą wartością zamówienia. Zanim dołożysz budżet na reklamy, popraw sklep: jeśli klienci odpadają na karcie produktu, w koszyku albo w formularzu zamówienia, nowe osoby z reklam trafią na te same przeszkody. Poniżej 12 poprawek, od których warto zacząć, i sposób, żeby sprawdzić, czy działają.`,body:[`## Dlaczego więcej ruchu nie zawsze daje więcej zamówień`,`Przychód sklepu to iloczyn trzech liczb: liczby wejść, konwersji (odsetka wejść, które kończą się zamówieniem) i średniej wartości zamówienia. Większość porad o zwiększaniu sprzedaży dotyczy pierwszej liczby: reklam, SEO, mediów społecznościowych. To ma sens, jeśli sklep dobrze obsługuje ruch, który już ma.`,`Prosty przykład do policzenia na własnych danych: sklep ma 10 000 wejść miesięcznie, konwersję 1% i średnie zamówienie 150 zł, czyli 15 000 zł przychodu. Żeby przy tej samej konwersji uzyskać 3000 zł przychodu więcej, potrzebuje 2000 dodatkowych wejść, za które zwykle płaci co miesiąc. Ten sam przychód da wzrost konwersji z 1% do 1,2% przy obecnym ruchu. Poprawka w sklepie działa potem na każde kolejne wejście, także z przyszłych kampanii.`,`To tylko przykładowe wyliczenie. Nie każdy sklep ma zapas w konwersji i nie każda poprawka zadziała. Warto jednak wiedzieć, gdzie są przeszkody, zanim zwiększysz budżet na ruch.`,`Przeszkód zwykle nie brakuje. Według zestawienia 50 badań [Baymard Institute](https://baymard.com/lists/cart-abandonment-rate) przeciętnie ok. 70% koszyków w sklepach internetowych zostaje porzuconych. Część tych osób tylko oglądała, ale wiele odpada przez rzeczy, które da się poprawić.`,`## Sprawdź, gdzie tracisz klientów`,`Zanim zaczniesz zmieniać sklep, zobacz w Google Analytics 4 albo w darmowym Microsoft Clarity, jak wygląda Twój lejek zakupowy. Porównaj kroki osobno dla telefonów i komputerów.`,`| | Co sprawdzić w danych | Gdzie szukać przyczyny`,`| Mało wejść na produkty | Ile osób z wejść ogląda karty produktów | Strona główna, menu, wyszukiwarka, filtry`,`| Mało dodań do koszyka | Ile osób z oglądających produkt dodaje go do koszyka | Karta produktu: cena, dostawa, warianty, zdjęcia, opinie`,`| Dużo porzuconych koszyków | Ile osób z koszyka kończy płatność | Koszt dostawy, konto, formularz, płatności`,`Krok z największym spadkiem to pierwsze miejsce do poprawy. Jak czytać te dane, opisuję szerzej w poradniku [Niska konwersja sklepu](/niska-konwersja-sklepu).`,`## Karta produktu: poprawki 1–4`,`- **1. Pokaż koszt i czas dostawy przy cenie.** W badaniu Baymard Institute zbyt wysokie dodatkowe koszty (dostawa, podatki, opłaty) to najczęstszy powód porzucenia zamówienia: wskazało go 40% kupujących w USA, którzy zrezygnowali z innego powodu niż „tylko oglądam”. W Polsce, według raportu Gemius „E-commerce w Polsce 2026”, ponad połowa kupujących rezygnuje z zakupu, gdy koszt dostawy okazuje się zbyt wysoki. Klient powinien znać ten koszt, zanim doda produkt do koszyka.`,`- **2. Podpowiedz, ile brakuje do darmowej dostawy.** Jeśli masz próg darmowej dostawy, napisz go przy cenie i w koszyku, najlepiej z kwotą: „Brakuje 41 zł do darmowej dostawy”. Próg schowany w stopce niewiele daje.`,`- **3. Napisz konkretnie, kiedy produkt dotrze.** „Wysyłka jutro” albo „dostawa w czwartek” mówi klientowi więcej niż „dostępny”. Jeśli czas jest długi, wyjaśnij od razu dlaczego, np. „szyjemy na zamówienie, gotowe w 10 dni”.`,`- **4. Ułatw wybór wariantu.** Pokaż rozmiary i kolory jako przyciski, oznacz niedostępne i zmieniaj zdjęcie po wyborze koloru. Tabela rozmiarów powinna być obok wyboru rozmiaru. Pełną listę punktów znajdziesz w [checkliście karty produktu](/karta-produktu-checklista).`,`::example 0`,`## Wyszukiwarka i zaufanie: poprawki 5–6`,`- **5. Sprawdź wyszukiwarkę na literówkach.** Wpisz w nią nazwy 10 najpopularniejszych produktów z błędem i w innej formie, np. w liczbie mnogiej. Pusty wynik klient czyta jak „nie mamy tego produktu” i wychodzi.`,`- **6. Umieść opinie i zasady zwrotu przy przycisku zakupu.** Klient, który nie ufa sklepowi, nie dokończy zamówienia. W badaniu Baymard 19% osób zrezygnowało, bo nie ufało stronie na tyle, by podać dane karty, a 13% przez niesatysfakcjonujące zasady zwrotu. Pokaż ocenę i liczbę opinii przy nazwie produktu, a przy przycisku jedno zdanie o zwrotach, np. „14 dni na zwrot bez podania przyczyny”.`,`## Koszyk i zamówienie: poprawki 7–10`,`- **7. Pokaż w koszyku kwotę łącznie z dostawą.** Według Baymard 12% osób porzuciło zamówienie, bo nie mogło wcześniej zobaczyć ani policzyć całkowitego kosztu. Na telefonie sprawdź też, czy przycisk przejścia do zamówienia jest widoczny bez przewijania i czy nie przesuwają go polecane produkty.`,`- **8. Pozwól kupić bez zakładania konta.** Wymóg konta to według Baymard powód porzucenia dla 18% osób. Konto zaproponuj po zamówieniu, jednym kliknięciem. Jak to włączyć na popularnych platformach, opisuję w poradnikach o [PrestaShop](/audyt-ux-prestashop), [WooCommerce](/audyt-ux-woocommerce) i [Shoperze](/audyt-ux-shoper).`,`- **9. Skróć formularz zamówienia.** Baymard policzył, że przeciętny checkout w 2024 roku miał 11,3 pola formularza, a większości sklepów wystarczy 8 ([Baymard](https://baymard.com/blog/checkout-flow-average-form-fields)). Usuń pola, których nie potrzebujesz do wysyłki, a dane do faktury pokaż dopiero po zaznaczeniu, że klient jej chce. Przy telefonie i kodzie pocztowym ustaw klawiaturę numeryczną.`,`- **10. Postaw na górze płatności i dostawy, których używają Twoi klienci.** Według raportu Gemius „E-commerce w Polsce 2026” z BLIK-a korzystało 67% kupujących online, a dla 72% automat paczkowy to najczęściej wybierana forma dostawy. Jeśli klient nie widzi znanej metody, łatwo zrezygnuje.`,`## Telefon i szybkość: poprawki 11–12`,`- **11. Sprawdź sklep na prawdziwym telefonie.** Według Gemius 2026 zakupy na smartfonie finalizuje 58% badanych. Zmniejszone okno przeglądarki na komputerze nie pokaże, że baner, newsletter i czat zasłaniają naraz cały ekran. Pokazuj najwyżej jedno okno naraz i pilnuj, żeby ikona czatu nie zasłaniała przycisku zakupu. Więcej w poradniku [UX sklepu na telefonie](/ux-sklepu-mobilnego).`,`- **12. Przyspiesz kartę produktu i koszyk.** Sprawdź je w [PageSpeed Insights](https://pagespeed.web.dev/) w wersji mobilnej. Zacznij od zbyt dużych zdjęć i skryptów z wtyczek lub aplikacji, których już nie używasz. Szybkość ma znaczenie także w Google: według [Google Search Central](https://developers.google.com/search/docs/appearance/page-experience) wskaźniki Core Web Vitals są używane przez systemy rankingowe.`,`## Trzecia dźwignia: wartość zamówienia`,`Poza konwersją możesz zwiększyć średnią wartość zamówienia, także bez dodatkowego ruchu. Kilka sposobów, które nie utrudniają zakupu:`,`- **Próg darmowej dostawy nieco powyżej średniego koszyka.** Jeśli przeciętne zamówienie to 150 zł, próg 180 zł może zachęcić do dobrania drobnego produktu. Kwota, której brakuje, musi być jednak widoczna w koszyku.`,`- **Produkty uzupełniające na karcie produktu.** Etui do telefonu, wkłady do długopisu, środek do pielęgnacji butów. Wystarczą jedna albo dwie trafne propozycje. Długa karuzela produktów odciąga uwagę od przycisku zakupu.`,`- **Większe opakowanie albo zestaw w lepszej cenie za sztukę.** Pokaż cenę za jednostkę, żeby klient od razu widział, ile oszczędza.`,`Uważaj tylko na koszyk. Polecane produkty, które przesuwają przycisk zamówienia poza ekran telefonu, mogą kosztować więcej zamówień, niż przyniosą. Zmiany w wartości zamówienia mierz tak samo jak poprawki konwersji: jedną naraz.`,`## Od czego zacząć, jeśli masz mało czasu`,`Ułóż poprawki według tego, jak blisko płatności dotyczą klienta. Problem w koszyku dotyczy osób, które już chciały kupić, więc zwykle kosztuje więcej zamówień niż problem na stronie głównej. Jeśli masz jeden dzień, zrób to w tej kolejności:`,`1. Przejdź zakup na własnym telefonie, na danych mobilnych, wchodząc z Google prosto na produkt. Zapisz każdy moment zawahania. Scenariusz krok po kroku opisuję w poradniku [Jak samodzielnie sprawdzić UX sklepu](/jak-sprawdzic-ux-sklepu).`,`1. Porównaj notatki z danymi o lejku i wybierz krok z największym spadkiem.`,`1. Wdróż najpierw poprawki, które są zmianą tekstu albo ustawień: koszt dostawy przy cenie, zakup bez konta, kolejność płatności. Często nie wymagają programisty.`,`1. Resztę zapisz na liście i wróć do niej po pierwszym pomiarze.`,`Pełną listę do odhaczenia znajdziesz w [checkliście audytu UX sklepu](/checklista-audytu-ux).`,`## Jak sprawdzić, czy poprawki działają`,`Zmieniaj jedną lub dwie rzeczy naraz i porównuj ten sam krok lejka przed zmianą i po niej, osobno dla telefonów i komputerów. Przy małym ruchu porównuj dłuższe okresy, np. cztery tygodnie przed i cztery po, bo kilka zamówień w jedną albo drugą stronę to jeszcze przypadek. Uwzględnij sezon i promocje, które prowadziłeś w tym czasie.`,`Nie każda poprawka da wynik, który zobaczysz w liczbach, i to normalne. Część zmian, np. jasna informacja o zwrotach, po prostu usuwa powód do wahania.`,`## Kiedy dołożyć ruch`,`Gdy klienci przechodzą przez sklep bez większych przeszkód, dodatkowy ruch ma większą szansę zamienić się w zamówienia. Wtedy jest dobry moment na kampanie, SEO i nowe kanały. Jeśli zastanawiasz się, czy Twój sklep bardziej potrzebuje pracy nad ruchem, czy nad samym sklepem, przeczytaj porównanie [Audyt UX a audyt SEO](/audyt-ux-a-audyt-seo).`,`::report`,`## Kiedy warto zamówić audyt UX`,`Samodzielne sprawdzenie ma jedno ograniczenie: własny sklep zna się zbyt dobrze. Wiesz, gdzie kliknąć, i nie widzisz tego, co dla nowego klienta jest niejasne.`,`W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) przechodzę całą ścieżkę zakupu jak klient, na komputerze i na telefonie. Raport w PDF z problemami ułożonymi od najważniejszych, ze zrzutem ekranu i konkretną poprawką przy każdym, otrzymasz w 5 dni roboczych od zaksięgowania płatności. Potem omawiamy go na rozmowie. Audyt kosztuje 2990 zł netto. Jeśli raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w terminie z przyczyn innych niż niedostępność Twojego sklepu, zwrócę całą kwotę.`,`Nie wiesz, czy to dobry moment? Zacznij od [bezpłatnej wstępnej oceny](/darmowy-audyt-sklepu). Jeśli masz mniej niż ok. 50 zamówień miesięcznie, napiszę wprost, gdy pełny audyt może się jeszcze nie zwrócić.`,`Źródła: [Baymard Institute, porzucone koszyki](https://baymard.com/lists/cart-abandonment-rate) (aktualizacja z września 2025), [Baymard Institute, liczba pól w checkoucie](https://baymard.com/blog/checkout-flow-average-form-fields) (2024), raport Gemius „E-commerce w Polsce 2026” w [omówieniu ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/), [Google Search Central](https://developers.google.com/search/docs/appearance/page-experience).`],faq:[[`Co szybciej zwiększa sprzedaż: reklama czy poprawki w sklepie?`,`To zależy od tego, gdzie jest problem. Jeśli sklep ma mało wejść, poprawki w nim niewiele zmienią i trzeba zacząć od ruchu. Jeśli wejść jest sporo, a zamówień mało, więcej ruchu oznacza zwykle więcej osób, które trafią na te same przeszkody. Wtedy zacznij od sklepu.`],[`Ile czasu trzeba, żeby zobaczyć efekt poprawek?`,`Część poprawek, np. koszt dostawy przy cenie, wdrożysz w jeden dzień. Kiedy zobaczysz efekt w danych, zależy od ruchu: przy kilkuset zamówieniach miesięcznie pierwsze porównanie zrobisz po kilku tygodniach, przy kilkudziesięciu warto poczekać dłużej, żeby przypadek nie zmylił wniosków.`],[`Czy darmowa dostawa zwiększa sprzedaż?`,`Nie ma jednej odpowiedzi, bo darmowa dostawa kosztuje i musi zmieścić się w marży. Pewne jest jedno: koszt dostawy powinien być widoczny wcześnie. Jeśli masz próg darmowej dostawy, pokaż go przy cenie i w koszyku, razem z kwotą, której brakuje.`],[`Czy rabaty i promocje to dobry sposób na większą sprzedaż?`,`Mogą podnieść sprzedaż na krótko, ale obniżają marżę i nie usuwają przeszkód w sklepie. Jeśli klienci rezygnują przez koszt dostawy pokazany za późno albo długi formularz, rabat tego nie zmieni. Najpierw usuń przeszkody, potem sprawdzaj, które promocje się opłacają.`],[`Czy do tych poprawek potrzebuję programisty?`,`Nie do wszystkich. Koszt dostawy przy cenie, zakup bez konta, kolejność płatności czy opis zwrotów zmienisz zwykle w ustawieniach platformy albo w treści. Zmiany w szablonie, np. przyklejony przycisk zakupu na telefonie, mogą wymagać programisty. Mogę je też zaprojektować i wdrożyć w ramach usługi wdrożenia poprawek.`]],cta:`Chcesz wiedzieć, od której poprawki zacząć w Twoim sklepie? Zacznij od bezpłatnej wstępnej oceny albo zamów audyt sklepu za 2990 zł netto.`}",
"\\"checklista-audytu-ux\\":{tldr:[`Sprawdzaj na telefonie, na danych mobilnych, w oknie prywatnym. Tak widzi sklep nowy klient.`,`Najważniejsze są punkty z koszyka, dostawy i płatności, bo dotyczą osób, które już chcą kupić.`,`Lista jest otwarta i bez zapisu. Możesz ją wydrukować albo przekazać zespołowi.`],path:`/checklista-audytu-ux`,crumb:`Checklista audytu UX`,date:`2026-11-03`,title:`Checklista audytu UX sklepu internetowego: 25 punktów`,lead:`Checklista audytu UX sklepu to 25 pytań, na które odpowiadasz „tak” albo „nie”, przechodząc swój sklep jak klient: od strony głównej po wybór płatności. Każde „nie” to miejsce, w którym klient może zrezygnować z zakupu. Przejście listy zajmuje ok. 20 minut i nie wymaga żadnych narzędzi poza telefonem.`,body:[`## Jak korzystać z listy`,`1. Weź telefon, wyłącz Wi-Fi i otwórz sklep w oknie prywatnym.`,`1. Wybierz jeden popularny produkt i jeden z wariantami, np. z rozmiarami.`,`1. Przy każdym punkcie zapisz „tak” albo „nie”. Jeśli się wahasz, wpisz „nie”.`,`1. Na koniec przejdź listę jeszcze raz na komputerze.`,`Scenariusz z czasem na każdy krok opisuję w poradniku [Jak samodzielnie sprawdzić UX sklepu w 30 minut](/jak-sprawdzic-ux-sklepu).`,`## Strona główna i nawigacja (1–3)`,`- **1. W kilka sekund wiesz, co sprzedaje sklep.** Hasło i zdjęcia na pierwszym ekranie mówią, jakie produkty tu kupisz, bez przewijania.`,`- **2. Menu prowadzi tam, gdzie się spodziewasz.** Nazwy kategorii zrozumie ktoś, kto nie zna Twojego asortymentu, a najpopularniejsze kategorie są na wierzchu.`,`- **3. Nic nie zasłania sklepu.** Baner cookies, zapis do newslettera i czat nie pojawiają się naraz. Każde okno zamkniesz jednym dotknięciem.`,`## Wyszukiwarka i filtry (4–6)`,`- **4. Wyszukiwarka jest widoczna od razu.** Na telefonie pole wyszukiwania jest w nagłówku albo pod jedną wyraźną ikoną.`,`- **5. Wyszukiwarka znajduje produkt z literówką i w innej formie.** Sprawdź nazwę z błędem i w liczbie mnogiej. Pusty wynik klient czyta jak „nie mamy”.`,`- **6. Filtry pokazują, ile produktów zostało.** Możesz zaznaczyć kilka filtrów naraz i łatwo cofnąć wybór.`,`## Karta produktu (7–11)`,`- **7. Cena i przycisk zakupu są widoczne bez przewijania**, także na telefonie.`,`- **8. Przy cenie jest koszt dostawy albo próg darmowej dostawy.** Klient zna koszt, zanim doda produkt do koszyka.`,`- **9. Przy cenie jest konkretny termin wysyłki.** Na przykład „wysyłka jutro” zamiast samego „dostępny”.`,`- **10. Warianty są przyciskami, a niedostępne są oznaczone.** Zdjęcie zmienia się po wyborze koloru, tabela rozmiarów jest obok wyboru rozmiaru.`,`- **11. Opinie i zasady zwrotu są blisko przycisku zakupu.** Ocena i liczba opinii przy nazwie, jedno zdanie o zwrotach przy przycisku.`,`Więcej punktów o samej karcie produktu znajdziesz w [checkliście karty produktu](/karta-produktu-checklista).`,`::example 0`,`## Koszyk (12–15)`,`- **12. Po dodaniu produktu wiesz, co się stało.** Widać potwierdzenie i jeden wyraźny przycisk przejścia do koszyka.`,`- **13. W koszyku widać kwotę łącznie z dostawą.** Według [Baymard Institute](https://baymard.com/lists/cart-abandonment-rate) 12% osób porzuciło zamówienie, bo nie mogło wcześniej zobaczyć ani policzyć całkowitego kosztu.`,`- **14. Koszyk podpowiada, ile brakuje do darmowej dostawy.** Na przykład „Brakuje 41 zł do darmowej dostawy”.`,`- **15. Przycisk przejścia do zamówienia jest widoczny na telefonie bez przewijania.** Nie przesuwają go polecane produkty ani pole kodu rabatowego.`,`## Dostawa i płatność (16–20)`,`- **16. Możesz kupić bez zakładania konta.** Wymóg konta to według Baymard powód porzucenia dla 18% osób. Konto można zaproponować po zamówieniu.`,`- **17. Formularz ma najwyżej ok. 8 pól.** Tyle według Baymard wystarcza większości sklepów, a przeciętny checkout w 2024 roku miał 11,3 pola ([Baymard](https://baymard.com/blog/checkout-flow-average-form-fields)). Dane do faktury pojawiają się dopiero po zaznaczeniu, że klient jej chce.`,`- **18. Przy telefonie i kodzie pocztowym pojawia się klawiatura numeryczna**, a przeglądarka podpowiada adres.`,`- **19. Błąd w polu jest pokazany przy tym polu, od razu.** Klient wie, co poprawić, zanim kliknie przycisk zamówienia.`,`- **20. Płatności i dostawy, których używają Twoi klienci, są na górze listy.** Według raportu Gemius „E-commerce w Polsce 2026” z BLIK-a korzystało 67% kupujących online, a dla 72% automat paczkowy to najczęściej wybierana forma dostawy ([ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/)).`,`## Telefon (21–23)`,`- **21. Przyciski i pola trafisz wygodnie kciukiem.** Nie klikasz w sąsiedni element i nie musisz powiększać ekranu.`,`- **22. Przycisk zakupu jest pod ręką po przewinięciu karty produktu**, np. przyklejony na dole ekranu.`,`- **23. Karta produktu i koszyk ładują się szybko na danych mobilnych.** Sprawdź je też w [PageSpeed Insights](https://pagespeed.web.dev/) w wersji mobilnej.`,`## Zaufanie (24–25)`,`- **24. Dane firmy i kontakt łatwo znaleźć.** Nazwa firmy, adres oraz telefon lub e-mail są w stopce i na stronie kontaktu, a w zamówieniu wiesz, z kim zawierasz umowę.`,`- **25. Zasady zwrotu i reklamacji są napisane prostym językiem.** W kilku zdaniach: ile dni na zwrot, kto płaci za odesłanie i jak to zrobić.`,`::report`,`## Co zrobić z wynikami`,`Policz odpowiedzi „nie” i ułóż je według tego, jak blisko płatności się pojawiły. Punkty 12–20 dotyczą klientów, którzy już chcą kupić, więc zwykle warto zacząć od nich.`,`Potem porównaj swoją listę z danymi z Google Analytics 4 lub Microsoft Clarity. Jeśli krok, przy którym masz najwięcej „nie”, to także krok, na którym odpada najwięcej klientów, wiesz, od czego zacząć. Jak czytać te dane, opisuję w poradniku [Niska konwersja sklepu](/niska-konwersja-sklepu).`,`Wiele punktów poprawisz w ustawieniach platformy. Konkretne miejsca w panelu opisuję w poradnikach o [PrestaShop](/audyt-ux-prestashop), [Shopify](/audyt-ux-shopify), [WooCommerce](/audyt-ux-woocommerce) i [Shoperze](/audyt-ux-shoper).`,`## Czego ta lista nie sprawdzi`,`Lista pokaże najbardziej widoczne problemy. Nie powie, który z nich kosztuje Cię najwięcej zamówień, i nie zastąpi świeżego spojrzenia, bo własny sklep zna się zbyt dobrze.`,`W [audycie UX sklepu internetowego](/audyt-sklepu-internetowego) sprawdzam całą ścieżkę zakupu, na komputerze i na telefonie, a każdy problem opisuję ze zrzutem ekranu i konkretną poprawką. Audyt kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Jak wygląda taki raport, zobaczysz w [przykładowym raporcie](/przykladowy-raport). Jeśli nie wiesz, czy audyt ma u Ciebie sens, zacznij od [bezpłatnej wstępnej oceny](/darmowy-audyt-sklepu).`],faq:[[`Czy checklista działa dla każdej platformy?`,`Tak. Punkty dotyczą tego, co widzi klient, więc sprawdzisz je w sklepie na PrestaShop, Shopify, WooCommerce, Shoperze, IdoSell i każdej innej platformie. Różni się tylko miejsce w panelu, w którym wprowadzisz poprawkę.`],[`Ile czasu zajmuje przejście checklisty?`,`Ok. 20 minut na telefonie i kilka kolejnych na komputerze. Warto powtórzyć ją dla dwóch, trzech różnych produktów, np. najpopularniejszego i takiego z wariantami.`],[`Czym checklista różni się od audytu UX?`,`Checklista mówi, czy dany element jest w porządku. Audyt mówi też, dlaczego klient się waha, co dokładnie zmienić i od czego zacząć. Każdy problem opisuję na zrzucie z Twojego sklepu, z konkretną poprawką do przekazania developerowi.`]],cta:`Masz kilka odpowiedzi „nie” i nie wiesz, od której zacząć? Sprawdzę to w bezpłatnej wstępnej ocenie albo w pełnym audycie sklepu za 2990 zł netto.`}",
"\\"audyt-ux-shoper\\":{tldr:[`Zacznij od kosztu dostawy i zakupu bez rejestracji. Oba ustawisz w panelu Shopera.`,`Sprawdź, czy masz szablon Storefront czy RWD, bo od tego zależy, co zmienisz w edytorze i które aplikacje zadziałają.`,`Każdą aplikację z Shoper App Store sprawdź na telefonie: czy nie dokłada okna i nie spowalnia karty produktu.`],path:`/audyt-ux-shoper`,crumb:`Audyt UX sklepu na Shoperze`,date:`2026-11-03`,title:`Audyt UX sklepu na Shoperze: co sprawdzić i poprawić`,lead:`W sklepie na Shoperze sprawdź najpierw siedem miejsc: szablon i stronę główną, kartę produktu, koszyk z kosztem dostawy, proces zamówienia, aplikacje i wyskakujące okna, płatności oraz wersję mobilną. Wiele poprawek zrobisz w panelu Shopera, bez programisty, np. włączysz zakup bez rejestracji albo ustawisz próg darmowej dostawy. Poniżej opisuję, gdzie tego szukać.`,body:[`::platforms`,`## 1. Szablon i strona główna`,`Shoper ma dwa rodzaje szablonów: starsze RWD i nowsze Storefront. W Storefront stronę układasz z sekcji w Shoper Visual Editor i możesz dopasować układ do urządzenia ([Shoper Learn](https://www.shoper.pl/learn/artykul/jak-przejsc-z-szablonu-rwd-na-storefront)). Edycja koszyka i stron płatności w Storefront jest według Shopera dostępna w pakiecie Shoper Premium.`,`**Co poprawić:** zostaw na pierwszym ekranie jasne hasło, najważniejsze kategorie i jeden wyraźny przycisk. Slider z kilkoma banerami zastąp jednym przekazem. Moduły strony zmienisz w Wygląd i treści → Wygląd sklepu → Obecny szablon graficzny → Moduły, po otwarciu Shoper Visual Editor.`,`## 2. Karta produktu`,`Sprawdź, czy przy cenie widać koszt dostawy i termin wysyłki oraz czy warianty da się wybrać bez rozwijania list. Na karcie produktu klient decyduje, czy kupić, więc każda brakująca informacja odsyła go do konkurencji.`,`**Co poprawić:** pokaż przy cenie dostępność, termin wysyłki i koszt dostawy albo próg darmowej dostawy. Opinie umieść blisko przycisku zakupu. Pełną listę znajdziesz w [checkliście karty produktu](/karta-produktu-checklista).`,`## 3. Koszyk i koszt dostawy`,`Koszty dostawy ustawiasz w panelu w Ustawienia → Obsługa zamówień → Formy dostawy. Dla każdej formy wpiszesz tam koszt albo próg darmowej dostawy ([Shoper Learn](https://www.shoper.pl/learn/artykul/kurs-e-commerce-dla-poczatkujacych-lekcja-5-konfigurujemy-sklep-na-shoperze)). Ustawienie progu to jednak dopiero połowa pracy: klient musi go zobaczyć.`,`**Co poprawić:** napisz próg darmowej dostawy przy cenie i w koszyku, najlepiej z kwotą, której brakuje. Według raportu Gemius „E-commerce w Polsce 2026” ponad połowa kupujących rezygnuje z zakupu, gdy koszt dostawy okazuje się zbyt wysoki ([ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/)).`,`::example 2`,`## 4. Proces zamówienia i zakup bez rejestracji`,`Sprawdź, czy klient może kupić bez zakładania konta. W Shoperze włączysz to w Ustawienia → Zarządzanie sprzedażą → Ustawienia zamówień i koszyka, opcją „Zezwól na zakup niezarejestrowanym” ([Shoper Learn](https://www.shoper.pl/learn/artykul/autoryzacja-kodem-w-podgladzie-zamowienia)). Dla klientów, którzy wolą się logować, Shoper udostępnia jedno konto Shoper ONE, działające w wielu sklepach na tej platformie, z logowaniem kodem jednorazowym ([komunikat Shopera](https://strefainwestorow.pl/wiadomosci/20260205/shoper-upraszcza-zakupy-w-sklepach-internetowych)).`,`**Co poprawić:** zostaw w formularzu tylko pola potrzebne do wysyłki, a dane do faktury pokaż po zaznaczeniu, że klient jej chce. Jeśli rozważasz aplikację skracającą koszyk z Shoper App Store, przed instalacją sprawdź, czy działa z Twoim szablonem. Część takich aplikacji obsługuje tylko szablony RWD.`,`## 5. Aplikacje i wyskakujące okna`,`Aplikacje w Shoper App Store tworzą w większości zewnętrzni partnerzy, a ich zgodność z szablonem Storefront zależy od autora aplikacji. Każda aplikacja do opinii, rabatów, newslettera czy czatu może dokładać skrypty i własne okno.`,`**Co poprawić:** zrób przegląd aplikacji, wyłącz nieużywane i sprawdź sklep na telefonie. Pokazuj najwyżej jedno okno naraz, nie wcześniej niż po chwili przeglądania, i pilnuj, żeby czat nie zasłaniał przycisku zakupu.`,`## 6. Płatności`,`Płatności w Shoperze uruchomisz m.in. przez Shoper Płatności (z Przelewy24 albo Autopay). Dostępni są też inni operatorzy, np. PayU, PayPal czy InPost Pay. Przy kilku bramkach lista metod szybko robi się długa.`,`**Co poprawić:** ułóż metody od tych, z których Twoi klienci korzystają najczęściej. Według Gemius 2026 z BLIK-a korzystało 67% kupujących online, a dla 53% to najczęściej używana metoda płatności. Pokaż logotypy metod płatności i dostawy już na karcie produktu albo w koszyku.`,`## 7. Wersja mobilna`,`Według Gemius 2026 zakupy na smartfonie finalizuje 58% badanych. Szablon, który dobrze wygląda na komputerze, na telefonie potrafi przesunąć przycisk zakupu pod opis albo schować wyszukiwarkę.`,`**Co poprawić:** przejdź cały zakup na telefonie, na danych mobilnych, wchodząc z Google prosto na produkt. W Storefront możesz dopasować układ sekcji do urządzenia. Więcej o tym w poradniku [UX sklepu na telefonie](/ux-sklepu-mobilnego).`,`::report`,`## Audyt UX sklepu na Shoperze w uxaudyt.pl`,`[Audyt UX sklepu internetowego](/audyt-sklepu-internetowego) obejmuje wszystkie powyższe miejsca, na komputerze i na telefonie. Do audytu wystarczy adres sklepu, bez dostępu do panelu Shopera. Kosztuje 2990 zł netto, a raport w PDF otrzymasz w 5 dni roboczych od zaksięgowania płatności. Przy każdej poprawce piszę, czy zmienisz ją w panelu lub w Shoper Visual Editor, czy potrzebna będzie aplikacja albo programista.`,`Jeśli chcesz, poprawki zaprojektuję i wdrożę w ramach usługi [wdrożenia poprawek](/wdrozenie-poprawek). Najczęstsze powody, dla których klienci nie kończą zakupu, opisuję w poradniku [Porzucone koszyki](/porzucone-koszyki), a sklepy na innych platformach w poradnikach o [PrestaShop](/audyt-ux-prestashop), [Shopify](/audyt-ux-shopify) i [WooCommerce](/audyt-ux-woocommerce). Wolisz najpierw sprawdzić sklep sam? Przejdź [checklistę audytu UX sklepu](/checklista-audytu-ux).`,`Źródła: [Shoper Learn: zakup bez rejestracji](https://www.shoper.pl/learn/artykul/autoryzacja-kodem-w-podgladzie-zamowienia), [Shoper Learn: konfiguracja sklepu](https://www.shoper.pl/learn/artykul/kurs-e-commerce-dla-poczatkujacych-lekcja-5-konfigurujemy-sklep-na-shoperze), [Shoper Learn: RWD a Storefront](https://www.shoper.pl/learn/artykul/jak-przejsc-z-szablonu-rwd-na-storefront), raport Gemius „E-commerce w Polsce 2026” w [omówieniu ITwiz](https://itwiz.pl/polski-e-commerce-wchodzi-w-nowy-etap-ai-pomaga-kupowac-ale-klient-decyduje/).`],faq:[[`Jak włączyć zakup bez rejestracji w Shoperze?`,`W panelu wejdź w Ustawienia → Zarządzanie sprzedażą → Ustawienia zamówień i koszyka i w sekcji „Składanie i realizacja zamówień” zaznacz „Zezwól na zakup niezarejestrowanym”.`],[`Czy do audytu potrzebujesz dostępu do panelu Shopera?`,`Nie. Wystarczy adres sklepu, bo sprawdzam to, co widzi klient. Dostęp do panelu jest potrzebny dopiero przy wdrożeniu poprawek.`],[`Czy warto przejść z szablonu RWD na Storefront?`,`To zależy od tego, co chcesz zmienić. Storefront daje więcej możliwości edycji w Shoper Visual Editor, ale sam szablon nie usunie przeszkód w zakupie. Jeśli planujesz zmianę, zrób audyt przed nią. Wtedy nowy szablon od początku rozwiąże problemy, które znalazłem w obecnym.`],[`Czy audyt sklepu na Shoperze różni się od audytu na innej platformie?`,`Ścieżka klienta jest taka sama, ale zalecenia uwzględniają możliwości Shopera: co zmienisz w panelu i w Shoper Visual Editor, co wymaga aplikacji z Shoper App Store, a co pracy programisty.`]],cta:`Sprawdzę Twój sklep na Shoperze. Pełny audyt kosztuje 2990 zł netto, a na start możesz poprosić o bezpłatną wstępną ocenę.`}"
],
"id": "3.1-3.3"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`Jak samodzielnie sprawdzić UX sklepu`,``,`/jak-sprawdzic-ux-sklepu`]]]",
"new": "[`Jak samodzielnie sprawdzić UX sklepu`,``,`/jak-sprawdzic-ux-sklepu`],[`Checklista audytu UX`,``,`/checklista-audytu-ux`],[`Jak zwiększyć sprzedaż sklepu`,``,`/jak-zwiekszyc-sprzedaz-sklepu`]]]",
"count": 1,
"id": "menu-podstawy"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "[`Audyt UX: Shopify`,``,`/audyt-ux-shopify`],[`Audyt UX a audyt SEO`",
"new": "[`Audyt UX: Shopify`,``,`/audyt-ux-shopify`],[`Audyt UX: Shoper`,``,`/audyt-ux-shoper`],[`Audyt UX a audyt SEO`",
"count": 1,
"id": "menu-platformy"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`jak-sprawdzic-ux-sklepu`,`darmowy-audyt-sklepu`],optionTitles:",
"new": "`jak-sprawdzic-ux-sklepu`,`darmowy-audyt-sklepu`,`jak-zwiekszyc-sprzedaz-sklepu`,`checklista-audytu-ux`,`audyt-ux-shoper`],optionTitles:",
"count": 1,
"id": "options"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "`Poradnik: Samodzielne sprawdzenie`,`Darmowy audyt sklepu`]",
"new": "`Poradnik: Samodzielne sprawdzenie`,`Darmowy audyt sklepu`,`Poradnik: Jak zwiększyć sprzedaż`,`Poradnik: Checklista audytu UX`,`Poradnik: Shoper`]",
"count": 1,
"id": "optionTitles"
},
{
"op": "rep",
"file": "src/pages.mjs",
"old": "'ux-sklepu-mobilnego', 'audyt-ux-woocommerce', 'audyt-ux-shopify', 'jak-sprawdzic-ux-sklepu', 'darmowy-audyt-sklepu'].map((k) => v7(k, '/' + k)),",
"new": "'ux-sklepu-mobilnego', 'audyt-ux-woocommerce', 'audyt-ux-shopify', 'jak-sprawdzic-ux-sklepu', 'darmowy-audyt-sklepu',\\n    'jak-zwiekszyc-sprzedaz-sklepu', 'checklista-audytu-ux', 'audyt-ux-shoper'].map((k) => v7(k, '/' + k)),",
"count": 1,
"id": "pages-new"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "\\"@type\\":`Person`,name:`Marcin Bednarz`,jobTitle:`Behavioral Designer / UX Specialist`}",
"new": "\\"@type\\":`Person`,name:`Marcin Bednarz`,jobTitle:`Behavioral Designer / UX Specialist`,url:`https://www.linkedin.com/in/marcin-bednarz-a3328910a/`,sameAs:[`https://www.linkedin.com/in/marcin-bednarz-a3328910a/`]}",
"count": 2,
"id": "LI-schema"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "linkedin:a=``,",
"new": "linkedin:a=`https://www.linkedin.com/in/marcin-bednarz-a3328910a/`,",
"count": 1,
"id": "LI-default"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "linkedin:{type:v.String,title:`LinkedIn URL`,defaultValue:``}",
"new": "linkedin:{type:v.String,title:`LinkedIn URL`,defaultValue:`https://www.linkedin.com/in/marcin-bednarz-a3328910a/`}",
"count": 1,
"id": "LI-control"
},
{
"op": "rep",
"file": "src/c/V7Home.mjs",
"old": "d(`a`,{className:`v7-ul v7-gauth-l`,href:`/#o-mnie`,children:`Więcej o mnie`}),",
"new": "u(`div`,{className:`v7-gauth-ls`,style:{display:`flex`,gap:20,flexWrap:`wrap`},children:[d(`a`,{className:`v7-ul v7-gauth-l`,href:`/#o-mnie`,children:`Więcej o mnie`}),d(`a`,{className:`v7-ul v7-gauth-l`,href:`https://www.linkedin.com/in/marcin-bednarz-a3328910a/`,target:`_blank`,rel:`noopener noreferrer`,children:`LinkedIn ↗`})]}),",
"count": 1,
"id": "LI-authorbox"
},
{
"op": "yfaq",
"text": "Czy potrzebujesz dostępu do panelu sklepu?\\nNie. Patrzę na sklep oczami klienta, na działającej stronie. Wystarczy mi jej adres. Nie proszę o hasła, dostęp do panelu ani do Google Analytics.\\n\\nCzym Twój raport różni się od raportu z narzędzi albo z AI?\\nNarzędzia mierzą szybkość i błędy techniczne. Ja sprawdzam to, czego nie zmierzą: czy klient rozumie ofertę, znajduje produkt, wie, ile zapłaci za dostawę, i czy nie gubi się w zamówieniu. Każdy problem pokazuję na zrzucie ekranu z Twojego sklepu i dopisuję poprawkę dla Twojego przypadku. Jak to wygląda, zobaczysz w [przykładowym raporcie](/przykladowy-raport).\\n\\nKto wykonuje audyt?\\nJa, osobiście. Nie korzystam z narzędzi, które generują raporty automatycznie. Każdy sklep przechodzę sam, krok po kroku, na komputerze i telefonie.\\n\\nCzy raport będzie zrozumiały, jeśli nie znam się na UX?\\nTak. Piszę prostym językiem, bez żargonu. Każdy problem ma zrzut ekranu, wyjaśnienie, dlaczego przeszkadza klientom, i konkretną poprawkę do przekazania developerowi.\\n\\nOtrzymam długą listę uwag i nie będę wiedzieć, od czego zacząć?\\nNie. Problemy układam od tych, które najbardziej wpływają na sprzedaż, i oznaczam: krytyczny, ważny, drobny. Zaczynasz od góry listy.\\n\\nNie mam developera. Co wtedy?\\nCzęść poprawek to zmiana tekstu albo ustawień, którą wprowadzisz sam w panelu. Resztę możesz przekazać dowolnemu wykonawcy: raport jest Twój, możesz go kopiować i przekazywać developerom i agencjom. Możesz też zlecić projekt i wdrożenie mnie, wycenę przygotuję po raporcie. Szczegóły na stronie [wdrożenia poprawek](/wdrozenie-poprawek).\\n\\nCzy audyt opłaca się małemu sklepowi?\\nNie zawsze. Jeśli masz mniej niż ok. 50 zamówień miesięcznie, pełny audyt może się jeszcze nie zwrócić. Zacznij wtedy od [bezpłatnej wstępnej oceny](/darmowy-audyt-sklepu). Szczerze napiszę, czy audyt ma u Ciebie sens.\\n\\nCo jeśli audyt nic nie wykaże albo raport się spóźni?\\nZwrócę całą kwotę w dwóch sytuacjach: raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w ciągu 5 dni roboczych od zaksięgowania płatności, chyba że opóźnienie wynika z niedostępności Twojego sklepu. Wystarczy e-mail na kontakt@uxaudyt.pl w ciągu 14 dni od terminu dostarczenia raportu albo od jego otrzymania. Zwrot otrzymasz w ciągu 14 dni tą samą metodą płatności. Zasady opisuje [§ 7 regulaminu](/regulamin#gwarancja).\\n\\nCzy gwarantujesz wzrost sprzedaży?\\nNie. Sprzedaż zależy też od ruchu, cen, oferty i tego, które poprawki wdrożysz. Gwarantuję raport w terminie i konkretne problemy, które realnie wpływają na sprzedaż. Jeśli ich nie znajdę, zwracam pieniądze.\\n\\nIle trwa audyt?\\nRaport otrzymasz w 5 dni roboczych od zaksięgowania płatności. Przy BLIK-u i karcie płatność księguje się zwykle od razu. Potem umawiamy rozmowę o raporcie, a w pakiecie z opieką warsztat online, w terminie, który Ci pasuje.\\n\\nCzym różni się audyt sklepu od audytu z opieką?\\nW obu otrzymasz ten sam raport w 5 dni roboczych od zaksięgowania płatności. W audycie sklepu (2990 zł netto) omawiamy go na rozmowie. Pakiet z opieką (4490 zł netto) dodaje warsztat online z omówieniem raportu z Tobą i zespołem, makiety wszystkich krytycznych poprawek, 30 dni wsparcia e-mailem od dnia warsztatu i jednorazowe ponowne sprawdzenie sklepu po zmianach. Porównanie znajdziesz na stronie [audytu z opieką](/audyt-sklepu-z-opieka).\\n\\nCzy audytujesz też strony firmowe?\\nTak. Sprawdzam strony firmowe do ok. 20 podstron: ofertę, nawigację, przyciski kontaktu, formularze i wersję mobilną. Taki [audyt strony](/audyt-strony-internetowej) kosztuje 1990 zł netto, a raport otrzymasz w 5 dni roboczych.\\n\\nNa jakich platformach działasz?\\nNa każdej, bo sprawdzam to, co widzi klient: PrestaShop, Shopify, WooCommerce, Shoper, IdoSell, Magento i inne. Przy PrestaShop mam status PrestaShop Expert, więc podpowiem też konkretne ustawienia i moduły. Więcej w [poradniku o PrestaShop](/audyt-ux-prestashop).\\n\\nJak wygląda płatność i faktura?\\nPłacisz z góry BLIK-iem, Przelewy24 albo kartą, przez bezpieczną bramkę Stripe. Do każdej płatności wystawiam fakturę VAT na dane podane w zamówieniu. Potwierdzenie otrzymasz od razu na e-mail.\\n\\nCzym właściwie jest audyt UX?\\nTo przejście Twojego sklepu albo strony oczami klienta i wskazanie miejsc, w których może się zawahać lub zrezygnować, razem z konkretnymi poprawkami. Więcej przeczytasz w poradniku [Audyt UX: co to jest, jak wygląda i ile kosztuje](/audyt-ux).",
"id": "Y-fallback"
}
],
"faq": {
"SKLEP": "Czy potrzebujesz dostępu do panelu sklepu?\\nNie. Patrzę na sklep oczami klienta, na działającej stronie. Wystarczy mi jej adres. Nie proszę o hasła, dostęp do panelu ani do Google Analytics.\\n\\nCzym Twój raport różni się od raportu z narzędzi albo z AI?\\nNarzędzia mierzą szybkość i błędy techniczne. Ja sprawdzam to, czego nie zmierzą: czy klient rozumie ofertę, znajduje produkt, wie, ile zapłaci za dostawę, i czy nie gubi się w zamówieniu. Każdy problem pokazuję na zrzucie ekranu z Twojego sklepu i dopisuję poprawkę dla Twojego przypadku. Jak to wygląda, zobaczysz w [przykładowym raporcie](/przykladowy-raport).\\n\\nKto wykonuje audyt?\\nJa, osobiście. Nie korzystam z narzędzi, które generują raporty automatycznie. Każdy sklep przechodzę sam, krok po kroku, na komputerze i telefonie.\\n\\nCzy raport będzie zrozumiały, jeśli nie znam się na UX?\\nTak. Piszę prostym językiem, bez żargonu. Każdy problem ma zrzut ekranu, wyjaśnienie, dlaczego przeszkadza klientom, i konkretną poprawkę do przekazania developerowi.\\n\\nOtrzymam długą listę uwag i nie będę wiedzieć, od czego zacząć?\\nNie. Problemy układam od tych, które najbardziej wpływają na sprzedaż, i oznaczam: krytyczny, ważny, drobny. Zaczynasz od góry listy.\\n\\nNie mam developera. Co wtedy?\\nCzęść poprawek to zmiana tekstu albo ustawień, którą wprowadzisz sam w panelu. Resztę możesz przekazać dowolnemu wykonawcy: raport jest Twój, możesz go kopiować i przekazywać developerom i agencjom. Możesz też zlecić projekt i wdrożenie mnie, wycenę przygotuję po raporcie. Szczegóły na stronie [wdrożenia poprawek](/wdrozenie-poprawek).\\n\\nCzy audyt opłaca się małemu sklepowi?\\nNie zawsze. Jeśli masz mniej niż ok. 50 zamówień miesięcznie, pełny audyt może się jeszcze nie zwrócić. Zacznij wtedy od [bezpłatnej wstępnej oceny](/darmowy-audyt-sklepu). Szczerze napiszę, czy audyt ma u Ciebie sens.\\n\\nCo jeśli audyt nic nie wykaże albo raport się spóźni?\\nZwrócę całą kwotę w dwóch sytuacjach: raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w ciągu 5 dni roboczych od zaksięgowania płatności, chyba że opóźnienie wynika z niedostępności Twojego sklepu. Wystarczy e-mail na kontakt@uxaudyt.pl w ciągu 14 dni od terminu dostarczenia raportu albo od jego otrzymania. Zwrot otrzymasz w ciągu 14 dni tą samą metodą płatności. Zasady opisuje [§ 7 regulaminu](/regulamin#gwarancja).\\n\\nCzy gwarantujesz wzrost sprzedaży?\\nNie. Sprzedaż zależy też od ruchu, cen, oferty i tego, które poprawki wdrożysz. Gwarantuję raport w terminie i konkretne problemy, które realnie wpływają na sprzedaż. Jeśli ich nie znajdę, zwracam pieniądze.\\n\\nIle trwa audyt?\\nRaport otrzymasz w 5 dni roboczych od zaksięgowania płatności. Przy BLIK-u i karcie płatność księguje się zwykle od razu. Potem umawiamy rozmowę o raporcie, a w pakiecie z opieką warsztat online, w terminie, który Ci pasuje.\\n\\nCzym różni się audyt sklepu od audytu z opieką?\\nW obu otrzymasz ten sam raport w 5 dni roboczych od zaksięgowania płatności. W audycie sklepu (2990 zł netto) omawiamy go na rozmowie. Pakiet z opieką (4490 zł netto) dodaje warsztat online z omówieniem raportu z Tobą i zespołem, makiety wszystkich krytycznych poprawek, 30 dni wsparcia e-mailem od dnia warsztatu i jednorazowe ponowne sprawdzenie sklepu po zmianach. Porównanie znajdziesz na stronie [audytu z opieką](/audyt-sklepu-z-opieka).\\n\\nCzy audytujesz też strony firmowe?\\nTak. Sprawdzam strony firmowe do ok. 20 podstron: ofertę, nawigację, przyciski kontaktu, formularze i wersję mobilną. Taki [audyt strony](/audyt-strony-internetowej) kosztuje 1990 zł netto, a raport otrzymasz w 5 dni roboczych.\\n\\nNa jakich platformach działasz?\\nNa każdej, bo sprawdzam to, co widzi klient: PrestaShop, Shopify, WooCommerce, Shoper, IdoSell, Magento i inne. Przy PrestaShop mam status PrestaShop Expert, więc podpowiem też konkretne ustawienia i moduły. Więcej w [poradniku o PrestaShop](/audyt-ux-prestashop).\\n\\nJak wygląda płatność i faktura?\\nPłacisz z góry BLIK-iem, Przelewy24 albo kartą, przez bezpieczną bramkę Stripe. Do każdej płatności wystawiam fakturę VAT na dane podane w zamówieniu. Potwierdzenie otrzymasz od razu na e-mail.\\n\\nCzym właściwie jest audyt UX?\\nTo przejście Twojego sklepu albo strony oczami klienta i wskazanie miejsc, w których może się zawahać lub zrezygnować, razem z konkretnymi poprawkami. Więcej przeczytasz w poradniku [Audyt UX: co to jest, jak wygląda i ile kosztuje](/audyt-ux).",
"OPIEKA": "Kiedy wybrać pakiet z opieką zamiast samego audytu?\\nGdy nie masz w zespole projektanta UX albo chcesz, żeby developer miał kogo zapytać w trakcie zmian. Jeśli Twój developer poradzi sobie z samym raportem, wystarczy [audyt sklepu](/audyt-sklepu-internetowego) za 2990 zł netto.\\n\\nCo obejmuje 30 dni wsparcia?\\nPrzez 30 dni od dnia warsztatu odpowiadam e-mailem na pytania Twoje i Twojego developera dotyczące poprawek z raportu. W tym czasie możesz też zgłosić jedno ponowne sprawdzenie sklepu po wprowadzeniu zmian.\\n\\nJak wygląda warsztat?\\nUmawiamy go zaraz po wysłaniu raportu, online, w terminie, który pasuje Tobie i zespołowi. Omawiamy wyniki, odpowiadam na pytania i razem ustalamy, w jakiej kolejności wdrażać poprawki. Od dnia warsztatu liczy się 30 dni wsparcia.\\n\\nIle trwa cały pakiet?\\nRaport otrzymasz w 5 dni roboczych od zaksięgowania płatności. Warsztat umawiamy zaraz potem, a od jego dnia liczy się 30 dni wsparcia.\\n\\nCzy potrzebujesz dostępu do panelu sklepu?\\nNie. Patrzę na sklep oczami klienta, na działającej stronie. Wystarczy mi jej adres. Nie proszę o hasła, dostęp do panelu ani do Google Analytics.\\n\\nKto wykonuje audyt?\\nJa, osobiście. Nie korzystam z narzędzi, które generują raporty automatycznie. Każdy sklep przechodzę sam, krok po kroku, na komputerze i telefonie.\\n\\nCzy raport będzie zrozumiały, jeśli nie znam się na UX?\\nTak. Piszę prostym językiem, bez żargonu. Każdy problem ma zrzut ekranu, wyjaśnienie, dlaczego przeszkadza klientom, i konkretną poprawkę do przekazania developerowi.\\n\\nCo jeśli audyt nic nie wykaże albo raport się spóźni?\\nZwrócę całą kwotę w dwóch sytuacjach: raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w ciągu 5 dni roboczych od zaksięgowania płatności, chyba że opóźnienie wynika z niedostępności Twojego sklepu. Wystarczy e-mail na kontakt@uxaudyt.pl w ciągu 14 dni od terminu dostarczenia raportu albo od jego otrzymania. Zwrot otrzymasz w ciągu 14 dni tą samą metodą płatności. Zasady opisuje [§ 7 regulaminu](/regulamin#gwarancja).\\n\\nCzy gwarantujesz wzrost sprzedaży?\\nNie. Sprzedaż zależy też od ruchu, cen, oferty i tego, które poprawki wdrożysz. Gwarantuję raport w terminie i konkretne problemy, które realnie wpływają na sprzedaż. Jeśli ich nie znajdę, zwracam pieniądze.\\n\\nNa jakich platformach działasz?\\nNa każdej, bo sprawdzam to, co widzi klient: PrestaShop, Shopify, WooCommerce, Shoper, IdoSell, Magento i inne. Przy PrestaShop mam status PrestaShop Expert, więc podpowiem też konkretne ustawienia i moduły. Więcej w [poradniku o PrestaShop](/audyt-ux-prestashop).\\n\\nJak wygląda płatność i faktura?\\nPłacisz z góry BLIK-iem, Przelewy24 albo kartą, przez bezpieczną bramkę Stripe. Do każdej płatności wystawiam fakturę VAT na dane podane w zamówieniu. Potwierdzenie otrzymasz od razu na e-mail.",
"STRONA": "Czy to jest audyt SEO?\\nNie. Audyt SEO sprawdza, jak Twoją stronę widzi Google. Ja sprawdzam, co robi człowiek, który już na nią trafił: czy rozumie ofertę i łatwo się z Tobą kontaktuje. Różnice opisuję w poradniku [Audyt UX a audyt SEO](/audyt-ux-a-audyt-seo).\\n\\nCzy potrzebujesz dostępu do panelu strony?\\nNie. Patrzę na stronę oczami klienta. Wystarczy mi jej adres.\\n\\nCzy sprawdzasz strony na WordPressie?\\nTak. Platforma nie ma znaczenia: WordPress, Webflow, Wix, Framer i inne. Sprawdzam to, co widzi odwiedzający.\\n\\nIle podstron obejmuje audyt?\\nDo ok. 20 podstron. Masz większy serwis? Napisz na kontakt@uxaudyt.pl, przygotuję indywidualną wycenę.\\n\\nCzy otrzymam makiety poprawek?\\nMakiety nie są częścią audytu strony. Każdą poprawkę opisuję słowami i pokazuję na zrzucie ekranu, tak żeby developer mógł ją wprowadzić. Jeśli chcesz projekt poprawek, przygotuję go w ramach [wdrożenia](/wdrozenie-poprawek).\\n\\nKto wykonuje audyt?\\nJa, osobiście. Nie korzystam z narzędzi, które generują raporty automatycznie. Każdą stronę przechodzę sam, krok po kroku, na komputerze i telefonie.\\n\\nCzy raport będzie zrozumiały, jeśli nie znam się na UX?\\nTak. Piszę prostym językiem, bez żargonu. Każdy problem ma zrzut ekranu, wyjaśnienie, dlaczego przeszkadza klientom, i konkretną poprawkę do przekazania developerowi.\\n\\nIle trwa audyt?\\nRaport otrzymasz w 5 dni roboczych od zaksięgowania płatności. Potem umawiamy rozmowę o raporcie.\\n\\nCo jeśli audyt nic nie wykaże albo raport się spóźni?\\nZwrócę całą kwotę w dwóch sytuacjach: raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w ciągu 5 dni roboczych od zaksięgowania płatności, chyba że opóźnienie wynika z niedostępności Twojej strony. Wystarczy e-mail na kontakt@uxaudyt.pl w ciągu 14 dni od terminu dostarczenia raportu albo od jego otrzymania. Zwrot otrzymasz w ciągu 14 dni tą samą metodą płatności. Zasady opisuje [§ 7 regulaminu](/regulamin#gwarancja).\\n\\nCzy gwarantujesz więcej zapytań?\\nNie. Liczba zapytań zależy też od ruchu, oferty i cen. Gwarantuję raport w terminie i konkretne problemy, które realnie przeszkadzają klientom. Jeśli nie znajdę żadnego, który wpływa na sprzedaż, zwracam pieniądze.\\n\\nJak wygląda płatność i faktura?\\nPłacisz z góry BLIK-iem, Przelewy24 albo kartą, przez bezpieczną bramkę Stripe. Do każdej płatności wystawiam fakturę VAT na dane podane w zamówieniu. Potwierdzenie otrzymasz od razu na e-mail.",
"WDROZENIE": "Czy muszę najpierw zamówić audyt?\\nZwykle tak, bo dopiero raport pokazuje, co jest do zrobienia i ile to potrwa. Jeśli masz już raport UX od innej firmy, opisz go w formularzu, a odpiszę, czy i jak mogę pomóc.\\n\\nIle kosztuje wdrożenie?\\nWycena zależy od liczby i rodzaju poprawek, dlatego przygotowuję ją po raporcie. Dla orientacji: w [przykładowym raporcie](/przykladowy-raport) siedem poprawek to ok. 3 dni pracy developera.\\n\\nCzy mogę wdrożyć tylko część poprawek?\\nTak. Sam decydujesz, które poprawki wdrażamy i w jakiej kolejności. Resztę możesz zrobić sam albo z innym wykonawcą.\\n\\nMam własnego developera. Do czego jesteś mi potrzebny?\\nMogę przygotować projekt poprawek w Figmie, przekazać go developerowi i odpowiadać na jego pytania. Zakres ustalamy przy wycenie.\\n\\nNa jakich platformach wdrażasz?\\nPrestaShop (mam status PrestaShop Expert), Shopify, WooCommerce, Shoper, IdoSell i inne. Na nietypowej platformie przygotuję projekt i poprowadzę Twojego developera.\\n\\nCzy wycena do czegoś mnie zobowiązuje?\\nNie. Wycena jest bez zobowiązań, a cena audytu się nie zmienia, niezależnie od tego, czy zlecisz wdrożenie.\\n\\nCzym różni się wdrożenie od audytu z opieką?\\nW [audycie z opieką](/audyt-sklepu-z-opieka) projektuję makiety krytycznych poprawek i przez 30 dni odpowiadam na pytania. Zmiany w sklepie wprowadza wtedy Twój zespół. We wdrożeniu mogę wprowadzić je sam."
},
"props": {
"faq": {
"index": "SKLEP",
"audyt-sklepu-internetowego": "SKLEP",
"audyt-sklepu-z-opieka": "OPIEKA",
"audyt-strony-internetowej": "STRONA",
"wdrozenie-poprawek": "WDROZENIE",
"*guides*": "SKLEP"
},
"rep": [
[
"Cała ścieżka zakupu na desktopie oraz urządzeniach mobilnych. Lista problemów od najważniejszych i 3 makiety poprawek.",
"Cała ścieżka zakupu na komputerze i telefonie. Raport PDF z problemami od najważniejszych, poprawka przy każdym i rozmowa o raporcie."
],
[
"Audyt sklepu, warsztat z omówieniem raportu, makiety krytycznych poprawek, 30 dni wsparcia i ponowne sprawdzenie sklepu.",
"Wszystko z audytu sklepu oraz warsztat online z omówieniem raportu, makiety wszystkich krytycznych poprawek, 30 dni wsparcia e-mailem od warsztatu i jednorazowe ponowne sprawdzenie sklepu."
],
[
"Strona firmowa do ok. 20 podstron: oferta, przyciski kontaktu, formularze i wersja mobilna.",
"Strona firmowa do ok. 20 podstron: oferta, przyciski kontaktu, formularze i wersja mobilna. Raport PDF i rozmowa o raporcie."
],
[
"Warsztat + 30 dni wsparcia",
"Warsztat, makiety i 30 dni wsparcia"
],
[
"Cała ścieżka zakupu na desktopie oraz urządzeniach mobilnych: strona główna, kategoria, karta produktu, koszyk i płatność.",
"Przykład poglądowy, uogólniony z typowych błędów w sklepach. Zakres taki jak w audycie: cała ścieżka zakupu na komputerze i telefonie, od strony głównej przez kategorię i kartę produktu po koszyk i płatność."
],
[
"Otrzymasz go w 5 dni roboczych, razem z makietami poprawek. Jeśli nie znajdę nic, co wpływa na sprzedaż, oddam Ci pieniądze.",
"Raport otrzymasz w 5 dni roboczych od zaksięgowania płatności. Audyt sklepu kosztuje 2990 zł netto (3677,70 zł brutto). Jeśli raport nie wskaże żadnego problemu, który realnie wpływa na sprzedaż, albo nie dotrze w terminie, chyba że opóźnienie wynika z niedostępności Twojego sklepu, zwrócę całą kwotę."
]
],
"newpages": [
"jak-zwiekszyc-sprzedaz-sklepu",
"checklista-audytu-ux",
"audyt-ux-shoper"
],
"linkedin": "https://www.linkedin.com/in/marcin-bednarz-a3328910a/"
},
"meta": {
"index": [
"Audyt UX sklepów i stron www od 1990 zł | uxaudyt.pl",
"Sprawdzę Twój sklep lub stronę oczami klienta i wskażę, co blokuje zakupy. Stała cena, raport z poprawkami w 5 dni roboczych, gwarancja zwrotu."
],
"audyt-sklepu-internetowego": [
"Audyt sklepu internetowego (UX) – 2990 zł | uxaudyt.pl",
"Przejdę całą ścieżkę zakupu w Twoim sklepie na telefonie i komputerze. Raport PDF z poprawkami od najważniejszych w 5 dni roboczych. 2990 zł netto."
],
"audyt-strony-internetowej": [
null,
"Sprawdzę ofertę, nawigację, formularze i wersję mobilną Twojej strony. Otrzymasz listę poprawek, które ułatwią klientom kontakt. 1990 zł netto."
],
"audyt-sklepu-z-opieka": [
"Audyt sklepu z opieką przy wdrożeniu – 4490 zł | uxaudyt.pl",
"Audyt UX sklepu, warsztat, makiety krytycznych poprawek i 30 dni wsparcia e-mailem od warsztatu. Na koniec sprawdzę sklep po zmianach. 4490 zł netto."
],
"wdrozenie-poprawek": [
"Wdrożenie poprawek z audytu UX w sklepie | uxaudyt.pl",
"Zaprojektuję poprawki z raportu w Figmie i wdrożę je na Twojej platformie, w tym w PrestaShop, albo poprowadzę Twojego developera. Wycena po raporcie."
],
"przykladowy-raport": [
"Przykładowy raport z audytu UX sklepu (wzór) | uxaudyt.pl",
"Zobacz wzór raportu z audytu UX sklepu: problemy od najważniejszych, poprawka i szacowany czas wdrożenia przy każdym. Przykład poglądowy."
],
"zamowienie": [
null,
"Zamów audyt UX sklepu lub strony. Stała cena, raport PDF w 5 dni roboczych od zaksięgowania płatności, gwarancja zwrotu."
],
"zamowienie-plan": [
null,
"Zamów audyt UX sklepu lub strony. Stała cena, raport PDF w 5 dni roboczych od zaksięgowania płatności, gwarancja zwrotu."
],
"audyt-ux": [
"Audyt UX: co to jest, jak wygląda i ile kosztuje (2026)",
null
],
"audyt-ux-a-audyt-seo": [
"Audyt UX a audyt SEO: różnice i od którego zacząć",
null
],
"audyt-ux-prestashop": [
null,
"Co w sklepie na PrestaShop utrudnia zakup i jak to poprawić: proces zamówienia, formularze, koszyk, płatności i szybkość. Poradnik od PrestaShop Expert."
],
"audyt-ux-shopify": [
"Audyt UX sklepu na Shopify: co sprawdzić i poprawić",
"Motyw, tłumaczenia, karta produktu, koszyk i aplikacje. Co sprawdzić w sklepie na Shopify przed checkoutem i co zmienisz bez planu Shopify Plus."
],
"audyt-ux-woocommerce": [
null,
"Formularz zamówienia w checkoucie blokowym i starszym, zakup bez konta, warianty, wtyczki i płatności. Co sprawdzić w sklepie na WooCommerce."
],
"porzucone-koszyki": [
null,
"8 najczęstszych powodów porzucania koszyków i poprawki do każdego. Jak zapobiegać, zanim zaczniesz odzyskiwać klientów mailami. Z listą kontrolną."
],
"niska-konwersja-sklepu": [
"Niska konwersja sklepu: przyczyny i jak je znaleźć",
"Ruch jest, a zamówień mało? Sprawdź, gdzie klienci rezygnują, jaka konwersja jest dobra i od czego zacząć poprawki w sklepie internetowym."
],
"karta-produktu-checklista": [
"Karta produktu: co powinna zawierać (checklista 20 pkt)",
"Co powinna zawierać karta produktu w sklepie internetowym? Checklista 20 punktów: zdjęcia, cena, dostawa, warianty, opis, opinie i wersja mobilna."
],
"darmowy-audyt-sklepu": [
null,
"Podaj adres sklepu, a sprawdzę go osobiście i odpiszę zwykle w ciągu 2 dni roboczych, czy coś zatrzymuje Twoich klientów. Bezpłatnie i bez zobowiązań."
],
"jak-sprawdzic-ux-sklepu": [
null,
"Scenariusz krok po kroku: przejdź zakup jak klient na telefonie i znajdź miejsca, w których Twój sklep gubi zamówienia. Bez płatnych narzędzi."
],
"jak-zwiekszyc-sprzedaz-sklepu": [
"Jak zwiększyć sprzedaż w sklepie internetowym: 12 poprawek",
"Zanim dołożysz budżet na reklamy, sprawdź, czy sklep nie gubi klientów. 12 poprawek w karcie produktu, koszyku i dostawie, które możesz wdrożyć sam."
],
"checklista-audytu-ux": [
"Checklista audytu UX sklepu: 25 punktów do sprawdzenia",
"25 punktów od strony głównej po płatność, które sprawdzisz w swoim sklepie w ok. 20 minut. Bez narzędzi i bez zapisu: odpowiadasz tak albo nie."
],
"audyt-ux-shoper": [
"Audyt UX sklepu na Shoperze: co sprawdzić i poprawić",
"Szablon, karta produktu, koszyk, dostawa i płatności. Co sprawdzić w sklepie na Shoperze i które poprawki zrobisz w panelu, bez programisty."
]
},
"llms": "# uxaudyt.pl\\n\\n> Audyty UX sklepów internetowych i stron firmowych w Polsce, zamawiane i opłacane online. Każdy audyt wykonuje osobiście Marcin Bednarz, projektant UX z 13-letnim doświadczeniem w projektowaniu produktów cyfrowych. Raport w PDF w 5 dni roboczych od zaksięgowania płatności, potem rozmowa omówienia raportu (w pakiecie z opieką warsztat online).\\n\\nAudyt UX w uxaudyt.pl to ekspercka ocena sklepu lub strony oczami klienta: przejście całej ścieżki zakupu albo kontaktu na komputerze i na telefonie oraz lista problemów ułożona od najważniejszych. Przy każdym problemie raport zawiera zrzut ekranu, wyjaśnienie i konkretną poprawkę do przekazania developerowi. Do audytu wystarczy adres sklepu lub strony; dostęp do panelu nie jest potrzebny.\\n\\nCeny (netto, jednorazowo, stałe):\\n- Audyt UX strony internetowej: 1990 zł netto (2447,70 zł brutto). Strony firmowe do ok. 20 podstron.\\n- Audyt UX sklepu internetowego: 2990 zł netto (3677,70 zł brutto). Cała ścieżka zakupu na komputerze i telefonie.\\n- Audyt sklepu z opieką przy wdrożeniu: 4490 zł netto (5522,70 zł brutto). Zakres audytu sklepu oraz warsztat online z omówieniem raportu, makiety wszystkich krytycznych poprawek, 30 dni wsparcia e-mailem przy wdrożeniu (liczone od dnia warsztatu) i jednorazowe ponowne sprawdzenie sklepu po zmianach.\\n- Wdrożenie poprawek: wycena indywidualna po raporcie. Projekt poprawek w Figmie i wdrożenie na platformie klienta (PrestaShop, WooCommerce, Shopify, Shoper, IdoSell) albo prowadzenie jego developera.\\n- Bezpłatna wstępna ocena: 0 zł, bez zobowiązań. Odpowiedź e-mailem, zwykle w ciągu 2 dni roboczych.\\n\\nZamówienie i płatność: płatność z góry przez Stripe (BLIK, Przelewy24, karta), faktura VAT. Gwarancja: zwrot całej kwoty, jeśli raport nie zostanie dostarczony w terminie (chyba że opóźnienie wynika z niedostępności sklepu klienta) albo nie wskaże żadnego problemu, który realnie wpływa na sprzedaż. Zgłoszenie e-mailem w 14 dni od terminu raportu lub jego otrzymania (§ 7 regulaminu). uxaudyt.pl nie gwarantuje konkretnego wzrostu sprzedaży ani konwersji.\\n\\nPlatformy: audyt obejmuje to, co widzi klient, więc działa na każdej platformie, m.in. PrestaShop, Shopify, WooCommerce, Shoper, IdoSell i Magento. Studio Creative Vision Marcina Bednarza ma status PrestaShop Expert.\\n\\nKontakt: kontakt@uxaudyt.pl, +48 534 154 230. Usługę prowadzi Marcin Bednarz Creative Vision, NIP 7952514299, Rzeszów. Praca zdalna, klienci z całej Polski.\\n\\n## Usługi\\n- [Audyt UX sklepu internetowego](https://www.uxaudyt.pl/audyt-sklepu-internetowego): 2990 zł netto, raport w 5 dni roboczych\\n- [Audyt UX strony internetowej](https://www.uxaudyt.pl/audyt-strony-internetowej): 1990 zł netto, strony firmowe do ok. 20 podstron\\n- [Audyt sklepu z opieką przy wdrożeniu](https://www.uxaudyt.pl/audyt-sklepu-z-opieka): 4490 zł netto, warsztat, makiety krytycznych poprawek i 30 dni wsparcia\\n- [Wdrożenie poprawek](https://www.uxaudyt.pl/wdrozenie-poprawek): projekt w Figmie i wdrożenie, wycena po raporcie\\n- [Bezpłatna wstępna ocena sklepu](https://www.uxaudyt.pl/darmowy-audyt-sklepu): odpowiedź e-mailem, zwykle w ciągu 2 dni roboczych\\n- [Przykładowy raport z audytu UX](https://www.uxaudyt.pl/przykladowy-raport): przykład poglądowy, sklep z kosmetykami\\n\\n## Poradniki\\n- [Audyt UX: co to jest, jak wygląda i ile kosztuje](https://www.uxaudyt.pl/audyt-ux)\\n- [Audyt UX a audyt SEO](https://www.uxaudyt.pl/audyt-ux-a-audyt-seo)\\n- [Niska konwersja sklepu: przyczyny i jak je znaleźć](https://www.uxaudyt.pl/niska-konwersja-sklepu)\\n- [Porzucone koszyki: dlaczego klienci nie kupują](https://www.uxaudyt.pl/porzucone-koszyki)\\n- [Karta produktu: checklista 20 punktów](https://www.uxaudyt.pl/karta-produktu-checklista)\\n- [UX sklepu na telefonie](https://www.uxaudyt.pl/ux-sklepu-mobilnego)\\n- [Jak samodzielnie sprawdzić UX sklepu w 30 minut](https://www.uxaudyt.pl/jak-sprawdzic-ux-sklepu)\\n- [Jak zwiększyć sprzedaż w sklepie internetowym](https://www.uxaudyt.pl/jak-zwiekszyc-sprzedaz-sklepu): 12 poprawek, najpierw sklep, potem ruch\\n- [Checklista audytu UX sklepu: 25 punktów](https://www.uxaudyt.pl/checklista-audytu-ux): otwarta lista do samodzielnego sprawdzenia\\n- [Audyt UX sklepu na PrestaShop](https://www.uxaudyt.pl/audyt-ux-prestashop)\\n- [Audyt UX sklepu na Shopify](https://www.uxaudyt.pl/audyt-ux-shopify)\\n- [Audyt UX sklepu na WooCommerce](https://www.uxaudyt.pl/audyt-ux-woocommerce)\\n- [Audyt UX sklepu na Shoperze](https://www.uxaudyt.pl/audyt-ux-shoper)\\n\\n## Optional\\n- [Regulamin](https://www.uxaudyt.pl/regulamin): zakres usług, płatność, terminy, gwarancja zwrotu\\n- [Polityka prywatności](https://www.uxaudyt.pl/polityka-prywatnosci)\\n- [Creative Vision](https://creative-vision.pl): studio projektowe stron, sklepów i aplikacji, Rzeszów\\n"
}''')

files = {}
def get(f):
    if f not in files:
        files[f] = open(os.path.join(ROOT, f), encoding='utf-8').read()
    return files[f]
def put(f, t):
    files[f] = t

log = {'applied': 0, 'skipped': 0}
def fail(msg):
    sys.exit('BŁĄD: ' + msg)

def sub(text, old, new, count, label):
    """Zwraca nowy tekst albo ten sam (gdy już zastosowano)."""
    n = text.count(old)
    if new in text and (old in new or n == 0):
        log['skipped'] += 1
        return text
    if n != count:
        fail('%s: stary literał występuje %d razy (oczekiwano %d): %r' % (label, n, count, old[:90]))
    log['applied'] += 1
    return text.replace(old, new)

# --- obiekty poradników Z[key] w V7Home.mjs ---
def skip_str(t, i):  # t[i] == '`'
    i += 1
    while t[i] != '`':
        i += 2 if t[i] == '\\' else 1
    return i + 1
def match_close(t, i, op, cl):  # t[i] == op
    depth = 0
    while True:
        ch = t[i]
        if ch == '`':
            i = skip_str(t, i); continue
        if ch == op: depth += 1
        elif ch == cl:
            depth -= 1
            if depth == 0: return i
        i += 1
def span(t, key):
    z = t.find('Z={"darmowy-audyt-sklepu":{')
    if z < 0: fail('nie znaleziono obiektu Z')
    s = t.find('"%s":{' % key, z)
    if s < 0: fail('brak poradnika ' + key)
    b = s + len(key) + 3
    return b, match_close(t, b, '{', '}') + 1

def guide_edit(key, fn):
    f = 'src/c/V7Home.mjs'
    t = get(f)
    a, b = span(t, key)
    put(f, t[:a] + fn(t[a:b]) + t[b:])

def el(s):
    if '`' in s or '${' in s: fail('niedozwolony znak w tekście: ' + s[:60])
    return '`' + s + '`'

for op in DATA['ops']:
    k = op['op']; label = op.get('id', '')
    if k == 'rep':
        put(op['file'], sub(get(op['file']), op['old'], op['new'], op['count'], label))
    elif k == 'grep':
        guide_edit(op['key'], lambda s: sub(s, op['old'], op['new'], 1, label + ' [' + op['key'] + ']'))
    elif k == 'gins':
        def f(s):
            new = ','.join(el(x) for x in op['lines'])
            if el(op['lines'][0]) in s:
                log['skipped'] += 1; return s
            anc = el(op['after'])
            if s.count(anc) != 1: fail('%s: kotwica %d razy: %r' % (label, s.count(anc), op['after'][:80]))
            log['applied'] += 1
            return s.replace(anc, anc + ',' + new)
        guide_edit(op['key'], f)
    elif k == 'gfaq':
        def f(s):
            item = '[' + el(op['q']) + ',' + el(op['a']) + ']'
            if el(op['q']) in s:
                log['skipped'] += 1; return s
            i = s.rfind('faq:[')
            if i < 0: fail(label + ': brak faq')
            i += 4
            end = match_close(s, i, '[', ']')
            items, j = [], i + 1
            while j < end:
                if s[j] == '[':
                    e = match_close(s, j, '[', ']'); items.append((j, e + 1)); j = e + 1
                else:
                    j += 1
            pos = op['pos']
            if pos == 'end' or (isinstance(pos, int) and pos >= len(items)):
                at = end; ins = (',' if items else '') + item
            else:
                at = items[pos][0]; ins = item + ','
            log['applied'] += 1
            return s[:at] + ins + s[at:]
        guide_edit(op['key'], f)
    elif k == 'yfaq':
        f = 'src/c/V7Home.mjs'; t = get(f)
        i = t.find(',Y=`') + 4; j = t.index('`', i)
        new = op['text'].replace('\n', '\\n')
        if t[i:j] == new: log['skipped'] += 1
        else:
            log['applied'] += 1; put(f, t[:i] + new + t[j:])
    elif k == 'newguides':
        f = 'src/c/V7Home.mjs'; t = get(f)
        if '"jak-zwiekszyc-sprzedaz-sklepu":{' in t:
            log['skipped'] += 1
        else:
            t = sub(t, '}},Xe=[', '},' + ','.join(op['objs']) + '},Xe=[', 1, label)
            put(f, t)
    else:
        fail('nieznana operacja ' + k)

# --- build.mjs: kopiowanie src/llms.txt do public/ ---
put('build.mjs', sub(get('build.mjs'),
    "fs.copyFileSync(path.join(ROOT, 'src/404.html'), path.join(OUT, '404.html'));\n",
    "fs.copyFileSync(path.join(ROOT, 'src/404.html'), path.join(OUT, '404.html'));\nfs.copyFileSync(path.join(ROOT, 'src/llms.txt'), path.join(OUT, 'llms.txt'));\n", 1, 'build-llms'))

# --- props.json ---
raw = get('src/props.json')
P = json.loads(raw)
PR = DATA['props']
def deep(v):
    if isinstance(v, str):
        for o, n in PR['rep']:
            if o in v and n not in v: v = v.replace(o, n)
        return v
    if isinstance(v, list): return [deep(x) for x in v]
    if isinstance(v, dict): return {a: deep(b) for a, b in v.items()}
    return v
P = deep(P)
for key in PR['newpages']:
    if key not in P:
        P[key] = copy.deepcopy(P['audyt-ux-shopify'])
        P[key]['main'][0]['page'] = key
for key, v in P.items():
    m = (v.get('main') or [None])[0]
    if not m or 'faq' not in m: continue
    which = PR['faq'].get(key, PR['faq']['*guides*'])
    m['faq'] = DATA['faq'][which]
for key, v in P.items():
    for m in (v.get('main') or []):
        if 'linkedin' in m and not m['linkedin']: m['linkedin'] = PR['linkedin']
put('src/props.json', json.dumps(P, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''))

# --- meta.json ---
raw = get('src/meta.json')
M = json.loads(raw)
for key, (title, desc) in DATA['meta'].items():
    if key not in M:
        M[key] = {'title': '', 'description': '', 'canonical': 'https://www.uxaudyt.pl/' + key,
                  'og_image': '/img/L7tYwRG1Z2LDw2rf7ooJXDB5gU.png', 'robots': 'max-image-preview:large', 'ldjson': []}
    if title: M[key]['title'] = title
    if desc: M[key]['description'] = desc
put('src/meta.json', json.dumps(M, ensure_ascii=False, indent=1) + ('\n' if raw.endswith('\n') else ''))

# --- llms.txt ---
put('src/llms.txt', DATA['llms'])
put('public/llms.txt', DATA['llms'])

for f, t in files.items():
    p = os.path.join(ROOT, f)
    old = open(p, encoding='utf-8').read() if os.path.exists(p) else None
    if old != t:
        open(p, 'w', encoding='utf-8').write(t)
        print('zapisano', f)
print('zastosowano: %(applied)d, pominięto (już było): %(skipped)d' % log)
