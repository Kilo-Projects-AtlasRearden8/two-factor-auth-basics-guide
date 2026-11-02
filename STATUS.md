# STATUS — Two-Factor Authentication Basics

## What was built

A beginner manual on two-factor authentication (2FA), delivered as Markdown docs plus a static HTML site.

**`docs/` — Markdown manual (9 files):**
- `01-introduction.md` — what 2FA is, who it's for, why passwords aren't enough
- `02-authenticator-apps.md` — authenticator apps, popular free options, setup steps, tips
- `03-sms-risks.md` — why SMS codes are risky (SIM swapping, porting, interception), when SMS is okay, stronger alternatives
- `04-recovery-codes.md` — recovery codes as an emergency spare key, how to store and use them
- `05-backing-up-accounts.md` — three layers of backup, new-phone migration, protecting your email
- `06-setup-email.md` — step-by-step for Gmail, Outlook/Microsoft, Yahoo, Apple ID
- `07-setup-banking.md` — general bank setup steps, what to watch for, locked-out recovery
- `08-setup-ai-tools.md` — general AI tool setup, notes for ChatGPT/OpenAI, Claude, Gemini, Copilot
- `worksheet.md` — printable worksheet (accounts table, authenticator app info, recovery codes, emergency contact)

**`site/` — static HTML site (10 files):**
- `index.html` — landing page
- One HTML page per docs chapter (`02-...` through `08-...`)
- `worksheet.html` — printable worksheet
- `style.css` — shared styles with `@media print` that hides navigation and prints cleanly

**`scripts/verify_site.py`** — verification script (HTML existence, internal link resolution, page structure, CSS/print styles, LICENSE exact copyright line, README credit, secret/personal-data heuristic scan, no `.github/workflows`).

**`LICENSE`** — MIT License, copyright line exactly: `Copyright (c) 2026 Asdale Dynamics, LLC`

**`README.md`** — overview, how to read/run/verify, credits Asdale Dynamics, LLC.

**`STATUS.md`** — this file.

## How to run it

No build step, no server, no internet required. It's a fully static site.

- **Read the site:** Open `site/index.html` in any web browser.
- **Read a chapter:** Open any `site/*.html` file directly.
- **Print the worksheet:** Open `site/worksheet.html` and use your browser's print (File → Print). Print styles strip navigation and background colors.
- **Read the docs:** Open any `docs/*.md` file in a Markdown viewer or text editor.

## Verification results

Ran `python3 scripts/verify_site.py`:

- 9 HTML files present ✓
- All pages have `<title>`, headings, and a worksheet link ✓
- All internal links resolve ✓
- `style.css` linked on every page ✓
- `@media print` present ✓
- `LICENSE` contains exact line `Copyright (c) 2026 Asdale Dynamics, LLC` ✓
- `README.md` credits Asdale Dynamics, LLC ✓
- Secret / personal-data heuristic scan: clean ✓
- No `.github/workflows` ✓

**Result: 0 errors, 0 warnings. All checks passed.**

## Known gaps

- Chapter HTML pages are hand-written static files rather than generated from the Markdown, so the docs and site must be kept in sync manually if content changes.
- The site has no search, dark mode, or multi-language support (out of scope for a beginner printable guide).
- Bank-specific setup steps are general because bank UIs vary widely; users may need to call their bank for exact screens.
- No AI tools, banking, or email accounts were actually created or tested — this is an education guide, not a live integration. Verification covers the site build and links only.

## Credit

Written and published by **Asdale Dynamics, LLC** (Indiana, formed October 2026). Dylan Asdale is a registered nurse turned AI author and founder of Asdale Dynamics.

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
