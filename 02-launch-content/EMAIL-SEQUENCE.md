# 📧 NEWSLETTER FOLLOW-UP SEQUENCE
## Stack 2026 — Lead Nurture (Day 0 → Day 8)

> **Doel:** Lead magnet downloads omzetten in betalende klanten of warm pipeline  
> **Format:** 4 mails over 8 dagen — Welcome + 3 nurture + soft offer  
> **Tooling:** Resend transactional + Pipedrive sync via `/api/subscribe`  
> **Tone:** Direct, geen hype, één punt per mail

---

## 🎯 SEQUENCE OVERZICHT

| Mail | Day | Doel | Type | CTA |
|------|-----|------|------|-----|
| 1 | 0 | Deliver PDF | Welcome + bijlage | Open PDF |
| 2 | 2 | Diepgang Module 1 | Story + tip | Reply if vraag |
| 3 | 5 | Case story €519k | Klantcase | Reply if interesse |
| 4 | 8 | Tier 1 offer | Soft pitch €97 workshop | Boek slot |

**Verwacht conversie pad:**
- 100 downloads
- 60% opent mail 2 (Day 2)
- 35% opent mail 3 (Day 5)  
- 25% opent mail 4 (Day 8)
- 3-5% boekt €97 workshop = 3-5 betalende klanten per 100 leads

---

## 📩 MAIL 1 — WELCOME (DAY 0)

**Trigger:** Direct na form submit  
**Status:** ✅ Al geïmplementeerd in `/api/subscribe.js`  
**Subject:** `📥 Recruitment Engineering Stack 2026 — jouw download`

---

## 📩 MAIL 2 — DAY 2 — BOOLEAN STORY

**Trigger:** 48 uur na download  
**Subject options (A/B test):**
- A: `Hoe ik 4 uur boolean searches naar 25 minuten bracht`
- B: `De fout die 90% van de recruiters maakt met boolean`
- C: `Module 1 in actie — concreet voorbeeld Veco`

**Aanbevolen winnaar:** B (curiosity gap > info delivery)

### Body:

```
Hi,

2 dagen geleden downloadde je de Stack 2026.

Vraag: heb je Prompt 1 al getest? (Boolean Search Engineer)

Zo niet — geen oordeel. Ik schrijf deze mail omdat 90% van de recruiters
één specifieke fout maakt met boolean searches die alles onnodig moeilijk
maakt.

De fout: ze beginnen met "wat staat er in de vacature".

Dat klinkt logisch. Maar de vacature beschrijft de IDEALE kandidaat. Niet
de daadwerkelijk vindbare kandidaat op LinkedIn.

Concreet voorbeeld van vorige week — Veco besturingstechnicus:

Vacature zei: "Senior Besturingstechnicus, 5+ jaar S7 ervaring".

Eerste boolean (vacature-driven):
("Senior Besturingstechnicus" OR "Senior Control Engineer") AND "Siemens S7"

Resultaten: 47 kandidaten. Te weinig.

Tweede boolean (skill-driven, zoals Prompt 1 leert):
("S7-1500" OR "TIA Portal" OR "Step7") AND ("PLC" OR "besturing")

Resultaten: 312 kandidaten. Veel beter.

Het verschil: niemand noemt zichzelf "Senior Control Engineer" op LinkedIn.
Mensen schrijven over de TOOLS waar ze mee werken.

Tip voor jouw volgende search:
Run Prompt 1 met je vacature, maar voeg deze regel toe aan de prompt:
"Geef 3 booleans: één skill-driven, één titel-driven, één bedrijfs-driven.
Vergelijk verwachte match counts."

De skill-driven wint in 80% van mijn searches.

Vragen? Reply gewoon — ik lees alle mails zelf.

Wouter

PS: Als je deze mail nuttig vond, weet dan dat ik elke 2 dagen één
specifieke trick uit de Stack uitlicht. Geen filler.
```

---

## 📩 MAIL 3 — DAY 5 — PIPELINE STORY (€519K CASE)

**Trigger:** 5 dagen na download  
**Subject options (A/B):**
- A: `Hoe ik €519.000 stuck pipeline weer in beweging kreeg`
- B: `Het ergste pipeline-probleem dat ik ooit zag (en hoe ik het oploste)`
- C: `60% recovery in 90 dagen — case story`

