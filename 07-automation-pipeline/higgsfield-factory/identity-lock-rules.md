# Identity Lock Rules

Single-page reference. Apply BEFORE submitting any render and AFTER receiving the result. If any locked element drifts, reject and regenerate.

> Brand bible source: `01-brand-bible/brand-bible.md` v1.3 (Mei 2026).
> Override note: campaign-orchestrator instruction is **calm authoritative gaze, max neutral-engaged expression — never broad smile**. This supersedes the brand bible's "warm open glimlach" cue for ad/hero use.

---

## ✅ Must stay identical across every render

### Face & head
- Dutch male, late 40s
- Salt-and-pepper hair, side-parted, neat (no buzz, no man-bun, no slick-back)
- 3-day salt-and-pepper stubble (not clean-shaven, not full beard)
- Light European complexion, healthy
- Real skin texture visible (pores, micro-detail)
- Eye color stays consistent across the set (blue-grey → keep one tone, do not drift to brown)
- Symmetric facial structure — no morphing across renders

### Eyewear (signature)
- Round-frame matte black acetate glasses
- Thick rim, statement piece, vintage-intellectual aesthetic
- ALWAYS present (never bare-eyed, never sunglasses, never wire-rim, never modern rectangular)

### Wardrobe
- Light grey wool blazer (charcoal-light, not navy, not black, not brown)
- White shirt underneath, no pattern, no stripes
- Black knit tie (textured, slightly chunky weave — NOT silk, NOT smooth)
- Tolerance: blazer can read slightly warmer or cooler depending on light, but base hue stays light grey wool
- No jewelry, no visible watch unless setting demands it (e.g. boardroom presentation)
- No fashion-loud accessories, no tie-pin, no pocket-square

### Expression
- Calm authoritative gaze
- Mouth: closed OR barely-parted (mid-thought)
- Eyes: focused, intelligent, slight openness
- **Never:** broad toothy smile, fake grin, smiling-into-camera, slack-jaw open mouth, sneer, neutral-corporate-zombie face
- Acceptable range: from "neutral focused" to "subtly engaged" — that's it

### Posture & energy
- Upright, grounded
- No slouching, no hunched shoulders
- Authority-with-accessibility — engineer, not banker, not influencer
- Hands natural — not crossed-and-stiff, not posed-in-pockets-fashion-shoot

---

## ✅ Must stay consistent within a campaign-set

(Slight variation across renders is fine, but a single 10-piece set should feel like one shoot.)

- Color grade: teal-orange cinematic by default
- Lens character: 50–85mm equivalent, shallow DoF f/2.0–f/2.8
- Lighting school: documentary-editorial (Rembrandt side-key + soft fill), never beauty-dish, never ring-light flat
- Skin: never beauty-filter smooth, never plastic
- Background: out-of-focus industrial / engineering / on-location, never generic stock office

---

## ❌ Sample failure modes — REJECT and regen if you see these

| Failure | Symptom | Fix |
|---------|---------|-----|
| Glasses missing | Rendered without eyewear | Add `wearing round-frame matte black acetate glasses` to top of prompt + bold |
| Wrong glasses | Rectangular / wire / aviator | Same fix; specify `round-frame matte black acetate, thick rim, NOT rectangular` |
| Wrong blazer color | Navy / black / brown / patterned | Specify `light grey wool blazer, charcoal-light hue (NOT navy NOT black)` |
| Tie wrong | Silk smooth tie / no tie / colored tie | Specify `black knit tie, textured chunky weave` |
| Toothy smile | Broad grin showing teeth | Add `closed-mouth calm gaze, NOT smiling, NO toothy grin, mid-thought neutral-engaged expression` |
| Fake stock-photo grin | Influencer face | Same as above + `documentary candid editorial style, NOT influencer, NOT stock photo` |
| Plastic skin | Beauty-filter smooth | Add `real skin texture visible, pores, NOT beauty-filter, NOT smoothed` |
| Hair drift | Buzz cut / slick / man-bun | Specify `salt-and-pepper hair, side-parted, neat, NOT buzz NOT slick-back` |
| Stubble drift | Clean-shaven OR full beard | Specify `3-day salt-and-pepper stubble, neat, NOT clean-shaven NOT full-beard` |
| Mouth open / talking | Speaking pose with open mouth | Add `mouth closed or barely-parted, NOT speaking, NOT mid-word` |
| Multiple people | Background humans in focus | Add to negative prompt `multiple people, no other faces visible` |
| Aebi Schmidt visible | Branding / logo / orange truck-livery | Add to negative prompt `no Aebi Schmidt branding, no orange municipal trucks` |
| Generic stock office | Boardroom / co-working glass walls | Specify `industrial documentary setting, real on-location, NOT corporate office, NOT co-working space` |
| AI artifacts | Distorted hands / extra fingers | Add to negative prompt `deformed hands, extra fingers, AI artifacts, distorted features` |
| Watermark / text noise | Brand watermarks on output | Add to negative prompt `watermark, signature, brand text, AI tool branding` |

---

## Pre-flight checklist (paste into your QA notes)

- [ ] Round-frame matte black acetate glasses present
- [ ] Light grey wool blazer (not navy, not black)
- [ ] White shirt underneath
- [ ] Black knit tie visible (textured, not silk)
- [ ] Salt-and-pepper hair side-parted
- [ ] 3-day stubble salt-and-pepper
- [ ] Calm authoritative expression — mouth closed or barely-parted
- [ ] No broad smile, no toothy grin, no influencer face
- [ ] Real skin texture (no beauty filter)
- [ ] Industrial / on-location setting (no generic office)
- [ ] At least 2 brand colors present (orange / blueprint blue / warm grey / deep black)
- [ ] No Aebi Schmidt elements (logos, trucks, livery)
- [ ] No readable text on screens / whiteboards (intentionally illegible)
- [ ] Trust markers (Veco · Beutech · Euromaster) — used max once per asset, no duplicates
- [ ] Aspect ratio matches template spec
- [ ] Output filename follows convention `{set}-{id}-{var}-{date}.{ext}`

If any single box is unchecked → reject + regen with corrective prompt.
