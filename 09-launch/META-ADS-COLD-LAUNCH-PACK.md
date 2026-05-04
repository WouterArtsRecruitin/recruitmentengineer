# 🎯 Meta Ads Cold-Launch Pack — €25/d 7-day baseline test

> **Doel:** in 7 dagen voldoende Lead-event signal verzamelen (≥30 leads) om Meta's Lead-optimization stabiel te laten draaien, zonder budget te verbranden op zwakke clicks.
>
> **Context:** Stack 2026 PDF lead-magnet is live (recruitmentengineer.nl). Pixel `238226887541404` vuurt `PageView`, `ViewContent`, `Lead`, `StackPDFRequest`. Optimizatie LOCKED op `Lead` event (zie `08-tracking-setup/meta-pixel-events.md`).
>
> **Wat je doet:** copy-paste deze setup in Ads Manager → laat 7 dagen draaien → na 7 dagen check de KPI-cutoffs onderin → schalen of pauzeren.
>
> **Wat je NIET doet:** geen LANDING_PAGE_VIEWS-warmup, geen LINK_CLICKS-optimalisatie, geen ThruPlay. Direct op Lead.

---

## 0. Pre-flight check (10 min, voor je launcht)

- [ ] Pixel `238226887541404` actief op recruitmentengineer.nl — check via Meta Pixel Helper Chrome extension
- [ ] `Lead` event vuurt op test-submit — submit met `+test01@…` email, check Events Manager → Test Events
- [ ] Custom Conversion `Stack2026Download` aangemaakt (Events Manager → Custom Conversions → "+ Create" → source: pixel `238226887541404`, rule: URL contains `recruitmentengineer.nl` AND event = Lead) — niet strikt nodig voor optimalisatie maar wel voor reporting
- [ ] Domain verified onder Recruitin Business Manager (avoids iOS 14.5 attribution loss)
- [ ] Aggregated Event Measurement priority: Lead = priority 1 (Events Manager → AEM)
- [ ] Ad-account: `act_1236576254450117` (Recruitin BV) — check spending limit ≥ €175 voor 7d test
- [ ] Page: Recruitin BV `660118697194302` — bevestig dat user (Wouter) admin-rechten heeft

---

## 1. Campaign

| Setting | Value |
|---------|-------|
| Campaign name | `RE-COLD-Stack2026-T1-Launch-week1` |
| Buying type | Auction |
| Objective | **Sales** (kies "Sales" — dit ontgrendelt OFFSITE_CONVERSIONS optimization op Lead event) |
| Special ad categories | None |
| Campaign budget optimization | **OFF** (CBO uit — we runnen budget op ad-set-niveau voor controle) |
| A/B test | Off |
| Advantage campaign budget | Off |

> ⚠️ **Niet Leads-objective kiezen.** "Leads"-campagnes optimaliseren op on-platform Instant Forms — wij willen offsite Lead-events vanuit onze landing.

---

## 2. Ad Sets — 3 stuks parallel

### Ad-set A: NL Hot 30 (broad cold)

| Setting | Value |
|---------|-------|
| Name | `AS-A-NL-Hot30-Lead7d` |
| Daily budget | **€10** |
| Schedule | Start tomorrow 09:00 NL — Run continuously |
| Performance goal | **Maximize number of conversions** |
| Conversion event | `Lead` (uit pixel `238226887541404`) |
| Conversion location | Website |
| Conversion window | **7-day click + 1-day view** |
| Cost per result goal | Empty (manual bid uit) |
| Audience | Saved audience "NL-Hot30" — zie spec hieronder |
| Placements | **Advantage+ Placements ON** (Meta kiest mix FB/IG/Reels/Stories) |
| Languages | Dutch (NL), English (EN) |
| Advantage detailed targeting | OFF (ICP is smal — laat algoritme niet expanden in week 1) |
| Advantage audience | OFF (zelfde reden — pas activeren na 30+ leads) |

**Saved audience "NL-Hot30":**
```
Geo: Netherlands
Age: 25–55
Gender: All
Detailed targeting INCLUDE (any of):
  Recruitment (industry)
  Human resources (industry)
  Talent acquisition (interests)
  LinkedIn Recruiter (interests)
  Recruitment agency (interests)
  Sourcing (recruiting) (interests)
Detailed targeting NARROW (must also match any of):
  Job title: Recruiter, Senior Recruiter, Talent Acquisition Specialist,
             HR Manager, HR Business Partner, Hiring Manager,
             Engineering Recruiter, Technical Recruiter
Languages: Dutch, English
Exclude: Recruitin BV employees + Stack-Downloaders-30d (Custom Audience #6)
```