**Aanbevolen winnaar:** A (specifiek bedrag = scroll-stopper)

### Body:

```
Hi,

Vorig jaar belde een tech-klant me. Ik kende ze via via, en ze waren
ten einde raad.

Hun probleem: 6 maanden stilstand in hun recruitment pipeline. €519.000
aan stuck deals in Stage 2. Vacatures die maar niet vol kwamen. Klanten
die begonnen te morren.

De directeur zei letterlijk: "Wouter, ik weet niet eens meer waar ik moet
beginnen."

Hier is wat ik deed in 30 minuten:

1. Pipedrive export gevraagd
2. Run Prompt 5 (Pipeline Health Diagnostician — staat in jouw PDF)
3. Output gelezen

De diagnose:

72% van de stuck deals zat vast op één specifiek punt — de transitie
van "Eerste interview gepland" naar "Tweede interview gepland".

Niet sourcing (zoals iedereen dacht). Niet salaris (zoals de directeur
gokte). Niet de markt.

Het was de eerste interview ZELF.

Hiring managers gaven feedback van 3-5 dagen later, vaak via een 2-zinnen
mail. Kandidaten waren tegen die tijd al weggekaapt door concurrentie.

De fix (3 acties per stuck deal, allemaal door Prompt 5 gegenereerd):

1. Hiring manager: 24h-rule afgesproken voor feedback (geen 5 dagen)
2. Recruiter: kandidaat krijgt na elke interview een "wat-nu" mail binnen
   2 uur (warm houden)
3. Klant-quote toegevoegd aan elke pipeline-rapport ("hiring manager 
   commitment")

Resultaat 90 dagen later:
- 60% van de €519k pipeline weer in beweging
- 7 hires gerealiseerd uit deals die "dood" leken
- Klant verlengde contract met 18 maanden

Het hele verhaal staat niet in deze mail. Ik schrijf er nu een uitgebreide
case-study over.

Maar de tool zit al in jouw PDF. Module 5 — Pipeline Health Diagnostician.

Vraag voor jou: heb jij een vergelijkbaar probleem? €X aan stuck deals
waarvan je niet weet waar ze hangen?

Reply met "Pipeline check" en ik kijk er gratis 30 min naar voor je.
Geen verkoop-agenda — gewoon kijken of ik kan helpen.

Wouter

PS: Deze 3-stappen recovery is letterlijk de output van Prompt 5 op de
echte data. Niets verzonnen.
```

---

## 📩 MAIL 4 — DAY 8 — SOFT OFFER €97 WORKSHOP

**Trigger:** 8 dagen na download  
**Subject options:**
- A: `Wil je dat ik dit live met je doe? (€97 Vacature Intake Mastery)`
- B: `1 vacature, 90 minuten, samen — €97`
- C: `Kleine workshop voor wie verder wil (geen €5k)`

**Aanbevolen winnaar:** B (prijs vooraf = filtert juiste mensen)

### Body:

```
Hi,

Het is 8 dagen geleden sinds je de Stack 2026 downloadde.

Misschien heb je de prompts al gebruikt. Misschien zit de PDF nog
ongeopend in je Downloads.

Beide is okay. Zo gaat dat met PDF's.

Maar voor wie het écht praktisch wil maken — en niet eerst een €5.000
strategie-traject met me wil — heb ik iets ontwikkeld:

VACATURE INTAKE MASTERY · 90 minuten · €97

Wat we doen:
- Jij stuurt vooraf 1 echte vacature waar je nu mee zit
- We doen samen het intake-proces (Prompt 3 uit de Stack)
- Ik laat zien hoe ik in 30 min een vacature uitwerk inclusief
  ICP, sourcing-strategie en 5 interview-vragen
- Je krijgt het complete vacature-pakket mee — direct uitvoerbaar

Voor wie:
- Recruiters bij tech bedrijven die 1-2 vacatures per maand zelf doen
- Hiring managers die het externe bureau willen overslaan
- Mensen die de Stack hebben gelezen en denken: "ik wil dit live zien"

Niet voor:
- Mensen die theorie zoeken (lees PDF)
- Bureaus die competitive intelligence zoeken
- Mensen die niet bereid zijn aan eigen pipeline te werken

Ik doe deze sessie 4x per maand, 1-op-1, online.

Hier boek je een slot: https://calendly.com/wouter-arts-/recruitment-apk-advies

Geen pushy follow-up als je niet boekt. Dit is mijn laatste mail in deze
serie.

Wat wel komt: 1 mail per week met 1 trick uit mijn praktijk. Schrijf je
uit als het niet bevalt.

Wouter

PS: Mocht je liever direct met Recruitin samenwerken voor een complete
vacature-traject, mail dan warts@recruitin.nl. Daar regelen we het
zonder workshop.
```

