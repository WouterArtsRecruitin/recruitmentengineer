# Prompt — Pipedrive Deal-note Update na meeting/call

**When:** Direct na elke prospect-meeting, klantcall of strategische intake. CRM-hygiëne.
**Format:** Pipedrive note · structured, machine-readable + human-readable
**Tone-mix:** Engineer logisch — geen marketing-speak. Feiten + intent + next action.
**Output length:** 200-400 woorden, structured per blok

---

## System prompt

```
Je schrijft een Pipedrive deal-note voor een Recruitin-deal na een meeting/call.

Doel: 6 maanden later moet je (of een collega/AI) deze note kunnen lezen en de
context binnen 30 sec begrijpen. Geen verhaal, wel feiten + interpretatie.

Format-rules:
- Machine-readable header voor latere AI-aggregatie
- Human-readable body voor jezelf
- Geen interpretatie zonder bron — als je iets gokt, label het als [GOK]
- Cijfers altijd specifiek (€-bedragen, FTE-aantallen, deadline-data)
- Klantnamen + jobtitels exact zoals genoemd (typo-vrij)

Standaard-template:
1. METADATA — datum / type / aanwezigen
2. CONTEXT — waar deze deal nu staat
3. KEY POINTS — bullet-lijst, max 7 items
4. PAIN-DIAGNOSIS — wat is het echte probleem (mijn interpretatie)
5. NEXT ACTION — concrete actie + deadline + owner
6. RISK FLAGS — wat kan misgaan
```

## Variables

- `{{DEAL_NAME}}` — Pipedrive deal-naam
- `{{COMPANY}}` — bedrijfsnaam
- `{{CONTACT}}` — naam + functie van contact
- `{{MEETING_TYPE}}` — intake / strategie / proposal-review / kick-off / status
- `{{KEY_TAKEAWAYS}}` — ruwe punten uit de meeting
- `{{NEXT_ACTION}}` — concrete vervolgstap

## User-prompt template

```
Schrijf een Pipedrive deal-note van een meeting met `{{COMPANY}}`.

Deal: {{DEAL_NAME}}
Contact: {{CONTACT}}
Meeting-type: {{MEETING_TYPE}}
Datum: <auto-fill datetime>

Ruwe takeaways:
{{KEY_TAKEAWAYS}}

Vervolg-actie:
{{NEXT_ACTION}}

Output volgt het standaard-template (METADATA / CONTEXT / KEY POINTS / PAIN /
NEXT ACTION / RISK FLAGS). Engineer-logisch tone, geen marketing.
```

## Sample input + output

**Input:**
- DEAL_NAME = "Beutech — 2 vacatures Q3"
- COMPANY = Beutech
- CONTACT = Mark de Vries, HR Manager
- MEETING_TYPE = intake
- KEY_TAKEAWAYS:
  - Twee vacatures: 1× besturingstechnicus S7, 1× projectleider automation
  - Boolean search heeft 6 weken gedraaid bij ander bureau, 4 reacties
  - Salarisrange klopt niet met markt (5% onder benchmark)
  - Mark zegt "we hebben tijd tot eind Q3, anders escaleert het bij directie"
  - Hiring manager (Tom) was niet aanwezig
- NEXT_ACTION = Stuur Vacature Intake Engineer-output binnen 48u, stel call met Tom voor

**Output:**

```
═══════════════════════════════════
[BEUTECH-2026Q3-INTAKE-001]
═══════════════════════════════════

METADATA
Datum: 2026-06-04
Type: Intake meeting
Aanwezig: Wouter Arts (Recruitin), Mark de Vries (Beutech HR Manager)
Afwezig (relevant): Tom Janssen (Beutech Hiring Manager)
Deal: Beutech — 2 vacatures Q3
Stage: 1 (Intake)
Verwachte waarde: €18k (twee vacatures × €9k bureaufee)

—

CONTEXT
Beutech zoekt al 6 weken via een ander bureau zonder resultaat (4 reacties op 200+ outreaches). Mark wil "een andere aanpak" en heeft Recruitin gevraagd voor een second opinion / takeover.

—

KEY POINTS
1. Vacature 1: Senior Besturingstechnicus, S7-1500 + TIA Portal vereist, locatie Tilburg.
2. Vacature 2: Projectleider Automation, MBO+/HBO, ervaring leiding 3-5 engineers.
3. Bestaand bureau: 200+ generieke InMails, 4 reacties, 0 op gesprek.
4. Salarisrange: €4.200-4.800 (besturingstechnicus). [GOK] Volgens mijn benchmark uit Veco-data dit jaar zit dat 5-7% onder markt voor S7-1500 senior-niveau.
5. Deadline: eind Q3 (sept 30, 2026). Daarna escalatie naar directie.
6. Tom (hiring manager) was niet aanwezig — Mark sprak namens hem. [RISK]
7. Beutech wil eerst zien wat ik kan voor ze starten met formal opdracht.

—

PAIN-DIAGNOSIS
Probleem is NIET sourcing-volume. Probleem is sourcing-precisie + outreach-kwaliteit + waarschijnlijk salaris.
- Sourcing: bestaand bureau zoekt op job-title ("Senior Besturingstechnicus"), terwijl talent op LinkedIn op tools schrijft (S7-1500, TIA Portal).
- Outreach: 200 generieke InMails op cold-LI = 8% benchmark, dit krijgt 2%.
- Salaris: 5% onder benchmark = automatische self-filter voor de juiste kandidaten.

—

NEXT ACTION
1. ✅ Vandaag: Vacature Intake Engineer (Module 3) draaien op huidige Beutech vacaturetekst → upgrade-versie. Deadline: 6 juni 2026 18:00.
2. ✅ 6 juni: Output sturen naar Mark + voorstel call met Tom inplannen.
3. ⏳ Week 24: Tom-call beleggen (intake vol).
4. ⏳ Week 25: Boolean Search Engineer + 30 InMails → eerste batch kandidaten.
Owner: Wouter Arts.

—

RISK FLAGS
- Tom (hiring manager) niet betrokken in intake → kandidaten kunnen later afgewezen worden zonder dat ik weet waarom.
- Salaris-mismatch: als Beutech salarisrange niet wil aanpassen, blijft pool klein.
- Bestaand bureau staat nog op deal — concurrent in lopende search.
- Eind Q3 deadline = 4 maanden = krap voor 2 vacatures, zeker bij salaris-friction.

—

Tags: #beutech #q3-2026 #intake-done #s7-1500 #automation
```

## Edit-checklist

- [ ] Header met machine-leesbare deal-ID
- [ ] METADATA blok compleet (datum, type, aanwezigen)
- [ ] KEY POINTS max 7 bullets
- [ ] PAIN-DIAGNOSIS gemarkeerd als interpretatie (niet als feit)
- [ ] [GOK] of [RISK] labels gebruikt waar nodig
- [ ] NEXT ACTION concreet (deadline + owner)
- [ ] RISK FLAGS apart blok
- [ ] Cijfers specifiek (geen "ongeveer" zonder bron)
- [ ] Tags onderaan voor latere filter
- [ ] Geen Aebi Schmidt
- [ ] Beutech volgorde correct als andere klanten genoemd (`Veco · Beutech · Euromaster`)
- [ ] Klantnamen typo-vrij
