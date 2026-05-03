# Prompt — Loom 3-min Video Script

**When:** Bij outreach naar enterprise-prospects of inbound-leads, of als deep-dive content (1× per maand).
**Format:** 3-minuten Loom screen-recording met talking-head insert
**Tone-mix:** Dominant `Energiek bewijsdrang` (15%) + secundair `Engineer logisch` (10%) of `Rustig autoriteit` (30%)
**Output length:** 3 minuten gesproken = ~430-500 woorden script + screen-recording cues

---

## System prompt

```
Je schrijft een Loom video-script voor Ing. Wouter Arts. Doel: live-demo of personal walkthrough sturen naar 1 prospect of als evergreen content op de site.

Loom-format-rules:
- 3 minuten = sweet spot (2:45-3:15). Langer wordt afgehaakt.
- Begin met visueel: NOOIT "hi this is wouter" als opener. Start met scherm of statement.
- Kies één visuele rode-draad: scherm / whiteboard / fysiek prop. Niet alle drie.
- Talking-head insert (rechtsonder of linksboven) ALTIJD aan tijdens uitleg.
- Captions: NIET nodig in Loom (audio is verplicht), wel transcript onder publish.

Brand-bible:
- Trust markers `Veco · Beutech · Euromaster` (in deze volgorde, 1×)
- ❌ Geen Aebi Schmidt
- Lichtgrijs blazer + ronde matte black bril aan
- Real-shot setting (niet AI background)

Script-structuur (3 min = ~480 woorden):
- 0:00-0:15 → HOOK (3-4 zinnen, vaste opener)
- 0:15-0:30 → CONTEXT (1 zin: waarom kijken)
- 0:30-2:00 → DEMO/WALKTHROUGH (3 stappen, met scherm-cue per stap)
- 2:00-2:30 → RESULT (concrete cijfer of output)
- 2:30-3:00 → CTA (1 next-step + URL of reply-prompt)

Voice:
- Spreektaal, niet schrijftaal
- Kortere zinnen (gemiddelde 8-12 woorden)
- Pause-moments markeren in script: [pause]
- Cijfers verbaal: "vier-en-veertig procent", niet "44%" (anders haalt brein 'het uit als getal-klank)
```

## Variables

- `{{TOPIC}}` — wat de Loom uitlegt
- `{{TOOL_OR_PROMPT}}` — concreet wat je demoot
- `{{CLIENT_REFERENCE}}` — Veco / Beutech / Euromaster (optioneel)
- `{{RESULT_NUMBER}}` — eindcijfer dat de demo bewijst
- `{{CTA_TYPE}}` — Stack 2026 download / Pipeline check DM / Workshop boek

## User-prompt template

```
Schrijf een 3-minuten Loom video-script over `{{TOPIC}}`.

Tool/prompt: {{TOOL_OR_PROMPT}}
Klant-referentie (optioneel): {{CLIENT_REFERENCE}}
Resultaat-cijfer: {{RESULT_NUMBER}}
CTA: {{CTA_TYPE}}

Output:
1. Script per scene met timestamps
2. Per scene: gesproken tekst + scherm-cue + duur
3. Pause-moments markeren met [pause]
4. Optioneel: text-overlay-suggesties (max 3 over hele video)

Doelgroep: HR Director of recruiter bij tech-bedrijf 50-800 FTE.
Spreektaal, geen schrijftaal.
```

## Sample input + output

**Input:**
- TOPIC = "Hoe ik 4u sourcing in 25 min doe"
- TOOL_OR_PROMPT = Boolean Search Engineer (Stack 2026 Module 1)
- CLIENT_REFERENCE = Beutech
- RESULT_NUMBER = "47 → 312 kandidaten"
- CTA_TYPE = Stack 2026 download

**Output:**

```
[0:00 — 0:15] HOOK
Scherm: lege LinkedIn boolean-search bar
Talking-head: rechtsonder, 250×250

Spoken:
"Vier uur sourcing in vijfentwintig minuten. Geen mythe.
Ik laat je nu zien hoe ik dit deed bij Beutech, vorige week,
voor een Besturingstechnicus.
[pause]
Eerste stap — niet wat je denkt."

Text-overlay (groot, oranje): "4U → 25 MIN"

—

[0:15 — 0:30] CONTEXT
Scherm: vacature-tekst Beutech in tab

Spoken:
"De vacature zegt: Senior Besturingstechnicus, vijf jaar S7-ervaring.
Hun bestaande boolean leverde zevenenveertig kandidaten op.
Niet één op gesprek. Drie weken zoeken."

—

[0:30 — 1:00] DEMO STAP 1
Scherm: Claude / Cursor open, prompt aan het typen

Spoken:
"Stap één: ik gooi de vacature in mijn Boolean Search Engineer prompt.
Acht seconden later geeft 'ie me drie booleans terug — skill-driven,
titel-driven, bedrijfs-driven.
[pause]
De skill-driven is altijd de winnaar."

—

[1:00 — 1:30] DEMO STAP 2
Scherm: LinkedIn met nieuwe boolean ingevuld

Spoken:
"Stap twee: ik plak de skill-driven boolean in LinkedIn.
S7-1500 OR TIA Portal OR Step7, en dan PLC of besturing.
Resultaat boven de zoekbalk: drie-honderd-twaalf kandidaten."

Text-overlay: "47 → 312"

—

[1:30 — 2:00] DEMO STAP 3
Scherm: top 30 filtering — locatie, werkstand

Spoken:
"Stap drie: ik filter top dertig op locatie en werkstand.
Daarvan stuur ik de twaalf die het beste matchen een gepersonaliseerde
InMail. Niet automatisch — wel via een tweede prompt die per persoon
drie hooks uit hun profiel haalt."

—

[2:00 — 2:30] RESULT
Scherm: Pipedrive met deze deal — kandidaten in pipeline

Spoken:
"Resultaat na twee weken: vier kandidaten op gesprek, één hire.
Voor Beutech — eenenveertig procent response rate op de InMails.
Industrie-gemiddelde is acht procent."

Text-overlay: "41% RESPONSE · 5× INDUSTRY"

—

[2:30 — 3:00] CTA
Scherm: cut naar wouter recht in camera (laatste 30 sec)

Spoken:
"Wil je deze prompt? Ik heb 'm in mijn Stack 2026 gestopt — gratis.
Plus vier andere prompts die ik dagelijks gebruik bij Veco · Beutech · Euromaster.
[pause]
Link in de Loom-beschrijving en hieronder:
recruitmentengineer.nl
[pause]
Bedankt voor het kijken."

Text-overlay laatste 5 sec: "recruitmentengineer.nl"
```

## Edit-checklist

- [ ] Totale duur 2:45-3:15 (gesproken-tempo check)
- [ ] Hook in eerste 15 seconden (cijfer of prikkel)
- [ ] 3 demo-stappen, niet meer, niet minder
- [ ] Beutech volgorde correct in CTA-segment
- [ ] Geen Aebi Schmidt
- [ ] Cijfer in CTA-segment
- [ ] Spreektaal — geen "voorts" / "ten eerste"
- [ ] Pause-moments aangegeven
- [ ] Text-overlay suggesties max 3 over hele video
- [ ] Script start NIET met "hi this is wouter" — start visueel
- [ ] CTA-URL is recruitmentengineer.nl
