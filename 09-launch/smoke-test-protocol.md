# Smoke-Test Protocol — Day 1 Pre-Launch

> 15-min end-to-end pipeline check. Run this before publishing Hero Post 1. **All 12 steps must pass GREEN.**

---

## Test setup

- **Test email:** `warts+smoke-day1@recruitin.nl` (Gmail-style plus-tag — same inbox, separate trace)
- **Test UTM:** `?utm_source=test&utm_campaign=smoke-test&utm_medium=manual&utm_content=day-1-pre-launch`
- **Browser:** Incognito Chrome (clean cookies, clean cache, clean localStorage/sessionStorage)
- **Tools open:**
  - Chrome DevTools → Network tab + Console tab
  - Pixel Helper extension
  - LinkedIn Insight Tag Helper extension
  - Pipedrive open in second tab → Pipeline 16
  - Resend dashboard open in third tab
  - Meta Events Manager → Test Events tab open
  - LinkedIn Campaign Manager → Insight Tag → Live activity

---

## Steps

### 1. Open landing in incognito
**Action:** Open `https://recruitmentengineer.nl/?utm_source=test&utm_campaign=smoke-test&utm_medium=manual&utm_content=day-1-pre-launch` in fresh incognito tab.

**Expect:**
- Page loads < 2s (mobile-emulated should also be < 2s)
- No console errors (red 4xx/5xx in Network tab)

---

### 2. Verify HTTP 200 + meta + tracking scripts loaded
**Action:** DevTools Network tab → filter "Doc" → see main HTML response.

**Expect:**
- `recruitmentengineer.nl` → 200 OK
- Response headers include `content-type: text/html; charset=utf-8`
- `<head>` contains:
  - `<meta property="og:image" content="..."/>` (1200×630)
  - `<meta name="twitter:card" content="summary_large_image"/>`
  - Inter font preconnect (font-loading via fonts.googleapis.com OR self-hosted)
  - Meta Pixel `fbq('init', '238226887541404')` script
  - LinkedIn Insight Tag script (with real Partner ID, NOT placeholder)
  - GA4 SKIPPED — block is HTML-comment, no JS execution

---

### 3. Submit form
**Action:** Fill form with `warts+smoke-day1@recruitin.nl`, submit.

**Expect:**
- POST `/api/subscribe` fires → 200 response (not 400/500/429)
- Response body: `{"success": true}`
- Form replaces with success-message inline

---

### 4. Verify response 200 + success-message
**Action:** DevTools Network → click `/api/subscribe` row → Preview tab.

**Expect:**
- Status: 200
- Response: `{"success": true}`
- Response time < 3s (Resend-send + Pipedrive-create combined)

---

### 5. Check inbox for PDF email
**Action:** Open `warts@recruitin.nl` inbox (Gmail/Outlook). Look for new mail from `wouter@recruitmentengineer.nl`.

**Expect:**
- Subject: `📥 Recruitment Engineering Stack 2026 — jouw download`
- From: `Wouter Arts <wouter@recruitmentengineer.nl>`
- Reply-to: `warts@recruitin.nl` (verify by hitting Reply — recipient should be `warts@recruitin.nl`)
- Attachment: `Recruitment-Engineering-Stack-2026.pdf` (~1-2MB)
- Body renders correctly (no broken HTML, brand-styling intact)
- Footer contains valid Resend unsubscribe link

---

### 6. Check Resend audience
**Action:** Resend dashboard → Audiences → "Stack 2026 Leads" → Contacts.

**Expect:**
- New row: `warts+smoke-day1@recruitin.nl` (status: subscribed)
- `first_name`: "Warts" (auto-derived from email-local — known limitation: plus-tag stripped)
- `created_at`: within last 60s

---

### 7. Check Pipedrive pipeline
**Action:** Pipedrive → Pipelines → "Authority Leads — Stack 2026" → Cold stage.

**Expect:**
- New deal: `Stack 2026 download — warts+smoke-day1@recruitin.nl`
- Stage: `223` (Cold)
- `lead_score`: `20` (if custom-field-key configured) OR empty (if not yet)
- Person attached: `Warts` with email `warts+smoke-day1@recruitin.nl` (label: work)

