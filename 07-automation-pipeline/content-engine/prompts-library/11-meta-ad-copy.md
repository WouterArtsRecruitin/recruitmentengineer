# Prompt — Meta Ad Copy (hook + body + CTA)

**When:** Bij elke nieuwe Meta-ad-set (audience tier × format × creative). 1× per week tijdens campaign-phase.
**Format:** Meta Ads (Instagram/Facebook). Ad-copy variants per format.
**Tone-mix:** Dominant `Brutaal direct` (25%) + secundair `Energiek bewijsdrang` (15%) — afhankelijk van audience-tier
**Output length:** 5 hooks + 3 bodies + 3 CTAs per format

---

## System prompt

```
Je schrijft Meta Ads-copy voor een leadmagnet-campaign (Stack 2026 PDF).

Brand-bible v1.4:
- Trust markers `Veco · Beutech · Euromaster` (max 1× Beutech per ad)
- ❌ Geen Aebi Schmidt
- Visual: warm/light setting, lichtgrijs blazer, ronde matte black bril (ALLE creatives — anders mismatch met brand)
- Numbers > adjectives

Meta-format-context:
- Reel 9:16 = vertical, 30-60 sec, audio-first (sound on default)
- Feed 1:1 = scroll-stopper hook, dual readability (sound on/off)
- Story 9:16 = quick, swipe-up CTA
- LinkedIn 16:9 = professional desktop, geen TikTok-stijl

Ad-copy structuur per ad:
- Primary text: 125 chars max readable on first scroll, 600 chars total cap
- Headline: max 40 chars (truncate na ~27 op mobile)
- Description: max 30 chars (alleen single-image, niet video)
- CTA-button: dropdown (Learn More, Download, Sign Up, Get Offer)

Hook-laddering — output altijd 5 hook-varianten met "brutality scale 1-10":
- Hook 1: brutality 2 (soft, story-driven)
- Hook 2: brutality 4 (curiosity gap)
- Hook 3: brutality 6 (cijfer-driven, geen bullshit)
- Hook 4: brutality 8 (provocatie + bewijs)
- Hook 5: brutality 10 (max contrarian, "iedereen doet het verkeerd")
```

## Variables

- `{{TOPIC}}` — wat de ad pitcht
- `{{FORMAT}}` — Reel 9:16 / Feed 1:1 / Story 9:16 / LinkedIn 16:9
- `{{AUDIENCE_TIER}}` — TOFU (cold) / MOFU (warm) / BOFU (hot)
- `{{NUMBER_HOOK}}` — getal voor hardere hooks
- `{{CLIENT_REFERENCE}}` — Veco / Beutech / Euromaster

## User-prompt template

```
Schrijf Meta Ads-copy voor een Stack 2026 leadmagnet ad.

Topic: {{TOPIC}}
Format: {{FORMAT}}
Audience tier: {{AUDIENCE_TIER}}
Hook-getal: {{NUMBER_HOOK}}
Klant-referentie: {{CLIENT_REFERENCE}}

Output:

A. 5 hooks (brutality scale 1-10):
   1. brutality 2 (soft)
   2. brutality 4 (curiosity gap)
   3. brutality 6 (cijfer-driven)
   4. brutality 8 (provocatie)
   5. brutality 10 (max contrarian)

B. 3 body-varianten (per body 80-150 woorden):
   - Variant A: story-driven (klantcase)
   - Variant B: tool-driven (prompt-share)
   - Variant C: provocatie-driven (markt-confront)

C. 3 CTA's (max 8 woorden):
   - CTA 1: download-driven
   - CTA 2: try-driven
   - CTA 3: ownership-driven

D. 1 headline (max 40 chars)
E. 1 description (max 30 chars, alleen voor static)
```

## Sample input + output

**Input:**
- TOPIC = "Stack 2026 — gratis playbook"
- FORMAT = Feed 1:1
- AUDIENCE_TIER = MOFU
- NUMBER_HOOK = 41
- CLIENT_REFERENCE = Veco

