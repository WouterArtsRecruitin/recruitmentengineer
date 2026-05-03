# Format Cheatsheet — Seedance Motion × Ad-Format × Audience-Tier

Single-page lookup. Pick the right motion template for the right ad-format and the right audience tier (TOFU / MOFU / BOFU).

> **Rule of thumb:** motion intensity should DECREASE as you move down the funnel. TOFU = bold parallax / environmental motion (thumb-stop). MOFU = subject engagement (gaze, tool). BOFU = quiet authority (push-in).

---

## Master matrix

| Format | Audience | Motion | Source still (Set A / Set C) | Duration | Why |
|--------|----------|--------|------------------------------|----------|-----|
| **9:16 Reel** | TOFU cold | M3 Parallax pan | A01 / A05 / A08 | 6s | Fast lateral motion = thumb-stop on Reels |
| **9:16 Reel** | TOFU cold | M6 Environmental | C.1 hook-card OR A05 | 8s | Subject still + chaos = curiosity |
| **9:16 Reel** | MOFU warm | M1 Push-in slow | A03 / A07 / C.2 | 6s | Pull-in for retargeted viewers |
| **1:1 Feed** | TOFU cold | M6 Environmental | A05 / A08 | 8s | Square + alive bg = scroll-pause |
| **1:1 Feed** | MOFU warm | M4 Subject-shift gaze | A06 / A10 / C.4 | 5s | Gaze-shift = "noticed you" |
| **1:1 Feed** | BOFU lead-magnet | M1 Push-in slow | A01 / A07 / C.4 | 6s | Authority push for warm audience |
| **16:9 LinkedIn** | TOFU/MOFU | M2 Slow zoom-out | A02 / A04 / A06 | 7s | Reveal context + setting |
| **16:9 LinkedIn** | BOFU authority | M1 Push-in slow | A03 / A07 / C.5 | 6s | Cinematic slow push for sponsored |
| **16:9 LinkedIn** | BOFU case-study | M5 Tool-in-hand | A02 / A03 / C.6 | 6s | "Look, the work happens" |
| **4:5 Feed-large** | TOFU cold | M3 Parallax pan | A01 / A05 / A08 | 6s | Tall format + parallax = scroll-stop |
| **4:5 Feed-large** | MOFU warm | M5 Tool-in-hand | A02 / A03 / A09 / C.8 | 6s | Subtle "active" feel for warm leads |
| **4:5 Feed-large** | BOFU stat-proof | M1 Push-in slow | A01 / A07 / C.8 | 6s | Quiet authority + numbers |

---

## By audience tier

### TOFU (cold, thumb-stop priority)
**Pick high-motion templates.** First 1.5 seconds must register motion.

| Format | Best motion | Source still |
|--------|------------|--------------|
| 9:16 Reel | M3 Parallax / M6 Environmental | A05 klant-locatie, A08 fabrieks-vloer |
| 1:1 Feed | M6 Environmental | A01 productiehal, A05 klant-locatie |
| 4:5 Feed-large | M3 Parallax | A01 productiehal, A05 klant-locatie |

### MOFU (warm, engagement priority)
**Pick subject-engagement templates.** Viewer already knows you; show them you "see" them.

| Format | Best motion | Source still |
|--------|------------|--------------|
| 1:1 Feed | M4 Subject-shift gaze | A06 conferentie, A10 kantoor-deurpost, C.4 |
| 4:5 Feed-large | M5 Tool-in-hand | A02 werkplaats, A03 blueprint-tafel, A09 magazijn-rek, C.8 |
| 9:16 Reel | M1 Push-in slow | A03 blueprint-tafel, A07 podium, C.2 |

### BOFU (lead-magnet / case-study / sponsored authority)
**Pick quiet, authoritative motion.** Trust signal > attention grab.

| Format | Best motion | Source still |
|--------|------------|--------------|
| 16:9 LinkedIn | M1 Push-in slow | A03 blueprint-tafel, A07 podium, C.5 |
| 16:9 LinkedIn | M5 Tool-in-hand (case-study) | A02 werkplaats, A03 blueprint-tafel, C.6 |
| 4:5 Feed-large | M1 Push-in slow (stat-proof) | A01 productiehal, A07 podium, C.8 |
| 1:1 Feed | M1 Push-in slow (lead-magnet) | A01 productiehal, A07 podium, C.4 |

---

