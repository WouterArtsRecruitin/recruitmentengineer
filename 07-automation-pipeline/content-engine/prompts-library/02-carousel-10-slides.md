# Prompt — Carousel 10 slides (LinkedIn)

**When:** 1× per week. Pijler A (framework), B (anti-list/debunker) of C (tool-tour).
**Format:** LinkedIn document carousel — 10 slides, 1080×1350 px elk
**Tone-mix:** Engineer logisch (10%) als dominant + Specialist confronterend (20%) of Brutaal direct (25%) als secundair
**Output length:** 10 slides · ~50-80 woorden per slide · cover + 8 insights + CTA-slide

---

## System prompt

```
Je schrijft een LinkedIn carousel-script voor Ing. Wouter Arts, Recruitment Engineer.

Brand-bible v1.4:
- Trust markers: `Veco · Beutech · Euromaster` (vaste volgorde, max 1× Beutech per carousel)
- ❌ Geen Aebi Schmidt
- Visual-DNA: blueprint-stijl, oranje (#FF6B1A) accent, blue-deep (#15293F) bg op donkere slides, warm-grey (#F5F0EB) op lichte. Inter Bold + JetBrains Mono.

Carousel-structuur (10 slides):
1. Cover — headline + subhead + "Swipe →"
2-9. Insights — 8 slides waarin je 1 idee per slide uitwerkt (max 60 woorden)
10. CTA — Stack 2026 PDF + recruitmentengineer.nl

Per slide:
- Slide-headline: max 7 woorden, Inter 800
- Body: max 60 woorden, Inter 400
- Cijfer of klant-referentie wanneer mogelijk
- Mono-label rechtsboven: bv. `[01/10]`, `[FRAMEWORK]`, `[CASE]`

Voice rules: zelfde 10 als hero-post (jij-vorm, ik niet wij, getallen > adjectieven, geen jargon).

LinkedIn-regel: native PDF-upload (NIET image-set). 1080×1350 portrait.
```

## Variables

- `{{TOPIC}}` — carousel-onderwerp
- `{{CLIENT_REFERENCE}}` — Veco / Beutech / Euromaster
- `{{NUMBER_HOOK}}` — getal voor cover-slide
- `{{PILLAR}}` — A / B / C
- `{{FORMAT_TYPE}}` — framework / anti-list / tool-tour / klantcase

## User-prompt template

```
Schrijf een 10-slide LinkedIn carousel over `{{TOPIC}}`.

Pijler: {{PILLAR}}
Format-type: {{FORMAT_TYPE}}
Klant-referentie: {{CLIENT_REFERENCE}}
Cover-getal: {{NUMBER_HOOK}}

Structuur:
- Slide 1 (Cover): headline + subhead + footer "Door Ing. W. Arts · Swipe →"
- Slides 2-9: per slide 1 idee/insight/laag/punt — max 60 woorden body
- Slide 10 (CTA): "Stack 2026 — gratis" + recruitmentengineer.nl

Per slide geef je:
- Mono-label rechtsboven (`[01/10]`, `[02/10]`, etc.)
- Headline (max 7 woorden, Inter 800)
- Body (max 60 woorden)
- Visual-cue voor designer (1 regel: bv. "Blueprint-diagram met 5 lagen", "Splitscreen oranje/blauw")

Tone: dominant Engineer logisch + secundair {{...}}.
Cijfers verplicht waar relevant. Geen HR-clichés.
```

## Sample input + output

**Input:**
- TOPIC = "5 lagen Recruitment Engineering"
- CLIENT_REFERENCE = Beutech
- NUMBER_HOOK = 5
- PILLAR = A
- FORMAT_TYPE = framework

**Output (excerpt — 3 slides):**

```
SLIDE 1 (Cover) [01/10]
Headline: "Recruitment Engineering"
Subhead: "De 5 lagen — en waarom 90% blijft hangen op laag 1"
Footer: "Door Ing. W. Arts · Swipe →"
Visual-cue: Blueprint-diagram, 5 horizontale lagen gestapeld, oranje accent op laag 1

SLIDE 2 [02/10] [PROBLEEM]
Headline: "90% werkt op laag 1"
Body: "Posten + zoeken + bellen. Dat is laag 1.
De échte impact zit in laag 2 t/m 5.
Daar wordt 80% van de leverage gemist.
Niet door slechte recruiters. Door verouderde aanpak."
Visual-cue: 5 lagen, alleen laag 1 ingekleurd oranje, rest grijs

SLIDE 3 [03/10] [LAAG 1]
Headline: "Laag 1 — Sourcing Engineering"
Body: "Wat 90% doet: LinkedIn boolean + hopen.
Wat ik doe: AI-prompted boolean + adjacent industry mapping + ICP-reverse-engineering.
Bewijs: Beutech kandidatenpool verdubbeld in 2 dagen."
Visual-cue: Schermrecording-mock met Claude/Cursor + boolean-output
```

(Slides 4-9 volgen zelfde patroon voor lagen 2-5 + 2 reflectie-slides.)

```
SLIDE 10 [10/10] [CTA]
Headline: "De complete stack — gratis"
Body: "Alle 5 lagen, 5 AI-prompts, 12 pagina's PDF, 3 video-walkthroughs en de Notion-template.
Geen funnel. Geen webinar. Gewoon de tools.
→ recruitmentengineer.nl"
Visual-cue: Orange CTA-button + URL groot
```

## Edit-checklist

- [ ] Beutech volgorde correct (en max 1× per carousel)
- [ ] Geen Aebi Schmidt
- [ ] Cover heeft cijfer in headline of subhead
- [ ] Slide 10 heeft URL `recruitmentengineer.nl`
- [ ] Per slide max 60 woorden body
- [ ] Mono-labels rechtsboven elke slide
- [ ] Visual-cues concreet genoeg voor designer
- [ ] Geen jargon (PLC/SCADA/CMMS)
- [ ] Cijfer of klantcase in minimaal 5 van de 10 slides
- [ ] LinkedIn caption (boven carousel) apart geschreven, max 1.500 chars
