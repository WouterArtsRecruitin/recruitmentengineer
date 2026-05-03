# Auto-Poster — Component 4 of the Recruitin Authority Campaign

> **Mission:** Notion content calendar drives auto-posting to LinkedIn + Meta with UTM-tagged links. When a row flips to `Status=Ready` and `Scheduled-time` is in the past, the poster publishes to the right platform(s), captures the post-URL, and flips status to `Published`.

---

## Architecture (high level)

```
[Notion Content Calendar]
        │
        │ (Status=Ready & Scheduled-time <= now)
        ▼
┌───────────────────────┐
│  AUTO-POSTER WORKER   │      reads body, hook, CTA, media, generated-link
│  (GH Actions OR Zap)  │      builds platform-specific payload
└───────────────────────┘
        │
        ├──▶ LinkedIn UGC Posts API  → returns urn:li:share:...
        ├──▶ Meta Graph /feed or /photos → returns post_id
        │
        ▼
[Notion row update]
   Status = Published
   Post-URL = canonical URL
   Performance = (rolled up after 24h via separate cron)
```

Every Notion row holds a `Generated-link` formula property: a recruitmentengineer.nl URL pre-tagged with UTM params (`utm_source`, `utm_medium=organic`, `utm_campaign`, `utm_content`). The poster injects that link into the body before publishing.

---

## Two implementation paths

### Path A — GitHub Actions cron (recommended)

- `.github/workflows/auto-poster.yml` runs every 15 min + manual `workflow_dispatch`.
- Python script reads Notion via `notion-client`, posts via `requests` to LinkedIn + Meta APIs, writes back to Notion.
- Secrets in GH repo: `NOTION_TOKEN`, `NOTION_DB_ID`, `LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_AUTHOR_URN`, `META_PAGE_TOKEN`, `META_PAGE_ID`.
- Idempotent: skips rows where `Post-URL` is already filled.

**Pros:**
- Free (within 2,000 GH Actions minutes/month — at 15-min interval ≈ 2,880 runs/month, each ~30 sec → ~1,440 min, fits).
- Full audit trail per run in GH Actions UI.
- Easy to extend (add Twitter/X, Bluesky, Threads with one more requests block).
- Code in version control — reviewable, diffable, rollback-able.
- No per-task fee.

**Cons:**
- Token rotation is manual (LinkedIn 60-day expiry, Meta long-lived 60-day).
- Initial setup: ~2 hours including OAuth flow.

### Path B — Zapier flow (alternative)

- Notion trigger ("Updated Database Item" with filter `Status=Ready` and `Scheduled-time≤now`).
- Branch by `Platform` multi-select → LinkedIn action + Meta action.
- On success: Notion update step → Status=Published + Post-URL.

**Pros:**
- No code, no token management (Zapier handles refresh).
- 5–10 min setup once you have the schema.
- UI to monitor task history.

**Cons:**
- ~1.5–3 tasks per published row (trigger + branch + update). At 5 posts/week × 4 weeks = 60–100 tasks/month → fits the €23/mo Pro tier.
- Higher running cost as volume scales (€73/mo at 50k tasks).
- Limited to Zapier's LinkedIn + Meta connector capabilities (no carousels via Zapier API today — fall back to Buffer/Publer connector for those).

---

## Decision matrix — A vs B

| Factor | Path A (GH Actions) | Path B (Zapier) |
|---|---|---|
| Volume <50 posts/mo | A is fine | B is fine |
| Volume 50–500 posts/mo | A | A (Zapier cost climbs) |
| Volume >500 posts/mo | A | Don't |
| Need carousels / video / multi-image | A (raw API control) | B limited |
| Want UI for non-tech editor | B | A only via Notion (which is already the editor) |
| Already have Zapier subscription | B | — |
| Need custom branching logic (e.g. dry-run for Mondays) | A | B (clunky paths) |
| Token rotation tolerance | A (manual every 60d) | B (auto) |

**Recommendation for this project:** Path A. We are well under volume limits, want carousel + video support without paying-per-task, and the rest of the Recruitin stack (DGR, KT, Meta-monitor) is already on GH Actions cron. Consistency wins.

Path B is documented in `zapier-flow-config.md` for situations where Wouter wants the team to operate without engineer involvement.

---

## File index

| File | Purpose |
|---|---|
| `notion-db-schema.md` | Full Notion DB schema + sample seed rows (5 hero posts) |
| `github-actions-workflow.yml` | `.github/workflows/auto-poster.yml` — ready to commit |
| `scripts/auto_poster.py` | The actual worker — Python 3.12 + `notion-client` + `requests` |
| `utm-generator.js` | Standalone CLI / Notion-formula reference for UTM URLs |
| `zapier-flow-config.md` | Path B step-by-step zap config |
| `secrets-checklist.md` | What to obtain + where to set up tokens before launching |

---

## Quickstart (Path A)

1. Read `secrets-checklist.md`. Obtain LinkedIn + Meta tokens, Notion integration token, Notion DB ID.
2. In Notion: create the "Content Calendar" database following `notion-db-schema.md`.
3. Share the database with your Notion integration (`...` → Connections → add).
4. Drop `auto_poster.py` into your repo at `scripts/auto_poster.py` and the workflow at `.github/workflows/auto-poster.yml`.
5. Add the 6 GH secrets listed above.
6. Manual dry-run: `gh workflow run auto-poster.yml -f dry_run=true`. Verify logs show "would post X to LinkedIn".
7. Live: drop a test row in Notion (e.g. "TEST — please delete"), set Status=Ready + Scheduled-time=5 min from now. Wait. Confirm post + Notion row update.
8. Seed the 5 hero posts (see `notion-db-schema.md` → Sample seed data).

---

## Failure modes + how the script handles them

- **Notion API 5xx** → retry with exponential backoff (3 attempts, 2/4/8 sec).
- **LinkedIn 401** (token expired) → mark row Status=Failed + Notes=`token_expired_<date>`. Wouter rotates token, sets back to Ready.
- **Meta 190 OAuthException** → same pattern as LinkedIn.
- **Meta 100 rate limit** → backoff 5 min, leave Status=Ready (will retry next cron).
- **Both platforms requested but only one succeeds** → row gets Status=Failed-Partial + Post-URL filled with the success URL + Notes describes which platform failed.
- **Idempotency** → re-running on a row that already has Post-URL is a no-op.

---

## Followups (out of scope for v1)

- Performance rollup cron (separate workflow, runs daily at 09:00 NL, fetches likes/comments/views from each post-URL via API, writes to `Performance` rich-text field).
- Carousel-image upload via LinkedIn `/assets?action=registerUpload` two-step. Stub method `_upload_linkedin_image` is in `auto_poster.py` but path-A v1 publishes single-image / text-only posts only. Multi-image carousels: extend in v2.
- LinkedIn-as-Recruitin-company-page (currently script posts as personal author URN). Switch by changing `LINKEDIN_AUTHOR_URN` to `urn:li:organization:{id}`.
- Bluesky + Threads adapters (one more `_post_<platform>` method each).
