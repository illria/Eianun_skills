#!/usr/bin/env python3
"""Search Seedance project docs and bundled references for evidence mode."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_DIRS = [
    "docs",
    "seedance-storyboard-prompt/references",
    "references",
]


def score(text: str, terms: list[str]) -> int:
    lowered = text.lower()
    return sum(lowered.count(term.lower()) for term in terms)


def excerpt(text: str, terms: list[str], width: int = 240) -> str:
    lowered = text.lower()
    index = -1
    for term in terms:
        index = lowered.find(term.lower())
        if index >= 0:
            break
    if index < 0:
        snippet = text[:width]
    else:
        start = max(0, index - width // 2)
        end = min(len(text), index + width // 2)
        snippet = text[start:end]
    return re.sub(r"\s+", " ", snippet).strip()


def iter_markdown(root: Path, extra_dirs: list[str]) -> list[Path]:
    candidates: list[Path] = []
    for rel in [*DEFAULT_DIRS, *extra_dirs]:
        directory = root / rel
        if directory.exists():
            candidates.extend(path for path in directory.rglob("*.md") if path.is_file())
    return sorted(set(candidates))


def main() -> None:
    parser = argparse.ArgumentParser(description="Search Seedance docs/references by keyword.")
    parser.add_argument("query", nargs="+", help="Search terms, e.g. 字幕 水印 人物漂移")
    parser.add_argument("--root", default=".", help="Project or repository root")
    parser.add_argument("--dir", action="append", default=[], help="Additional relative directory to search")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    terms = [term for term in re.split(r"\s+", " ".join(args.query).strip()) if term]
    if not terms:
        raise SystemExit("empty query")

    hits: list[tuple[int, Path, str]] = []
    for path in iter_markdown(root, args.dir):
        text = path.read_text(encoding="utf-8", errors="ignore")
        hit_score = score(text, terms)
        if hit_score > 0:
            hits.append((hit_score, path, excerpt(text, terms)))

    for hit_score, path, snippet in sorted(hits, key=lambda item: (-item[0], str(item[1])))[: args.limit]:
        print(f"[{hit_score}] {path.relative_to(root)}")
        print(f"    {snippet}")


if __name__ == "__main__":
    main()
