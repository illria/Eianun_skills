# Codex Instructions: YouTube Thumbnail Producer

This project is image-generation-first, but the default look is human-made PS/Canva Chinese tutorial thumbnail, not AI poster art.

## Most important rule

Use Codex's native image generation capability for the final thumbnail, but prompt it to produce a flat, manually-designed PS/Canva layout. Do not rely on the local Python/SVG renderer as the final visual, but do make the generated result look like a manually assembled PS/Canva layout. The local scripts only help with:

- title candidate drafting
- direct title-to-brief conversion
- brief JSON creation
- native image prompt creation
- revision prompt creation
- editable source/blueprint export
- image quality checks after a generated file exists
- anti-AI-style prompt shaping: flat color panels, readable typography, simple icons, restrained effects

## Decide the workflow mode first

### If the user provides notes but no final title

1. Generate three groups of title candidates: search traffic, CTR hook, tutorial clarity.
2. Ask the user to pick one title.
3. Create `dist/thumbnail_brief.json`.
4. Run `scripts/build_codex_image_prompt.py` to create `dist/codex_image_prompt.md`.
5. Use Codex's built-in image generation with that prompt and the provided style references in `assets/style_references/`. Keep the output looking like a human PS/Canva composition, not a cinematic poster.

### If the user provides the title directly

1. Do not rewrite the title unless the user asks.
2. Run `scripts/title_to_brief.py` to create `dist/thumbnail_brief.json`.
3. Review the brief and make sure the visible thumbnail text is shorter than the full title.
4. Run `scripts/build_codex_image_prompt.py` to create `dist/codex_image_prompt.md`.
5. Use Codex's built-in image generation with that prompt and the provided style references in `assets/style_references/`. Keep the output looking like a human PS/Canva composition, not a cinematic poster.

## Default workflow in Codex

1. Read the user's notes/topic/title.
2. Choose the correct entry mode.
3. Create `dist/thumbnail_brief.json`.
4. Build `dist/codex_image_prompt.md`.
5. Use native image generation.
6. Save/export the generated 16:9 image as `dist/thumbnail.png` or a similar final filename.
7. Run `scripts/thumbnail_qc.py dist/thumbnail.png` if a local image file exists.
8. Save all editable sources: brief JSON, prompt markdown, revision notes, and optional SVG source blueprint.

## Do not

- Do not add a bottom red progress bar.
- Do not output a plain flat template as the final thumbnail.
- Do not create too many small text blocks.
- Do not turn the examples into a copy of another creator's exact thumbnail; use them as style direction only.
- Do not use glossy 3D coins, cinematic green lighting, over-detailed fintech dashboards, lens flares, or AI poster depth by default.
- Do not keep the entire long video title verbatim on the canvas when a shorter hierarchy will read better.
- When output has AI taste, regenerate with `references/ps-made-style-guide.md` and `--variant ps_made`.
