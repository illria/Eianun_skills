# YouTube Thumbnail Producer 使用说明

这个 Skill 用来生成中文 YouTube 标题候选、缩略图 brief、Codex 生图 prompt、可编辑源文件和修订方案。它的审美目标是中文教程/评测区常见的 PS/Canva 手工缩略图，而不是电影海报感 AI 图。

## 1. 两种主要用法

### 用法 A：还没有标题，先生成标题候选

适合你只有选题、笔记、视频大纲、受众和关键词时。

```text
$youtube-thumbnail-producer

选题：Wise 内地用户开户教程
受众：想开海外账户的新手
关键词：Wise、海外账户、无门槛、教程、出金
目标：先给我标题候选，再给缩略图方向
```

它会先产出：

- 搜索关键词型标题
- 好奇心/点击率型标题
- 教程清晰型标题
- 推荐选择
- 缩略图文字层级建议

你选定标题后，再继续：

```text
用第 2 个标题继续生成缩略图 brief 和 Codex 图片 prompt。
```

### 用法 B：已经有标题，直接做缩略图

适合你已经有最终标题，只想快速出封面方向。

```text
$youtube-thumbnail-producer

标题：Neverless深度评测：数字货币零手续费交易美股，自带同名IBAN | 无损出金Wise
目标：直接生成中文 YouTube 缩略图方案
风格：中文金融科技教程，PS/Canva 手工感，信息密度高但不要乱
```

它会把长标题拆成：

- 角标/标签
- 主视觉大字
- 副钩子
- 证明点/利益点
- 背景和产品元素
- 颜色和层级

## 2. 推荐输入格式

```text
$youtube-thumbnail-producer

视频标题：____
视频主题：____
目标观众：____
关键词：____
必须出现的品牌/产品：____
不想出现的元素：____
缩略图风格：中文科技教程 / 金融评测 / AI 工具推荐 / 对比测评
输出：
1. 标题优化建议
2. 缩略图 brief
3. Codex 生图 prompt
4. 可编辑 SVG 源文件建议
```

## 3. 文案和画面原则

缩略图文字不要直接塞完整标题。优先拆成 2-3 组大字：

```text
角标：实测 / 教程 / 免费 / 避坑
主钩子：最短、最大、最有点击欲的词
副钩子：结果、收益、反差或风险
底部条：一个证明点
```

示例：

```text
原标题：免费 AI API 大合集：不用信用卡也能跑模型

缩略图文字：
角标：免费 API
主钩子：不用信用卡
副钩子：也能跑模型
底部条：新手低成本起步
```

## 4. 让 Codex 直接生成图片

```text
$youtube-thumbnail-producer

标题：____
直接生成缩略图图片。
要求：
1. 先给缩略图 brief
2. 再调用内置图片生成
3. 16:9
4. 中文大字要少而准
5. 不要电影海报风
```

如果中文文字容易错，可以这样说：

```text
中文文字尽量少，只保留 2 组大字，其余用色块和图形表达。
```

## 5. 本地脚本用法

安装依赖：

```bash
python3 -m pip install -r requirements.txt
```

从标题直接生成 brief：

```bash
python3 scripts/title_to_brief.py \
  --title "你的标题" \
  --topic "视频主题" \
  --audience "目标观众" \
  --keywords "关键词1, 关键词2" \
  --out dist/thumbnail_brief.json
```

生成 Codex 图片 prompt：

```bash
python3 scripts/build_codex_image_prompt.py \
  --brief dist/thumbnail_brief.json \
  --style references/thumbnail-style-guide.md \
  --variant ps_made \
  --out dist/codex_image_prompt.md
```

生成可编辑 SVG 蓝图：

```bash
python3 scripts/make_source_svg.py \
  --brief dist/thumbnail_brief.json \
  --out dist/editable_source.svg
```

检查最终图片比例：

```bash
python3 scripts/thumbnail_qc.py dist/thumbnail.png
```

## 6. 修图/改稿

把反馈说具体：

```text
$youtube-thumbnail-producer 修改这张缩略图方案：

问题：
1. 字太多
2. 主标题不够大
3. AI 味太重
4. 背景不够像中文科技教程

保留：
1. 标题方向不变
2. 主色调蓝白

请输出新版 brief 和新版 Codex 生图 prompt。
```

## 7. 不建议这样用

不要一次要求：

- 10 个品牌 logo 都上图
- 完整长标题全部放封面
- 很多小字
- 又赛博朋克又金融教程又可爱卡通
- 同时做 5 个不同视频的封面

更稳的方式是一次做一个标题，一个主视觉，一个明确风格。
