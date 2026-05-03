# Audience Exports — Meta Custom Audience

Generated CSVs in this directory are **PII (even hashed)** and are gitignored. Never commit them.

## Source

- Resend audience: **Stack 2026 Leads** (`703b9a1f-fc00-4796-8bf3-664350a89879`)
- Hash spec: SHA256 of `email.strip().lower()` per [Meta hashing guidelines](https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences/#hash)

## How to run

```bash
cd /Users/wouterarts/projects/recruitmentengineer
source ~/recruitin/.env       # loads RESEND_API_KEY
python3 scripts/export_audience_meta.py
```

CLI flags (all optional):

- `--audience <id>` — override default audience ID
- `--output <path>` — override default output path
- `--no-plaintext` — write only the `email_sha256` column (default writes both)

Default output path: `09-launch/audience-exports/audience-meta-YYYY-MM-DD.csv` (UTC date).

## How to upload to Meta

1. Ads Manager → **Audiences** → **Create Audience** → **Custom Audience**
2. Source: **Customer List**
3. Upload the CSV from this directory
4. Map columns:
   - `email_sha256` → **Email (already hashed)**
   - `email` → **Email** (Meta also hashes this server-side; both columns max match rate)
5. Name it e.g. `RE Stack 2026 Leads — YYYY-MM-DD`
6. Once populated (~30 min), build a **Lookalike** (1–3% NL) and use as targeting on retargeting ad-sets.

## Cadence

**Re-export weekly** so the Lookalike refreshes against new sign-ups. Replace the
existing Custom Audience or upload as a new one (Meta dedupes by hash).

## Notes

- Unsubscribed contacts are skipped automatically
- Invalid / missing emails are skipped
- Empty audience produces a CSV with header row only (still safe to upload — Meta will refuse, no harm)
