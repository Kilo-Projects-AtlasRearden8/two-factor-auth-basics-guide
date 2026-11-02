#!/usr/bin/env python3
"""Verify the Two-Factor Authentication Basics static site.

Checks:
- every HTML file in site/ exists and parses
- every internal link resolves to an existing file
- every chapter page has a <title>, at least one <h1>/<h2>, and a link to the worksheet
- LICENSE contains the exact required copyright line
- README credits Asdale Dynamics, LLC

Run: python3 scripts/verify_site.py
"""

from __future__ import annotations

import html.parser
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(ROOT, "site")

HTML_FILES = [
    "index.html",
    "02-authenticator-apps.html",
    "03-sms-risks.html",
    "04-recovery-codes.html",
    "05-backing-up-accounts.html",
    "06-setup-email.html",
    "07-setup-banking.html",
    "08-setup-ai-tools.html",
    "worksheet.html",
]

ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(msg)
    print(f"  ERROR: {msg}")


def warning(msg):
    WARNINGS.append(msg)
    print(f"  WARN:  {msg}")


def ok(msg):
    print(f"  ok: {msg}")


class LinkChecker(HTMLParser):
    """Collect href/src links and heading/title presence from an HTML file."""

    def __init__(self):
        super().__init__()
        self.links = []
        self.has_title = False
        self.title_text = ""
        self.headings = []
        self.has_worksheet_link = False
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._in_title = True
            self.has_title = True
        if tag == "a":
            href = attrs.get("href")
            if href:
                self.links.append(href)
                if "worksheet" in href:
                    self.has_worksheet_link = True
        elif tag in ("img", "script", "link"):
            for attr in ("src", "href"):
                val = attrs.get(attr)
                if val:
                    self.links.append(val)
        if tag in ("h1", "h2", "h3"):
            self.headings.append(tag)

    def handle_data(self, data):
        if self._in_title:
            self.title_text += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False


def parse_file(path):
    parser = LinkChecker()
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    parser.feed(content)
    return parser, content


def normalize_link(href, base_dir):
    """Resolve an href relative to base_dir; return (normalized_path, is_external)."""
    if href.startswith("mailto:") or href.startswith("tel:"):
        return None, True
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https"):
        return None, True
    # strip fragment
    path = parsed.path
    # resolve relative to base_dir
    full = os.path.normpath(os.path.join(base_dir, path))
    return full, False


def main():
    print("== Verify Two-Factor Authentication Basics site ==")
    print(f"Root: {ROOT}")
    print(f"Site dir: {SITE_DIR}\n")

    # 1. HTML files exist
    print("1. HTML files exist:")
    for name in HTML_FILES:
        path = os.path.join(SITE_DIR, name)
        if os.path.isfile(path):
            ok(f"{name}")
        else:
            error(f"missing: {name}")

    # 2. Parse each page, check title/headings/worksheet link
    print("\n2. Page structure (title, headings, worksheet link):")
    for name in HTML_FILES:
        path = os.path.join(SITE_DIR, name)
        if not os.path.isfile(path):
            continue
        parser, _ = parse_file(path)
        issues = []
        if not parser.has_title:
            issues.append("no <title>")
        if not parser.headings:
            issues.append("no <h1>/<h2> headings")
        if name != "worksheet.html" and not parser.has_worksheet_link:
            issues.append("no link to worksheet.html")
        if issues:
            error(f"{name}: " + "; ".join(issues))
        else:
            ok(f"{name} (title='{parser.title_text.strip()}', {len(parser.headings)} headings, worksheet link={parser.has_worksheet_link})")

    # 3. Internal links resolve
    print("\n3. Internal links resolve:")
    for name in HTML_FILES:
        path = os.path.join(SITE_DIR, name)
        if not os.path.isfile(path):
            continue
        parser, _ = parse_file(path)
        base_dir = SITE_DIR
        for href in parser.links:
            resolved, external = normalize_link(href, base_dir)
            if external:
                continue
            if not os.path.isfile(resolved):
                error(f"{name}: broken link -> {href} (resolved {resolved})")
            else:
                # only report a sample of ok links to keep output small
                pass
        ok(f"{name}: {len(parser.links)} link(s) checked")

    # 4. style.css exists and is linked
    print("\n4. CSS:")
    css_path = os.path.join(SITE_DIR, "style.css")
    if os.path.isfile(css_path):
        ok("style.css exists")
    else:
        error("style.css missing")
    for name in HTML_FILES:
        path = os.path.join(SITE_DIR, name)
        if not os.path.isfile(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if 'href="style.css"' in content or "href='style.css'" in content:
            pass
        else:
            error(f"{name}: does not link style.css")

    # 5. Print media query present
    print("\n5. Print styles:")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    if "@media print" in css:
        ok("print media query present")
    else:
        error("no @media print in style.css")

    # 6. LICENSE exact copyright line
    print("\n6. LICENSE:")
    license_path = os.path.join(ROOT, "LICENSE")
    if os.path.isfile(license_path):
        with open(license_path, "r", encoding="utf-8") as f:
            lic = f.read()
        required = "Copyright (c) 2026 Asdale Dynamics, LLC"
        if required in lic:
            ok(f"LICENSE contains exact line: {required}")
        else:
            error(f"LICENSE missing exact line: {required}")
    else:
        error("LICENSE missing")

    # 7. README credits Asdale Dynamics, LLC
    print("\n7. README:")
    readme_path = os.path.join(ROOT, "README.md")
    if os.path.isfile(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme = f.read()
        if "Asdale Dynamics, LLC" in readme:
            ok("README credits Asdale Dynamics, LLC")
        else:
            error("README does not credit Asdale Dynamics, LLC")
    else:
        error("README.md missing")

    # 8. No secrets / personal data scan (basic heuristic)
    print("\n8. Secret / personal data scan (heuristic):")
    patterns = {
        "API key-ish": r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*['\"][A-Za-z0-9]{16,}['\"]",
        "email address": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "phone number": r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b",
    }
    scanned = 0
    for dirpath, _, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for fn in files:
            if fn.endswith((".git",)):
                continue
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception:
                continue
            scanned += 1
            for label, pat in patterns.items():
                for m in re.finditer(pat, content):
                    line = content[: m.start()].count("\n") + 1
                    # allow known benign: noreply github email in README, example placeholders
                    snippet = content[m.start(): m.end()].replace("\n", " ")
                    warning(f"{os.path.relpath(fp, ROOT)}:{line}: possible {label}: {snippet[:60]}")

    # 9. No .github/workflows
    print("\n9. No GitHub Actions workflows:")
    wf_dir = os.path.join(ROOT, ".github", "workflows")
    if os.path.isdir(wf_dir) and os.listdir(wf_dir):
        error(f".github/workflows exists and is non-empty: {os.listdir(wf_dir)}")
    else:
        ok("no .github/workflows")

    # Summary
    print("\n== Summary ==")
    print(f"Files scanned: {scanned}")
    print(f"Errors: {len(ERRORS)}")
    print(f"Warnings: {len(WARNINGS)}")
    if ERRORS:
        print("\nFAILURES:")
        for e in ERRORS:
            print(f"  - {e}")
        return 1
    if WARNINGS:
        print("\nWarnings (non-fatal):")
        for w in WARNINGS:
            print(f"  - {w}")
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
