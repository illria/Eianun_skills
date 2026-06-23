#!/usr/bin/env python3
"""Create a revision prompt from an existing brief and user feedback."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief", required=True)
    parser.add_argument("--feedback", required=True)
    parser.add_argument("--previous-prompt", default="")
    parser.add_argument("--out-brief", default="dist/thumbnail_brief_revised.json")
    parser.add_argument("--out-prompt", default="dist/revision_prompt.md")
    args = parser.parse_args()

    brief_path = Path(args.brief)
    brief = json.loads(brief_path.read_text(encoding="utf-8"))
    history = brief.setdefault("revision_history", [])
    history.append(
        {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "feedback": args.feedback,
        }
    )
    Path(args.out_brief).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_brief).write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")

    previous = Path(args.previous_prompt).read_text(encoding="utf-8") if args.previous_prompt and Path(args.previous_prompt).exists() else ""
    prompt = f"""# Native Image Revision Prompt

Use Codex's built-in image generation to regenerate the thumbnail.

User feedback:
{args.feedback}

Keep these constraints:
- 16:9 YouTube thumbnail, 1280x720
- no bottom red progress bar
- large readable Chinese text
- keep selected title/topic unless feedback says otherwise
- keep brand/product identity accurate
- do not make it a flat template

Brief JSON path: {args.out_brief}

Previous prompt context:
{previous[:6000]}

Make the new version more polished and closer to the user's requested direction.
"""
    Path(args.out_prompt).write_text(prompt, encoding="utf-8")
    print(f"Wrote {args.out_brief} and {args.out_prompt}")


if __name__ == "__main__":
    main()