**Output:**

```
A. 5 HOOKS (brutality scale 1-10):

1. (brutality 2) — Story
"In 2005 begon ik in recruitment — opgeleid als ingenieur. Vandaag deel ik mijn complete stack."

2. (brutality 4) — Curiosity gap
"De prompt die mijn outreach-rate van 8% naar 41% bracht — staat hier."

3. (brutality 6) — Cijfer-driven
"41% response rate. 25 min sourcing per vacature. €519k pipeline recovered. Hier is hoe."

4. (brutality 8) — Provocatie
"200 InMails per week is geen recruitment. Het is volume-spam. Hier is wat wel werkt."

5. (brutality 10) — Max contrarian
"Recruitment is kapot. Niet door slechte recruiters. Door een verouderd proces dat niemand durft te herontwerpen."

—

B. 3 BODY-VARIANTEN:

Variant A (story-driven, ~120 woorden):
"Vorig jaar belde Veco. Ze zochten een Maintenance Planner. Hun bureau had 200 InMails verstuurd in 6 weken. 16 antwoorden. Niet één hire.
Ik nam over. Andere prompt, ander mentaal model, andere selectie.
Twee weken later: 20 InMails verstuurd, 8 antwoorden. 41% response rate. Eén hire.
Geen tool-magie. Een proces.
Ik schreef het op in 12 pagina's PDF. 5 prompts. Gratis.
Stack 2026 → recruitmentengineer.nl"

Variant B (tool-driven, ~110 woorden):
"5 AI-prompts die ik dagelijks gebruik bij Veco · Beutech · Euromaster:
→ Boolean Search Engineer (47 → 312 hits)
→ Outreach Hook Extractor (8% → 41% response)
→ Vacature Intake Engineer (8u → 90 min)
→ CV Match Score (20 min → 4 min per CV)
→ Pipeline Health Diagnostician (€519k recovery)
Allemaal copy-paste-klaar. 12 pagina's PDF. Gratis.
Geen funnel, geen webinar, geen email-cursus. Gewoon de prompts.
recruitmentengineer.nl"

Variant C (provocatie-driven, ~115 woorden):
"De gemiddelde recruiter werkt op laag 1: posten + zoeken + bellen.
Daar zit niet de impact. Die zit op laag 2 t/m 5: outreach, intake, kwalificatie, pipeline.
80% van de leverage wordt gemist.
Ik heb mijn complete proces vorig half jaar herontworpen — en daar 12 pagina's over geschreven.
Voor wie wil zien hoe het anders kan: gratis te downloaden, geen email-funnel.
Stack 2026 — recruitmentengineer.nl
Voor recruiters bij tech-bedrijven 50-800 FTE."

—

C. 3 CTA's:

1. (download-driven) "Download Stack 2026"
2. (try-driven) "Probeer 5 prompts"
3. (ownership-driven) "Pak de Stack"

—

D. HEADLINE (max 40 chars):
"Stack 2026 — 5 AI prompts gratis"  (33 chars ✓)

E. DESCRIPTION (max 30 chars):
"12 pagina's. 0 funnel."  (23 chars ✓)
```

## Edit-checklist

- [ ] 5 hooks geleverd, brutality 2-10 verdeeld
- [ ] 3 bodies geleverd (story / tool / provocatie)
- [ ] 3 CTAs geleverd
- [ ] Headline ≤ 40 chars
- [ ] Description ≤ 30 chars
- [ ] Beutech volgorde correct (max 1× per ad)
- [ ] Geen Aebi Schmidt
- [ ] Cijfer in minimaal 3 hooks
- [ ] CTA's actiewerkwoord (download / probeer / pak)
- [ ] Geen "wij" in body — alleen "ik"
- [ ] Format-correct (1:1 vs 9:16 vs 16:9 specs)
- [ ] Geen rounded corners >4px in visual-cue
