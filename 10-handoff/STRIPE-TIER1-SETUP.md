# Stripe Setup — Vacature Intake Mastery (€97)

> Click-by-click instructie voor Wouter. Tijd: ~25 minuten. Stripe-account: Recruitin BV (al actief, live mode).
> Resultaat: één werkende `https://buy.stripe.com/xxxxx` betaal-link die op de Tier 1 landingspagina geplakt wordt.

---

## 0. Voorbereiding (1 min)

- Log in op https://dashboard.stripe.com → check rechtsboven dat je in **Live mode** zit (toggle staat AAN), en dat het account "Recruitin B.V." is.
- Zorg dat **Customer Portal** + **Tax** features beschikbaar zijn — wordt al gebruikt voor DGR/KT/APK dus dat zit goed.

---

## 1. Product aanmaken (3 min)

1. Linkernavigatie → **Producten** → **Productcatalogus**.
2. Rechtsboven blauwe knop **+ Product toevoegen**.
3. Velden invullen:
   - **Naam**: `Vacature Intake Mastery`
   - **Beschrijving**: `90 minuten 1-op-1 online sessie. We bouwen samen je eerste vacature volgens de Engineering Stack 2026: rol-functie-bonus framework, ICP-mapping, salarismatrix en intake-checklist. Inclusief opname + werkdocument. 7 dagen geld-terug-garantie.`
   - **Afbeelding**: optioneel — upload het Tier-1 hero visual van de landing page als je die bij de hand hebt (geen blocker).
4. **Prijsinformatie**:
   - Prijsmodel: **Standaard prijsbepaling**
   - Prijs: `97,00`
   - Valuta: **EUR**
   - Type: **Eenmalig** (NIET terugkerend)
5. **Belastinggedrag** (rechtskolom, klap "Geavanceerd" open):
   - Toggle **Stripe Tax** AAN (als nog niet globaal aan staat: linkernavigatie → **Meer** → **Tax** → activeer voor NL).
   - Belastinggedrag: **Inclusief btw** (€97 = bruto, klant ziet €97 totaal, jij krijgt €80,17 netto + €16,83 btw NL 21%).
   - Tax-categorie: **Diensten** → **Algemene professionele diensten** (`txcd_20030000`). Niet "Software" of "Consulting" — Stripe NL UI vraagt expliciete categorie.
6. Knop rechtsonder **Product opslaan**.

→ Je belandt op de productpagina. Noteer/kopieer het **prijs-ID** (begint met `price_…`) — heb je niet meteen nodig maar handig voor evt. webhook later.

---

## 2. Payment Link maken (8 min)

1. Linkernavigatie → **Betaal-links** (onder "Producten").
2. Rechtsboven blauwe knop **+ Nieuwe betaal-link**.
3. **Productselectie**:
   - Klik **Bestaand product toevoegen** → zoek "Vacature Intake Mastery" → selecteer → **Toevoegen**.
   - Aantal: **1** · Vink **NIET** "Klant kan aantal aanpassen" aan.
