---
name: youtube-thumbnail-producer
description: generate high-retention youtube video titles and premium 16:9 youtube thumbnails, especially chinese tutorial thumbnails with bold readable text, ps/canva-like manual layout, brand/product visuals, and iterative revisions. use when the user provides video notes, a topic, screenshots, opinions, keywords, or example thumbnails and wants title candidates, direct title-to-thumbnail generation, codex/native image-generation prompts, final thumbnail generation, editable source files, or feedback-based thumbnail revisions.
---

# YouTube Thumbnail Producer

Use this skill to run an end-to-end thumbnail workflow for Chinese YouTube content. The final thumbnail should be made with a native image-generation tool when available, but the default aesthetic must look like a human-made PS/Canva Chinese tutorial thumbnail, not a cinematic AI poster. Local scripts are support utilities for title ideation, title-to-brief conversion, prompt creation, quality checks, and editable source packs.

## Entry modes

Use one of these two entry modes.

### Mode A: title ideation first

Use when the user gives notes, topic, audience, or opinions but has not fixed the final title.

1. Intake the user's topic, notes, audience, keywords, constraints, style references, and feedback.
2. Generate title candidates in three buckets: search/keyword, curiosity/CTR, and tutorial/clarity. Use `references/title-frameworks.md`. If running in Codex or a shell-only environment, `scripts/generate_titles.py` can create a deterministic first pass.
3. Ask the user to choose a title, or choose the strongest one yourself only when the user explicitly asks you to proceed.
4. Create a structured thumbnail brief. Use `references/brief-schema.md`. In Codex, `scripts/make_brief_from_candidate.py` can convert a chosen title candidate into a brief.

### Mode B: direct title to thumbnail

Use when the user already gives a final or near-final title and wants to see the thumbnail effect immediately.

1. Keep the supplied title as the source of truth unless the user asks to rewrite it.
2. Decompose the title into thumbnail text hierarchy, usually:
   - badge/header: brand, review label, version label, or angle marker
   - main hook: the shortest high-value concept
   - secondary hook: the promise, result, or differentiator
   - support strip: one concise proof point or benefit
3. Use `references/direct-title-thumbnail-playbook.md` to shorten and prioritize the visible text. Do not place the full long video title on the canvas.
4. In Codex or a shell-only environment, use `scripts/title_to_brief.py` to create `dist/thumbnail_brief.json` directly from the supplied title.

## Shared generation workflow

After either entry mode:

1. Build 2-4 image-generation prompt variants. Use `references/codex-native-image-workflow.md`, `references/direct-title-thumbnail-playbook.md`, and `references/thumbnail-style-guide.md`.
2. Generate the thumbnail with the native image-generation tool. Do not present a Pillow/SVG layout as the final visual unless the user explicitly asks for a local mockup.
3. Export editable source files alongside the image: the chosen title, brief JSON, image prompt markdown, revision notes, and optional SVG layout/source blueprint.
4. For revisions, preserve the selected title and key message unless the user asks to change them. Apply the feedback to the prompt/brief, regenerate with native image generation, and append to revision history.

## Native image generation rule

When image generation is available, use it directly for the final thumbnail. The script-generated SVG is only an editable source blueprint for text/layout handoff, not the final design. The final image should look like a polished human-designed PS/Canva YouTube thumbnail: bold flat typography, simple color blocks, rounded pills, brand/product elements, limited shadows, and high contrast. Avoid cinematic AI poster effects.

If the environment cannot call a native image generator, write the exact prompt to `dist/codex_image_prompt.md`, tell the user to run it with Codex's built-in image generation, and provide the editable brief/source files.

## Visual constraints

- Use 16:9 composition, default 1280x720.
- Never add a bottom red progress bar. A time badge is allowed only if the user asks.
- Use at most 2-3 large Chinese text groups plus one support strip or chip.
- Preserve exact brand/product names when the user provides them. Brand logos are allowed.
- Do not overfill the canvas. Keep one clear focal hierarchy.
- Prefer strong contrast, chunky typography, rounded labels, flat or lightly shaded product cards, simple icons/logos, and visual metaphors from the supplied examples. Default to PS/Canva-like manual composition, not AI cinematic rendering.
- If Chinese text rendering is unstable, shorten the visible text rather than shrinking the font. Prefer background-only generation plus editable HTML/SVG text overlay when exact text is critical.

## Useful files

- `AGENTS.md`: codex-facing operating instructions.
- `references/codex-native-image-workflow.md`: how to use Codex/native image generation as the main renderer.
- `references/direct-title-thumbnail-playbook.md`: how to go straight from a user-supplied title to a thumbnail brief and prompt.
- `references/ps-made-style-guide.md`: how to suppress AI-poster taste and make outputs look like human PS/Canva thumbnails.
- `references/thumbnail-style-guide.md`: visual DNA extracted from the user's example screenshots.
- `references/title-frameworks.md`: title candidate patterns.
- `references/brief-schema.md`: thumbnail brief JSON fields.
- `references/revision-playbook.md`: revision handling.
- `prompts/thumbnail_generation_prompt.md`: reusable prompt template.
- `prompts/revision_prompt.md`: prompt template for modifications.
- `scripts/title_to_brief.py`: convert a user-supplied title directly into a thumbnail brief.
- `scripts/build_codex_image_prompt.py`: build a final image-generation prompt from a brief.
- `scripts/make_source_svg.py`: create an editable SVG layout blueprint from the brief.
- `scripts/thumbnail_qc.py`: check final image size/aspect ratio after generation.
