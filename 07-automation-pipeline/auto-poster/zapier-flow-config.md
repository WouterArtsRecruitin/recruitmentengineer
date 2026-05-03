# Path B — Zapier Auto-Poster Flow

> Use this if you want a no-code path to publishing the Notion content calendar. Path A (GitHub Actions) is recommended for this project; this doc is here for fallback / handoff to non-engineer operators.

---

## Cost estimate

- Zapier Pro plan (€23.50/mo, 2,000 tasks): supports paths + multi-step zaps. Required, the free plan does not.
- Each published row consumes ~3–5 tasks (trigger + filter + 1–2 actions + Notion update).
- 5 posts/week × 4 weeks ≈ 20 publishes/mo ≈ 100 tasks → fits comfortably.

---

## Pre-requisites

1. **Notion** — same `Recruitin Authority — Content Calendar` DB as Path A. Status property has option `Ready`.
2. **Zapier connections** (Settings → My Apps):
   - Notion (OAuth flow, grant access to the workspace + DB).
   - LinkedIn (OAuth, scopes: `w_member_social` for personal — note: Zapier currently **does not** support posting as a Company Page; if you need that, use Path A).
   - Facebook Pages (OAuth, scope: `pages_manage_posts`).
3. The DB schema must already be set up per `notion-db-schema.md`.

---

## Zap 1 — LinkedIn publisher

**Name:** `Auto-Poster · Notion → LinkedIn`

### Step 1 — Trigger: Notion "Updated Database Item"

- App: Notion
- Event: `Updated Database Item`
- Account: your Notion connection
- Database: `Recruitin Authority — Content Calendar`
- Trigger property: `Status`

### Step 2 — Filter: only continue if eligible

Conditions (all must match):

- `Status` text exactly matches `Ready`
- `Platform` text contains `LinkedIn`
- `Scheduled-time` (Date) — `Continue ONLY IF... (Date) before now` (Zapier built-in)
- `Post-URL` exactly matches *(empty)* (idempotency)

### Step 3 — Formatter: build LinkedIn body

- App: Formatter by Zapier → Text → Replace
- Input: `Body` rich-text from step 1
- Find: `{LINK}`
- Replace with: `Generated-link` from step 1

### Step 4 — Action: Create Share Update (LinkedIn)

- App: LinkedIn
- Event: `Create Share Update`
- Comment: output of step 3 (LinkedIn-flavored body with link)
- Visibility: Public
- (If row has Media): use the Media URL as image attachment.

### Step 5 — Action: Update Database Item (Notion)

- App: Notion
- Event: `Update Database Item`
- Database: same DB
- Item: page id from step 1
- Status → `Published`
- Post-URL → URL output from step 4 (use Zapier's "Update URL" or "Permalink" field — LinkedIn returns `https://www.linkedin.com/feed/update/urn:li:share:...`)

### Step 6 — Path: Failure handler

- Use Zapier "Paths" (Pro feature). Add a path triggered when step 4 errors out.
- Path A (success) → step 5 above.
- Path B (failure) → Notion update: Status=`Failed`, Notes ← append timestamp + error.

---

## Zap 2 — Meta publisher

Mirror of Zap 1, but:

- Step 2 filter: `Platform` contains `Meta` (instead of LinkedIn)
- Step 4: app = Facebook Pages, event = `Create Page Post` (text + link). For image, use `Create Page Photo`.
- Step 5: same Notion update with Meta's returned URL.

---

## Zap 3 (optional) — Performance rollup

Run daily at 09:00 NL.

- Trigger: Schedule by Zapier → Every Day at 09:00.
- Step 1: Notion → Find Database Items where `Status=Published` and `Performance` is empty and `Scheduled-time` ≤ 24h ago.
- Step 2: For each, call LinkedIn / Meta API for stats (Webhooks by Zapier → custom request).
- Step 3: Notion update → write summary string to `Performance`.

This zap consumes more tasks than Path A's GH Actions equivalent — consider Path A if you scale beyond ~20 published posts/week.

---

## Decision points where Path B is **not** sufficient

1. **Carousel posts** — Zapier's LinkedIn integration cannot publish multi-image carousels natively. Workaround: connect Buffer/Publer as the publisher (still no-code) or fall back to Path A and implement the LinkedIn `/assets?action=registerUpload` two-step.
2. **Posting as Company Page** — Zapier's LinkedIn connector only supports personal profiles. For `urn:li:organization:{recruitin}` posts, Path A.
3. **Custom UTM logic** — Path B uses the `Generated-link` Notion formula directly; if you want per-platform `utm_source` rewriting (linkedin vs meta vs cross), add a Formatter "Replace" step before the Create Share action. Path A's `_build_link_for_platform` already handles this.
4. **>500 tasks/mo** — Zapier billing climbs; Path A's GH Actions stays free.

---

## Migration path (Path B → Path A)

If you start on Zapier and outgrow it:

1. Deploy Path A as parallel runner with `DRY_RUN=true`.
2. Verify dry-run output matches what Zapier would post (manual diff for 1 week).
3. Disable Zaps. Set Path A `DRY_RUN=false`.
4. The Notion DB schema is identical, so no data migration needed.
