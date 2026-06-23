#!/usr/bin/env python3
"""Generate a deterministic visual brief/prompt pack from project metadata.

This script is intentionally simple. It does not replace ChatGPT's judgment;
it gives Codex a stable way to write prompt packs to files after the copy spine
has been decided.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

TEMPLATE_HINTS = {
    "free-resource-directory": "resource-map",
    "open-source-replacement": "before-after",
    "capability-breakthrough": "workflow-diagram",
    "ai-agent-framework": "workflow-diagram",
    "developer-automation": "workflow-diagram",
    "local-first-tool": "tool-card",
    "model-research-release": "tool-card",
    "product-launch": "tool-card",
    "warning-or-risk": "warning-card",
    "build-in-public-project": "tool-card",
}


def clean_list(value: str) -> list[str]:
    return [x.strip() for x in value.split(",") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate image prompt pack for AI tool posts.")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--project-type", default="developer-automation")
    parser.add_argument("--core-value", required=True)
    parser.add_argument("--audience", default="中文 X/Twitter 的 AI 工具用户、独立开发者、自学者")
    parser.add_argument("--features", default="模型,API,工具,工作流")
    parser.add_argument("--image-title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--aspect-ratio", default="16:9")
    parser.add_argument("--output-dir", default="out/visual_pack")
    args = parser.parse_args()

    features = clean_list(args.features)
    template = TEMPLATE_HINTS.get(args.project_type, "tool-card")
    title = args.image_title or args.project_name
    subtitle = args.subtitle or args.core_value
    feature_text = "、".join(features[:5]) or "AI 工具工作流"

    prompt = (
        f"Create a clean modern SaaS/developer style cover image for a Chinese X/Twitter post about {args.project_name}. "
        f"The visual theme is {args.core_value}. Use a polished product UI composition with rounded cards, subtle gradients, "
        f"developer-tool aesthetics, organized information hierarchy, and enough whitespace. Show conceptual modules for {feature_text}. "
        f"Make it feel practical, credible, and useful for {args.audience}, not exaggerated advertising. "
        f"No people, no cartoon style, no fake screenshots, no misleading official logos. "
        f"If text is included, keep it minimal and large: title '{title}', subtitle '{subtitle}'. Aspect ratio {args.aspect_ratio}."
    )

    no_text_prompt = (
        f"Create a clean modern SaaS/developer style background illustration for an AI tool post about {args.project_name}. "
        f"Represent {args.core_value} using abstract UI cards, workflow nodes, code/API panels, and organized category chips. "
        f"No readable text, no people, no logos, no screenshots. Leave clear empty space for later Chinese title overlay. "
        f"Aspect ratio {args.aspect_ratio}."
    )

    data = {
        "project_name": args.project_name,
        "project_type": args.project_type,
        "selected_template": template,
        "visual_strategy": f"Use a {template} visual because the post's core value is {args.core_value}.",
        "image_title": title,
        "subtitle": subtitle,
        "feature_chips": features[:5],
        "aspect_ratio": args.aspect_ratio,
        "prompt": prompt,
        "no_text_background_prompt": no_text_prompt,
        "screenshot_recommendation": "Use a real README/demo/pricing screenshot instead of generated art when factual UI proof is central.",
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "visual_pack.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "image_prompt.txt").write_text(prompt + "\n", encoding="utf-8")
    (out_dir / "no_text_background_prompt.txt").write_text(no_text_prompt + "\n", encoding="utf-8")
    md = [
        "# Visual Prompt Pack",
        "",
        f"- Project: {args.project_name}",
        f"- Template: {template}",
        f"- Title: {title}",
        f"- Subtitle: {subtitle}",
        f"- Feature chips: {', '.join(features[:5])}",
        f"- Aspect ratio: {args.aspect_ratio}",
        "",
        "## Direct image prompt",
        "",
        prompt,
        "",
        "## No-text background prompt",
        "",
        no_text_prompt,
        "",
        "## Screenshot recommendation",
        "",
        data["screenshot_recommendation"],
    ]
    (out_dir / "visual_pack.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"wrote visual prompt pack to {out_dir}")


if __name__ == "__main__":
    main()
