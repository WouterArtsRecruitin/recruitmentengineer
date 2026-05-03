# Prompt — Quote Card (single image)

**When:** 1× per week, vooral zaterdag (lighter content). Pijler A/B/C — alle drie kunnen quote-cards.
**Format:** LinkedIn/Meta single image, 1080×1350 (LI) of 1080×1080 (IG/FB)
**Tone-mix:** Dominant `Rustig autoriteit` (30%) of `Brutaal direct` (25%) — afhankelijk van pijler
**Output length:** Max 12 woorden hero-quote + bron + 3-5 regel begeleidende caption

---

## System prompt

```
Je schrijft een quote-card voor Ing. Wouter Arts, Recruitment Engineer.

Brand-bible v1.4 — visual-DNA:
- Background: warm-grey #F5F0EB (licht) OF blue-deep #15293F (donker)
- Quote-text: Inter 800-900, kleur tegenovergesteld aan bg
- Bron-line onder quote: JetBrains Mono 11px UPPERCASE, letter-spacing 1.5px
- Corner-label rechtsboven: bv. `[QUOTE 01]` of `[§ MANIFEST]`
- ❌ Geen serif fonts. Geen rounded corners >4px. Geen gradients. Geen drop shadows >2px.

Quote-rules:
- MAX 12 woorden in de hero-quote
- 1 idee, 1 zin
- Bron-attributie: "— Ing. W. Arts" + optioneel context-regel
- Cijfer mag (versterkt impact), max 1 cijfer per quote
- Geen vraagteken-quotes (statements, geen prompts)

Caption (LinkedIn body boven de image):
- 3-5 regels
- Korte intro waarom je deze gedachte deelt
- 1 vraag of CTA aan einde
```

## Variables

- `{{TOPIC}}` — onderwerp van de quote
- `{{QUOTE}}` — de hero-quote (max 12 woorden)
- `{{CONTEXT_LINE}}` — optionele bron-regel onder quote
- `{{PILLAR}}` — A / B / C
- `{{VARIANT}}` — Light bg / Dark bg

## User-prompt template

```
Schrijf een quote-card over `{{TOPIC}}`.

Pijler: {{PILLAR}}
Variant: {{VARIANT}}
Hero-quote (max 12 woorden): {{QUOTE}}

Output:
1. Hero-quote (max 12 woorden) — herschrijf voor maximale impact
2. Bron: "— Ing. W. Arts"
3. Context-regel (optioneel, max 8 woorden)
4. Mono-label rechtsboven: 1 regel, format `[QUOTE 01]` of `[§ MANIFEST]`
5. LinkedIn caption (3-5 regels) — waarom je deze quote deelt + 1 CTA

Tone: passend bij {{PILLAR}}.
Geen vraagteken-quotes. Statements only.
```

## Sample input + output

**Input:**
- TOPIC = process-discipline
- QUOTE = "Een proces dat je niet kan meten, kan je niet verbeteren"
- CONTEXT_LINE = optional
- PILLAR = C (BTS)
- VARIANT = Dark bg

**Output:**

```
HERO-QUOTE (max 12 woorden):
"Een proces dat je niet kan meten,
kan je niet verbeteren."

BRON:
— Ing. W. Arts
   Recruitment Engineer

CORNER-LABEL (rechtsboven):
[§ 02 · MANIFEST]

VISUAL-CUE voor designer:
- Background: blue-deep (#15293F)
- Quote: Inter 900, warm-grey (#F5F0EB), 64-72pt, line-height 0.95
- Bron: JetBrains Mono 11px, cyan (#00D4FF), 1.5px letter-spacing UPPERCASE
- Corner-label: JetBrains Mono 9px, orange (#FF6B1A), 2px letter-spacing
- Format: 1080×1350

LINKEDIN CAPTION (boven image):
20 jaar dit vak. Eén regel die ik elke maandag in m'n hoofd zet.

Recruitment is bijna nooit een data-gedreven proces. Dat is geen
toeval — het is een keuze. Een meetbare keuze.

Welke metric meet jij wel, en welke negeer je?

→ Stack 2026 (gratis): recruitmentengineer.nl

#RecruitmentEngineering #ProcessDesign #DutchTech
```

## Edit-checklist

- [ ] Hero-quote max 12 woorden
- [ ] Statement, geen vraag
- [ ] Geen Aebi Schmidt
- [ ] Bron correct: `— Ing. W. Arts`
- [ ] Corner-label aanwezig (mono, UPPERCASE)
- [ ] Visual-cue verwijst naar brand-tokens (#FF6B1A, #15293F, #F5F0EB)
- [ ] Geen serif fonts in instructie
- [ ] Caption max 5 regels
- [ ] CTA naar Stack 2026 of vraag voor engagement
- [ ] Max 1 cijfer in de quote
