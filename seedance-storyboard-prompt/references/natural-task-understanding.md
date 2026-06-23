# Natural Task Understanding / 自然任务理解

作者：eianun

Use this reference whenever the user gives ordinary, informal instructions instead of a strict command. The user does not need to say mode names such as `证据模式`, `垫图模式`, `空间连续性问题`, or `知识库入库`. Infer the real task from the full context, current materials, and requested output.

## Core Principle

Do not build a rigid keyword router. Treat trigger words only as examples. The assistant must reason from context like a normal ChatGPT workflow:

1. Understand the user's real goal.
2. Collect all available materials: current prompt, previous scene, uploaded files, linked pages, project docs, bundled references, and user feedback.
3. Search available knowledge before making claims that need support.
4. Decide the task type and problem type autonomously.
5. Output in the user's requested format, or choose the most useful format when not specified.
6. Separate document facts, current-content observations, AI reasoning, and experience suggestions.

## What the User May Say

The user may use plain language such as:

- `这个文档加进去，以后参考。`
- `这个网页也存起来。`
- `这段生成出来声音怪，帮我查资料后改。`
- `这两个场次接不上。`
- `把这个角色提取成垫图。`
- `按之前格式给我最终 Prompt。`
- `这个画面不对，你看看怎么修。`

Do not force the user to restate the request using technical terminology.

## Autonomous Task Decision

After reading the user's message, decide whether the task is one or more of:

- Add a file to the knowledge base.
- Add a web page to the knowledge base.
- Compare a provided source package against the current skill and integrate only non-duplicative reusable rules.
- Search the knowledge base and answer with evidence.
- Diagnose generated-video problems.
- Revise an existing prompt.
- Generate storyboard tables and final Seedance prompts.
- Generate a pad-image prompt.
- Translate or normalize dialogue.
- Reformat, package, or document the workflow.
- Handle a new related task not listed above.

Do not stop merely because the exact task type is not listed. Plan reasonable steps from the user's goal.

## Evidence-First Rule

For Seedance prompt diagnosis, generation feedback, or claims about best practice, inspect available sources first:

1. Current user-provided prompt / scene / feedback.
2. Nearby scenes or previous/next shots if provided.
3. Uploaded files or project docs.
4. `docs/MANIFEST.md`, `docs/sources/`, `docs/web/`, `docs/cases/` when working in a Codex-style project.
5. Bundled references and runnable source docs, especially `docs/MANIFEST.md`, `docs/NATURAL_WORKFLOW.md`, `source-library-workflow.md`, and `seedance-2-multimodal.md` when the task relates to source provenance, docs ingestion, or Seedance 2.0 multimodal behavior.
6. Web search only when the user asks for current public documentation or the fact may have changed.

Every important recommendation should be labeled as:

- 【资料明确依据】: directly supported by a document, web page, uploaded file, or knowledge-base entry.
- 【当前内容依据】: directly observed in the user's current prompt, scene, feedback, or provided neighboring scene.
- 【AI 推理判断】: the assistant's reasoning from the current content and sources.
- 【经验优化建议】: practical advice without direct source support.

Never present AI reasoning or experience as if it were document text.

## Example: Scene Continuity Feedback

User may say:

`问题是和 SC_3_6 衔接有问题，SC_3_6 镜头对着莉迪亚背影，美杜莎在画面前端，SC_3_7 不应该是莉迪亚正对镜头，后面是美杜莎从座位上起来给她找吃。`

The assistant should not require a special rule called `空间连续性问题`. It should infer:

- The user is reporting generated-video feedback.
- The specific problem is scene continuity / spatial continuity / staging logic.
- The assistant should compare the end of SC_3_6 and the start of SC_3_7.
- The current content establishes a previous over-shoulder or rear-view spatial relationship.
- The next shot should inherit that relationship before cutting to Medusa's action.
- The revised prompt should separate `Lydia's hunger reaction` from `Medusa getting up to fetch food` if mixing them causes spatial confusion.

Output should explain this as current-content evidence and AI reasoning, then revise the prompt.

## Example: Add File

If the user says `这个文档加进去，以后遇到声音问题要参考`, treat it as a knowledge ingestion task:

1. Save or ingest the file under the appropriate knowledge folder.
2. Extract title, source, date/version when visible, and applicability.
3. Summarize rules relevant to Seedance prompt work.
4. Update the manifest or index.
5. Tell the user where it was saved and when it should be used.

If the user says `整合到 GitHub / 整合到 skill / 对比整合，不是覆盖`, treat it as a source integration task:

1. Inspect the provided files.
2. Compare them with existing `SKILL.md` and `references/`.
3. Add only reusable missing rules.
4. Update the source manifest.
5. Avoid raw duplication of full manuals, large image exports, nested skill zips, and generated outputs.

## Example: Add Web Page

If the user says `这个网页也加入资料库`, treat it as a web ingestion task:

1. Fetch or read the page if accessible.
2. Save readable content or summary under `docs/web/`.
3. Extract practical rules.
4. Update the manifest.
5. If access fails, say what failed and ask for pasted content, PDF, DOCX, or screenshots.

## Example: Video Problem Feedback

If the user says `美杜莎声音很怪，流泪很生硬，帮我查资料后改`, infer:

- Diagnose the current prompt.
- Search sources related to audio, dialogue, duration, shot cuts, and micro-expression continuity.
- Distinguish document-backed points from prompt-structure reasoning.
- Give one or more repair plans.
- Provide a revised final prompt.

## Output Flexibility

Use the user's requested format. When the user does not specify a format:

- For added documents: return saved location, summary, manifest update, and future usage.
- For web pages: return fetch status, saved location, extracted rules, and future usage.
- For integrated source packages: return source families reviewed, files changed, key new rules, and what was intentionally not copied.
- For feedback: return diagnosis, evidence, reasoning, repair plan, and revised prompt.
- For pad images: return 场景档案 + English Prompt + Negative.
- For storyboard generation: return 分镜表格版 + 最终可复制 Prompt 版.

Ask a follow-up only when a required material is missing and cannot be inferred. Keep follow-ups short.
