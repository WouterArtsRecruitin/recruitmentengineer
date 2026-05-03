#!/usr/bin/env python3
"""
OG-image generator for recruitmentengineer.nl.

Renders scripts/og-image-template.html via headless Chromium (Playwright)
and writes the result as JPEG (quality 85) to:
    06-landing-page/public/og-image.jpg

Target: 1200x630, <300 KB. Re-run after editing the template.
"""

import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = REPO_ROOT / "scripts" / "og-image-template.html"
OUTPUT_PATH = REPO_ROOT / "06-landing-page" / "public" / "og-image.jpg"

VIEWPORT = {"width": 1200, "height": 630}


def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        return True
    except ImportError:
        print("[!] playwright not installed. Run: pip install playwright && playwright install chromium")
        return False


def render():
    from playwright.sync_api import sync_playwright

    if not TEMPLATE_PATH.exists():
        print(f"[!] template missing: {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_url = f"file://{TEMPLATE_PATH}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=1,
        )
        page = context.new_page()
        page.goto(file_url, wait_until="networkidle")

        # Wait for fonts to be ready (Google Fonts CDN can be flaky on cold load)
        try:
            page.evaluate("document.fonts.ready")
            page.wait_for_function("document.fonts && document.fonts.status === 'loaded'", timeout=8000)
        except Exception:
            pass
        time.sleep(2.0)  # belt-and-suspenders for font flicker

        page.screenshot(
            path=str(OUTPUT_PATH),
            type="jpeg",
            quality=85,
            full_page=False,
            clip={"x": 0, "y": 0, "width": VIEWPORT["width"], "height": VIEWPORT["height"]},
        )
        browser.close()


def report():
    if not OUTPUT_PATH.exists():
        print("[!] output file not produced", file=sys.stderr)
        sys.exit(1)
    size_bytes = OUTPUT_PATH.stat().st_size
    size_kb = size_bytes / 1024
    print(f"[ok] wrote {OUTPUT_PATH}")
    print(f"[ok] size: {size_kb:.1f} KB ({size_bytes} bytes)")
    try:
        from PIL import Image
        with Image.open(OUTPUT_PATH) as im:
            print(f"[ok] dimensions: {im.size[0]}x{im.size[1]} ({im.format})")
    except ImportError:
        print("[!] PIL not available; skipping dimension check")
    if size_kb > 300:
        print(f"[!] WARNING: file >300 KB target ({size_kb:.1f} KB)")


def main():
    if not ensure_playwright():
        sys.exit(2)
    render()
    report()


if __name__ == "__main__":
    main()
