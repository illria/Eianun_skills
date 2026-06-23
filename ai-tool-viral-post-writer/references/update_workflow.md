# Update Workflow: Learning from New Viral Examples

## Important limitation

Installed skills are static packages. A future assistant cannot silently rewrite an already-installed skill in the background. To “learn” new examples permanently, the user should ask ChatGPT to update/repackage the skill, or provide the current skill zip/folder in a writable environment.

In a normal conversation without file-write/package access, produce a structured case-library update block that can later be merged into `references/case_library.md`.

## When user sends new examples

Use this process:
1. Group examples by structure, not topic.
2. For each group, extract:
   - hook type
   - pain setup
   - proof style
   - feature listing style
   - cost/time comparison
   - CTA style
   - risk/boundary style
   - best-fit project types
   - misuse cases where the pattern should not be applied
3. Add distilled patterns to `case_library.md`.
4. If examples reveal a new architecture, add it to `copywriting_frameworks.md`.
5. If examples reveal safety issues, update `claim_safety.md`.
6. Repackage complete skill as `skill.zip`.

## Suggested user prompt for permanent update

“用 ai-tool-viral-post-writer 更新素材库：下面是新爆款文案案例。请只提炼结构，不照抄措辞；把可复用结构写入 references/case_library.md，并重新打包 skill.zip。”

## Quick update block format

When file-writing is unavailable, return:

```markdown
## New Pattern: <name>

Source examples: <brief note>

Reusable mechanics:
- ...

Use for:
- ...

Do not use for:
- ...

Example hook variants:
- ...
```

## Codex persistent update contract

When Codex has local file access, a permanent update must modify files. A valid update report must include:
- changed files
- new pattern name(s)
- whether `references/case_library.md` was modified
- whether `references/copywriting_frameworks.md` was modified
- whether validation ran
- whether `skill.zip` was regenerated

If no file changed, call the result “当前对话拆解” rather than “已入库”.

## Image execution contract

When the user asks for direct image generation:
1. Generate the visual prompt pack only.
2. State that this Skill is currently configured not to call image APIs.
3. Do not read API keys, call image scripts, or save generated image files.
4. Do not block copy generation because image execution is disabled.
