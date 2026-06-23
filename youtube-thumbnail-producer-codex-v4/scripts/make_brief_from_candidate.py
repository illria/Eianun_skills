#!/usr/bin/env python3
"""Create a thumbnail brief JSON from a selected title candidate."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def split_csv(text: str) -> list[str]:
    return [x.strip() for x in text.replace(";", ",").replace("|", ",").split(",") if x.strip()]


def pick_candidate(payload: dict, candidate_id: str | None) -> dict:
    candidates = payload.get("candidates", [])
    if not candidates:
        raise SystemExit("No candidates found in JSON.")
    if candidate_id:
        for item in candidates:
            if item.get("id") == candidate_id:
                return item
        raise SystemExit(f"Candidate id not found: {candidate_id}")
    return candidates[0]


def guess_color(keywords: list[str], topic: str) -> str:
    text = " ".join(keywords + [topic]).lower()
    if any(x in text for x in ["wise", "bank", "card", "finance"]):
        return "green, deep navy, white, subtle neon accent"
    if any(x in text for x in ["binance", "crypto", "coin", "btc"]):
        return "black, gold, wheat yellow, sky blue accent"
    if any(x in text for x in ["cloudflare", "cdn", "cloud"]):
        return "orange, dark navy, white, cyan accent"
    if any(x in text for x in ["esim", "phone", "mobile"]):
        return "sky blue, white, magenta accent, clean phone UI"
    return "deep navy, white, topic-matched accent color"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--id", dest="candidate_id")
    parser.add_argument("--topic", default="")
    parser.add_argument("--audience", default="")
    parser.add_argument("--keywords", default="")
    parser.add_argument("--user-angle", default="")
    parser.add_argument("--brand-logos", default="")
    parser.add_argument("--visual", default="")
    parser.add_argument("--out", default="dist/thumbnail_brief.json")
    args = parser.parse_args()

    payload = load_json(args.candidates)
    candidate = pick_candidate(payload, args.candidate_id)
    topic = args.topic or payload.get("topic", "")
    audience = args.audience or payload.get("audience", "")
    keywords = split_csv(args.keywords) or payload.get("keywords", [])
    angle = candidate.get("thumbnail_angle", {})
    brand_logos = split_csv(args.brand_logos)

    brief = {
        "video_topic": topic,
        "audience": audience,
        "selected_title": candidate["title"],
        "title_bucket": candidate.get("bucket", "custom"),
        "keywords": keywords,
        "user_angle": args.user_angle,
        "thumbnail": {
            "main_text": angle.get("main_text") or topic[:16],
            "secondary_text": angle.get("secondary_text") or "",
            "badge_text": angle.get("badge_text") or "",
            "support_text": "",
            "language": "zh-CN",
            "visual_focal_object": args.visual or angle.get("visual_hint", "product card, app logo, device UI"),
            "brand_logos": brand_logos,
            "color_direction": guess_color(keywords, topic),
            "composition": "left-text-right-product",
            "mood": "ps/canva-made, clear, high-trust, punchy",
            "style_mode": "ps_made",
        },
        "image_generation": {
            "mode": "codex-native",
            "aspect_ratio": "16:9",
            "size": "1280x720",
            "style_reference_assets": [
                "assets/style_references/user-example-grid-1.png",
                "assets/style_references/user-example-grid-2.png",
                "assets/style_references/user-example-grid-3.png",
                "assets/style_references/user-example-grid-4.png",
            ],
            "must_include": ["large Chinese text", "ps/canva-like manual layout", "simple product/logo visual", "high contrast"],
            "avoid": ["bottom red progress bar", "tiny text", "cinematic AI poster look", "glossy 3D render", "over-detailed dashboard", "exact copy of a reference"],
        },
        "revision_history": [],
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
