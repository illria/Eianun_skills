#!/usr/bin/env python3
"""Fetch a webpage into a Seedance project knowledge base."""

from __future__ import annotations

import argparse
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import re
import urllib.request


class SimpleHTMLText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        stripped = data.strip()
        if stripped:
            self.parts.append(stripped)


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", text).strip("-").lower()
    return slug[:80] or "web-source"


def update_manifest(root: Path, rel: Path, url: str, title: str) -> None:
    manifest = root / "docs" / "MANIFEST.md"
    existing = manifest.read_text(encoding="utf-8") if manifest.exists() else "# Seedance Knowledge Manifest\n\n"
    rel_text = str(rel)
    if rel_text in existing:
        return
    entry = (
        f"\n### {rel_text}\n"
        "- Type: web\n"
        f"- URL: {url}\n"
        f"- Title: {title}\n"
        f"- Added: {date.today().isoformat()}\n"
        "- Summary: fetched webpage; inspect the markdown file for extracted text.\n"
        "- Use when: source-backed Seedance diagnosis or prompt planning needs this webpage.\n"
    )
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(existing.rstrip() + entry + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch a URL into docs/web and update docs/MANIFEST.md.")
    parser.add_argument("url")
    parser.add_argument("--root", default=".")
    parser.add_argument("--title")
    args = parser.parse_args()

    request = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(request, timeout=30).read().decode("utf-8", "ignore")
    parser = SimpleHTMLText()
    parser.feed(html)

    title = args.title or args.url.rstrip("/").split("/")[-1] or "web-source"
    content = "\n".join(parser.parts).strip()
    if not content:
        raise SystemExit("no readable text extracted; provide exported PDF/DOCX/text/screenshots instead")

    root = Path(args.root).resolve()
    out_dir = root / "docs" / "web"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{slugify(title)}.md"
    out.write_text(f"# {title}\n\nURL: {args.url}\n\n---\n\n{content}\n", encoding="utf-8")
    rel = out.relative_to(root)
    update_manifest(root, rel, args.url, title)
    print(f"Ingested {args.url} -> {rel}")


if __name__ == "__main__":
    main()