---

### Ad-set B: NL Tech Decision Makers (mid-market)

| Setting | Value |
|---------|-------|
| Name | `AS-B-NL-TechDM-Lead7d` |
| Daily budget | **€10** |
| Performance goal | Maximize number of conversions |
| Conversion event | `Lead` |
| Conversion window | 7-day click + 1-day view |
| Audience | Saved "NL-TechDM-50to800fte" — zie hieronder |
| Placements | Advantage+ |
| Languages | Dutch, English |

**Saved audience "NL-TechDM-50to800fte":**
```
Geo: Netherlands — Gelderland, Overijssel, Noord-Brabant
       (kerngebied per brand-bible — uitbreiden naar landelijk in week 2 als CPL stabiel)
Age: 30–60
Gender: All
Detailed targeting INCLUDE:
  Job title: CEO, CTO, COO, HR Director, VP HR,
             Chief People Officer, Managing Director,
             General Manager
Detailed targeting NARROW (must match):
  Industry: Manufacturing, Industrial automation, Mechanical engineering,
            Maintenance & repair, Information technology
  Employer size: 50–1000 employees
Exclude: Recruitin BV employees + Stack-Downloaders-30d
```

---

### Ad-set C: NL Engineering Heavy (LinkedIn-active)

| Setting | Value |
|---------|-------|
| Name | `AS-C-NL-EngHeavy-Lead7d` |
| Daily budget | **€5** |
| Performance goal | Maximize number of conversions |
| Conversion event | `Lead` |
| Conversion window | 7-day click + 1-day view |
| Audience | Saved "NL-EngHeavy" — zie hieronder |

**Saved audience "NL-EngHeavy":**
```
Geo: Netherlands
Age: 28–55
Gender: All
Detailed targeting INCLUDE (any of):
  Job title: Mechanical Engineer, Electrical Engineer, PLC Programmer,
             Automation Engineer, Industrial Engineer, Process Engineer,
             Technical Recruiter, Engineering Recruiter
  Interests: LinkedIn (engagement-based), Engineering professional development,
             Industry 4.0, IoT engineering
Exclude: Recruitin BV employees + Stack-Downloaders-30d
```

---

## 3. Creatives — 4 ads, 2 per ad-set rotation

> **Render volgorde:** P1, P4, P8 (Higgsfield batch-1) zijn de drie kern-images. Voeg P11 toe als carousel-cover als je wilt testen of carousel beter presteert dan static.

### Ad 1 — Manifesto Static (image only)

| Field | Value |
|-------|-------|
| Format | Single image |
| Image | `02-higgsfield-assets/quote-cards/P9-manifesto-bold.jpg` (GEEN VACATURES. EEN SYSTEEM.) |
| Primary text | (1300 chars max — kies één hieronder, A/B test 2-3 varianten) |
| Headline (40 chars) | `5 prompts voor recruitment in 2026` |
| Description (30 chars) | `Gratis PDF · ~12 minuten lezen` |
| Destination | Website |
| URL | `https://recruitmentengineer.nl?utm_source=meta&utm_medium=cpc&utm_campaign=stack2026-launch&utm_content=ad1-manifesto&utm_term={{adset.name}}` |
| Call-to-action | `Download` |

**Primary-text variant A (brutaal-direct):**
```
Ik ben ingenieur. En recruiter.

In 8 jaar bij Veco, Beutech en Euromaster heb ik 47 prompts ontwikkeld voor
recruitment-werk. 23 zijn waardeloos. 5 zijn productie-klaar.

Die 5 zitten in de Stack 2026.

Download de PDF (12 pagina's, ~12 min lezen). Geen webinar.
Geen agency-pitch.

— Ing. W. Arts
```

**Primary-text variant B (numerical hook):**
```
47 prompts getest. 23 ervan zijn waardeloos.

Maar 5 leverden me €519k aan pipeline-recovery in 1 quarter bij Veco.

Die 5 staan in de Stack 2026 — gratis PDF voor recruiters & hiring
managers in tech.

Geen agency-pitch. Geen webinar. Eén PDF, 12 minuten.
```

---

### Ad 2 — Production Hall hero (image)

