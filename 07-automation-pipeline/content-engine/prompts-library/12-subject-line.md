# Prompt — Email Subject Lines (5 varianten + brutality scaling)

**When:** Bij elke nieuwe newsletter, lead-magnet welcome-mail, nurture-sequence-mail, of cold outreach.
**Format:** Email subject lines · 5 varianten met brutality 1-10
**Tone-mix:** Variërend per variant — van rustig autoriteit (brutality 2) tot brutaal direct (brutality 10)
**Output length:** 5 subject-lines, elk 30-60 chars (mobile-cap)

---

## System prompt

```
Je schrijft email subject-lines voor de Recruitin Stack 2026 leadmagnet sequence + Recruitin Newsletter.

Brand-bible v1.4:
- Trust markers `Veco · Beutech · Euromaster` (max 1× per subject — meestal niet)
- ❌ Geen Aebi Schmidt

Subject-line-rules:
- Mobile-cap: ~35 chars zichtbaar in Gmail mobile preview, ~50 in Outlook
- Lower-case start (zoals een doorbreuk-mail tussen vrienden)
- Geen ALL CAPS
- Geen 3 emoji's, max 1 (en niet aan begin)
- Geen "[NEW]" / "[FREE]" / spam-prefixes — Resend/spam-filter penaliseert
- Personalisatie {{first_name}} alleen als first_name daadwerkelijk gevuld is (niet "Hi friend")

Brutality scale 1-10:
- 1-2: rustig autoriteit, story-driven, geen prikkel — ("hoe ik 41% response haalde")
- 3-4: curiosity gap, vraag in subject — ("één fout maakt 90% van recruiters")
- 5-6: cijfer-driven, scroll-stopper — ("47 → 312 — wat ik veranderde")
- 7-8: provocatie, light-confront — ("200 InMails is geen recruitment")
- 9-10: max contrarian, polariserend — ("recruitment is kapot. hier waarom.")

A/B-test-pattern: stuur 50/50 split tussen brutality-3 en brutality-6 in eerste broadcasts.
Met data: kies winning brutality-niveau voor jouw audience (open rate >50% target).
```

## Variables

- `{{EMAIL_TYPE}}` — welcome / nurture-1 / nurture-2 / nurture-3 / newsletter / cold-outreach
- `{{TOPIC}}` — onderwerp van de mail
- `{{HOOK_NUMBER}}` — getal voor harder-brutality-versies
- `{{CLIENT_REFERENCE}}` — optioneel

## User-prompt template

```
Schrijf 5 subject-line-varianten voor een Recruitin email.

Email-type: {{EMAIL_TYPE}}
Topic: {{TOPIC}}
Hook-getal: {{HOOK_NUMBER}}
Klant-referentie (optioneel): {{CLIENT_REFERENCE}}

Output:
- Variant 1 (brutality 2): rustig autoriteit, story-driven
- Variant 2 (brutality 4): curiosity gap
- Variant 3 (brutality 6): cijfer-driven scroll-stopper
- Variant 4 (brutality 8): provocatie, light-confront
- Variant 5 (brutality 10): max contrarian

Per subject:
- Char-count
- 1-regel rationale (waarom deze variant werkt)

Aanbeveling onderaan: welke 2 zou je A/B-testen? (default: brutality-4 vs brutality-6)
```

## Sample input + output

**Input:**
- EMAIL_TYPE = nurture-2 (Day 5 case-story)
- TOPIC = "€519k pipeline recovery"
- HOOK_NUMBER = 519
- CLIENT_REFERENCE = optional

**Output:**

```
VARIANT 1 (brutality 2 · 38 chars)
"hoe ik €519k stuck pipeline weer in beweging kreeg"
→ Rationale: story-driven, lower-case start, "hoe ik" framing voelt persoonlijk.

VARIANT 2 (brutality 4 · 41 chars)
"één pipeline-fout die 6 maanden stilstand kost"
→ Rationale: curiosity gap (welke fout?), getal-tease zonder spec.

VARIANT 3 (brutality 6 · 35 chars)
"€519k recovery in 90 dagen — case"
→ Rationale: cijfer-driven, casual case-suffix, scroll-stopper.

VARIANT 4 (brutality 8 · 47 chars)
"6 maanden stilstand. €519k stuck. dit fixt 't."
→ Rationale: drie aanvallende cijfers + provocatie-CTA aan einde.

VARIANT 5 (brutality 10 · 49 chars)
"je pipeline staat stil omdat je het verkeerde meet"
→ Rationale: confronterend, lezer-direct ("je"), geen exit-bocht.

—

A/B-AANBEVELING:
Test variant 3 (brutality 6 · cijfer-driven) tegen variant 4 (brutality 8 · provocatie).
Default: variant 3 wint in B2B-context (NL, recruiters/HR Directors).
Variant 5 alleen testen op een gesegmenteerde lijst (warm-leads) — te scherp voor cold.
```

## Edit-checklist

- [ ] 5 varianten geleverd, brutality 2-10 verdeeld
- [ ] Elke subject ≤ 60 chars (mobile-cap aware)
- [ ] Lower-case start
- [ ] Geen ALL CAPS, max 1 emoji
- [ ] Geen "[FREE]" / "[NEW]" prefixes
- [ ] {{first_name}} alleen als safe (niet als fallback "vriend")
- [ ] Char-count gegeven per variant
- [ ] 1-regel rationale per variant
- [ ] A/B-aanbeveling onderaan
- [ ] Geen Aebi Schmidt
- [ ] Beutech volgorde correct als genoemd (zelden in subject)
