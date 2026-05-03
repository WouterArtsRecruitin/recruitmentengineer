# Identity Lock Rules

Single-page reference. Apply BEFORE submitting any render and AFTER receiving the result. If any locked element drifts, reject and regenerate.

> **Brand bible source:** `01-brand-bible/brand-bible.md` v1.4 (Mei 2026).
> **Soul-ID:** `948dbc10-ba8d-406c-b771-e15610ae8674` — *Ing W Arts Recruitment Engineer* (trained, production-ready).
> **Override note:** campaign-orchestrator instruction is **calm authoritative gaze, max neutral-engaged expression — never broad smile**. This supersedes the brand bible's "warm open glimlach" cue for ad/hero use.

---

## Soul-ID handles most identity. Document drift cases below.

When you submit a Set-A or Set-C portrait with the locked Soul-ID, the model preserves face geometry, hair pattern, eye color, glasses-frame shape, skin texture, and the "Wouter look" automatically. You don't have to describe the face in the prompt — that's already trained in.

**What can still drift even with Soul-2:**
- Mouth-state (open / closed) — depends on prompt
- Wardrobe color when prompt overspecifies
- Glasses-frame fidelity in extreme angles or motion blur
- Hand-anatomy (Soul does NOT lock hands — always at risk)
- Setting/lighting bleed onto subject (skin tone shift in heavy color casts)

