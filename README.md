<div align="center">

**中文** · [English](./README.en.md)

# Eianun Skills

#### 个人 Agent Skills 集合

[![Skills](https://img.shields.io/badge/Skills-3-10B981?style=for-the-badge)](#-skills)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Compatible-3B82F6?style=for-the-badge)](https://agentskills.io)
[![License](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](./LICENSE)

</div>

这个仓库用于存放可直接安装到 Codex、Claude Code、OpenCode、OpenClaw、Hermes 等 Agent 环境里的 Skills。

当前包含文案生成、YouTube 缩略图、Seedance 分镜提示词等个人常用 Skills。每个 Skill 都是独立目录，可以单独安装，也可以一次性安装全部。

---

## 能帮你做什么

- **AI 工具文案**：输入 GitHub 仓库、产品链接或工具说明，输出中文区可发的推文。
- **YouTube 缩略图**：从标题/选题生成中文 YouTube 标题候选、缩略图 brief、Codex 生图 prompt 和修订方案。
- **Seedance 分镜**：把故事、脚本、反馈转成可复制的视频生成分镜提示词。
- **素材库维护**：通过 `case_library.md` 沉淀可复用文案结构。

---

## 目录

| Skill | 一句话 | 入口 |
|---|---|---|
| `ai-tool-viral-post-writer` | 中文 X/Twitter AI 工具爆款文案生成与案例库维护 | [SKILL.md](./ai-tool-viral-post-writer/SKILL.md) · [使用说明](./ai-tool-viral-post-writer/USAGE.md) |
| `youtube-thumbnail-producer-codex-v4` | 中文 YouTube 标题与高点击缩略图生成工作流 | [SKILL.md](./youtube-thumbnail-producer-codex-v4/SKILL.md) · [使用说明](./youtube-thumbnail-producer-codex-v4/USAGE.md) |
| `seedance-storyboard-prompt` | Seedance 分镜提示词、垫图描述、反馈诊断与修订 | [SKILL.md](./seedance-storyboard-prompt/SKILL.md) · [使用说明](./seedance-storyboard-prompt/USAGE.md) |

---

## 安装方式

### 方式 1：一键安装到本机 Codex Skills

```bash
git clone https://github.com/illria/Eianun_skills.git
cd Eianun_skills
bash setup.sh
```

默认会复制所有 Skill 到：

```bash
~/.codex/skills/
```

只安装指定 Skill：

```bash
bash setup.sh ai-tool-viral-post-writer youtube-thumbnail-producer-codex-v4
```

### 方式 2：手动安装

```bash
git clone https://github.com/illria/Eianun_skills.git
mkdir -p ~/.codex/skills
cp -R Eianun_skills/ai-tool-viral-post-writer ~/.codex/skills/
cp -R Eianun_skills/youtube-thumbnail-producer-codex-v4 ~/.codex/skills/
cp -R Eianun_skills/seedance-storyboard-prompt ~/.codex/skills/
```

### 方式 3：Agent 内安装

在支持 Skills 的 Agent 里说：

```text
帮我安装这个 skill：https://github.com/illria/Eianun_skills/tree/main/ai-tool-viral-post-writer
```

---

## 使用方式

安装后，在 Codex 或支持 Skills 的 Agent 里直接调用：

```text
$ai-tool-viral-post-writer 文案生成 https://github.com/owner/repo
```

生成文案并配图：

```text
$ai-tool-viral-post-writer 文案+图片 项目地址：https://github.com/owner/repo
```

拆解参考文案：

```text
$ai-tool-viral-post-writer 拆解学习：
这里粘贴一段爆款文案
```

更新素材库：

```text
$ai-tool-viral-post-writer 更新素材库：
这里粘贴一段你想沉淀的案例
```

---

## Skills

### ai-tool-viral-post-writer

> 把 AI 工具、GitHub 项目、开源产品写成中文 X/Twitter 能传播的文案。

适合：

- AI 工具推荐
- GitHub 项目介绍
- 开源替代品
- Agent / MCP / Coding 工具
- 模型、API、开发者产品
- 工具合集、资源导航
- 爆款文案拆解与素材库维护

核心文件：

- [SKILL.md](./ai-tool-viral-post-writer/SKILL.md)
- [文案框架](./ai-tool-viral-post-writer/references/copywriting_frameworks.md)
- [素材库](./ai-tool-viral-post-writer/references/case_library.md)
- [事实与风险边界](./ai-tool-viral-post-writer/references/claim_safety.md)
- [配图策略](./ai-tool-viral-post-writer/references/visual_brief.md)
- [使用说明](./ai-tool-viral-post-writer/USAGE.md)

### youtube-thumbnail-producer-codex-v4

> 为中文 YouTube 内容生成标题候选、缩略图 brief、生图 prompt 和修订方案。

适合：

- 中文 YouTube 教程/评测/工具类缩略图
- 从选题或笔记生成标题候选
- 从标题直接生成缩略图方案
- Codex 内置图片生成 prompt
- 缩略图反馈修订

入口：

- [SKILL.md](./youtube-thumbnail-producer-codex-v4/SKILL.md)
- [README](./youtube-thumbnail-producer-codex-v4/README.md)
- [使用说明](./youtube-thumbnail-producer-codex-v4/USAGE.md)

### seedance-storyboard-prompt

> 把故事、脚本、小说、场景反馈整理成 Seedance 可用的分镜提示词。

适合：

- 短剧/故事分镜
- 视频生成提示词
- 垫图描述词
- 角色、道具、场景提取
- 生成失败后的诊断与修订

入口：

- [SKILL.md](./seedance-storyboard-prompt/SKILL.md)
- [使用说明](./seedance-storyboard-prompt/USAGE.md)
- [使用指南](./seedance-storyboard-prompt/USAGE_GUIDE.md)

## 开发与校验

校验 Skill 文件完整性和敏感信息：

```bash
python3 ai-tool-viral-post-writer/scripts/validate_content_pack.py --skill-root ai-tool-viral-post-writer
```

注意：仓库不会提交 `.local/`、`out/`、生成图片、API key 或本地私有配置。

---

## License

MIT