4. **Type**: **Producten of abonnementen verkopen** (default).
5. **Opties** (klap elke sectie open via pijltje):

   ### 5a. Belasting & valuta
   - Stripe Tax: **AAN** (volgt productinstelling).
   - Valuta: **EUR** (locked).

   ### 5b. Betaalmethoden
   - **Kaart**: AAN (default).
   - **iDEAL**: AAN — klik in lijst, vink aan. Cruciaal voor NL conversie.
   - **SEPA-incasso**: AAN — voor zakelijke klanten die liever via bankafschrift.
   - **Bancontact**: AAN (BE-traffic, lage kosten).
   - **Apple Pay / Google Pay**: AAN (mobiele conversie).
   - 3D Secure: laat **Standaard (Stripe Radar)** staan — geen handmatige override.

   ### 5c. Velden bij afrekenen
   - **Klant-gegevens**: e-mailadres = verplicht (default).
   - Telefoonnummer (Stripe-veld) = vraag in custom field hieronder ipv het Stripe-veld → uit laten staan.
   - Factuuradres = **Verzamel volledig adres** (voor btw-factuur).
   - Naam factuur = **AAN** (verplicht voor zakelijke factuur).

   ### 5d. Aangepaste velden (klik **+ Veld toevoegen** — 3x)
   1. **Veld 1**:
      - Type: **Tekst** · Label: `Telefoonnummer` · Optioneel: **AAN** · Max tekens: 30
   2. **Veld 2**:
      - Type: **Tekst** · Label: `Bedrijf` · Optioneel: **AAN** · Max tekens: 100
   3. **Veld 3**:
      - Type: **Tekst** · Label: `Vacature waar je nu mee zit (URL of korte beschrijving)` · Optioneel: **UIT (verplicht)** · Max tekens: 1000
      - Helptekst onder veld: `Plak de vacature-URL of de tekst van de huidige vacature. We gebruiken dit als startpunt voor de sessie.`

   ### 5e. Na betaling
   - Optie: **Doorverwijzen naar je eigen website**.
   - URL na succes:
     ```
     https://recruitmentengineer.nl/vacature-intake-mastery?status=success&session_id={CHECKOUT_SESSION_ID}
     ```
     LET OP: `{CHECKOUT_SESSION_ID}` is letterlijk een Stripe template-token — exact zo overtypen, met accolades. Stripe vervangt dit per transactie.
   - Annulering-URL (klap "Geavanceerd" open): `https://recruitmentengineer.nl/vacature-intake-mastery?status=cancel`

   ### 5f. Bevestigingspagina (zelfde "Na betaling" sectie)
   - Wisselaar **Bevestigingsbericht weergeven** = AAN (komt samen met redirect).
   - Bericht-tekst:
     ```
     Betaling gelukt — welkom bij Vacature Intake Mastery.

     Boek nu direct je 90-min sessie via Calendly:
     👉 https://calendly.com/wouter-arts-/vacature-intake-mastery-90min

     Je krijgt binnen 5 min ook een bevestiging op je e-mail. Bekijk al vast de Stack 2026 PDF voorbereiding zodat we tijdens de sessie direct aan de slag kunnen.

     Tot snel — Wouter Arts
     ```
     LET OP: vervang de Calendly-URL pas zodra File 2 (CALENDLY-VIM-EVENT-SETUP.md) is uitgevoerd en je de echte event-link hebt.

   ### 5g. Geavanceerd
   - **Promotiecodes toepassen**: AAN (handig voor early-bird kortingen later).
   - **Limiteer aantal**: laat leeg — geen hard cap op betalingen (Calendly stuurt op 4 slots/maand).
   - **Verzamel adres voor verzending**: UIT (digitale dienst).

6. Rechtsonder **Betaal-link maken**.

→ Je krijgt nu een URL in de vorm `https://buy.stripe.com/xxxxxxxxxxxx` (12-char ID). **Kopieer deze URL** — die heb je in stap 4 nodig.

---

## 3. Webhook (optioneel, aanbevolen — 5 min)

> Voor latere Pipedrive-deal-creation via Vercel Function. Skip nu en kom later terug als de Vercel-endpoint nog niet bestaat.

1. Linkernavigatie → **Ontwikkelaars** → **Webhooks**.
2. **+ Eindpunt toevoegen**.
3. Eindpunt-URL: `https://recruitmentengineer.nl/api/stripe-webhook` (placeholder — moet nog gebouwd worden).
4. Beschrijving: `VIM Tier 1 — Pipedrive deal creation`.
5. Te verzenden gebeurtenissen → **+ Gebeurtenissen selecteren** → zoek en vink AAN:
   - `checkout.session.completed`
   - `charge.refunded` (voor refund-tracking)
6. **Eindpunt toevoegen** → kopieer de **Signing secret** (begint met `whsec_…`) en bewaar in `~/recruitin/.env` als `STRIPE_VIM_WEBHOOK_SECRET=…`.

---

## 4. Refund-policy instellen (2 min)

1. Linkernavigatie → **Instellingen** (tandwiel rechtsboven) → **Bedrijfsinstellingen** → **Klanten** → **Restitutiebeleid**.
2. **Restitutie-tekst** (komt op Stripe-receipt):
   ```
   7 dagen no-questions geld-terug-garantie. Mail warts@recruitin.nl en je krijgt het volledige bedrag teruggestort binnen 5 werkdagen.
   ```
3. **Opslaan**.

Refunds doe je handmatig vanuit de Payments-tabel (Klant niet tevreden? → klik op betaling → **Restitueren** → kies "Volledig" → bevestig). Stripe sturen een automatische refund-receipt.

---

## 5. Landingspagina updaten (3 min)

