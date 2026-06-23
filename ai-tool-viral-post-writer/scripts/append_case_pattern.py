#!/usr/bin/env python3
"""Append a distilled viral-copy pattern to references/case_library.md.

This script intentionally appends only a reviewed markdown pattern block. It is
not an LLM and does not extract structure from raw examples by itself.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

REQUIRED_HEADINGS = ["Reusable mechanics", "Use for", "Do not use for"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", default=".")
    parser.add_argument("--pattern-file", required=True, help="Markdown file containing distilled pattern block")
    parser.add_argument("--case-library", default="references/case_library.md")
    args = parser.parse_args()

    skill_root = Path(args.skill_root).resolve()
    pattern_path = Path(args.pattern_file).resolve()
    case_path = skill_root / args.case_library
    if not case_path.exists():
        raise SystemExit(f"missing case library: {case_path}")
    block = pattern_path.read_text(encoding="utf-8").strip()
    if not block.startswith("##"):
        raise SystemExit("pattern block must start with a markdown heading, e.g. ## Pattern: ...")
    missing = [h for h in REQUIRED_HEADINGS if h not in block]
    if missing:
        raise SystemExit(f"pattern block missing required headings: {', '.join(missing)}")
    current = case_path.read_text(encoding="utf-8")
    marker = f"\n\n---\n\n<!-- added {date.today().isoformat()} by append_case_pattern.py -->\n\n"
    case_path.write_text(current.rstrip() + marker + block + "\n", encoding="utf-8")
    print(f"appended pattern to {case_path}")


if __name__ == "__main__":
    main()
