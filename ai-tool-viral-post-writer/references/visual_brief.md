# Visual Brief System for Chinese X/Twitter AI Tool Posts

Use this file after copy generation when the user wants 配图、图片提示词、生图、封面图、素材图, or when the default output asks for media suggestions.

## Goal

Turn the same content spine used for the post into a publishable visual brief. The image must support the copy instead of becoming a random cyberpunk AI picture.

## Default visual direction

Use a restrained Chinese X/Twitter AI-tool cover style:
- modern SaaS / developer / GitHub product feel
- clean, credible, practical, not over-hyped
- high contrast, clear hierarchy, enough whitespace
- no people by default unless the project is personal/creator-led
- avoid cartoon explosion, fake UI chaos, misleading logos, or false screenshots
- do not show exact trademarks/logos unless the user provides assets or asks for a conceptual mockup

## Visual template selection

Choose one primary visual template based on project type:

### 1. Tool card cover
Best for: GitHub repos, AI tools, APIs, agents, developer tools.
Visual metaphor: product card + feature chips + GitHub/repo panel.
Text: project name, one-line value, 3 short benefit chips.

### 2. Resource map cover
Best for: free-resource-directory, tool roundups, model/API lists.
Visual metaphor: organized map/grid of models, APIs, local tools, agents.
Text: “免费 AI 资源地图” style title, category chips, low-cost workflow angle.

### 3. Workflow diagram cover
Best for: agent/workflow, automation, Codex/MCP, research tools.
Visual metaphor: left-to-right workflow with nodes and arrows.
Text: pain → tool → output.

### 4. Before/after comparison card
Best for: open-source replacement, capability breakthrough, cost-saving tools.
Visual metaphor: old workflow vs new workflow.
Text: “以前：...” / “现在：...”.

### 5. Research/report proof card
Best for: Deep Research, multi-agent research, dashboards, analysis/report tools.
Visual metaphor: research dashboard, evidence cards, report preview, agent nodes.
Text: task, evidence, report output.

### 6. Warning/risk card
Best for: hidden cost, privacy/security/hardware warnings.
Visual metaphor: alert card + technical evidence panel.
Text: specific risk, what to check, mitigation cue.

## Image text rules

This Skill uses Codex's built-in image generation for image requests. It does not call third-party image APIs.

For built-in image generation, prefer polished low-text cover visuals over dense Chinese information diagrams. Use one of these modes:

1. Official-style infographic mode: preferred when the user wants readable Chinese text in a generated image prompt. Write the prompt as a complete design-spec narrative, similar to an official infographic prompt:
   - Start with "这张信息图采用..." and define palette, visual style, and overall mood.
   - Define the full page layout before listing details, usually three left-to-right sections or a strict dashboard grid.
   - Put the title location and exact title/subtitle near the beginning.
   - For each section, provide the section title, visual container style, icon/metaphor, and exact text strings.
   - Use natural paragraphs with numbered sections, not terse keyword lists only.
   - Prefer common, easy Chinese words and avoid many near-duplicate short labels such as "少改动/少改改".
   - End with strict text constraints: all text clear, complete, no extra text, no garbled text, no model-added watermarks.
2. Infographic text mode: use when the image needs a more concise but still explicit structured prompt. Specify overall style, exact layout regions, every text string, and where each text string appears. Treat the image like a designed infographic, not a generic cover.
3. Text-light mode: use 3-8 short Chinese words only, but still specify exact placement and all text content.
4. No-text mode: use when the user will overlay text manually. Note that some image models may still invent labels, so manual review is required.

When generating images:
- choose the visual strategy privately
- keep visible Chinese text minimal and easy
- do not show the full prompt unless requested
- mention when a real README screenshot would be more credible than generated art

Never ask the model to "invent UI text" or "add labels" without listing the exact labels. Avoid tiny text, dense paragraphs, fake screenshots, and many small code snippets because they produce blurred or wrong text.

### Infographic prompt structure

When image text must be accurate, write prompts in this structure:

1. Overall style and palette.
2. Canvas layout: left/middle/right columns, top title area, bottom note, or card grid.
3. Exact title and subtitle text.
4. For each section: section title, icon/visual metaphor, exact bullet labels.
5. Reading order and hierarchy.
6. Text accuracy instruction: all text must be exactly as specified, large, sharp, legible, and not substituted.
7. Negative constraints: no extra text, no garbled characters, no fake logos, no tiny unreadable labels.

### Official-style three-column prompt structure

This is the preferred structure after the user's successful Sensenova examples:

1. Opening style sentence: "这张信息图采用..." plus palette, mood, and design genre.
2. Global layout sentence: "整体排版从左到右分为三个主要区块..." or "版面严格按照模块化网格排列...".
3. Title block: exact main title and subtitle, including location.
4. Section 1: section name, purpose, visual container, 2-4 exact labels, icon/metaphor per item.
5. Section 2: workflow/core mechanism, usually vertical axis, funnel, router, ladder, or node flow.
6. Section 3: rules/results/use cases, usually memo panel, API cards, output cards, or status panel.
7. Footer/status bar: one concise conclusion sentence if useful.
8. Final constraints: no unlisted text, no garbled text, no fake screenshots/logos, all Chinese sharp and readable.

Use this structure for developer tools, AI agents, APIs, GitHub repos, skill roundups, and research/report tools. Avoid glitch/Y2K/liquid styles when exact Chinese text matters; those styles intentionally distort text.

## Required visual output package

For every visual pack, include:
- visual strategy: why this visual fits the post
- selected template
- image title: 4-12 Chinese characters if possible
- subtitle: one short sentence
- 3-5 visual chips/keywords
- generated image via built-in imagegen
- aspect ratio recommendation: default 16:9 for X/Twitter; 4:3 if more readable; 1:1 only for cross-platform reuse
- screenshot recommendation: whether to use README/demo/pricing screenshots instead of generated art

## Safety and accuracy

- Do not place unverified stats, star counts, pricing, model versions, or benchmark numbers inside the image.
- If using GitHub visual elements, say “GitHub-style repository card” rather than claiming an exact screenshot unless a real screenshot is used.
- For finance/research examples, include “仅供研究，不构成投资建议” as overlay suggestion if the image mentions results or strategies.
