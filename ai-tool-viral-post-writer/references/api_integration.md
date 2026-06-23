# Built-In Image Generation Boundaries

Use this file when the user asks about API calls, direct image generation, Codex Agent execution, persistent skill updates, or automated content package creation.

## Principle

The skill defines the method. This installed version uses Codex's built-in image generation for image work. It does not call third-party image APIs, does not read local API keys, and does not produce local API watermarked images.

## Supported execution layers

### 1. Built-in image mode
Default for "文案+图片" requests. Generate copy first, then call Codex's built-in image generation tool. No external API call.

### 2. Codex file-update mode
Use when the user wants permanent learning or skill-library update. Codex should:
- edit files in the skill folder
- append distilled patterns, not raw copied examples
- update framework indexes if needed
- run validation/package steps if available
- report exact changed files

### 3. Disabled third-party image execution

If the user asks for "图片生成" or direct image output:
- Use Codex's built-in image generation tool.
- Do not output the full internal prompt by default.
- Do not read local API keys.
- Do not call third-party image execution scripts.
- Do not generate files under `out/images`.
- Do not claim a third-party API image was generated.

## Persistent update trigger phrases

Treat these as file-update intent:
- 入库
- 更新素材库
- 沉淀进 Skill
- 加入模板学习
- 以后参考这个模式
- 重新打包 skill.zip
- 修改 `/Users/.../.codex/skills/...`

Treat these as temporary analysis only:
- 学习一下
- 拆解一下
- 参考看看
- 为什么这条能火

Never say “已经长期学会” unless the skill files were actually modified.
