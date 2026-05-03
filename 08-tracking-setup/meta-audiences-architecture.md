# Meta Audiences Architecture — recruitmentengineer.nl
## 15-audience setup voor Authority Campaign Fase 1-3

> **Pixel:** `238226887541404` (shared Recruitin pixel)
> **Ad Account:** `act_1236576254450117` (Recruitin BV)
> **Status:** Spec voor handmatige Meta Ads Manager-setup. Geen bulk-CSV-import — handmatig maken voor consent + audit.
> **Reference:** `meta-pixel-events.md` voor event-payload definitions, `funnel-tier-mapping.md` voor tier-mapping.

---

## 1. Architecture overview

```
TOFU (5 audiences)        MOFU (5 audiences)        BOFU (5 audiences)
─────────────────         ─────────────────         ─────────────────
1. NL Hot 30              6.  Stack-DL 30d           11. WorkshopInquiry 90d
2. NL Tech 50-800         7.  Engaged Pageview 7d    12. Cart-abandon 30d
3. NL LinkedIn Engineer   8.  ViewContent 14d        13. Customer 1× (€97)
4. Lookalike 1% Stack     9.  AddToCart 30d          14. Customer 2× (€497)
5. Pageview 7d            10. Newsletter-engaged     15. Lookalike 1% Customer

Cold acquisition          Re-engagement              High-intent / sales
(saved Meta audiences)    (Custom Audiences from     (Custom + Lookalike
                          Pixel events)              from Customers)
```

---

## 2. TOFU — 5 audiences

### Audience #1 — NL Hot 30 (saved Meta audience)
**Doel:** Cold targeting voor recruiters + HR-managers die actief in tech-recruitment werken — primaire ICP.

| Spec | Value |
|------|-------|
| Type | Saved audience (Meta interests-based) |
| Source-event | n/a |
| Geo | Nederland (NL) |
| Age | 25-55 |
| Gender | All |
| Languages | Dutch + English |
| Detailed targeting (interests + job titles) | Recruitment, Talent acquisition, HR-management, Tech recruitment, AI in HR, LinkedIn recruiting |
| Job titles include | Recruiter, HR Manager, HR Director, Talent Acquisition Specialist, Recruitment Consultant |
| Job industry include | Information Technology, Engineering, Industrial Automation, Manufacturing |
| Behavior | "Engaged shoppers" + "Business decision makers" |
| Retention | n/a (saved audience, refreshed weekly) |
| Expected size | 280k-450k |
| Pixel-criteria-spec | Geen — Meta interest-graph only |
| Setup-instructions | Ads Manager → Audiences → Create → Saved audience → Spec hierboven invoeren → Save als "RE-T1-NL-Hot-30" |

---

### Audience #2 — NL Tech 50-800 FTE Decision Makers (saved)
**Doel:** Cold targeting voor HR Directors + CEO's bij mid-market tech-bedrijven — secundaire ICP (de uiteindelijke buyer).

| Spec | Value |
|------|-------|
| Type | Saved audience (Meta interests + employer-size) |
| Geo | NL — Gelderland, Overijssel, Noord-Brabant (regio-targeting per brand-bible) |
| Age | 30-60 |
| Job titles include | CEO, CTO, COO, HR Director, VP HR, Chief People Officer, Managing Director |
| Job industry include | Engineering, Industrial Automation, Manufacturing, Renewable Energy, Oil & Gas, Construction |
| Employer size | 51-200, 201-500, 501-1.000 (excludes < 50 and > 1.000) |
| Behavior | "B2B decision makers" + "Engaged employers" |
| Retention | n/a |
| Expected size | 35k-65k |
| Pixel-criteria-spec | n/a |
| Setup-instructions | Ads Manager → Saved audience → "RE-T1-NL-Tech-Mid-Market" |

---

### Audience #3 — NL LinkedIn Engineering Heavy (saved)
**Doel:** Engineers + technical recruiters met active LinkedIn engagement — pre-warmed via professional-platform behavior.

| Spec | Value |
|------|-------|
| Type | Saved audience |
| Geo | NL |
| Age | 28-55 |
| Job titles include | Mechanical Engineer, Electrical Engineer, PLC Programmer, Automation Engineer, Industrial Engineer, Process Engineer + Technical Recruiter, Engineering Recruiter |
| Detailed interests | LinkedIn (platform usage), Engineering communities, Tech blogs, AI-tools (Claude, ChatGPT, GitHub Copilot) |
| Behavior | "Tech early adopters" + "Engaged professionals" |
| Retention | n/a |
| Expected size | 90k-150k |
| Pixel-criteria-spec | n/a |
| Setup-instructions | Ads Manager → Saved audience → "RE-T1-NL-LI-Engineer" |

