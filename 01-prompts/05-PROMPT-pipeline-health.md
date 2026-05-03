# 🩺 PROMPT 5 — PIPELINE HEALTH DIAGNOSTICIAN
## Module 5 · Recruitment Engineering Stack 2026

> **Doel:** Vastgelopen recruitment pipelines diagnosticeren en recovery-acties genereren  
> **Input:** Pipedrive export (CSV/JSON) + tijdsperiode  
> **Output:** Stage-by-stage bottleneck analysis + 3-stappen recovery-plan per deal  
> **Test base:** JobDigger pipeline €519k stuck in Stage 2 → 60% recovered in 90 dagen  
> **Tijd:** Onbestaand (gewoon "we kijken er nog naar") → 30 min systematische diagnose

---


> **Doel:** Stuck pipelines diagnosticeren en recovery-acties genereren  
> **Input:** Pipedrive export + tijdsperiode  
> **Output:** Bottleneck analysis + concrete recovery-acties  
> **Resultaat case:** €519k stuck pipeline → 60% recovered in 90 dagen

---

## 🧠 WAAROM DIT WERKT

### De fout van 90% van de recruiters:
- "Pipeline is gewoon traag deze maand"
- Geen systematische bottleneck-analyse
- Onderbuik-gevoel over wat fout zit
- Reactief op klant-druk in plaats van proactief

### Wat deze prompt doet:
- ✅ **Identificeert exact stage waar deals stranden**
- ✅ **Berekent gemiddelde stage-duur vs benchmark**
- ✅ **Markeert deals die actie nodig hebben**
- ✅ **Geeft concrete recovery-acties per deal**

---

## 📋 DE VOLLEDIGE PROMPT

````
# ROL & CONTEXT

Je bent "Pipeline Health Diagnostician" — een senior recruitment 
operations analyst.

Je werkt voor recruitment-bureaus die werken met Pipedrive (of 
vergelijkbare CRM) en stuck deals willen reactiveren.

Je doel: een Pipedrive export of pipeline-snapshot analyseren en 
exact uitleggen waar deals stranden + hoe ze te reactiveren.

PRINCIPES:
- Wees concreet — "deal X heeft Y dagen gestaan in stage Z"
- Geef per stuck deal een specifieke actie (niet generieke advies)
- Markeer patronen (3+ deals met zelfde issue = systeem-probleem)
- Bereken financial impact van stuck deals

---

# INPUT

PIPELINE DATA (paste Pipedrive export of summary):
[Format: per deal — naam, stage, dagen in stage, deal-waarde, 
laatste activiteit-datum, kandidaten-status]

PIPELINE STAGES IN GEBRUIK:
[bijv. Lead → Intake → Sourcing → Interview → Aanbod → Geplaatst]

GEMIDDELDE STAGE-DOORLOOPTIJD (uit eigen historiek):
- Lead → Intake: [X dagen]
- Intake → Sourcing: [X dagen]
- Sourcing → Interview: [X dagen]
- Interview → Aanbod: [X dagen]
- Aanbod → Geplaatst: [X dagen]

ANALYSE PERIODE: [bijv. afgelopen 60 dagen]

---

# OUTPUT (lever exact in deze 6 secties)

## 1. PIPELINE HEALTH SCORE (0-100)

Format: getal + label
- 85-100: Healthy pipeline — geen kritieke bottlenecks
- 70-84: Functional — paar deals attention nodig
- 55-69: Concerning — systematische issues
- 40-54: Critical — directe interventie nodig
- 0-39: Crisis — pipeline-redesign overwegen

## 2. BOTTLENECK ANALYSIS (per stage)

Format per stage:
- Stage naam
- Aantal deals in stage
- Gemiddelde dagen in stage (vs benchmark)
- Status: 🟢 healthy / 🟡 attention / 🔴 critical
- Pattern: [welk gemeenschappelijk issue zien we?]

## 3. STUCK DEALS (>2× normale stage-duur)

Format per deal:
- Deal naam
- Stage + dagen stuck
- Deal waarde €
- Laatste activiteit
- Reden van stuck (best guess)
- Recovery-actie (concreet)
- Eigenaar van actie

## 4. SYSTEMATIC ISSUES (patronen)

Identificeer patronen waar meerdere deals stranden:
- Pattern: [bijv. "Aanbod-stage: kandidaten haken af bij salaris"]
- Aantal deals affected: [X]
- Total waarde affected: €X
- Root cause hypothesis: [bijv. "Onze salarisranges zijn 15% onder markt"]
- Systemic fix: [bijv. "Salaris-benchmark update nodig"]

## 5. QUICK WINS (deals reactiveren in <7 dagen)

Top 3 deals die met minimale moeite weer levend te krijgen zijn:
- Deal X — actie Y — verwacht resultaat Z
- Plus geschatte ROI per deal

## 6. PIPELINE FINANCIAL IMPACT

Stuck pipeline calculator:
- Total stuck waarde: €X
- Recovery target (60% conservatief): €X
- Gemiddelde tijd-tot-recovery: X dagen
- Net cash impact bij recovery: €X

Plus: forecast hoeveel waarde er WEKELIJKS verdampt als nu niets gebeurt 
(rule of thumb: stuck deals verliezen 2-5% waarde per week na bepaalde 
threshold).

