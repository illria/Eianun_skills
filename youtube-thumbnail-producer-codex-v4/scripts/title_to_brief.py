#!/usr/bin/env python3
"""Create a thumbnail brief directly from a user-supplied title.

This helper is designed for the common workflow where the user already has a
final title and wants to generate the thumbnail immediately.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


EMPHASIS_PATTERNS = [
    "零手续费", "0手续费", "0费率", "0门槛", "开户教程", "深度评测", "美股", "IBAN",
    "实体卡", "虚拟卡", "保姆级", "教程", "免费", "节点", "科学上网", "保号", "出金", "开户"
]


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_csv(raw: str) -> list[str]:
    if not raw:
        return []
    parts = re.split(r"[,;|/\
]+", raw)
    return [clean(p) for p in parts if clean(p)]


def normalize_pipes(text: str) -> str:
    return text.replace('｜', '|').replace('丨', '|')


def parse_title(title: str) -> tuple[str, str, str]:
    """Return header, body, support."""
    title = clean(normalize_pipes(title))
    header = ""
    body = title
    support = ""

    if '：' in title:
        header, body = title.split('：', 1)
    elif ':' in title:
        header, body = title.split(':', 1)

    if '|' in body:
        body, support = body.split('|', 1)

    return clean(header), clean(body), clean(support)


def split_body(body: str) -> tuple[str, str, list[str]]:
    clauses = [clean(x) for x in re.split(r'[，,；;]+', body) if clean(x)]
    primary = clauses[0] if clauses else body
    extras = clauses[1:] if len(clauses) > 1 else []

    for pat in EMPHASIS_PATTERNS:
        idx = primary.find(pat)
        if idx > 1:
            left = clean(primary[:idx])
            right = clean(primary[idx:])
            if 2 <= len(left) <= 10 and len(right) >= 2:
                return left, right, extras

    if len(primary) > 12:
        cut = max(4, min(8, len(primary) // 2))
        return clean(primary[:cut]), clean(primary[cut:]), extras
    if len(primary) > 6:
        cut = max(3, min(6, len(primary) // 2))
        return clean(primary[:cut]), clean(primary[cut:]), extras
    return primary, '', extras


def infer_brand_logos(title: str, provided: list[str]) -> list[str]:
    out = list(provided)
    mapping = [
        ('wise', 'Wise'),
        ('neverless', 'Neverless'),
        ('binance', 'Binance'),
        ('cloudflare', 'Cloudflare'),
        ('visa', 'Visa'),
        ('bitcoin', 'Bitcoin'),
        ('btc', 'Bitcoin'),
        ('telegram', 'Telegram'),
        ('google', 'Google'),
    ]
    low = title.lower()
    for needle, label in mapping:
        if needle in low and label not in out:
            out.append(label)
    return out


def guess_color(keywords: list[str], title: str) -> str:
    text = ' '.join(keywords + [title]).lower()
    if any(x in text for x in ['wise', 'bank', 'iban', 'visa', 'finance', 'neverless']):
        return 'green, teal, deep navy, white, subtle neon accent'
    if any(x in text for x in ['binance', 'crypto', 'coin', 'btc']):
        return 'black, gold, green accent, dark navy'
    if any(x in text for x in ['cloudflare', 'cdn', 'cloud']):
        return 'orange, dark navy, white, cyan accent'
    if any(x in text for x in ['esim', 'phone', 'mobile']):
        return 'sky blue, white, magenta accent, clean phone UI'
    return 'deep navy, white, topic-matched accent color'


def make_visual_hint(title: str, brand_logos: list[str], visual: str) -> str:
    if visual:
        return visual
    low = title.lower()
    hints = []
    if 'neverless' in low:
        hints.append('Neverless app dashboard')
        hints.append('global account bank card')
    if 'wise' in low:
        hints.append('Wise withdrawal cue or logo')
    if 'iban' in low:
        hints.append('IBAN / bank account cue')
    if any(x in low for x in ['btc', 'bitcoin', 'crypto', '数字货币']):
        hints.append('crypto coin or trading chart cue')
    if '美股' in title:
        hints.append('US stock account or market chart cue')
    if not hints:
        hints.append('product card, device UI, app dashboard, bold product visual')
    if brand_logos:
        hints.append('allowed logos: ' + ', '.join(brand_logos))
    return ', '.join(hints)


def shorten_header(header: str) -> str:
    if not header:
        return ''
    header = header.replace('深度评测', '深度评测').replace('教程', '教程')
    if len(header) <= 18:
        return header.replace(':', ' | ').replace('：', ' | ')
    return header[:18]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--topic', default='')
    parser.add_argument('--audience', default='')
    parser.add_argument('--keywords', default='')
    parser.add_argument('--user-angle', default='')
    parser.add_argument('--brand-logos', default='')
    parser.add_argument('--visual', default='')
    parser.add_argument('--out', default='dist/thumbnail_brief.json')
    args = parser.parse_args()

    title = clean(args.title)
    keywords = split_csv(args.keywords)
    provided_brands = split_csv(args.brand_logos)
    brands = infer_brand_logos(title, provided_brands)

    header, body, support = parse_title(title)
    main_text, secondary_text, extras = split_body(body)
    support_parts = extras[:]
    if support:
        support_parts.append(support)
    support_text = ' | '.join(support_parts)
    if len(support_text) > 28 and ' | ' in support_text:
        support_text = ' | '.join(support_parts[:2])

    if not header and brands:
        header = brands[0]
    badge_text = shorten_header(header)

    brief = {
        'video_topic': args.topic or title,
        'audience': args.audience,
        'selected_title': title,
        'title_bucket': 'direct_title',
        'keywords': keywords,
        'user_angle': args.user_angle,
        'thumbnail': {
            'main_text': main_text,
            'secondary_text': secondary_text,
            'badge_text': badge_text,
            'support_text': support_text,
            'language': 'zh-CN',
            'visual_focal_object': make_visual_hint(title, brands, args.visual),
            'brand_logos': brands,
            'color_direction': guess_color(keywords, title),
            'composition': 'left-text-right-product',
            'mood': 'ps/canva-made, clear, high-trust, punchy',
            'style_mode': 'ps_made',
        },
        'image_generation': {
            'mode': 'codex-native',
            'aspect_ratio': '16:9',
            'size': '1280x720',
            'style_reference_assets': [
                'assets/style_references/user-example-grid-1.png',
                'assets/style_references/user-example-grid-2.png',
                'assets/style_references/user-example-grid-3.png',
                'assets/style_references/user-example-grid-4.png',
            ],
            'must_include': [
                'large Chinese text',
                'ps/canva-like manual layout',
                'simple product/logo visual',
                'high contrast',
                'visible hierarchy shorter than full title',
            ],
            'avoid': ['bottom red progress bar', 'tiny text', 'cinematic AI poster look', 'glossy 3D render', 'over-detailed dashboard', 'flat template look', 'exact copy of a reference'],
        },
        'revision_history': [],
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