| Field | Value |
|-------|-------|
| Format | Single image |
| Image | `02-higgsfield-assets/hero-portraits/P4-production-hall.jpg` |
| Primary text | (zie variant C hieronder) |
| Headline | `Recruitment Engineering Stack 2026` |
| Description | `5 productie-prompts · gratis PDF` |
| URL | `…&utm_content=ad2-production-hall…` |
| CTA | `Download` |

**Primary-text variant C (story-led):**
```
Een vacature van Veco bleef 6 maanden open staan.
3 bureaus eraan begonnen, alle 3 gestopt.

Ik heb hem ingevuld in 4 weken. Met deze 5 prompts.

Download de Stack 2026 — concrete prompts die ik vandaag nog
gebruik op opdrachten voor maak- en techbedrijven.
```

---

### Ad 3 — Numerical hook (image)

| Field | Value |
|-------|-------|
| Format | Single image |
| Image | `02-higgsfield-assets/quote-cards/P8-numerical-hook.jpg` (47 prompts. Hier zijn er 5.) |
| Primary text | Variant B (zie boven, alternative met andere opening) |
| Headline | `47 prompts. 5 die werken.` |
| Description | `Download Stack 2026 — gratis` |
| URL | `…&utm_content=ad3-numerical…` |
| CTA | `Download` |

---

### Ad 4 — Carousel (4 slides, optional als batch-1 P11 klaar)

| Field | Value |
|-------|-------|
| Format | Carousel (4 cards) |
| Cover | `P11-reverse-engineering.jpg` |
| Card 2 image | `P5-blueprint-table.jpg` — text: "Module 1: Boolean Engineer" |
| Card 3 image | `P12-multi-monitor.jpg` — text: "Module 3: Vacature Intake" |
| Card 4 image | `P9-manifesto-bold.jpg` — text: "Download de PDF →" |
| Each card link | recruitmentengineer.nl + UTM |
| Primary text | Variant B |
| CTA | `Download` |

---

### Distribution per ad-set

| Ad | Ad-set A (Hot30) | Ad-set B (TechDM) | Ad-set C (EngHeavy) |
|----|------------------|--------------------|----------------------|
| Ad 1 manifesto | ✅ | ✅ | ✅ |
| Ad 2 production hall | ✅ | ✅ | — |
| Ad 3 numerical | ✅ | — | ✅ |
| Ad 4 carousel | — | ✅ | ✅ |

> Doel: 2-3 ads per ad-set zodat algoritme creative-rotatie kan doen. Niet meer dan 4 — je verlamt learning-phase met te veel varianten op €5-10/d.

---

## 4. Budget & timeline

| Day | Cumulative spend | Expected leads | Expected CPL | Notes |
|-----|------------------|----------------|--------------|-------|
| 1   | €25              | 0–2            | n/a          | Learning phase opstart — geen acties |
| 3   | €75              | 3–8            | €9–15        | Halverwege — geen acties tenzij CPL > €40 |
| 5   | €125             | 8–15           | €8–12        | Eerste variant-pause-beslissing mogelijk |
| 7   | €175             | 15–30          | €6–10        | **End of test** — KPI-cutoffs toepassen |

**Variabelen:**
- Hogere CPL (€15-25) is normaal in learning-phase. Sluit pas af bij CPL > €40 op dag 3.
- Lager budget (€10/d total ipv €25) → schaal expectations met factor 0.4 (en verlangt ook 14d ipv 7d test).

---

## 5. Day-7 KPI cutoffs (beslismatrix)

Na 7 dagen, check de cijfers in Ads Manager → check per ad-set:

| Metric | Schaal-up | Houden | Pauzeer |
|--------|-----------|--------|---------|
| **CPL (cost per Lead)** | < €8 | €8–€20 | > €20 |
| **CTR (link click rate)** | > 1.5% | 0.8–1.5% | < 0.8% |
| **Leads (totaal in 7d)** | > 8 | 4–8 | < 4 |
| **Conversion rate (LP-views → Lead)** | > 8% | 4–8% | < 4% |

**Decision tree per ad-set:**
- 3× **schaal-up** → +50% budget, runtime 14d (of activeer Advantage+ audience expansion)
- 2× schaal + 1× houden → +25% budget, run nog 7d
- 2× houden + 1× pauzeer → no-change, run nog 7d met variant-rotatie
- 2× pauzeer → kill ad-set; schuif budget naar best-performing ad-set
- 3× pauzeer → kill campagne, herzien creatives + audience

