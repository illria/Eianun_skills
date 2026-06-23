<div align="center">

**中文** · [English](./README.en.md)

# Eianun Skills

#### 面向中文 X/Twitter 的 AI 工具爆款文案 Skill

[![Skills](https://img.shields.io/badge/Skills-1-10B981?style=for-the-badge)](#-skills)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Compatible-3B82F6?style=for-the-badge)](https://agentskills.io)
[![License](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](./LICENSE)

</div>

这个仓库用于存放可直接安装到 Codex、Claude Code、OpenCode、OpenClaw、Hermes 等 Agent 环境里的 Skills。

当前主力 Skill 是 **ai-tool-viral-post-writer**：它会围绕 AI 工具、GitHub 项目、开源产品、模型、Agent、API、开发者工具，生成适合中文 X/Twitter 发布的长文案、短文案、开头钩子、评论区补充和配图策略。

它也支持把你给的爆款案例沉淀成可复用的素材库模式，但不会直接复制原文。仓库里保留了当前本地的 `case_library.md`，作为后续迭代的文案资料库。

---

## 能帮你做什么

- **项目文案生成**：输入 GitHub 仓库、产品链接或工具说明，输出中文区可发的推文。
- **多版本拆分**：默认生成长文案、中文案、短文案、钩子和评论区补充。
- **事实边界控制**：对免费、价格、star、benchmark、安全、爬虫等容易翻车的表达做约束。
- **案例学习模式**：区分“临时拆解”和“永久入库”，避免误说已经学习。
- **配图协同**：在支持内置图片生成的环境里，先输出文案，再生成匹配封面图。
- **素材库维护**：通过 `references/case_library.md` 沉淀可复用文案结构。

---

## 目录

| Skill | 一句话 | 入口 |
|---|---|---|
| `ai-tool-viral-post-writer` | 中文 X/Twitter AI 工具爆款文案生成与案例库维护 | [SKILL.md](./ai-tool-viral-post-writer/SKILL.md) |

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
bash setup.sh ai-tool-viral-post-writer
```

### 方式 2：手动安装

```bash
git clone https://github.com/illria/Eianun_skills.git
mkdir -p ~/.codex/skills
cp -R Eianun_skills/ai-tool-viral-post-writer ~/.codex/skills/
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

---

## 开发与校验

校验 Skill 文件完整性和敏感信息：

```bash
python3 ai-tool-viral-post-writer/scripts/validate_content_pack.py --skill-root ai-tool-viral-post-writer
```

生成发布 zip：

```bash
cd ai-tool-viral-post-writer
zip -r skill.zip SKILL.md references scripts agents
```

注意：仓库不会提交 `.local/`、`out/`、生成图片、API key 或本地私有配置。

---

## License

MIT
