#!/usr/bin/env python3
"""Generate first-pass YouTube title candidates in three buckets.

This is a deterministic helper for Codex. ChatGPT/Codex can and should improve
these candidates conversationally when more context is available.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


def clean_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_keywords(raw: str) -> list[str]:
    if not raw:
        return []
    parts = re.split(r"[,;|/\n]+", raw)
    return [clean_spaces(p) for p in parts if clean_spaces(p)]


def read_notes(path: str | None) -> str:
    if not path:
        return ""
    p = Path(path)
    return p.read_text(encoding="utf-8") if p.exists() else ""


def first_nonempty(items: Iterable[str], fallback: str) -> str:
    for item in items:
        item = clean_spaces(item)
        if item:
            return item
    return fallback


def make_candidates(topic: str, audience: str, keywords: list[str], notes: str) -> list[dict]:
    topic = clean_spaces(topic) or first_nonempty(keywords, "your topic")
    audience = clean_spaces(audience) or "beginners"
    k1 = first_nonempty(keywords[:1], topic)
    k2 = first_nonempty(keywords[1:2], audience)
    k3 = first_nonempty(keywords[2:3], "fees")
    k4 = first_nonempty(keywords[3:4], "risks")

    latest = "\u6700\u65b0"
    tutorial = "\u6559\u7a0b"
    beginner = "\u96f6\u57fa\u7840"
    mainland = "\u5927\u9646\u7528\u6237"
    full = "\u5b8c\u6574\u6d41\u7a0b"
    avoid = "\u907f\u5751"
    explain = "\u4e00\u6b21\u8bf4\u6e05"
    worth = "\u8fd8\u503c\u5f97\u7528\u5417"
    cost = "\u6210\u672c\u548c\u98ce\u9669"
    no_threshold = "0\u95e8\u69db"
    account = "\u5f00\u6237"
    guide = "\u6307\u5357"
    hands = "\u4fdd\u59c6\u7ea7"
    test = "\u5b9e\u6d4b"
    do_not = "\u5148\u522b\u6025\u7740"
    changed = "\u653f\u7b56\u53c8\u53d8\u4e86"

    buckets = [
        (
            "search",
            "Search traffic",
            [
                f"{latest}{topic}{tutorial} | {audience} {full} | {k3}/{k4} {explain}",
                f"{topic}{account}{guide} | {mainland} | {no_threshold} | {k3} {avoid}",
                f"{k1}{tutorial} | {beginner}{full} | {k2} {k3} {k4}",
                f"{audience}{topic}{guide} | {account}/{k3}/{k4} {explain}",
            ],
        ),
        (
            "ctr",
            "CTR hook",
            [
                f"{test}{topic}: {worth}",
                f"{do_not}{topic}{account}: {cost}{explain}",
                f"{topic}{changed}: {mainland}\u5fc5\u770b",
                f"{no_threshold}\u8fd8\u662f\u9690\u85cf\u6210\u672c? {topic}{avoid}",
            ],
        ),
        (
            "tutorial",
            "Tutorial clarity",
            [
                f"{topic}{beginner}{tutorial}: {account}\u5230\u4f7f\u7528{full}",
                f"{hands}{topic}{tutorial}: {audience}\u4ece0\u52301",
                f"{topic}{full}{tutorial}: {k1} {k2} {k3} {explain}",
                f"{mainland}{topic}{guide}: {account}\u3001\u9a8c\u8bc1\u3001\u8d39\u7528\u3001\u4f7f\u7528",
            ],
        ),
    ]
    candidates: list[dict] = []
    for bucket, bucket_name, titles in buckets:
        for idx, title in enumerate(titles, 1):
            title = clean_spaces(title)
            candidates.append(
                {
                    "id": f"{bucket}-{idx}",
                    "bucket": bucket,
                    "bucket_name": bucket_name,
                    "title": title,
                    "thumbnail_angle": infer_thumbnail_angle(bucket, title, topic, keywords),
                    "why_it_might_work": explain_candidate(bucket),
                }
            )
    return candidates


def make_main_thumbnail_text(topic: str, keywords: list[str]) -> str:
    text = " ".join([topic] + keywords).lower()
    if "wise" in text:
        return "Wise\u5f00\u6237"
    if "binance" in text or "\u5e01\u5b89" in text:
        return "\u5e01\u5b89\u6559\u7a0b"
    if "cloudflare" in text:
        return "Cloudflare"
    if "3xui" in text or "x-ui" in text:
        return "3XUI\u9762\u677f"
    if "esim" in text:
        return "eSIM\u6559\u7a0b"
    if "safepal" in text or "card" in text:
        return "\u6d77\u5916\u94f6\u884c\u5361"
    if topic:
        return topic[:16]
    return keywords[0] if keywords else "BIG IDEA"


def infer_thumbnail_angle(bucket: str, title: str, topic: str, keywords: list[str]) -> dict:
    main_text = make_main_thumbnail_text(topic, keywords)
    if bucket == "search":
        secondary = "\u5b8c\u6574\u6559\u7a0b"
        badge = "\u6700\u65b0\u7248"
    elif bucket == "ctr":
        secondary = "\u5148\u770b\u518d\u505a"
        badge = "\u5b9e\u6d4b"
    else:
        secondary = "\u96f6\u57fa\u7840"
        badge = "\u4fdd\u59c6\u7ea7"
    return {
        "main_text": main_text,
        "secondary_text": secondary,
        "badge_text": badge,
        "visual_hint": "product card, app logo, device UI, bold Chinese text, premium lighting",
    }


def explain_candidate(bucket: str) -> str:
    if bucket == "search":
        return "Keyword dense; useful for search and recommended-video matching."
    if bucket == "ctr":
        return "Shorter with tension/curiosity; useful when the topic has risk, policy, or hidden-cost angles."
    return "Clear beginner promise; useful for tutorial trust and conversion."


def write_md(candidates: list[dict], path: str) -> None:
    grouped: dict[str, list[dict]] = {}
    for item in candidates:
        grouped.setdefault(item["bucket_name"], []).append(item)
    lines = ["# Title Candidates", ""]
    for bucket_name, items in grouped.items():
        lines += [f"## {bucket_name}", ""]
        for item in items:
            lines.append(f"### {item['id']}")
            lines.append(item["title"])
            lines.append("")
            angle = item["thumbnail_angle"]
            lines.append(f"- Thumbnail main text: {angle['main_text']}")
            lines.append(f"- Secondary text: {angle['secondary_text']}")
            lines.append(f"- Badge: {angle['badge_text']}")
            lines.append(f"- Why: {item['why_it_might_work']}")
            lines.append("")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--audience", default="")
    parser.add_argument("--keywords", default="")
    parser.add_argument("--notes-file")
    parser.add_argument("--out-md", default="dist/title_candidates.md")
    parser.add_argument("--out-json", default="dist/title_candidates.json")
    args = parser.parse_args()

    notes = read_notes(args.notes_file)
    keywords = split_keywords(args.keywords)
    candidates = make_candidates(args.topic, args.audience, keywords, notes)
    payload = {
        "topic": args.topic,
        "audience": args.audience,
        "keywords": keywords,
        "notes_excerpt": notes[:1200],
        "candidates": candidates,
    }
    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_md(candidates, args.out_md)
    print(f"Wrote {args.out_md} and {args.out_json}")


if __name__ == "__main__":
    main()
