# YouTube Thumbnail Producer

A Codex-ready and Skill-ready workflow for Chinese YouTube thumbnails and title ideation.

This version is designed around Codex/native image generation, but the default visual taste is PS/Canva-like manual Chinese tutorial thumbnail rather than cinematic AI poster. The scripts do not try to replace image generation. They create strong title options, structured briefs, prompt files, editable source blueprints, and quality checks.

## Supported workflows

### 1. Topic/notes -> title candidates -> thumbnail

Use when the user has not finalized the title yet.

```bash
python -m pip install -r requirements.txt

python scripts/generate_titles.py   --topic "Wise mainland account opening"   --audience "mainland beginners"   --keywords "Wise, overseas bank, no threshold, tutorial"   --notes-file examples/notes.md   --out-md dist/title_candidates.md   --out-json dist/title_candidates.json

python scripts/make_brief_from_candidate.py   --candidates dist/title_candidates.json   --id "search-1"   --topic "Wise mainland account opening"   --audience "mainland beginners"   --keywords "Wise, overseas bank, no threshold, tutorial"   --out dist/thumbnail_brief.json

python scripts/build_codex_image_prompt.py   --brief dist/thumbnail_brief.json   --style references/thumbnail-style-guide.md   --out dist/codex_image_prompt.md
```

### 2. Direct title -> thumbnail

Use when the user already gives the exact title and wants to see the cover effect immediately.

```bash
python scripts/title_to_brief.py   --title "Neverless深度评测：数字货币零手续费交易美股，自带同名IBAN | 无损出金Wise"   --topic "Neverless 深度评测"   --audience "对数字货币交易美股、海外账户、Wise 出金感兴趣的中文用户"   --keywords "Neverless, 数字货币, 零手续费, 美股, IBAN, Wise"   --brand-logos "Neverless, Wise, Visa, Bitcoin"   --visual "Neverless app dashboard, global account card, growth chart, IBAN cue, Wise withdrawal cue"   --out dist/thumbnail_brief.json

python scripts/build_codex_image_prompt.py   --brief dist/thumbnail_brief.json   --style references/thumbnail-style-guide.md   --variant ps_made   --out dist/codex_image_prompt.md
```

Then use Codex's built-in image generation with `dist/codex_image_prompt.md` and the reference images in `assets/style_references/`.

Optional editable source blueprint:

```bash
python scripts/make_source_svg.py   --brief dist/thumbnail_brief.json   --out dist/editable_source.svg
```

After Codex exports a generated image:

```bash
python scripts/thumbnail_qc.py dist/thumbnail.png
```

## Output files

- `title_candidates.md`: grouped title options.
- `title_candidates.json`: machine-readable title options.
- `thumbnail_brief.json`: selected title, message hierarchy, visual direction, constraints.
- `codex_image_prompt.md`: final prompt for Codex/native image generation.
- `editable_source.svg`: optional editable layout blueprint, not the final thumbnail.
- `revision_prompt.md`: prompt for the next generation round after user feedback.

## Design note

The supplied screenshots show a strong Chinese tech/tutorial YouTube style: huge Chinese text, high contrast color blocks, brand/product references, clear keyword hierarchy, and a manually assembled PS/Canva feeling, not glossy AI poster art. This project preserves that DNA while using native image generation for the polished final image.
