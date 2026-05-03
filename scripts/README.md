# scripts/ — recruitmentengineer.nl utilities

## og-image generator (temporary fallback)

This directory contains a **temporary HTML/CSS-rendered OG-image** for
`recruitmentengineer.nl`. It exists to unblock LinkedIn / Twitter / WhatsApp
social shares while the final Higgsfield-rendered hero image is being
produced. The Higgsfield version will live in `02-higgsfield-assets/` once
available, and the meta-tag in `06-landing-page/public/index.html` will be
re-pointed accordingly.

### Files

| File | Purpose |
|---|---|
| `og-image-template.html` | Self-contained 1200×630 layout — Inter + JetBrains Mono via Google Fonts CDN, dark `#0A1929` background with blueprint grid, Recruitin oranje (`#FF6B1A`) accents. |
| `generate_og_image.py` | Headless-Chromium (Playwright) renderer → JPEG quality 85 → `06-landing-page/public/og-image.jpg`. |

### Usage

```bash
# from repo root
python3 scripts/generate_og_image.py
```

Output:
```
/Users/wouterarts/projects/recruitmentengineer/06-landing-page/public/og-image.jpg
```

Target: 1200×630, JPEG quality 85, <300 KB.

### Editing

Tweak `og-image-template.html` (inline `<style>` block, no external CSS),
then re-run the generator. The template is self-contained — open it
directly in a browser to preview before re-rendering.

### Brand spec (locked)

- Primary accent: `#FF6B1A` (Recruitin Oranje)
- Authority blue: `#1E3A5F`
- Tech accent: `#00D4FF` (AI Cyaan)
- Background dark: `#0A1929`
- Display font: Inter, weight 800–900, letter-spacing −0.03em to −0.04em
- Mono labels: JetBrains Mono, weight 500–700

### Replace with Higgsfield version

Once `02-higgsfield-assets/og-image-final.jpg` (or similar) is approved:

1. Copy/rename it to `06-landing-page/public/og-image.jpg`
   (or update `index.html` `og:image` URL to point at the new asset).
2. Verify with `curl -I https://recruitmentengineer.nl/og-image.jpg` →
   `Content-Type: image/jpeg`, `Content-Length` < 300 KB.
3. Re-test social previews via:
   - LinkedIn: https://www.linkedin.com/post-inspector/
   - Twitter/X: https://cards-dev.twitter.com/validator
   - Facebook: https://developers.facebook.com/tools/debug/