The checklist below covers both Soul-locked properties (verify they didn't drift) AND prompt-driven properties (where you must describe correctly).

---

## ✅ Must stay identical across every render

### Face & head (Soul-locked, but verify)
- Dutch male, late 40s
- Salt-and-pepper hair, side-parted, neat (no buzz, no man-bun, no slick-back)
- 3-day salt-and-pepper stubble (not clean-shaven, not full beard)
- Light European complexion, healthy
- Real skin texture visible (pores, micro-detail)
- Eye color stays consistent across the set (blue-grey → keep one tone, do not drift to brown)
- Symmetric facial structure — no morphing across renders

### Eyewear (signature, Soul-locked but extreme-angle risk)
- Round-frame matte black acetate glasses
- Thick rim, statement piece, vintage-intellectual aesthetic
- ALWAYS present (never bare-eyed, never sunglasses, never wire-rim, never modern rectangular)

### Wardrobe (Soul-locked, but heavy color cast can shift hue)
- Light grey wool blazer (charcoal-light, not navy, not black, not brown)
- White shirt underneath, no pattern, no stripes
- Black knit tie (textured, slightly chunky weave — NOT silk, NOT smooth)
- Tolerance: blazer can read slightly warmer or cooler depending on light, but base hue stays light grey wool
- No jewelry, no visible watch unless setting demands it (e.g. boardroom presentation)
- No fashion-loud accessories, no tie-pin, no pocket-square

### Expression (PROMPT-DRIVEN — describe correctly every time)
- Calm authoritative gaze
- Mouth: closed OR barely-parted (mid-thought)
- Eyes: focused, intelligent, slight openness
- **Never:** broad toothy smile, fake grin, smiling-into-camera, slack-jaw open mouth, sneer, neutral-corporate-zombie face
- Acceptable range: from "neutral focused" to "subtly engaged" — that's it

### Posture & energy (PROMPT-DRIVEN)
- Upright, grounded
- No slouching, no hunched shoulders
- Authority-with-accessibility — engineer, not banker, not influencer
- Hands natural — not crossed-and-stiff, not posed-in-pockets-fashion-shoot
- **Hands carry the highest AI-artifact risk.** Inspect every render at 100% zoom on hand zones.

---

## ✅ Must stay consistent within a campaign-set

(Slight variation across renders is fine, but a single 10-piece set should feel like one shoot.)

- Color grade: teal-orange cinematic by default
- Lens character: 50–85mm equivalent (24mm allowed for establishing wides), shallow DoF f/2.0–f/2.8
- Lighting school: documentary-editorial (Rembrandt side-key + soft fill), never beauty-dish, never ring-light flat
- Skin: never beauty-filter smooth, never plastic
- Background: out-of-focus industrial / engineering / on-location, never generic stock office

---

## ❌ Sample failure modes — REJECT and regen if you see these

### Soul-related drift (re-render with Soul-ID re-confirmed)

| Failure | Symptom | Fix |
|---------|---------|-----|
| Face morph | Render doesn't look like the trained Soul (different bone structure, different age) | Verify `soul_id: 948dbc10-...` is actually applied. Higgsfield UI sometimes drops it on cache-miss. Re-submit. |
| Glasses missing | Rendered without eyewear despite Soul lock | Add `wearing round-frame matte black acetate glasses, statement piece, ALWAYS visible` to prompt. Soul should hold this — if it doesn't, escalate to Higgsfield Soul retraining. |
| Glasses morph | Rectangular / wire / aviator instead of round-acetate | Same as above + specify `round-frame matte black acetate, thick rim, NOT rectangular, NOT wire, NOT aviator`. |
| Eye-color drift | Eye color shifted (blue-grey → brown) | Re-render. If repeated, escalate Soul retraining. |
| Skin too smooth | Beauty-filter look despite Soul (extreme prompt-style overrode trained texture) | Add `real skin texture visible, pores, micro-detail, NOT beauty-filter, NOT smoothed, documentary candid` to prompt. |

### Prompt-driven drift (regen with corrective prompt)

| Failure | Symptom | Fix |
|---------|---------|-----|
| Mouth open / talking | Speaking pose with open mouth | Add `mouth closed or barely-parted, NOT speaking, NOT mid-word, NOT toothy grin` |
| Toothy smile / fake grin | Broad smile showing teeth | Same fix + `documentary candid editorial style, NOT influencer, NOT stock photo` |
| Wrong blazer color | Blazer shifted navy / black / brown / patterned (extreme color cast) | Specify `light grey wool blazer, charcoal-light hue (NOT navy NOT black)` and reduce color-cast intensity in prompt. |
| Tie wrong | Silk smooth tie / no tie / colored tie | Specify `black knit tie, textured chunky weave, NOT silk, NOT colored` |
| Hair drift | Buzz cut / slick / man-bun (extreme prompt-style) | Specify `salt-and-pepper hair, side-parted, neat, NOT buzz NOT slick-back NOT man-bun` |
| Stubble drift | Clean-shaven OR full beard | Specify `3-day salt-and-pepper stubble, neat, NOT clean-shaven NOT full-beard` |
| Multiple people | Background humans in focus | Add to negative prompt `multiple people, no other faces visible in focus` |
| Aebi Schmidt visible | Branding / logo / orange truck-livery | Add to negative prompt `Aebi Schmidt branding, orange municipal trucks, Aebi Schmidt orange livery` |
| Generic stock office | Boardroom / co-working glass walls | Specify `industrial documentary setting, real on-location, NOT corporate office, NOT co-working space` |

### AI-artifact failures (regen, sometimes Soul-2 escalation)

| Failure | Symptom | Fix |
|---------|---------|-----|
| Hand-anatomy errors | Distorted hands / extra fingers / fused fingers | Add to negative prompt `deformed hands, extra fingers, malformed fingers, AI artifacts, distorted features`. Re-render up to 3x; if persistent, change pose to one without visible hands. |
| Watermark / text noise | Brand watermarks / random letters on output | Add to negative prompt `watermark, signature, brand text, AI tool branding, random text artifacts` |
| Readable text leak | Visible legible text on screens / whiteboards / signage | Add `text on screens intentionally illegible, blurred, abstract code` to setting description; add `readable text on screens, legible signage` to negative |

---

## Pre-flight checklist (paste into your QA notes)

### Soul-locked properties
- [ ] Soul-ID `948dbc10-ba8d-406c-b771-e15610ae8674` was applied to this render
- [ ] Face matches trained Soul (no morph, no age-shift)
- [ ] Eye color consistent with previous renders in the set
- [ ] Round-frame matte black acetate glasses present (not rectangular, not wire, not missing)
- [ ] Salt-and-pepper hair side-parted, neat
- [ ] 3-day stubble salt-and-pepper

### Prompt-driven properties
- [ ] Light grey wool blazer (not navy, not black)
- [ ] White shirt underneath
- [ ] Black knit tie visible (textured, not silk)
- [ ] Calm authoritative expression — mouth closed or barely-parted
- [ ] No broad smile, no toothy grin, no influencer face
- [ ] Real skin texture (no beauty filter)
- [ ] Industrial / on-location setting (no generic office)
- [ ] At least 2 brand colors present (orange / blueprint blue / warm grey / deep black)
- [ ] No Aebi Schmidt elements (logos, trucks, livery)
- [ ] No readable text on screens / whiteboards (intentionally illegible)
- [ ] Trust markers (Veco · Beutech · Euromaster) — used max once per asset, no duplicates
- [ ] Hands clean (no extra fingers, no anatomy errors) — inspect at 100% zoom
- [ ] Aspect ratio matches template spec
- [ ] Output filename follows convention `{set}-{id}-{var}-{date}.{ext}`

If any single Soul-property box is unchecked → verify Soul-ID was applied, re-submit. If any prompt-driven box is unchecked → regen with corrective prompt. If hand-anatomy fails 3x → switch to a pose without visible hands.

---

## When to retrain the Soul

If across 5+ renders you see persistent face morph, eye-color drift, or wrong glasses-frame despite passing the correct Soul-ID, escalate to Higgsfield Soul retraining (re-upload anchor photos, re-run training pass). Don't keep regen-ing on a broken Soul — it'll burn credits.