**Ad-level beslissing (binnen ad-set):**
- Top-performer: ≥ 50% van leads in ad-set → houden
- Bottom-performer: ≤ 10% van leads na 5+ days → pauzeer
- Mid: laat draaien tot dag 14, dan opnieuw beoordelen

---

## 6. Lookalike-launch — wacht-criteria

**Audience #4 — Lookalike 1% Stack-Downloaders:**

Activeer pas wanneer Custom Audience "RE-MOFU-Stack-Downloaders-30d" ≥ 100 conversies bevat. Verwacht: einde week 4-5 bij €25/d.

Wanneer ≥ 100 leads:
1. Ads Manager → Lookalikes → Create
2. Source: `RE-MOFU-Stack-Downloaders-30d`
3. Country: NL
4. Lookalike size: 1% (smallest = highest match-quality)
5. Naam: `RE-T1-LAL-1%-StackDL-NL`
6. Voeg toe als 4e ad-set parallel aan A/B/C met €10/d → 7d test → KPI-cutoffs

---

## 7. Daily monitoring (5 min per dag)

**Ads Manager → Campaigns → filter laatste 7 dagen:**

```
RE-COLD-Stack2026-T1-Launch-week1
├── AS-A-NL-Hot30-Lead7d        → Spend / Leads / CPL / CTR
├── AS-B-NL-TechDM-Lead7d       → Spend / Leads / CPL / CTR
└── AS-C-NL-EngHeavy-Lead7d     → Spend / Leads / CPL / CTR
```

**Direct alert-triggers (overweeg pauze, niet auto-pause):**
- CPL > €30 op dag 3+ in een ad-set
- Frequency > 4.0 in 7 dagen (audience-fatigue → variant-swap nodig)
- CTR < 0.5% op enige ad (creative kapot)
- Spend ≥ €30/dag op 1 ad-set zonder Lead (algoritme zit vast)

---

## 8. Naming conventions (vasthouden vanaf launch)

```
Campaign:      RE-COLD-Stack2026-T1-Launch-{weekN}
Ad-set:        AS-{A,B,C}-{audience-shorthand}-Lead{Nd}
Ad:            AD-{adsetletter}{N}-{creative-shorthand}-{variantA/B/C}
UTM source:    meta
UTM medium:    cpc
UTM campaign:  stack2026-launch
UTM content:   {ad-shorthand}
UTM term:      {{adset.name}}  (Meta auto-fills)
```

---

## 9. Cross-references

- **Pixel-events spec:** `08-tracking-setup/meta-pixel-events.md` — exact event payloads + AD-SET OPTIMIZATION RULE
- **Audience architecture:** `08-tracking-setup/meta-audiences-architecture.md` — alle 15 audiences (TOFU/MOFU/BOFU)
- **UTM scheme:** `08-tracking-setup/utm-scheme.md`
- **Creative source files:** `02-higgsfield-assets/HIGGSFIELD-BATCH-1-PROMPTS.md`
- **Pipedrive lead-handling:** `08-tracking-setup/pipedrive-pipeline-mapping.md` (pipeline 16, stage 222 = "New Lead — Stack PDF")

---

## ⚠️ Quirks per `feedback_meta_api_quirks_2026.md`

- **`url_tags`** moet op ad-level (`PATCH /v19.0/{AD_ID}`), NIET op creative — anders silent ignore
- **`targeting.exclusions.interests`** is deprecated → gebruik `targeting.flexible_spec` met negative filters
- **`advantage_audience` flag** verplicht sinds v19.0 — zonder flag worden ad-sets silent rejected (we hebben Advantage+ Audience expressies UIT, maar de flag MOET aanwezig)
- **Pixel ID:** `238226887541404` (gedeelde Recruitin pixel). NIET `660118697194302` (= FB Page ID, geen pixel — silent fail patroon)

Setup via Ads Manager UI vermijdt al deze API-quirks. Doe deze launch via UI, niet API.

---

## ✅ Launch checklist

- [ ] Pre-flight check (§0) volledig groen
- [ ] Higgsfield batch-1 P1, P4, P8, P9, P11 gerenderd & opgeslagen
- [ ] Campaign + 3 ad-sets aangemaakt in Ads Manager
- [ ] Per ad-set 2-3 ads gepubliceerd met UTM + correcte CTA
- [ ] Custom Audience "RE-MOFU-Stack-Downloaders-30d" actief (zie meta-audiences-architecture.md §6)
- [ ] Eerste 24u monitoring-call ingeplant in agenda voor dag 2
- [ ] Day-7 review-moment ingeplant in agenda
