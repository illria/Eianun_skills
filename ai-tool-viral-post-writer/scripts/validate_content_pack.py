#!/usr/bin/env python3
"""Lightweight validation for the AI tool viral post writer skill."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/persona.md",
    "references/copywriting_frameworks.md",
    "references/case_library.md",
    "references/output_formats.md",
    "references/claim_safety.md",
    "references/visual_brief.md",
    "references/image_prompt_templates.md",
    "references/api_integration.md",
    "references/codex_agent_playbook.md",
    "scripts/generate_visual_pack.py",
    "scripts/append_case_pattern.py",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,}"),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", default=".")
    args = parser.parse_args()
    root = Path(args.skill_root).resolve()

    missing = [path for path in REQUIRED_FILES if not (root / path).exists()]
    if missing:
        raise SystemExit("missing required files:\n" + "\n".join(missing))

    findings: list[str] = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".py", ".yaml", ".yml", ".json", ".txt"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    findings.append(str(path.relative_to(root)))
                    break
    if findings:
        raise SystemExit("possible hardcoded secrets found:\n" + "\n".join(findings))

    print(f"content pack validation passed: {root}")


if __name__ == "__main__":
    main()
