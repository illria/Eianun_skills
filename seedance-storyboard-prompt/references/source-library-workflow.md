# Source Library Workflow

Use this reference when the user asks to add documents/webpages/cases, asks what sources were used, asks for evidence-backed diagnosis, or says plain-language requests such as `这个文档加进去`, `这个网页也参考`, `查资料后改`, or `以后遇到类似问题参考这个`.

## Purpose

The Seedance workflow should behave like a runnable project knowledge base. This skill package includes a `docs/` skeleton copied from the runnable Seedance package so it can be sent to another Codex environment and used directly.

- `docs/MANIFEST.md`: source index and priority map.
- `docs/sources/`: official docs, PDFs, DOCX/TXT/MD exports, product guides, FAQ.
- `docs/web/`: saved webpage text or manually copied web content.
- `docs/cases/`: failed generations, before/after prompt examples, diagnosis reports.

When these folders exist inside the skill package, treat them as bundled source files. When the user is working in a separate project that has its own `docs/`, prefer the project docs for project-specific evidence.

## Knowledge lookup order

For source-backed Seedance work, inspect information in this order:

1. current user prompt, storyboard, neighboring scene, uploaded file, image, or feedback
2. current project source index if available: `docs/MANIFEST.md`
3. project sources: `docs/sources/`, `docs/web/`, `docs/cases/`
4. skill references:
   - `docs/MANIFEST.md`
   - `docs/NATURAL_WORKFLOW.md`
   - `docs/sources/`, `docs/web/`, `docs/cases/`
   - `references/seedance-2-multimodal.md`
   - `references/evidence-mode.md`
   - `references/troubleshooting.md`
5. public web only when the user asks for current public information or a referenced page must be fetched

If no source is accessible, state that limitation and label subsequent advice as current-content reasoning or experience.

## Adding local documents

When the user gives a local document and asks to add it for future reference:

1. Inspect the file type and extract readable text when possible.
2. Save a distilled markdown version under `docs/sources/` if working inside a project knowledge base.
3. Update `docs/MANIFEST.md` with:
   - file path
   - source title
   - source type
   - date/version if visible
   - summary
   - when to use it
4. Report exactly which files changed.

If the document is large, do not preserve the raw binary by default. Convert or summarize into markdown and keep the original path in the manifest.

## Adding webpages

When the user gives a webpage and asks to add it:

1. Fetch/read the page if available.
2. Save readable content or a distilled summary under `docs/web/`.
3. Update `docs/MANIFEST.md`.
4. If the page requires login, dynamic rendering, or access fails, ask for exported PDF/DOCX/text/screenshots.

## Adding cases

When the user provides a failed generation or before/after example:

Save a distilled case under `docs/cases/` with:

- original prompt or summary
- observed problem
- diagnosis
- evidence labels
- revised prompt
- what future tasks should reuse

Do not store private/raw media unless the user explicitly requests it.

## Searching sources

For small repositories, use `rg` directly:

```bash
rg -n "字幕|水印|人物漂移|声音|口型|首尾帧|全能参考|延长|一镜到底" docs seedance-storyboard-prompt/references
```

For a project with search scripts, a simple keyword search over `docs/` is enough. Search terms should include the problem type, subject, and medium:

- `字幕 水印`
- `人物漂移 多人同脸`
- `声音 哭腔 口型`
- `空间连续性 镜头衔接`
- `首尾帧 全能参考 @图片 @视频 @音频`

## Evidence-backed answer shape

For diagnosis or revision tasks, use:

```markdown
## 问题结论

## 查到的资料依据

## 当前内容依据

## AI 推理判断

## 修改方案

## 修改后的 Prompt
```

The user may ask only for the final prompt. In that case, keep the diagnosis short but do not put diagnosis labels inside the final video prompt.

## Final prompt self-containment

The final prompt sent to Seedance must be executable by the video model alone. Do not include project meta-language such as:

- `承接上一镜`
- `承接 SC_3_6`
- `参考前文`
- `根据官方指南`
- `当前内容依据`
- `AI 推理判断`
- `资料显示`

Rewrite these into concrete visible information inside the current shot.

Bad:

```text
承接 SC_3_6 镜头C，保持莉迪亚背后视角。
```

Good:

```text
镜头位于@莉迪亚身后偏侧位置，画面前景只见@莉迪亚的肩背、半侧脸轮廓与按在腹部附近的手；画面前方是@美杜莎背对镜头端坐在@钢刃王座上的背影。
```

When continuity is complex, split it into separate shots instead of relying on hidden context.