Dit is de cruciale stap — zonder dit wijst de knop naar `mailto:` fallback.

Open `/Users/wouterarts/projects/recruitmentengineer/06-landing-page/public/vacature-intake-mastery.html` in je editor.

### 5a. Stripe-URL invullen

Zoek (Cmd+F) `STRIPE_CHECKOUT_URL = ""` (regel 1005). Vervang door:

```javascript
const STRIPE_CHECKOUT_URL = "https://buy.stripe.com/PLAK-HIER-JE-ECHTE-LINK"; // ← gevuld op {DATUM}
```

### 5b. Dev-banner uitzetten

Zoek `data-live="false"` (regel 583). Vervang door `data-live="true"`. De gele waarschuwingsbanner verdwijnt direct.

### 5c. Commit + push

```bash
cd /Users/wouterarts/projects/recruitmentengineer
git add 06-landing-page/public/vacature-intake-mastery.html
git commit -m "Tier 1 VIM — Stripe payment link live"
git push
```

Vercel auto-deployt binnen ~60 sec → check op `https://recruitmentengineer.nl/vacature-intake-mastery` dat de gele banner weg is en de knop nu naar `buy.stripe.com` linkt.

---

## 6. Test-checklist (5 min)

Werk deze 5 stappen exact af voor je de link extern deelt:

1. **Test mode submission** — switch Stripe-dashboard naar **Test mode** (toggle rechtsboven), maak in test mode een identieke betaal-link aan, doe een betaling met testkaart `4242 4242 4242 4242` (elke datum, elke CVC). Check dat de redirect naar `/vacature-intake-mastery?status=success&session_id=cs_test_…` werkt en de Calendly-tekst zichtbaar is op de bevestigingspagina.
2. **Real mode €97** — schakel terug naar **Live mode**, doe één echte betaling van €97 met je eigen creditcard naar `warts@recruitin.nl`. Check de receipt-mail, check dat de €97 in je Stripe-balance verschijnt (mag je later naar jezelf restitueren als test).
3. **Pipedrive deal** — als je de webhook in stap 3 hebt geconfigureerd: check Pipedrive pipeline 14 (of waar VIM-deals binnenkomen) of er een nieuwe deal staat met de juiste contact-naam + €97 waarde. Skip als webhook nog niet live is.
4. **Pixel `Purchase` event** — open https://business.facebook.com/events_manager → kies de Recruitin pixel (`238226887541404`) → tab **Test events** → genereer test-link → bezoek `https://recruitmentengineer.nl/vacature-intake-mastery?status=success&session_id=cs_test_x` met de test-link parameters. Check dat het `Purchase` event arriveert met value `97.00` en currency `EUR`.
5. **Calendly embed** — op de Stripe success-pagina (binnen Stripe-domein, vóór redirect) check dat de Calendly-link in de bevestigingstekst klikbaar is en in een nieuw tab de juiste event-page opent (`Vacature Intake Mastery — 90 min`).

---

## 7. Edge cases & noten

- **iDEAL** is na 1 sept 2026 verplicht via NL Adyen-pipeline → Stripe regelt dit automatisch zolang Stripe Tax actief is. Geen actie.
- **SEPA-incasso** geeft 1-3 dagen vertraging tot betaling settled. Calendly-confirmation wordt direct getriggerd door Stripe success-redirect — dus klant boekt slot voordat geld binnen is. Risico is laag (€97), accepteer dit.
- **3D Secure** triggert bij ~30% van NL-creditcards. Geen actie nodig — Stripe handelt af.
- **Promotiecodes** kun je later genereren via Producten → product-pagina → tab **Coupons** → **+ Coupon**. Standaard codes: `EARLYBIRD20` (-20%) of `BETA50` (-50% voor eerste 5 klanten).
- **Refund > 7 dagen na aankoop** = bespreek individueel, geen automatische policy. Stripe staat refunds 180 dagen toe.
- **Btw-factuur**: Stripe genereert automatisch een PDF-factuur met "Recruitin B.V. — KvK 75303647 — BTW NL860230533B01" mits je deze gegevens onder Instellingen → Bedrijfsinstellingen → Belasting hebt staan. Verifieer voor je live gaat.

---

## Klaar

Tijd-investering totaal: ~25 min. Volgende stap = `CALENDLY-VIM-EVENT-SETUP.md` (gelijktijdig of na deze doc).
