#!/usr/bin/env python3
"""Create a draft case-library update from raw viral copy examples.

This helper does not replace human judgment. It groups examples with simple
heuristics so ChatGPT can review, edit, and merge the output into
references/case_library.md when updating the skill package.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

PATTERNS = [
    (
        "hidden-risk warning",
        ["偷偷", "固态", "ssd", "硬盘", "风险", "泄露", "越狱", "安全", "伤", "账单"],
        "Use for hidden costs, security, privacy, hardware, or billing risk posts.",
    ),
    (
        "free resource burst",
        ["免费", "白嫖", "不用信用卡", "零", "$0", "free", "订阅", "额度"],
        "Use for free tiers, free resource collections, API credits, and low-cost entry posts.",
    ),
    (
        "open-source replacement",
        ["开源", "github", "本地", "离线", "mit", "零依赖", "自部署"],
        "Use for open-source or local alternatives to paid/cloud tools.",
    ),
    (
        "workflow breakthrough",
        ["一次", "自动", "生成", "record", "replay", "实时", "一键", "端到端", "全程"],
        "Use for features that compress multi-step work into a simpler workflow.",
    ),
    (
        "agent composition",
        ["agent", "智能体", "codex", "mcp", "claude code", "cursor", "工具", "子智能体"],
        "Use for agent orchestration, MCP, coding agents, and tool-using AI workflows.",
    ),
    (
        "builder project launch",
        ["我做了", "在线体验", "dashboard", "看板", "项目", "反馈", "streamlit", "huggingface"],
        "Use for build-in-public demos and user-created projects.",
    ),
    (
        "personal stack list",
        ["必备", "我的", "工具类", "聊天类", "软件", "清单"],
        "Use for personal stacks, weekly lists, and subjective roundups.",
    ),
    (
        "research/model release explainer",
        ["模型", "训练", "benchmark", "分数", "论文", "发布", "hugging face", "aaai"],
        "Use for model, research, paper, and benchmark explainers.",
    ),
]


def split_examples(text: str) -> list[str]:
    chunks = re.split(r"\n\s*(?=\d+[\.、])", text.strip())
    return [c.strip() for c in chunks if c.strip()]


def classify(example: str) -> tuple[str, str]:
    lower = example.lower()
    scores: list[tuple[int, str, str]] = []
    for name, keywords, usage in PATTERNS:
        score = sum(1 for kw in keywords if kw.lower() in lower)
        scores.append((score, name, usage))
    score, name, usage = max(scores, key=lambda item: item[0])
    if score == 0:
        return "general viral tool post", "Use when no stronger pattern is detected."
    return name, usage


def hook_line(example: str) -> str:
    lines = [line.strip() for line in example.splitlines() if line.strip()]
    return lines[0][:120] if lines else ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="text file containing numbered viral examples")
    parser.add_argument("--output", default="case_update_draft.md")
    args = parser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    examples = split_examples(text)
    grouped: dict[str, list[str]] = defaultdict(list)
    usage_map: dict[str, str] = {}

    for ex in examples:
        name, usage = classify(ex)
        grouped[name].append(hook_line(ex))
        usage_map[name] = usage

    out: list[str] = ["# Case Library Update Draft", "", "Review and edit before merging into references/case_library.md.", ""]
    for name, hooks in grouped.items():
        out.append(f"## Pattern: {name}")
        out.append("")
        out.append(usage_map[name])
        out.append("")
        out.append("Observed hooks:")
        for hook in hooks[:10]:
            out.append(f"- {hook}")
        out.append("")
        out.append("Reusable mechanics:")
        out.append("- Identify the actual project type before using this pattern.")
        out.append("- Keep one main narrative line per draft.")
        out.append("- Translate features into user jobs and concrete scenarios.")
        out.append("- Add boundary/caveat when claims involve free, finance, scraping, safety, or benchmarks.")
        out.append("")

    Path(args.output).write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {args.output} with {len(examples)} examples grouped into {len(grouped)} patterns")


if __name__ == "__main__":
    main()