---

## 🛠 IMPLEMENTATIE — RESEND BROADCASTS

Resend heeft een Broadcasts feature. Setup:

### Stap 1: Audience aanmaken
```
Audience name: "Stack 2026 Leads"
```

### Stap 2: Bij subscribe.js — voeg lead toe aan audience
Update `/api/subscribe.js` met extra Resend-call na email-send:

```javascript
// Add to Resend audience for nurture sequence
await fetch(`https://api.resend.com/audiences/${RESEND_AUDIENCE_ID}/contacts`, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${RESEND_API_KEY}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: email,
    first_name: email.split('@')[0],
    unsubscribed: false
  })
});
```

### Stap 3: Schedule broadcasts in Resend dashboard
- Mail 2: Schedule 48h na audience-add (op delay basis)
- Mail 3: 5 dagen
- Mail 4: 8 dagen

⚠️ **Resend heeft geen native delay-trigger.** Je hebt twee opties:

**Optie A — Simpel:** Verstuur mail 2/3/4 handmatig wekelijks naar nieuwe leads van die week. Laatste 7 dagen filter.

**Optie B — Geautomatiseerd:** Gebruik Zapier/Make:
- Trigger: New Resend audience contact
- Wait 48h → Send mail 2 via Resend API
- Wait 3 days → Send mail 3
- Wait 3 days → Send mail 4

Voor fase 1 (eerste 50 leads): Optie A is prima. Schaal later naar B.

---

## 📊 KPI TARGETS

Voor de eerste 100 leads, meet:

| Metric | Target | Actie als <target |
|--------|--------|-------------------|
| Open rate Mail 1 | >70% | Subject lijn aanpassen |
| Open rate Mail 2 | >50% | Day-2 te vroeg, schuif naar Day 3 |
| Open rate Mail 3 | >35% | Subject van Mail 3 minder cliché |
| Open rate Mail 4 | >25% | Te commercieel, soften offer |
| Reply rate Mail 3 | >5% | "Pipeline check" CTA niet duidelijk genoeg |
| Conversie Mail 4 → boeking | >2% | Workshop-formaat aanpassen |

---

## 🚨 DELIVERABILITY CHECKS

Voor je deze sequence live zet:

✓ Domein `recruitmentengineer.nl` geverifieerd in Resend (DKIM + SPF + DMARC)  
✓ `from:` = `wouter@recruitmentengineer.nl`  
✓ `reply_to:` = `warts@recruitin.nl` (zodat replies in jouw mailbox komen)  
✓ Unsubscribe-link in elke mail (Resend voegt automatisch toe)  
✓ Plain-text alternatief naast HTML (Resend doet dit auto)  
✓ Test eerst zelf: stuur naar 3 eigen email-adressen (gmail, outlook, eigen)  
✓ Check spam-score op mail-tester.com (target: 9+/10)

---

## 📝 NOTITIES VOOR LATER

### Sequence v2 (na 100 leads, week 6+):
- Splits doelgroep: HR Director vs Recruiter vs Hiring Manager (verschillende mail 4)
- Voeg Mail 5 toe: case study volledig (PDF van €519k pipeline recovery)
- Mail 6: gebruik LinkedIn DM ipv email voor warmere leads
- A/B test subjectlines op cohort-basis

### Sequence v3 (maand 3+):
- Branched: bij reply mail 3 → andere flow (warm)
- Bij open zonder click mail 4 → re-engagement
- Cohort tagging in Pipedrive (Authority Lead → Stack 2026)

---

> **Status:** ✅ v1.0 Productie-klaar — schrijven  
> **Deploy:** Wacht op Resend domein-verificatie (recruitmentengineer.nl)  
> **Owner:** Ing. W. Arts · Recruitin B.V.