## By motion template (reverse lookup)

### M1 Push-in slow → BOFU formats
- 16:9 LinkedIn sponsored authority
- 4:5 Feed-large stat-proof
- 1:1 Feed BOFU lead-magnet
- 9:16 Reel MOFU warm pull-in

### M2 Slow zoom-out reveal → MOFU/BOFU LinkedIn case-study
- 16:9 LinkedIn TOFU/MOFU "context reveal"
- 4:5 Feed-large case-study reveal (rare, prefer M5)

### M3 Parallax pan → TOFU thumb-stop
- 9:16 Reel TOFU cold
- 4:5 Feed-large TOFU cold

### M4 Subject-shift gaze → MOFU engagement
- 1:1 Feed MOFU warm
- 4:5 Feed-large MOFU warm engagement (alternative to M5)

### M5 Tool-in-hand → MOFU/BOFU "active work" feel
- 16:9 LinkedIn BOFU case-study
- 4:5 Feed-large MOFU warm
- 1:1 Feed MOFU warm (alternative to M4)

### M6 Environmental motion → TOFU "still authority + chaos"
- 1:1 Feed TOFU cold typography ads
- 9:16 Reel TOFU cold (alternative to M3)
- 4:5 Feed-large TOFU (rare, prefer M3)

---

## Quick selection logic

```
Step 1: What's the format? (Reel / Feed / LinkedIn / Feed-large)
Step 2: What's the audience tier? (TOFU / MOFU / BOFU)
Step 3: Look up the cell in the master matrix → get motion template + recommended still
Step 4: Open motion-templates.md → grab the prompt + identity-string
Step 5: Open Set A or Set C → grab the matching Soul-rendered still from inputs/
Step 6: Submit to Seedance
Step 7: Run identity-preservation-rules.md QA
Step 8: Export at recommended bitrate (see seedance README)
```

---

## Combination examples

### "I want a TOFU 9:16 hook for cold Meta audience"
→ M3 Parallax pan, source still A08 fabrieks-vloer walking-away (6s, 30fps, 1080×1920, 6–8 Mbps)

### "I want a BOFU LinkedIn 16:9 sponsored authority ad"
→ M1 Push-in slow, source still A07 podium looking-at-camera (6s, 24fps, 1920×1080, 8–10 Mbps)

### "I want a MOFU 1:1 Feed engagement clip with subtle motion"
→ M4 Subject-shift gaze, source still A06 conferentie in-conversation (5s, 30fps, 1080×1080, 4–6 Mbps)

### "I want a TOFU 1:1 Feed clip where Wouter is the still rock and the world moves"
→ M6 Environmental motion, source still A05 klant-locatie three-quarter (8s, 30fps, 1080×1080, 4–6 Mbps)

### "I want a MOFU/BOFU 4:5 stat-proof ad with subtle 'live demo' feel"
→ M5 Tool-in-hand, source still C.8 (Set C portrait+stat 4:5) OR A09 magazijn-rek holding-laptop (6s, 30fps, 1080×1350, 6–8 Mbps)

---

## Anti-patterns (do NOT combine)

| Don't combine | Why |
|---------------|-----|
| TOFU + M1 Push-in slow | Too quiet for thumb-stop on cold feeds |
| BOFU + M3 Parallax pan | Too kinetic for trust-building authority moments |
| Reel 9:16 + M2 Slow zoom-out | Vertical reels feel stuck with zoom-out reveals — use M3 instead |
| Set B brand-visual still + any motion | Set B is non-portrait (data-viz, typography). Don't motion these — Seedance is for portraits with face-anchoring. Use static export or Lottie for data-viz motion. |
| Soul-less ad still (C.1, C.3, C.7) + any motion | Typography-only stills don't have a face to preserve — Seedance just adds noise. Keep these as static images or use After Effects type-on. |

---

## Audio recommendations (per format)

| Format | Audio | Why |
|--------|-------|-----|
| 9:16 Reel | Optional voice-over (48kHz AAC stereo) | Reels often watched with sound |
| 1:1 Feed | Silent | Feed mostly muted |
| 16:9 LinkedIn | Optional VO | LinkedIn often watched with sound on desktop |
| 4:5 Feed-large | Silent | Feed mostly muted |

If using VO: record separately, sync in post (DaVinci / FCP). Wouter's voice = same authority register as visual — never radio-DJ, never influencer.
