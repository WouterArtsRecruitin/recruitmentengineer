# Notion Content Calendar — DB Schema

**Database name:** `Recruitin Authority — Content Calendar`
**Owner:** Ing. W. Arts
**Workspace:** Recruitin
**Integration:** Create a new internal integration at https://www.notion.so/my-integrations → "Recruitin Auto-Poster" → grant Read content + Update content + Insert content. Share this DB with the integration.

---

## Property schema

| # | Property | Type | Configuration | Notes |
|---|---|---|---|---|
| 1 | **Title** | Title | — | Internal-only post-title, e.g. `Day 1 — Manifesto (LI)` |
| 2 | **Status** | Status | Options: `Draft`, `Ready`, `Published`, `Failed`, `Failed-Partial`, `Archived` | Auto-poster only acts on `Ready` rows |
| 3 | **Platform** | Multi-select | Options: `LinkedIn`, `Meta`, `Both` | If `Both`, poster pushes to both |
| 4 | **Format** | Select | Options: `Long-post`, `Carousel`, `Reel`, `Image`, `Video`, `Story` | Drives which API endpoint poster uses |
| 5 | **Tone-mix** | Multi-select | Options: `Rustig autoriteit`, `Brutaal direct`, `Specialist confronterend`, `Energiek bewijsdrang`, `Engineer logisch` | Editorial tag, not used by poster — keeps editor honest |
| 6 | **Body** | Rich text | — | Final copy. May contain `{LINK}` placeholder which poster replaces with `Generated-link` |
| 7 | **Hook** | Rich text | — | First 3 lines (target < 200 chars). Editor-only; not separately submitted |
| 8 | **CTA** | Rich text | — | Trailing call-to-action sentence |
| 9 | **Media** | Files & media | Accepts image/video upload | Single file for v1; multi-file (carousel) is v2 |
| 10 | **Scheduled-time** | Date | "Include time" = ON, "Date format" = ISO | When `now ≥ this`, poster eligibility opens |
| 11 | **UTM-source** | Formula | `lower(replaceAll(prop("Platform").map(p, p), ",", "-"))` (see formula below) | Auto-derived |
| 12 | **UTM-campaign** | Text | Manual, e.g. `stack-2026-launch` | Set per campaign |
| 13 | **UTM-content** | Formula | Slug of Title (see formula below) | Auto-derived |
| 14 | **Generated-link** | Formula | Concatenates landing URL + UTM params (see formula below) | What poster injects in body |
| 15 | **Post-URL** | URL | Empty until publish | Set by poster on success; idempotency key |
| 16 | **Performance** | Rich text | — | Rolled up daily by separate cron (out of scope v1). v1 leaves blank |
| 17 | **Notes** | Rich text | — | Free-form. Poster appends error reasons here on failure |

---

## Formulas (copy-paste into Notion)

### `UTM-source` (formula)

When `Platform` = LinkedIn → `linkedin`
When `Platform` = Meta → `meta`
When `Platform` = Both → `cross` (poster will override per-platform — see `auto_poster.py` `_build_link_for_platform`)

```
if(prop("Platform").includes("LinkedIn") and prop("Platform").includes("Meta"), "cross",
  if(prop("Platform").includes("LinkedIn"), "linkedin",
    if(prop("Platform").includes("Meta"), "meta", "unknown")))
```

### `UTM-content` (formula — slug of Title)

```
lower(replaceAll(replaceAll(replaceAll(replaceAll(prop("Title"),
  "[ÀÁÂÄÃÅàáâäãåÒÓÔÖÕòóôöõÈÉÊËèéêëÌÍÎÏìíîïÙÚÛÜùúûüÑñÇç]", ""),
  "[^a-zA-Z0-9 -]", ""),
  " +", "-"),
  "-+", "-"))
```

