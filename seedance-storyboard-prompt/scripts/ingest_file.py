#!/usr/bin/env python3
"""Ingest a local source file into a Seedance project knowledge base."""

from __future__ import annotations

import argparse
import re
import zipfile
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET


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
    return slug[:80] or "source"


def read_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paragraphs: list[str] = []
    for paragraph in root.findall(".//w:p", ns):
        texts = [node.text for node in paragraph.findall(".//w:t", ns) if node.text]
        if texts:
            paragraphs.append("".join(texts))
    return "\n\n".join(paragraphs)


def read_pdf(path: Path) -> str:
    try:
        import pdfplumber  # type: ignore

        with pdfplumber.open(path) as pdf:
            return "\n\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception:
        pass

    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        return "\n\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as exc:
        raise SystemExit("PDF support requires pdfplumber or pypdf. Export the PDF to text/markdown first.") from exc


def read_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt", ".csv", ".json", ".yaml", ".yml"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    if suffix == ".docx":
        return read_docx(path)
    if suffix in {".html", ".htm"}:
        parser = SimpleHTMLText()
        parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
        return "\n".join(parser.parts)
    if suffix == ".pdf":
        return read_pdf(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def update_manifest(root: Path, rel: Path, title: str, kind: str, source_name: str) -> None:
    manifest = root / "docs" / "MANIFEST.md"
    existing = manifest.read_text(encoding="utf-8") if manifest.exists() else "# Seedance Knowledge Manifest\n\n"
    rel_text = str(rel)
    if rel_text in existing:
        return
    entry = (
        f"\n### {rel_text}\n"
        f"- Type: {kind}\n"
        f"- Title: {title}\n"
        f"- Source file: {source_name}\n"
        f"- Added: {date.today().isoformat()}\n"
        "- Summary: ingested source; inspect the markdown file for detailed extracted text.\n"
        "- Use when: source-backed Seedance diagnosis, prompt revision, or storyboard planning needs this material.\n"
    )
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(existing.rstrip() + entry + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest a local file into docs/sources, docs/web, or docs/cases.")
    parser.add_argument("file")
    parser.add_argument("--kind", choices=["sources", "web", "cases"], default="sources")
    parser.add_argument("--root", default=".")
    parser.add_argument("--title")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    source = Path(args.file).resolve()
    if not source.exists():
        raise SystemExit(f"missing file: {source}")

    title = args.title or source.stem
    content = read_file(source).strip()
    if not content:
        raise SystemExit(f"no readable text extracted from: {source}")

    out_dir = root / "docs" / args.kind
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{slugify(title)}.md"
    out.write_text(f"# {title}\n\nSource file: `{source.name}`\n\n---\n\n{content}\n", encoding="utf-8")
    rel = out.relative_to(root)
    update_manifest(root, rel, title, args.kind, source.name)
    print(f"Ingested {source} -> {rel}")


if __name__ == "__main__":
    main()