---

### Audience #4 — Lookalike 1% — Stack 2026 Downloaders (NL)
**Doel:** Highest-quality cold acquisition — modeled op users die werkelijk geconverteerd zijn op de lead magnet.

| Spec | Value |
|------|-------|
| Type | Lookalike audience (1% NL) |
| Source | Custom Audience: "RE-MOFU-Stack-Downloaders-30d" (audience #6) |
| Source minimum size | ≥100 conversies (build na week 4 launch — ≥250 voor stabiele LAL) |
| Geo | NL |
| Lookalike % | 1% (smallest = highest similarity) |
| Retention | Refreshed weekly via Meta auto-update |
| Expected size | ~170k (1% NL adult population) |
| Pixel-criteria-spec | Source-audience uses `Stack2026Download` custom event |
| Setup-instructions | Ads Manager → Lookalikes → Create → Source: "RE-MOFU-Stack-Downloaders-30d" → Country: NL → Audience size: 1% → Name: "RE-T1-LAL-1%-StackDL-NL" |
| **Blocker** | Wacht tot ≥100 Stack-downloaders (~week 3-4 post-launch) |

---

### Audience #5 — Pageview 7-day Retargeting (Custom Audience)
**Doel:** Cold-warm bridge — users die 7 dagen geleden landed maar niet converted. Lichte re-engagement.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel) |
| Source-event | `PageView` (LIVE) |
| Retention | 7 dagen |
| URL filter | `recruitmentengineer.nl` (any subdomain) |
| Exclude | Audience #6 (Stack-Downloaders 30d) |
| Expected size | 800-3.500 (after 30 dagen launch) |
| Pixel-criteria-spec | `event_name = 'PageView'` AND `domain CONTAINS 'recruitmentengineer.nl'` |
| Setup-instructions | Ads Manager → Custom Audiences → Create → Website Traffic → "All website visitors" → Past 7 days → Name: "RE-T1-Pageview-7d" → Save |

---

## 3. MOFU — 5 audiences

### Audience #6 — Stack 2026 Downloaders 30 dagen (Custom)
**Doel:** Source-audience voor Lookalike #4 + retargeting voor Tier 1 €97 workshop upsell.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel — custom event) |
| Source-event | `Stack2026Download` (NEW per D2) OR `Lead` (LIVE — fallback if custom event not active yet) |
| Retention | 30 dagen |
| Exclude | n/a |
| Expected size | 50-300 in launch-month, growing to 1k-2.5k by month 3 |
| Pixel-criteria-spec | `event_name = 'Stack2026Download'` (preferred) — fallback `event_name = 'Lead'` AND `content_name CONTAINS 'Stack 2026'` |
| Setup-instructions | Ads Manager → Custom Audiences → Create → Website Traffic → "People who took specific actions" → Event: Stack2026Download → Past 30 days → Name: "RE-MOFU-Stack-Downloaders-30d" → Save |

---

### Audience #7 — Engaged Pageview 7d (50% scroll, Custom)
**Doel:** Lichter dan Pageview retargeting — users die 50%+ scrollen kwalificeren als "depth-readers" voor MOFU mid-priced upsell.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel) |
| Source-event | `ViewContent` (NEW per D2) |
| Retention | 7 dagen |
| Exclude | Audience #6 (already converted) |
| Expected size | 250-800 |
| Pixel-criteria-spec | `event_name = 'ViewContent'` AND `content_category = 'lead_magnet_preview'` |
| Setup-instructions | Custom Audiences → Website → Specific event "ViewContent" → 7 days → Name: "RE-MOFU-Engaged-7d" |

---

### Audience #8 — ViewContent 14-dagen (saw stack-modules)
**Doel:** Bredere engagement-window dan #7. Voor 14-dagen retargeting cycle voorafgaand aan MOFU launch.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel) |
| Source-event | `ViewContent` |
| Retention | 14 dagen |
| Exclude | Audience #6 |
| Expected size | 500-1.500 |
| Pixel-criteria-spec | `event_name = 'ViewContent'` AND `content_ids CONTAINS 'M01'` (any module ID) |
| Setup-instructions | Custom Audiences → Website → ViewContent → 14 days → "RE-MOFU-ViewContent-14d" |

---

