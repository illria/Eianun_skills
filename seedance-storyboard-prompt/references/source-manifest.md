# Seedance Source Manifest

This file is the distilled source index for the Seedance Storyboard Prompt skill. It records what external/user-provided materials have been integrated, where their reusable rules were merged, and when to consult them.

Do not paste the original documents verbatim into outputs. Use this manifest to cite source families and then use the relevant reference file for operational rules.

## Integrated sources

### 即梦 Seedance 2.0 使用手册（全新多模态创作体验）.zip

- Source path reviewed: `/Users/wenruo/Downloads/ai短剧提示词skills/🎬 即梦 Seedance 2.0 使用手册（全新多模态创作体验）.zip`
- Source type: Seedance 2.0 product/manual export with markdown plus many image examples.
- Integrated as: `references/seedance-2-multimodal.md`
- Use for:
  - Seedance 2.0 input limits and interaction modes.
  - Multimodal reference planning with images, video, audio, and text.
  - `@素材` reference role writing.
  - video extension, multi-reference, video edit, one-take continuity, music beat matching, emotion acting, and consistency advice.
  - realistic human-face upload limitations.
- Do not store in this repository:
  - the raw 208 MB image export
  - all original case tables
  - full image examples

### seedance-prompt-agent-codex(1) (1).zip

- Source path reviewed: `/Users/wenruo/Downloads/ai短剧提示词skills/seedance-prompt-agent-codex(1) (1).zip`
- Source type: Codex starter project for Seedance Prompt Agent with `AGENTS.md`, `docs/MANIFEST.md`, `docs/NATURAL_WORKFLOW.md`, ingestion/search scripts, and a packaged skill.
- Integrated as:
  - `references/source-library-workflow.md`
  - updates to `references/natural-task-understanding.md`
  - updates to `references/evidence-mode.md`
- Use for:
  - source library folder conventions
  - manifest/index behavior
  - evidence lookup order
  - plain-language ingestion tasks
  - troubleshooting with source labels
- Do not store in this repository:
  - nested `skills/skill.zip`
  - generated project outputs
  - duplicate starter project folders

### Seedance Prompt Agent 项目使用指南.pdf

- Source path reviewed: `/Users/wenruo/Downloads/ai短剧提示词skills/Seedance Prompt Agent 项目使用指南.pdf`
- Source type: user-facing setup and usage guide for the Seedance Prompt Agent project.
- Integrated as:
  - `references/source-library-workflow.md`
  - updates to `references/output-formats.md`
  - updates to `USAGE.md`
- Use for:
  - how to add documents or webpages to a Codex project knowledge base
  - how to verify sources are indexed in `docs/MANIFEST.md`
  - why final video prompts must be self-contained
  - common plain-language commands for source-backed repair
- Do not store in this repository:
  - full PDF text
  - installation screenshots
  - Mac/Codex app onboarding details that are not needed by the skill

## Evidence citation policy

When answering source-backed tasks, cite or name the integrated source family, then label the recommendation:

- 【资料明确依据】: backed by an integrated source or a user/project document.
- 【当前内容依据】: visible in the current prompt, storyboard, neighboring scene, or feedback.
- 【AI 推理判断】: inferred from source + current content.
- 【经验优化建议】: useful production advice without direct source support.

If the user asks whether a rule came from a document, answer precisely:

- `Seedance 2.0 多模态/输入限制相关` -> from the 即梦 Seedance 2.0 manual summary.
- `资料库、MANIFEST、入库、检索、证据标签相关` -> from the Prompt Agent project guide/starter workflow.
- `分镜格式、对白翻译、垫图、Seedance-safe 限制` -> from this skill's own bundled rules unless a project source also supports it.

## Integration boundary

This repository keeps distilled reusable instructions, not raw archives. If the user later provides updated official docs, integrate them by:

1. extracting reusable rules,
2. updating this manifest,
3. updating the relevant reference file,
4. avoiding raw duplication of large exports.