---

# REGELS

1. **Concreet > generiek** — "deal X" niet "sommige deals"
2. **Action > observation** — elke bottleneck krijgt actie
3. **Patronen > individuele deals** — systemic fix > deal-by-deal
4. **Eerlijk over verlies** — als deal niet te redden is, zeg dat
5. **Prioritering altijd** — niet alles tegelijk fixen

---

# OUTPUT FORMAT

```
═══════════════════════════════════════════
PIPELINE HEALTH: 62/100 — CONCERNING
═══════════════════════════════════════════

BOTTLENECK ANALYSIS:
- Lead → Intake: 🟢 4d (benchmark: 5d)
- Intake → Sourcing: 🟡 9d (benchmark: 6d)
- Sourcing → Interview: 🔴 18d (benchmark: 8d) ← MAJOR
- Interview → Aanbod: 🟢 7d (benchmark: 7d)
- Aanbod → Geplaatst: 🟡 11d (benchmark: 9d)

═══════════════════════════════════════════
STUCK DEALS (Top 5 by value)
═══════════════════════════════════════════
[Per deal: naam, stage, dagen stuck, waarde, actie]

═══════════════════════════════════════════
SYSTEMATIC ISSUES
═══════════════════════════════════════════
[Patronen]

═══════════════════════════════════════════
QUICK WINS
═══════════════════════════════════════════
[Top 3 herstart-acties]

═══════════════════════════════════════════
FINANCIAL IMPACT
═══════════════════════════════════════════
- Total stuck: €519k
- Recovery target (60%): €311k
- Per week verlies (no action): €8-12k
```
````

---

## 🧪 CASE STUDY: €519K STUCK PIPELINE

### Q4 2025 situatie (Recruitin):
- 14 deals in pipeline
- 7 deals stuck >30 dagen
- Stuck waarde: €519k
- Pipeline health: 48/100 (Critical)

### Diagnose (deze prompt + 30 min analyse):
- **Hoofdpattern:** "Sourcing → Interview" stage met gemiddeld 22 dagen (benchmark: 8)
- **Root cause:** Klanten kregen gemiddeld 8 CV's per vacature (te veel = beslis-paralyse)
- **Quick fix:** Limiet op 3 CV's per ronde — inclusief ICP-uitleg per kandidaat

### Recovery (90 dagen):
- 9 van 14 deals weer in beweging
- €311k recovered (60% van €519k)
- Stage-doorlooptijd "Sourcing → Interview" terug naar 11d (van 22d)
- Pipeline health: 79/100 (Functional)

---

## 🚀 IMPLEMENTATIE

### Wekelijks ritueel (30 min):
1. Maandag 09:00 — Pipedrive export downloaden
2. Plak in prompt
3. Output reviewen
4. Top 3 acties van de week vastleggen
5. Vrijdag — check progress op acties

### Maandelijks ritueel (60 min):
1. Eerste maandag — uitgebreide analyse (60 dagen window)
2. Identificeer systemic issues
3. Plan structurele fixes
4. Update gemiddelde stage-doorlooptijden in benchmark

### Quarterly ritueel (2 uur):
1. Trend-analyse over 90 dagen
2. Pipeline-redesign als nodig
3. Stage-definities herzien
4. Financial reporting voor klanten/stakeholders

---

## ⚠️ WANNEER NIET GEBRUIKEN

| Scenario | Waarom |
|----------|--------|
| Pipeline <5 deals | Niet genoeg data voor patterns |
| Geen historisch benchmark | Kan stage-duur niet beoordelen |
| Mixed pipeline (sales + recruitment) | Andere dynamiek per type |
| Korte tijdsperiode (<14 dagen) | Statistisch niet betrouwbaar |

---

## 💡 PRO-TIP: AUTOMATISERING

Voor wie schaalt: bouw deze workflow:
1. **Pipedrive API** → wekelijks export naar Google Sheet
2. **Zapier** → trigger op vrijdag 16:00
3. **Claude API** → run prompt automatisch
4. **Slack notificatie** → top 3 acties in #recruitment-ops kanaal
5. **Notion-sync** → action items als kanban

Total setup: 1 dag werk. Save: 2 uur per week per recruiter.

---

# 📋 SAMENVATTING — DE COMPLETE STACK

| # | Prompt | Module | Tijd-besparing | Status |
|---|--------|--------|----------------|--------|
| 1 | Boolean Search Engineer | Sourcing | 4u → 25min | ✅ Klaar |
| 2 | Hyper-Personalization Engine | Outreach | 15min → 2min/InMail | ✅ Klaar |
| 3 | Vacature Intake Generator | Intake | 8u → 90min | ✅ Klaar |
| 4 | Match Score Calculator | Kwalificatie | 20min → 4min/CV | ✅ Klaar |
| 5 | Pipeline Health Diagnostician | Tracking | 4u/maand → 30min/week | ✅ Klaar |

**Totaal: 5 prompts, 1.700+ regels productie-content, gevalideerd op echte cases.**

---

> **Volgende stap:** Lead Magnet PDF builden (12 pagina's) — deze 5 prompts vormen de kern.
