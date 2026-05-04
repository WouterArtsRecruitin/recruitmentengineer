# Calendly Setup — Vacature Intake Mastery (90 min)

> Click-by-click instructie voor Wouter. Tijd: ~20 minuten. Calendly-account: warts@recruitin.nl (al actief).
> Resultaat: één werkende event-link `https://calendly.com/wouter-arts-/vacature-intake-mastery-90min` die in de Stripe-bevestigingspagina geplakt wordt (zie `STRIPE-TIER1-SETUP.md` stap 2 sectie 5f).

---

## 0. Voorbereiding (2 min)

- Log in op https://calendly.com → check rechtsboven dat je in `wouter-arts-` workspace zit.
- **Zoom-integratie** verifiëren: linkernavigatie → **Integrations** → **Conferencing** → check dat **Zoom** als "Connected" staat (groen vinkje). Zo niet → klik **Connect** → log in op Zoom → autoriseer Calendly → klaar. Zonder Zoom auto-link kun je geen `Location: Zoom` instellen op de event.
- **Tijdzone-default**: linkernavigatie → **Account** → **Account settings** → check dat **Timezone** = `Europe/Amsterdam (UTC+1)`. Cruciaal voor de availability-rules hieronder.

---

## 1. Event-type aanmaken (3 min)

1. Linkernavigatie → **Event types** → blauwe knop rechtsboven **+ Create**.
2. Kies **One-on-One**.
3. Velden:
   - **Event name**: `Vacature Intake Mastery — 90 min`
   - **Location**: dropdown → kies **Zoom** (Calendly maakt automatisch een unieke Zoom-link per booking).
   - **Description / Instructions** (verschijnt in confirmation-email):
     ```
     90 minuten 1-op-1. Wij bouwen samen je eerste vacature volgens de Engineering Stack 2026 — rol-functie-bonus framework, ICP-mapping, salarismatrix.

     Voor we beginnen:
     1. Stuur de vacature-URL of de tekst van de vacature in via het formulier hieronder
     2. Lees de Stack 2026 PDF (gestuurd in de welkomsmail van Stripe)

     Tot snel — Wouter
     ```
   - **Event link** (URL-suffix onderaan): wijzig naar `vacature-intake-mastery-90min` zodat de full URL `https://calendly.com/wouter-arts-/vacature-intake-mastery-90min` wordt.
   - **Event color**: pick **Custom** → plak hex `#FF6B1A` (oranje, brand-match Recruitment Engineer).
4. **Next** → naar de uitgebreide settings.

---

## 2. Scheduling instellingen (5 min)

### 2a. Duration

- **Event duration**: `90 minutes` (custom value invullen — niet de default 30/60/90 keuzes; gebruik 90 exact).

### 2b. Date range

- **Date range**: **Indefinitely into the future**, met **Rolling 60 days** (klanten kunnen 60 dagen vooruit boeken).

### 2c. Availability

- **Availability schedule**: **Custom** → klik **+ Create new schedule** → naam: `VIM Slots`.
- Per dag invullen:
  - **Mon-Fri**: `09:00 — 12:30` AND `13:30 — 17:00` (twee blokken per dag, lunchpauze geblokt).
  - **Sat-Sun**: **Unavailable** (toggle uit).
- **Time zone**: `Europe/Amsterdam`.
- **Save** schedule → terug naar event-type → kies `VIM Slots` als active schedule.

### 2d. Booking limits (cruciaal voor 4 slots/maand cap)

Klik tab **Booking limits**:

- **Max events per day**: `1` — enforce.
- **Max events per week**: `1` — enforce. (4 weken × 1/week = 4 sessies/maand cap zonder hard maandelijks limit nodig)
- **Buffer time before event**: `30 minutes` (mentale prep + setup).
- **Buffer time after event**: `60 minutes` (notes uitwerken + Pipedrive update).
- **Minimum scheduling notice**: `2 days` (klanten kunnen niet morgen al boeken — geeft prep-tijd).
- **Start time increments**: `30 minutes`.

→ Resultaat: per geboekte sessie wordt 30 + 90 + 60 = **3 uur 30 min** geblokt op de kalender. Met 1/dag + 1/week cap kom je rond ~4 sessies/maand uit.

### 2e. Time zone display

- **Display time zones for invitee**: AAN — toon klant tijden in zijn lokale TZ (default Calendly-gedrag).

---

## 3. Custom questions (3 min)

Tab **Invitee questions** → standaard staan er 2 vragen (Name, Email). Klik **+ Add new question**:

### Vraag 1
- **Question**: `Heb je de Stack 2026 PDF gedownload en gelezen?`
- **Answer type**: **One line**
- Note: Calendly heeft geen native ja/nee-veld — gebruik **Phone** is overkill, dus eenvoudige tekst werkt het best (klant typt "ja" of "nee"). Alternatief: gebruik **Multiple choice** met opties `Ja, helemaal door` / `Ja, oppervlakkig` / `Nog niet — ga ik voor de sessie doen`.
- **Required**: AAN.

