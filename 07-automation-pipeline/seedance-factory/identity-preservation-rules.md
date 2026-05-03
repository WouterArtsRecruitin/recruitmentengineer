# Identity Preservation Rules — Seedance 2.0

Hard rules + sample failure modes. Apply BEFORE submitting any Seedance render and AFTER receiving the clip. If any locked element drifts BETWEEN frame 1 and the final frame, reject.

> **Source still:** Higgsfield Soul-2 render (Soul-ID `948dbc10-ba8d-406c-b771-e15610ae8674`) from Set A or Set C.
> **Brand bible:** `01-brand-bible/brand-bible.md` v1.4.

---

## The core problem

Seedance 2.0 is image-to-video. It takes your Soul-2 still as frame 1 and generates 5–8 seconds of motion forward from that frame. The model is good at preserving identity across short clips — but not perfect. Common drift modes:

1. **Face morph** — frame 1 looks like Wouter, frame 180 looks like a different person (rare on 5–8s clips, more common on 10s+)
2. **Mouth-state break** — still has mouth closed; clip generates a "talking" frame mid-way (lips part, teeth show) even though prompt says no talking
3. **Blazer-color shift** — light grey wool drifts toward navy or brown across frames as the model interpolates lighting
4. **Glasses-frame change** — round acetate becomes thin-wire on rapid motion frames (or motion-blur eats the rim)
5. **Hand-anatomy errors** — extra fingers / fused fingers appear on motion frames where the still had clean hands
6. **Background-motion bleed** — background animation distorts subject silhouette (worker passing behind blends into shoulder)

**These are reject-conditions, not "we'll fix in post."** Re-render with corrective prompt or change the source still.

---

## ✅ Must stay identical between frame 1 and final frame

### Face & expression (HIGHEST PRIORITY)
- Same face geometry (no morph)
- Same eye color
- Mouth state stable — closed in still = closed throughout clip; barely-parted in still = barely-parted throughout
- **NEVER:** broad smile, toothy grin, open-mouth-talking, slack-jaw appearing mid-clip
- Gaze can shift naturally (M4 template) but expression doesn't change to "smiling"

### Wardrobe
- Light grey wool blazer — base hue stable across frames (small lighting variation OK, color shift NOT OK)
- White shirt — no pattern leak, no color tint
- Black knit tie — texture stable, no silk-shift, never disappears

### Eyewear
- Round-frame matte black acetate glasses — present in EVERY frame
- Frame shape stable — never goes wire / rectangular / aviator across clip
- Lens reflections OK (cinematic), but lens edge always visible

### Hair & stubble
- Salt-and-pepper hair side-parted — no flow change, no color drift
- 3-day stubble — no morph to clean-shaven mid-clip, no morph to full beard

### Hands (HIGH RISK — inspect every frame)
- Finger count stable — 5 per hand, every frame
- Finger anatomy clean — no fused, no malformed
- Palm/back-of-hand orientation stable
- If still has hands hidden (in pocket, behind back, off-frame) and motion frames suddenly reveal them with errors → reject

### Body posture
- Posture stable across clip (M1–M6 are all "subject anchored" templates)
- No slouching, no sudden body-twist
- Walking-away (A08 source) is the only template with body motion — and it's lateral stride, not full-body change

---

## ❌ Failure modes — REJECT and regen if you see these

### Hard rejects (clip is unusable)

| Failure | Symptom | Fix |
|---------|---------|-----|
| Face morph | Frame 1 looks right, frame 120+ looks like a different person | Re-submit with shorter clip duration (5s instead of 8s). If persists, change source still. |
| Mouth opens to grin | Lips part to show teeth mid-clip | Append `mouth closed throughout, NO lip-movement, NO smile, NO talking pose, NO teeth visible` to motion prompt. Re-render. |
| Blazer drifts navy | Light grey blazer becomes dark navy by final frame | Append `blazer color stable throughout — light grey wool, NOT navy, NOT black` to motion prompt. Reduce environmental color cast in source still. |
| Glasses disappear or morph | Round acetate becomes wire-frame mid-clip | Append `round-frame matte black acetate glasses present and stable in every frame, NOT wire, NOT thin-rim` to motion prompt. |
| Extra fingers appear | Hand has 6 fingers in motion frames | Re-render. If 3x retries fail, change source still to one with hands hidden or use different motion template. |
| Background bleeds onto subject | Worker passing fuses into shoulder; machine merges with blazer | Reduce background motion intensity. Switch from M6 Environmental to M4 Subject-shift gaze (less ambient motion). |

### Soft rejects (clip needs re-grade or trim)

| Failure | Symptom | Fix |
|---------|---------|-----|
| Mid-clip lighting shift | Brightness ramps up/down unintentionally | Trim clip to 4–5s, use the stable middle. |
| Color grade drift | Teal-orange grade weakens by final frame | Apply post-grade in DaVinci Resolve / FCP to lock teal-orange across full clip. |
| Slight expression drift | Eyes "tighten" or "soften" mid-clip in unwanted way | Acceptable if subtle; reject only if it reads as expression change. |

---

## Pre-flight checklist (paste into your QA notes)

Before submitting:
- [ ] Source still is from Set A (Soul-ID `948dbc10-ba8d-406c-b771-e15610ae8674`) and passed identity-lock-rules.md QA
- [ ] Source still is in `seedance-factory/inputs/` (mirrored)
- [ ] Motion template (M1–M6) selected from `motion-templates.md` matches the format-tier need
- [ ] Identity-string block appended to motion prompt
- [ ] Aspect ratio matches output target

After receiving:
- [ ] Frame 1 face matches Soul (no morph)
- [ ] Final frame face matches Soul (no morph)
- [ ] Mouth state stable (closed in still = closed throughout)
- [ ] No broad smile or toothy grin appears in any frame
- [ ] Blazer stays light grey wool (no navy/brown drift)
- [ ] Glasses round-acetate visible in every frame
- [ ] Hair salt-and-pepper stable
- [ ] Stubble 3-day stable
- [ ] Hand anatomy clean across all frames (inspect at 100% zoom on hand zones)
- [ ] No background-bleed onto subject silhouette
- [ ] Color grade stable teal-orange across full clip
- [ ] Loop-friendly ending (if Reel/Feed)
- [ ] Aspect ratio + resolution + bitrate match format spec
- [ ] Output filename follows `{format}-{template}-{tier}-{variant}-{date}.{ext}`

If ANY hard-reject box fails → re-render or escalate. If soft-reject only → trim/grade in post.

---

## When to escalate

- 3+ consecutive renders show the same drift on the same source still → swap source still
- Same drift appears across multiple source stills with same motion template → motion template might be incompatible with current Seedance build; pick a different template
- Persistent face-morph across all motion templates → escalate to Higgsfield Soul retraining (Soul-2 model itself may need anchor-photo refresh)

Don't burn credits regen-ing on a broken Soul or a fundamentally incompatible still+motion combo.
