#!/usr/bin/env node
/**
 * utm-generator.js — small standalone helper for the Recruitin
 * Authority Campaign auto-poster.
 *
 * Two uses:
 *   1) CLI: build a UTM-tagged URL from title + platform + campaign.
 *      $ node utm-generator.js "Day 1 Manifesto LI" linkedin stack-2026-launch
 *      → https://recruitmentengineer.nl?utm_source=linkedin&utm_medium=organic&utm_campaign=stack-2026-launch&utm_content=day-1-manifesto-li
 *
 *   2) Reference for the Notion `Generated-link` formula. The
 *      `buildUtmUrl()` function below mirrors what the Notion formula
 *      computes — keep them in sync if you change one.
 *
 * Why JS?  This file doubles as the canonical reference both for the
 * Notion formula language (which is JS-flavoured) and for any future
 * Vercel / Edge Function rewrites of the pipeline.
 */

"use strict";

const LANDING_URL = "https://recruitmentengineer.nl";

/**
 * Convert a free-form title to a URL-safe slug.
 * - lowercases
 * - strips diacritics (NFD + remove combining marks)
 * - removes non-alphanumeric except spaces and hyphens
 * - collapses whitespace to single hyphen
 *
 * @param {string} title
 * @returns {string}
 */
function slugify(title) {
  if (!title) return "";
  return title
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

/**
 * Map raw platform input to canonical utm_source value.
 * Accepts: "LinkedIn", "linkedin", "li", "Meta", "meta", "fb", "ig",
 *          "Both", "cross". Defaults to platform string itself, lowercased.
 *
 * @param {string} platform
 * @returns {string}
 */
function normalizePlatform(platform) {
  const p = (platform || "").toLowerCase().trim();
  if (["linkedin", "li"].includes(p)) return "linkedin";
  if (["meta", "fb", "facebook", "ig", "instagram"].includes(p)) return "meta";
  if (["both", "cross", "all"].includes(p)) return "cross";
  return p;
}

/**
 * Build a fully UTM-tagged URL for a recruitmentengineer.nl post.
 *
 * @param {Object} opts
 * @param {string} opts.title       — post-title (used for utm_content slug)
 * @param {string} opts.platform    — "linkedin" | "meta" | "both" | etc.
 * @param {string} opts.campaign    — utm_campaign, e.g. "stack-2026-launch"
 * @param {string} [opts.medium]    — utm_medium, default "organic"
 * @param {string} [opts.base]      — landing URL, default LANDING_URL
 * @returns {string}
 */
function buildUtmUrl({ title, platform, campaign, medium = "organic", base = LANDING_URL }) {
  const params = new URLSearchParams({
    utm_source: normalizePlatform(platform),
    utm_medium: medium,
    utm_campaign: campaign || "untagged",
    utm_content: slugify(title),
  });
  return `${base}?${params.toString()}`;
}

// ---------------------------------------------------------------------------
// CLI entry
// ---------------------------------------------------------------------------

function _cliMain() {
  const [, , title, platform, campaign, medium] = process.argv;
  if (!title || !platform || !campaign) {
    console.error(
      "usage: node utm-generator.js <title> <platform> <campaign> [medium]\n" +
        '  e.g. node utm-generator.js "Day 1 Manifesto LI" linkedin stack-2026-launch'
    );
    process.exit(64);
  }
  console.log(buildUtmUrl({ title, platform, campaign, medium }));
}

if (require.main === module) {
  _cliMain();
}

module.exports = { buildUtmUrl, slugify, normalizePlatform, LANDING_URL };