---

### 8. Check deal-note for UTM block
**Action:** Open the deal → Notes section.

**Expect:**
- Note 1: `Authority Lead — Stack 2026 download via recruitmentengineer.nl (source: landing)`
- Followed by:
  ```
  --- UTM / attribution ---
  utm_source: test
  utm_medium: manual
  utm_campaign: smoke-test
  utm_content: day-1-pre-launch
  ```

---

### 9. Check Meta Events Manager → Test Events
**Action:** Meta Events Manager → Pixel `238226887541404` → Test Events tab.

**Expect:**
- Within 60s: `Lead` event arrives
- Match score: > 80% (hashed email + IP + UA)
- Action source: `website` (server-side via CAPI) or `client` (client-side via fbq)
- Custom data: `content_name: stack-2026`, `value: 49`, `currency: EUR`

**If client-side only fires:** CAPI not yet wired in `subscribe.js` — acceptable for v1 launch but flag for fase 2.

---

### 10. Check LinkedIn Insight Tag → traffic ping
**Action:** LinkedIn Campaign Manager → Account assets → Insight Tag → "Tag activity" / "Live activity".

**Expect:**
- Within 60s: traffic ping recorded for recruitmentengineer.nl visit
- Conversion event `Stack 2026 PDF Download` fires (if conversion-fire is wired in form-handler)

---

### 11. Confirm GA4 (if enabled — SKIPPED for v1)
**Action:** Skip step 11 — GA4 deliberately not enabled in v1 launch.

**(Future v2):**
- GA4 → Admin → DebugView → see `generate_lead` event arrive within 60s
- DebugView shows event-params: `value: 49`, `currency: EUR`, UTM-params

---

### 12. Cleanup
**Action:**
- Pipedrive → archive smoke-test deal (don't delete — keep audit-trail). Click deal → "More actions" → "Archive deal".
- Resend → Audience → remove `warts+smoke-day1@recruitin.nl` contact (don't keep test-data in production audience). Click contact → "Delete contact".
- Pipedrive → archive smoke-test person if no other deals attached.

**Verify cleanup:**
- Pipeline 16 → Cold stage no longer shows smoke-test deal
- Resend audience contact-count returns to pre-test number

---

## Pass criteria

**ALL 12 steps must show GREEN before publishing Hero Post 1.**

If ANY step fails:
1. Don't launch.
2. Diagnose using `09-launch/launch-checklist.md` "Fallbacks" table.
3. Fix root-cause.
4. Re-run smoke-test from step 1.

---

## Troubleshooting cheatsheet

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Step 3: 400 invalid_email | Form-input validation regex too strict | Check `subscribe.js` regex line 93 |
| Step 3: 429 rate_limited | Same IP > 3 submits in 60s | Wait 60s or change IP (mobile data tether) |
| Step 5: no email arrives | Resend domain not verified OR DKIM missing | Resend dashboard → Domain → verify DKIM all green |
| Step 6: contact not in audience | RESEND_AUDIENCE_ID env-var wrong | Vercel env → re-check UUID matches dashboard |
| Step 7: deal not in Pipedrive | PIPEDRIVE_API_KEY invalid OR auth pattern wrong | Check `PIPEDRIVE_AUTH_REGEL` — query-param style for personal token |
| Step 7: deal in wrong stage | PIPEDRIVE_STAGE_ID env not set OR wrong | Vercel env → set to `223` |
| Step 9: Meta Lead event not arriving | Pixel-ID is page-id (660118697194302) not pixel-id | Verify `fbq('init', '238226887541404')` |
| Step 10: LinkedIn tag silent | Partner ID still placeholder | sed-replace `LI_PARTNER_ID_PLACEHOLDER` in index.html |

---

## Smoke-test re-runs

Run this protocol:
- **Pre-launch (Day 0)** — must pass before Hero Post 1
- **Post any code-deploy to landing-page** — verify regression-free
- **After any env-var change in Vercel** — verify env-vars still loaded
- **Day 7** — quick re-verify nothing has broken silently