### Audience #9 — AddToCart 30 dagen (mailto-click intent)
**Doel:** High-intent retargeting — users die op `mailto:warts@recruitin.nl` klikken signaleren werkbereidheid voor 1:1 engagement.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel) |
| Source-event | `AddToCart` (NEW per D2) |
| Retention | 30 dagen |
| Exclude | Audience #11 (WorkshopInquiry — already further) |
| Expected size | 30-100 (rare event) |
| Pixel-criteria-spec | `event_name = 'AddToCart'` AND `content_ids CONTAINS 'workshop-97'` |
| Setup-instructions | Custom Audiences → Website → AddToCart → 30 days → "RE-MOFU-AddToCart-30d" |

---

### Audience #10 — Newsletter-engaged (open-rate ≥50%)
**Doel:** Email-engagement signal voor warm retargeting. Resend nurture-flow tracked in metadata.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Customer file upload) |
| Source-event | Resend audience export — emails met `open_rate ≥ 0.5` over laatste 30 dagen |
| Retention | n/a (manual file refresh weekly) |
| Exclude | Audience #11 |
| Expected size | 20-150 (highly engaged subset) |
| Pixel-criteria-spec | n/a — uses email-hash matching |
| Setup-instructions | 1. Resend dashboard → Audiences → Export CSV met email + open_rate filter ≥50% 2. Ads Manager → Custom Audiences → Customer File → Upload CSV (column: email) → Match-quality should be ≥75% 3. Name: "RE-MOFU-Newsletter-Engaged" 4. Refresh weekly via cron-script (TBD: `~/recruitin/scripts/sync_resend_to_meta.py`) |

---

## 4. BOFU — 5 audiences

### Audience #11 — WorkshopInquiry 90 dagen
**Doel:** Highest-intent BOFU retargeting — users die werkelijk Calendly-URL klikken.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel) |
| Source-event | `WorkshopInquiry` (NEW per D2) |
| Retention | 90 dagen (BOFU = lange retention voor close-rate) |
| Exclude | Audience #13 (already-customer) |
| Expected size | 5-50 (rare) |
| Pixel-criteria-spec | `event_name = 'WorkshopInquiry'` |
| Setup-instructions | Custom Audiences → Website → WorkshopInquiry → 90 days → "RE-BOFU-Workshop-Inquiry-90d" |

---

### Audience #12 — Cart-abandon 30 dagen (Stripe checkout incomplete)
**Doel:** Recover users die op Stripe-checkout zijn geweest maar niet afgerond. Vereist Stripe Webhooks → Pixel CAPI integration.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel — InitiateCheckout zonder Purchase) |
| Source-event | `InitiateCheckout` AND NOT `Purchase` (binnen 30 dagen) |
| Retention | 30 dagen |
| Exclude | Audience #13 + #14 |
| Expected size | 0 (pre-Stripe go-live) → 5-30 post-launch |
| Pixel-criteria-spec | `event_name = 'InitiateCheckout'` AND `email_hash NOT IN (Purchase audience email_hash list)` |
| Setup-instructions | **WACHT op Stripe go-live**. Dan: Custom Audiences → Website → "People who initiated checkout but didn't purchase" → 30 days → "RE-BOFU-Cart-Abandon-30d" |
| **Blocker** | Stripe checkout setup + `InitiateCheckout` event implementatie (vereist `/api/stripe-checkout` Vercel function) |

---

### Audience #13 — Customer 1× (€97 workshop buyers)
**Doel:** Tier 1 customers — source voor Tier 2 upsell + Lookalike.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel) |
| Source-event | `Purchase` AND `value = 97.00` |
| Retention | 180 dagen (BOFU customer = lange retention) |
| Exclude | n/a |
| Expected size | 0 (pre-launch) → 5-30 by month 3 |
| Pixel-criteria-spec | `event_name = 'Purchase'` AND `value = 97.00` AND `currency = 'EUR'` |
| Setup-instructions | Custom Audiences → Website → Purchase + value filter → 180 days → "RE-BOFU-Customer-Workshop-€97" |
| **Blocker** | Stripe go-live |

---

### Audience #14 — Customer 2× (€497 course buyers)
**Doel:** Tier 2 customers — source voor Tier 3 bootcamp upsell + high-LTV Lookalike.

| Spec | Value |
|------|-------|
| Type | Custom Audience (Pixel) |
| Source-event | `Purchase` AND `value = 497.00` |
| Retention | 365 dagen |
| Exclude | n/a |
| Expected size | 0 (pre-launch) → 2-10 by month 5 |
| Pixel-criteria-spec | `event_name = 'Purchase'` AND `value = 497.00` |
| Setup-instructions | Custom Audiences → Website → Purchase + value=497 → 365 days → "RE-BOFU-Customer-Course-€497" |
| **Blocker** | Stripe go-live + Tier 2 product launch (maand 5) |

---

### Audience #15 — Lookalike 1% — High-LTV Customers
**Doel:** Cold acquisition modeled op highest-LTV customers — Tier 2 + Tier 3 buyers.