(Notion's regex inside `replaceAll` is JS-flavored; the diacritic stripper above is a pragmatic compromise. For exotic titles, set `UTM-content` manually as text and skip this formula.)

### `Generated-link` (formula)

```
"https://recruitmentengineer.nl?utm_source=" + prop("UTM-source")
  + "&utm_medium=organic"
  + "&utm_campaign=" + prop("UTM-campaign")
  + "&utm_content=" + prop("UTM-content")
```

Result example: `https://recruitmentengineer.nl?utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-1-manifesto-li`

---

## Default views

| View name | Type | Filter | Sort |
|---|---|---|---|
| 🟢 Queue | Table | Status = Ready | Scheduled-time ↑ |
| ✏️ Drafts | Table | Status = Draft | Scheduled-time ↑ |
| 📅 Calendar | Calendar | (none) | by Scheduled-time |
| ✅ Published | Table | Status = Published | Scheduled-time ↓ |
| 🚨 Failed | Table | Status ∈ {Failed, Failed-Partial} | Scheduled-time ↓ |
| 📊 Performance | Table | Status = Published, Post-URL is not empty | Scheduled-time ↓ |

---

## Sample seed data — Fase 1 hero posts (5 rows)

Pre-load these 5 rows after creating the DB. Body is intentionally pulled from `06-hero-posts/PAD-B-LAUNCH-SCHEDULE.md` so the canonical-source remains that file. Body trimmed here for schema-doc readability.

> **Replace `{NEXT_TUE_HHMM}` etc. with concrete ISO timestamps before saving.** All times Europe/Amsterdam.

### Row 1 — Day 1 Manifesto

| Field | Value |
|---|---|
| Title | `Day 1 — Manifesto (LI)` |
| Status | `Draft` (flip to `Ready` after profile-banner upload) |
| Platform | `LinkedIn` |
| Format | `Long-post` |
| Tone-mix | `Rustig autoriteit`, `Brutaal direct` |
| Body | (full text from PAD-B Day 1 — ends with) `Link in de comments.` Last line of body must include `{LINK}` placeholder for the auto-poster: append `\n\nStack 2026 → {LINK}` to the manifesto body. |
| Hook | `Vandaag herlanceer ik mezelf op LinkedIn als Recruitment Engineer. Niet als grap.` |
| CTA | `Stack 2026 → {LINK}` |
| Media | (optional) Hero portrait #1 |
| Scheduled-time | `2026-05-05T08:00:00+02:00` (next Tuesday 08:00 NL — adjust) |
| UTM-source | (formula → `linkedin`) |
| UTM-campaign | `stack-2026-launch` |
| UTM-content | (formula → `day-1-manifesto-li`) |
| Generated-link | (formula → `https://recruitmentengineer.nl?utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-1-manifesto-li`) |
| Post-URL | (empty) |
| Notes | `First post of campaign. Comment-1 manual: "Stack 2026 → {LINK}". Comment-2 after 2h: see PAD-B.` |

### Row 2 — Day 2 €519k Story

| Field | Value |
|---|---|
| Title | `Day 2 — €519k Pipeline Story (LI)` |
| Status | `Draft` |
| Platform | `LinkedIn` |
| Format | `Long-post` |
| Tone-mix | `Rustig autoriteit`, `Engineer logisch` |
| Body | PAD-B Day 2 body + trailing `\n\nStack 2026 → {LINK}` |
| Hook | `6 maanden stilstand. €519.000 stuck pipeline. Vacatures die niet vol kwamen.` |
| CTA | `Stack 2026 → {LINK}` |
| Scheduled-time | `2026-05-06T17:30:00+02:00` |
| UTM-campaign | `stack-2026-launch` |

### Row 3 — Day 3 Boolean Tip

| Field | Value |
|---|---|
| Title | `Day 3 — Boolean Search Tip (LI)` |
| Status | `Draft` |
| Platform | `LinkedIn` |
| Format | `Long-post` |
| Tone-mix | `Engineer logisch`, `Specialist confronterend` |
| Body | PAD-B Day 3 body + `\n\nStack 2026 → {LINK}` |
| Hook | `90% van de recruiters maakt deze fout met boolean searches.` |
| CTA | `Module 1 + 4 andere prompts → {LINK}` |
| Scheduled-time | `2026-05-07T08:00:00+02:00` |
| UTM-campaign | `stack-2026-launch` |

### Row 4 — Day 4 Contrarian

| Field | Value |
|---|---|
| Title | `Day 4 — ChatGPT Contrarian (LI)` |
| Status | `Draft` |
| Platform | `LinkedIn` |
| Format | `Long-post` |
| Tone-mix | `Brutaal direct`, `Specialist confronterend` |
| Body | PAD-B Day 4 body + `\n\nStack 2026 → {LINK}` |
| Hook | `Onpopulaire mening: ChatGPT maakt de meeste recruiters slechter, niet beter.` |
| CTA | `Stack 2026 → {LINK}` |
| Scheduled-time | `2026-05-08T09:00:00+02:00` |
| UTM-campaign | `stack-2026-launch` |

### Row 5 — Day 5 Results

| Field | Value |
|---|---|
| Title | `Day 5 — Week-1 Results (LI)` |
| Status | `Draft` |
| Platform | `LinkedIn` |
| Format | `Long-post` |
| Tone-mix | `Rustig autoriteit`, `Energiek bewijsdrang` |
| Body | PAD-B Day 5 body + `\n\nWil je geen post missen? Schrijf je in via {LINK}` |
| Hook | `4 dagen geleden lanceerde ik mezelf als Recruitment Engineer.` |
| CTA | `Schrijf je in via {LINK}` |
| Scheduled-time | `2026-05-11T08:00:00+02:00` |
| UTM-campaign | `stack-2026-launch` |

---

## Important behavioral notes

1. **`{LINK}` placeholder convention:** the auto-poster does a literal `body.replace("{LINK}", row.Generated-link)`. If a body has no `{LINK}`, the poster appends `\n\n{Generated-link}` to the end. This guarantees every post carries the UTM-tagged URL exactly once.

2. **Status=Ready is the trigger.** Drafts are ignored. Setting Status=Ready while Scheduled-time is in the past = post within 15 minutes (next cron tick).

3. **Idempotency:** if a row already has `Post-URL` filled, the poster skips it even if Status=Ready. To genuinely re-post, clear `Post-URL` first.

4. **Failed rows:** on failure, Status flips to `Failed` and `Notes` gets a timestamped error line appended. The row stays out of the queue. Operator inspects → fixes → flips back to `Ready` to retry.

5. **`Both` platform behavior:** poster does LinkedIn first, then Meta. If LinkedIn succeeds and Meta fails → Status=`Failed-Partial`, `Post-URL`=LinkedIn URL, `Notes`=Meta error. If both fail → Status=`Failed`, both errors in Notes. The script never re-posts to a platform whose URL is already in Post-URL.

6. **Carousel posts (v1):** out of scope. Mark `Format=Carousel` rows as `Status=Draft` until v2 ships, or post manually using the body from Notion. The poster v1 will skip Carousel/Video/Reel/Story formats and write `Notes=skipped: format <X> requires v2 carousel adapter`.
