<div align="center">

[中文](./README.md) · **English**

# Eianun Skills

#### Personal Agent Skills collection

[![Skills](https://img.shields.io/badge/Skills-3-10B981?style=for-the-badge)](#skills)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Compatible-3B82F6?style=for-the-badge)](https://agentskills.io)
[![License](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](./LICENSE)

</div>

This repository contains installable Skills for Codex, Claude Code, OpenCode, OpenClaw, Hermes, and other Agent environments that support the Agent Skills format.

It currently includes personal Skills for Chinese AI-tool copywriting, YouTube thumbnail production, and Seedance storyboard prompts. Each Skill is an independent directory and can be installed separately.

## Skills

| Skill | Description | Entry |
|---|---|---|
| `ai-tool-viral-post-writer` | Chinese X/Twitter viral copywriting for AI tools and GitHub projects | [SKILL.md](./ai-tool-viral-post-writer/SKILL.md) |
| `youtube-thumbnail-producer-codex-v4` | Chinese YouTube title and thumbnail production workflow | [SKILL.md](./youtube-thumbnail-producer-codex-v4/SKILL.md) |
| `seedance-storyboard-prompt` | Seedance storyboard prompts, pad-image prompts, diagnostics, and revisions | [SKILL.md](./seedance-storyboard-prompt/SKILL.md) |

## Install

Install all skills into `~/.codex/skills`:

```bash
git clone https://github.com/illria/Eianun_skills.git
cd Eianun_skills
bash setup.sh
```

Install only one skill:

```bash
bash setup.sh ai-tool-viral-post-writer youtube-thumbnail-producer-codex-v4
```

Manual install:

```bash
git clone https://github.com/illria/Eianun_skills.git
mkdir -p ~/.codex/skills
cp -R Eianun_skills/ai-tool-viral-post-writer ~/.codex/skills/
cp -R Eianun_skills/youtube-thumbnail-producer-codex-v4 ~/.codex/skills/
cp -R Eianun_skills/seedance-storyboard-prompt ~/.codex/skills/
```

## Usage

Generate copy:

```text
$ai-tool-viral-post-writer 文案生成 https://github.com/owner/repo
```

Generate copy plus a matching built-in image:

```text
$ai-tool-viral-post-writer 文案+图片 项目地址：https://github.com/owner/repo
```

Analyze a reference post:

```text
$ai-tool-viral-post-writer 拆解学习：
paste a reference post here
```

Update the case library:

```text
$ai-tool-viral-post-writer 更新素材库：
paste a case here
```

YouTube thumbnail workflow:

```text
$youtube-thumbnail-producer 这个标题做一张中文 YouTube 缩略图：
paste title here
```

Seedance storyboard prompts:

```text
$seedance-storyboard-prompt 把这个故事拆成 6 个分镜：
paste story material here
```

## Validation

```bash
python3 ai-tool-viral-post-writer/scripts/validate_content_pack.py --skill-root ai-tool-viral-post-writer
```

This repository intentionally excludes `.local/`, generated images, API keys, and private runtime output.

## License

MIT