### Vraag 2
- **Question**: `Stuur je vacature-URL of plak de tekst van de vacature waar we mee aan de slag gaan (verplicht — anders kunnen we de sessie niet voorbereiden)`
- **Answer type**: **Multiple lines**
- **Required**: AAN.

### Vraag 3
- **Question**: `Wat is de kern-uitdaging die je hoopt op te lossen in deze sessie?`
- **Answer type**: **Multiple lines**
- **Required**: AAN.

→ **Save**.

---

## 4. Notifications & emails (5 min)

Tab **Notifications and workflows** → klik op elk template om te bewerken:

### 4a. Confirmation email (zodra klant boekt)

Subject: `Bevestigd: VIM-sessie {{Event date and time}} — even voorbereiden`

Body (~150 woorden, brand-voice):
```
Hi {{Invitee first name}},

Geboekt: {{Event date and time}}, 90 min via Zoom. Link staat in deze mail én in je agenda-uitnodiging.

Twee dingen voor de sessie:

1. Stack 2026 PDF lezen (10 min — krijg je in de welkomsmail van Stripe)
2. Je vacature-tekst aanleveren — als je die nog niet via het Calendly-formulier hebt gedeeld, mail die nu naar warts@recruitin.nl

We gaan tijdens de 90 min concreet werken: rol-functie-bonus uitschrijven, ICP mappen, salaris-spread checken, intake-checklist invullen. Geen theorie-praatje. Notes + werkdocument krijg je achteraf.

Annuleren of verzetten kan tot 24 uur voor de sessie via de link onderin deze mail. Daarna is de sessie verloren — graag dezelfde dag laten weten als er iets tussenkomt zodat ik mijn agenda kan herplannen.

Tot dan,
Wouter Arts
Recruitment Engineer
```

### 4b. Reminder email (24h voor sessie)

Subject: `Morgen 11:00 — VIM-sessie`

Body (~30 woorden):
```
Hi {{Invitee first name}},

Morgen {{Event date and time}}. Vacature-link al ingestuurd? Zo niet → mail nu naar warts@recruitin.nl, anders begin ik blind.

Zoom-link in agenda-uitnodiging.

Tot morgen,
Wouter
```

Trigger-tijd: **24 hours before event**.

### 4c. Cancellation policy

Tab **Cancellation policy** (in workflow-overzicht):
```
Annuleren of verzetten kan tot 24 uur voor de sessie. Binnen 24 uur is het slot helaas verloren — €97 wordt niet teruggestort tenzij het écht overmacht is. Mail in dat geval direct warts@recruitin.nl.
```

(Dit is een softere policy dan strict no-refund — geeft je marge om in echte uitzonderingen toch coulance te tonen.)

→ Save alle workflows.

---

## 5. Embed-link kopiëren (1 min)

1. Terug naar event-type overzicht → klik op **Vacature Intake Mastery — 90 min**.
2. Bovenaan staat **Share** → klik → **Copy link**.
3. URL is iets als `https://calendly.com/wouter-arts-/vacature-intake-mastery-90min`.
4. **Plak deze URL** in de Stripe payment-link confirmation-text (zie `STRIPE-TIER1-SETUP.md` stap 2 sectie 5f, regel die nu een placeholder bevat).

---

## 6. Verify-checklist (5 min)

Werk deze 4 stappen af voordat de Stripe-link extern wordt gedeeld:

1. **Test booking in incognito** — open een incognito-tab → bezoek `https://calendly.com/wouter-arts-/vacature-intake-mastery-90min` → boek een test-slot voor jezelf op een vrij moment. Vul de 3 custom questions in. Submit. Check dat je een confirmation-mail krijgt op je test-email binnen 30 sec.
2. **Zoom-link auto-generated** — open de confirmation-mail. Check dat er een **unieke Zoom-meeting URL** in staat (vorm: `https://zoom.us/j/xxxxxxxxxxx?pwd=…`). Klik de link en check dat hij naar een werkende Zoom-room navigeert (host = jij). Als de link niet automatisch is gegenereerd → terug naar Integrations → Zoom → Disconnect + Reconnect.
3. **Confirmation email landed** — check dat de NL-tekst die je in stap 4a invulde in de mail staat (geen Calendly-default-Engels). Reminder pas testen door 24u te wachten of de event-tijd op +25u te zetten en handmatig een trigger te forceren via Workflows → "Send test now".
4. **Cancellation flow** — klik in de confirmation-mail op **Cancel**. Geef "test annulering" als reden. Check dat je een cancellation-mail krijgt EN dat het slot weer vrij staat in de Calendly-kalender. Daarna kun je het test-event helemaal verwijderen via Calendly dashboard → **Scheduled events** → **Past** → vind je test → **Delete**.

---

## 7. Klaar

Calendly-event live op `https://calendly.com/wouter-arts-/vacature-intake-mastery-90min`. Plak deze URL nu in de Stripe payment-link confirmation-tekst (zie `STRIPE-TIER1-SETUP.md` stap 2 sectie 5f) en re-save de Stripe payment-link. Daarna is de complete Tier 1-flow live: landing → Stripe → success-page met Calendly → boeking → confirmation-mail.

Tijd-investering totaal: ~20 min.
