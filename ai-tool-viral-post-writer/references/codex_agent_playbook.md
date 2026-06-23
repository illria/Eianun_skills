# Codex Agent Playbook

This playbook turns the skill into an executable workflow inside Codex or another local agent with file and shell access.

## Workflow A: persistent case-library update

Use when the user provides viral examples and explicitly asks to update the skill.

Steps:
1. Locate skill root. Prefer current working directory if it contains `SKILL.md`; otherwise use the user-provided path.
2. Read `references/case_library.md`, `references/copywriting_frameworks.md`, and `references/claim_safety.md`.
3. Distill the new examples into reusable patterns:
   - name
   - source note
   - reusable mechanics
   - use for
   - do not use for
   - hook variants
   - safety boundaries
4. Append to `references/case_library.md` with a new dated section.
5. If the pattern is not covered by existing frameworks, add or revise one framework in `references/copywriting_frameworks.md`.
6. If claims create new risk categories, update `references/claim_safety.md`.
7. Run a lightweight validation:
   - required files exist
   - no raw API keys are present
   - no huge pasted raw-case dump was copied verbatim
8. Package the full skill as `skill.zip` when packaging tools are available.
9. Report changed files and whether a new zip was produced.

Suggested local command sequence:

```bash
python3 scripts/append_case_pattern.py --pattern-file /path/to/pattern.md --skill-root .
python3 scripts/validate_content_pack.py --skill-root .
```

Then package with the available skill packaging command or zip the skill folder if validation tools are unavailable.

## Workflow B: copy + visual prompt package

Use when the user provides a project link or tool notes and asks for post generation.

Steps:
1. Verify current facts using GitHub/search/official pages where available.
2. Create copy spine.
3. Generate long/medium/short posts.
4. Generate visual brief using `references/visual_brief.md`.
5. Generate a private image prompt for built-in image generation.
6. Put the main ready-to-post draft in a fenced `text` code block for one-click copy.
7. If the user asked for image output, call Codex's built-in image generation tool.
8. Do not call third-party image APIs.

## Workflow C: direct image generation

Use Codex's built-in image generation tool only.

If the user asks for direct generation, do not call third-party image APIs and do not reveal the full internal prompt unless requested.
