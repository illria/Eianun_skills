#!/usr/bin/env python3
"""Build a native image-generation prompt from a thumbnail brief."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_text(path: str | None) -> str:
    if not path:
        return ""
    p = Path(path)
    return p.read_text(encoding="utf-8") if p.exists() else ""


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items if item)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief", required=True)
    parser.add_argument("--style", default="references/thumbnail-style-guide.md")
    parser.add_argument("--ps-style", default="references/ps-made-style-guide.md")
    parser.add_argument("--variant", default="ps_made", choices=["ps_made", "more_ctr", "clean_tutorial", "brand_heavy", "premium"])
    parser.add_argument("--out", default="dist/codex_image_prompt.md")
    args = parser.parse_args()

    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    thumb = brief.get("thumbnail", {})
    image = brief.get("image_generation", {})
    style_text = load_text(args.style)
    ps_text = load_text(args.ps_style)

    variant_notes = {
        "ps_made": "Default style. Make it look like a Chinese creator manually assembled it in Photoshop/Canva: flat blocks, pasted logos/cards, bold text, restrained effects.",
        "more_ctr": "Increase contrast and title impact while keeping a human PS/Canva layout, not cinematic AI art.",
        "clean_tutorial": "Make it clearer, flatter, and less crowded; emphasize beginner-friendly tutorial trust.",
        "brand_heavy": "Use brand/product visuals, but show them like pasted assets or simple cards, not glossy 3D ads.",
        "premium": "Make it cleaner and more professional through spacing and typography, not through cinematic lighting or 3D rendering.",
    }

    support_instruction = ""
    if thumb.get("support_text"):
        support_instruction = f"Render support text as one concise rounded strip or chip: {thumb.get('support_text', '')}"

    lines = [
        "# Codex Native Image Generation Prompt",
        "",
        "Use Codex's built-in image generation to create the final image, but make it look like a human-made Photoshop/Canva Chinese YouTube thumbnail, not AI poster art.",
        "",
        "Create a polished 16:9 YouTube thumbnail, 1280x720, suitable for a Chinese tech/tutorial channel.",
        "The image should feel manually designed: bold 2D typography, flat color panels, rounded capsules, pasted product/logo/card elements, and restrained shadows.",
        "Do not make it cinematic, photorealistic, glossy, holographic, or over-rendered.",
        "",
        "## Visible text to render exactly",
        f"Main text: {thumb.get('main_text', '')}",
        f"Secondary text: {thumb.get('secondary_text', '')}",
        f"Badge text: {thumb.get('badge_text', '')}",
        f"Support text: {thumb.get('support_text', '')}",
        "",
        "Use only 2-3 large text groups. Do not add extra tiny copy.",
        support_instruction,
        "",
        "## Topic and message",
        f"Video topic: {brief.get('video_topic', '')}",
        f"Selected title: {brief.get('selected_title', '')}",
        f"Title bucket: {brief.get('title_bucket', '')}",
        f"Audience: {brief.get('audience', '')}",
        f"User angle: {brief.get('user_angle', '')}",
        f"Keywords: {', '.join(brief.get('keywords', []))}",
        "",
        "## Visual direction",
        f"Composition: {thumb.get('composition', '')}",
        f"Visual focal object: {thumb.get('visual_focal_object', '')}",
        f"Brand/logos allowed: {', '.join(thumb.get('brand_logos', []))}",
        f"Color direction: {thumb.get('color_direction', '')}",
        f"Mood: {thumb.get('mood', '')}",
        f"Style mode: {thumb.get('style_mode', 'ps_made')}",
        f"Variant instruction: {variant_notes[args.variant]}",
        "",
        "Recommended layout recipe: top-left small brand/header badge, center-left oversized hook text, below that one or two rounded support chips, right side product hero/logo/app card pasted into a simple graphic layout.",
        "If the title is long, preserve the full title only as context, but keep the on-canvas text to the shorter hierarchy above.",
        "",
        "## Must include",
        bullet(image.get("must_include", [])) or "- large Chinese text\n- high contrast\n- PS/Canva-like manual layout",
        "",
        "## Avoid",
        bullet(image.get("avoid", [])) or "- bottom red progress bar",
        "- a bottom red progress bar of any kind",
        "- cinematic AI poster look",
        "- photorealistic 3D render",
        "- glossy 3D coins by default",
        "- lens flare, hologram, smoky lighting, dramatic depth of field",
        "- over-detailed fintech dashboard with tiny UI text",
        "- random invented app screens full of small copy",
        "- excessive glow, world-map sci-fi background, or product-ad look",
        "- crowded small text",
        "- exact copying of another creator's layout",
        "",
        "## Reference images",
        "Use these as style references if available, not as exact templates:",
        bullet(image.get("style_reference_assets", [])) or "- assets/style_references/",
        "",
        "## PS/Canva style guide excerpt",
        ps_text[:4000],
        "",
        "## General style guide excerpt",
        style_text[:3000],
        "",
        "## Final output requirement",
        "Generate a complete thumbnail image that looks like a skilled creator assembled it in Photoshop/Canva: sharp, high-contrast, mobile-readable, bold, and intentionally graphic. It should not look like an AI-generated cinematic fintech poster.",
    ]
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(line for line in lines if line is not None), encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
