# AI Tool Viral Post Writer 使用说明

这个 Skill 用来写中文 X/Twitter AI 工具文案。适合 GitHub 项目、开源工具、AI 产品、模型/API、Agent/MCP、开发者工具、工具合集和案例素材库维护。

## 1. 最常用的调用方式

### 生成项目文案

```text
$ai-tool-viral-post-writer 文案生成
项目地址：https://github.com/owner/repo
```

默认会输出：

- 项目判断
- 长文案 1 条
- 中文案 3 条
- 短文案 5 条
- 开头钩子
- 评论区补充
- 配图建议

### 生成文案 + 配图

```text
$ai-tool-viral-post-writer 文案+图片
项目地址：https://github.com/owner/repo
```

规则：

- 先输出文案
- 主文案放在 `text` 代码块里，方便一键复制
- 再调用 Codex 内置图片生成
- 默认不展示完整图片 prompt
- 不调用第三方图片 API

### 指定文案长度

```text
$ai-tool-viral-post-writer 写一条 500 字左右的中文 X 文案
项目地址：https://github.com/owner/repo
```

```text
$ai-tool-viral-post-writer 给我 10 个开头钩子
项目地址：https://github.com/owner/repo
```

## 2. 输入什么效果最好

最小输入：

```text
项目地址：https://github.com/owner/repo
```

更好的输入：

```text
项目地址：https://github.com/owner/repo
目标人群：AI 工具用户 / 开发者 / 独立开发者
主打角度：省钱 / 本地部署 / 替代某个付费工具 / 风险提醒
希望语气：犀利一点 / 稳一点 / 像中文 X 爆款
是否要图片：要
```

如果是非 GitHub 产品，可以给：

- 官网链接
- 产品截图
- 功能列表
- 价格页
- 你想突出的卖点
- 不想夸大的边界

## 3. 案例学习和素材库

### 临时拆解，不入库

用在你只是想分析参考文案结构时：

```text
$ai-tool-viral-post-writer 拆解学习：
【粘贴一段爆款文案】
```

它会解释：

- 开头钩子怎么写
- 痛点怎么铺
- 功能怎么翻译成场景
- 结尾怎么收
- 这个模式适合什么项目

不会说已经永久学习。

### 更新素材库，永久入库

用在你希望以后继续参考这个模式时：

```text
$ai-tool-viral-post-writer 更新素材库：
【粘贴一段爆款文案】
```

它会把结构沉淀到：

```text
references/case_library.md
```

注意：

- 不保存原文
- 只保存可复用结构
- 会记录适合项目、不适合项目、公式、钩子和边界
- 只有实际修改文件后，才会说“已入库”

## 4. 常见项目类型写法

### GitHub 工具

```text
$ai-tool-viral-post-writer 文案生成
项目地址：https://github.com/owner/repo
角度：开源替代品
```

### AI Agent / MCP

```text
$ai-tool-viral-post-writer 文案生成
项目地址：https://github.com/owner/repo
角度：AI 工作流从单聊天变成工具系统
```

### 免费资源 / API / 模型集合

```text
$ai-tool-viral-post-writer 文案生成
项目地址：https://github.com/owner/repo
角度：低成本入门，不要写永久免费
```

### 风险提醒

```text
$ai-tool-viral-post-writer 写一条风险提醒文案
项目地址：https://github.com/owner/repo
重点：隐私、成本、权限、合规
```

## 5. 事实和安全边界

这个 Skill 会尽量核实：

- GitHub star
- 免费额度
- 价格
- 支持平台
- 模型版本
- benchmark
- 安全相关说法

不要要求它硬写：

- 永久免费
- 无限制
- 零成本
- 最强
- 吊打
- 必赚
- 绕过付费
- 规避限制

除非官方来源明确支持，否则会改成更稳的表达。

## 6. 推荐完整提示词

```text
$ai-tool-viral-post-writer 文案+图片

项目地址：https://github.com/owner/repo
目标平台：中文 X/Twitter
目标人群：AI 工具用户、开发者、独立开发者
主打角度：省钱 + 工作流效率
语气：年轻、直接、不要官方 PR 味
要求：
1. 先给主文案，放 text 代码块
2. 再给 3 条短文案
3. 最后生成一张首图
4. 不要夸大免费、star、benchmark
```

## 7. 维护命令

校验文件完整性和敏感信息：

```bash
python3 scripts/validate_content_pack.py --skill-root .
```

生成视觉 brief 文件：

```bash
python3 scripts/generate_visual_pack.py \
  --project-name "项目名" \
  --project-type developer-automation \
  --core-value "一句话价值" \
  --features "功能1,功能2,功能3"
```
