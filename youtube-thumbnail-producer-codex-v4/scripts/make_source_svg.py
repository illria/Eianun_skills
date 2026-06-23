#!/usr/bin/env python3
"""Create an editable SVG layout blueprint from the thumbnail brief.

This is not the final thumbnail renderer. It is a source/reference file that can
be edited in Figma/Illustrator/Inkscape or used to guide native image generation.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


def svg_text(x: int, y: int, text: str, size: int, weight: int = 900) -> str:
    text = html.escape(text)
    return f'<text x="{x}" y="{y}" font-family="Arial, Noto Sans CJK SC, sans-serif" font-size="{size}" font-weight="{weight}" fill="white" stroke="black" stroke-width="6" paint-order="stroke fill">{text}</text>'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief", required=True)
    parser.add_argument("--out", default="dist/editable_source.svg")
    args = parser.parse_args()
    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    thumb = brief.get("thumbnail", {})
    main_text = thumb.get("main_text", "MAIN TEXT")
    secondary = thumb.get("secondary_text", "")
    badge = thumb.get("badge_text", "")
    support = thumb.get("support_text", "")
    color_note = html.escape(thumb.get("color_direction", "topic colors"))
    visual = html.escape(thumb.get("visual_focal_object", "product visual"))

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
  <title>Editable thumbnail source blueprint</title>
  <desc>Blueprint only. Final image should be generated with native image generation.</desc>
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="#07131f"/>
      <stop offset="1" stop-color="#0c6b54"/>
    </linearGradient>
  </defs>
  <rect width="1280" height="720" rx="0" fill="url(#bg)"/>
  <rect x="48" y="52" width="1184" height="616" rx="42" fill="rgba(0,0,0,0.22)" stroke="rgba(255,255,255,0.16)" stroke-width="3"/>
  <rect x="60" y="70" width="310" height="78" rx="34" fill="rgba(255,255,255,0.92)"/>
  <text x="90" y="122" font-family="Arial, Noto Sans CJK SC, sans-serif" font-size="42" font-weight="900" fill="#111827">{html.escape(badge)}</text>
  {svg_text(72, 290, main_text, 92)}
  {svg_text(72, 410, secondary, 72)}
  <text x="82" y="500" font-family="Arial, Noto Sans CJK SC, sans-serif" font-size="38" font-weight="800" fill="#d7fff1">{html.escape(support)}</text>
  <rect x="810" y="120" width="340" height="430" rx="44" fill="rgba(255,255,255,0.92)" stroke="rgba(0,0,0,0.25)" stroke-width="4"/>
  <text x="850" y="210" font-family="Arial, sans-serif" font-size="38" font-weight="900" fill="#111827">PRODUCT / LOGO</text>
  <text x="850" y="280" font-family="Arial, sans-serif" font-size="26" font-weight="700" fill="#334155">{visual}</text>
  <text x="850" y="345" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#334155">Colors: {color_note}</text>
  <text x="72" y="655" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="rgba(255,255,255,0.72)">Source blueprint only - no bottom red progress bar</text>
</svg>
'''
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(svg, encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
