# Secrets Checklist — Auto-Poster (Path A)

Set these as **GitHub Actions repo secrets** (`Settings → Secrets and variables → Actions → New repository secret`) before the first cron tick.

| Secret | Where to obtain | Notes |
|---|---|---|
| `NOTION_TOKEN` | https://www.notion.so/my-integrations → New integration → "Recruitin Auto-Poster". Capabilities: Read content, Update content, Insert content. | Starts with `secret_…` (legacy) or `ntn_…`. After creation, share the Content-Calendar DB with the integration via DB → `…` → `Connections` → add. |
| `NOTION_DB_ID` | Open the DB in Notion → copy URL. The 32-char hex string between the slash and the `?` is the DB ID. | Format: 8-4-4-4-12 with or without dashes. Both work in `notion-client`. |
| `LINKEDIN_ACCESS_TOKEN` | https://www.linkedin.com/developers/apps → create app under Recruitin Page → Products → request "Share on LinkedIn". OAuth flow scopes: `w_member_social`, `r_basicprofile`. | **Personal** access token. Expires every 60 days — set a calendar reminder to refresh. For company-page posting, request "Marketing Developer Platform" instead (longer review). |
| `LINKEDIN_AUTHOR_URN` | After OAuth: GET `https://api.linkedin.com/v2/userinfo` (with token), `sub` field is the member id. URN format: `urn:li:person:{id}`. For org page posts: `urn:li:organization:{org_id}`. | The script uses this verbatim as the post author. |
| `META_PAGE_TOKEN` | https://developers.facebook.com → create Business app → request `pages_manage_posts` + `pages_read_engagement`. Use Graph API Explorer: select your Page, exchange short-lived token for long-lived (60d) Page token. | Document the Page → `/me/accounts` returns the Page-scoped token. |
| `META_PAGE_ID` | https://www.facebook.com/{your-page} → About → Page transparency → Page ID. Or via Graph API `/me/accounts`. | Numeric, ~15 digits. |

---

## Local-dev test

Before flipping the GH Actions cron live, run once locally with dry-run:

```bash
cd 07-automation-pipeline/auto-poster
python3 -m venv .venv && source .venv/bin/activate
pip install "notion-client>=2.2.1" "requests>=2.32.0"

export NOTION_TOKEN="..."
export NOTION_DB_ID="..."
export LINKEDIN_ACCESS_TOKEN="..."
export LINKEDIN_AUTHOR_URN="urn:li:person:..."
export META_PAGE_TOKEN="..."
export META_PAGE_ID="..."
export DRY_RUN=true

python scripts/auto_poster.py
```

You should see lines like:

```
[INFO] Auto-poster start. DRY_RUN=True
[INFO] Found 1 eligible row(s)
[INFO] Processing row Day 1 — Manifesto (LI) (Ready) → ['LinkedIn']
[INFO] [DRY] Would post 1850-char body to LinkedIn:
Vandaag herlanceer ik mezelf op LinkedIn als Recruitment Engineer....
```

After that, set the actual GH secrets and run `gh workflow run auto-poster.yml -f dry_run=true` for the same dry-run sanity check in CI.

---

## Token rotation cadence

| Token | Expiry | What to do |
|---|---|---|
| `NOTION_TOKEN` | No expiry (manual revoke) | Rotate every 90 days as a security baseline. |
| `LINKEDIN_ACCESS_TOKEN` | 60 days | Calendar reminder. When script starts returning Status=Failed with `401 invalid_token`, refresh via OAuth flow and update GH secret. |
| `META_PAGE_TOKEN` | 60 days (long-lived) | Same as LinkedIn. Can be programmatically extended via `/oauth/access_token?grant_type=fb_exchange_token` if you store the FB App secret. |

---

## Security baseline

- These tokens grant **post-on-behalf-of** rights. Treat as production-grade.
- Never paste them into Notion notes, Slack, or unencrypted files.
- The auto-poster repo MUST be private (the GitHub Actions log can leak token fragments if a step explicitly echoes them — the workflow we ship does not).
- If a token is leaked: revoke immediately
  - LinkedIn: developer portal → app → Auth → revoke
  - Meta: developers.facebook.com → app → Settings → revoke OR remove app permission from the Page
  - Notion: my-integrations → integration → Security → "Revoke secret"

---

## Followups

- Add `RESEND_API_KEY` if/when we want failure alerts emailed to `warts@recruitin.nl` instead of just GH Actions logs.
- Add `SLACK_WEBHOOK_URL` if we want failure pings in `C0AMP0SEUP5` (the live monitoring channel — see CLAUDE.md SLACK_WEBHOOK_REGEL).