| Spec | Value |
|------|-------|
| Type | Lookalike (1% NL) |
| Source | Combined Custom Audience: "RE-BOFU-All-Customers" (union van #13 + #14 + future Tier 3 audience) |
| Source minimum size | ≥100 customers (build na maand 6-9) |
| Geo | NL |
| Lookalike % | 1% |
| Retention | Auto-refresh |
| Expected size | ~170k |
| Pixel-criteria-spec | Source-audience: union of `Purchase` events |
| Setup-instructions | 1. First create combined audience: Custom Audiences → "RE-BOFU-All-Customers" = Customer-€97 OR Customer-€497 2. Lookalikes → Source: All-Customers → 1% NL → "RE-T1-LAL-1%-Customers-NL" |
| **Blocker** | ≥100 customers (~maand 6-9 horizon) |

---

## 5. Audience hygiene rules

1. **Naming convention**: `RE-{TIER}-{NAME}-{RETENTION}` (e.g. `RE-MOFU-Stack-Downloaders-30d`).
2. **Exclusions**: Always exclude already-converted users from earlier-stage audiences. Bv. #5 Pageview-7d exclude #6 Stack-Downloaders.
3. **Retention windows**: TOFU-retargeting = 7d, MOFU = 14-30d, BOFU = 90-365d. Don't go shorter dan 7d (statisch) of langer dan 365d (privacy).
4. **Lookalike lower-bound**: 100 source-users minimum, 250+ for stable model. Don't build LAL too early.
5. **Privacy**: All Custom Audiences from Pixel only fire na consent (in-house consent banner gates `fbq` calls).
6. **GDPR**: Resend → Meta CAPI customer-file upload requires user-consent-status check pre-export.
7. **Audit log**: Maintain spreadsheet `~/recruitin/meta-audiences-recruitmentengineer.csv` met audience-ID + naam + size + last-refresh-date.

---

## 6. Implementation roadmap

### Phase 1 — Pre-launch (deze week)
- [ ] Audiences #1, #2, #3 — saved audiences setup (geen Pixel-data nodig)
- [ ] Audience #5 — Pageview 7d (fire't direct vanaf launch)
- [ ] Document audience-IDs in `~/recruitin/meta-audiences-recruitmentengineer.csv`

### Phase 2 — Post-launch week 1-2
- [ ] Audiences #6, #7, #8, #9 — als events fire'n + retentie-data accumuleert
- [ ] Audience #10 — eerste Resend-export pas zinvol bij ≥20 newsletter-recipients

### Phase 3 — Post-launch week 4
- [ ] Audience #4 — Lookalike 1% Stack-DL (vereist ≥100 conversies)

### Phase 4 — Post-Stripe go-live (maand 3+)
- [ ] Audiences #11, #12, #13 — pas relevant met Stripe checkout
- [ ] Audience #14 — pas relevant met Tier 2 launch (maand 5)
- [ ] Audience #15 — pas relevant met ≥100 customers (maand 6-9)

---

## 7. Bulk-import CSV (optional, post-launch)

Wanneer audiences #1-#10 stabiel gebruikt worden, kan een bulk-import CSV gemaakt voor mass-update. Format:

```csv
audience_id,audience_name,type,source_event,retention_days,expected_size,status
A001,RE-T1-NL-Hot-30,saved,n/a,n/a,350000,active
A005,RE-T1-Pageview-7d,custom_pixel,PageView,7,2000,active
A006,RE-MOFU-Stack-Downloaders-30d,custom_pixel,Stack2026Download,30,500,active
...
```

**Note:** Meta Ads Manager heeft geen "bulk-import audience definitions"-feature. Deze CSV is voor handmatige tracking + audit-trail, niet voor API-import. Audience-creation blijft handmatig per audience via UI of via Meta Marketing API (Ads Manager API endpoint `/customaudiences`).

---

## 8. Cross-reference

- Event payload definitions: `meta-pixel-events.md`
- Funnel tier-mapping (welk audience → welk product → welk KPI): `funnel-tier-mapping.md`
- Pixel-config + privacy: `08-tracking-setup/README.md`
- Recruitin-shared-pixel reference: `feedback_meta_pixel_vs_page_id.md` in `~/.claude/projects/-Users-wouterarts/memory/`

---

> **Status:** ✅ Architecture spec compleet. Phase 1 audiences #1-#3 + #5 kunnen pre-launch al ingericht.
> **Owner:** Ing. W. Arts
> **Blockers:** Lookalike #4 (wacht op 100 conversies), audiences #11-#15 (wachten op Stripe + Tier 2 + customers).
