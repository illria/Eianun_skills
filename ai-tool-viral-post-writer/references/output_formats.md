# Output Formats

## Default response order

1. 项目判断
2. 长文案 1 条
3. 中文案 3 条
4. 短文案 5 条
5. 开头钩子 10 个
6. 评论区补充
7. 配图建议
8. 已生成图片（使用 Codex 内置图片生成）

For "文案生成+图片" tasks:
- Send the copywriting output first.
- Put the ready-to-post main draft inside a fenced `text` code block so the UI keeps a one-click copy button.
- Then call Codex's built-in image generation tool.
- Do not call third-party image APIs.
- Do not output the full image prompt unless the user asks for it.

Never place images before the copy.

When the user asks only for drafts, keep analysis short. When the user asks to “拆解/分析”, expand the judgment section.

## Project judgment template

- 项目类型：...
- 最适合主线：...
- 不适合强套：...
- 中文区人群：...
- 核心爆点：...
- 需要核实/避免夸大的点：...

## Long post template

Length: 800-1500 Chinese characters.

Structure:
1. Hook: one clear strong opening.
2. Pain: 3-6 real user problems.
3. Definition: what the project is in one sentence.
4. Features/benefits: concrete, scenario-based.
5. What it replaces/saves.
6. How to use: 2-5 steps.
7. Boundary/caveat.
8. Personal worldview/opinion.
9. Link.

## Medium post template

Length: 350-800 Chinese characters.

Create 3 angles by default:
- angle 1: pain/save-money
- angle 2: practical workflow/how-to-use
- angle 3: personal viewpoint/trend judgment

Each medium post must stand alone. Do not rely on the long post.

## Short post template

Length: 80-300 Chinese characters.

Use:
- one hook
- 2-5 concrete points
- one judgment
- optional link

Short posts should test different hooks rather than merely compress the same post.

## Hook bank format

Return hooks as concise alternatives:
1. 别再...
2. 有人把...
3. 这个项目解决的不是...而是...
4. 我越来越觉得...
5. 对...来说，这个很适合收藏

## Comment supplement template

Use this when the main post would be cluttered:

补充一下：
- 它是资源目录/开源项目/本地工具，不是万能工具
- 免费额度/价格/模型列表可能变化，使用前看官方页面
- 我建议先从 X 区开始看，再看 Y 区
- 链接：...

## Media suggestion template

Suggest 1-3 screenshots:
- README 顶部: stars, badges, one-line description
- feature table: shows categories/functions
- demo screenshot: if available
- pricing/free-tier page: if free claim is central
- before/after comparison: if tool changes workflow

## Visual package template

Return this after media suggestions by default:

### 配图策略
- 推荐模板：tool-card / resource-map / workflow-diagram / before-after / research-proof / warning-card
- 为什么匹配：一句话说明它如何承接文案主线
- 适合作为：首图 / 第二张信息图 / 评论区补图

### 图上文字
- 主标题：4-12 个中文字符，尽量短
- 副标题：一句话，不放未经核实的数据
- 标签：3-5 个功能/场景词

### 图片生成
Use Codex's built-in image generation tool. Do not show the full internal image prompt by default.

### 参数建议
- 默认比例：16:9
- 备选：4:3 for information cards, 1:1 for cross-platform reuse
- 如果项目截图更可信，优先建议真实截图而不是生成图
