# Seedance Storyboard Prompt 使用说明

这个 Skill 用来把故事、剧本、小说、散文、粗分镜、角色设定、生成失败反馈，转成 Seedance / 生视频模型可用的分镜 Prompt、垫图 Prompt 和修订方案。

更完整的历史说明见 [USAGE_GUIDE.md](./USAGE_GUIDE.md)。这份 `USAGE.md` 是快速上手版。

## 1. 最常用的调用方式

### 从原文生成分镜

```text
$seedance-storyboard-prompt

把下面原文生成 6 个分镜。
要求：
1. 输出分镜表格
2. 输出最终可复制 Prompt
3. 中文对白自动翻译成英文
4. 不要字幕、不要 logo、不要水印

原文：
【粘贴故事/剧本】
```

### 只生成前两个分镜

```text
$seedance-storyboard-prompt

先只生成前两个分镜给我看。
画幅：9:16
风格：写实短剧
对白：中文转英文

原文：
【粘贴内容】
```

### 生成完整场次

```text
$seedance-storyboard-prompt

场次编号：SC_3_6
画幅：竖屏 9:16
风格：写实短剧
总时长：12s
镜头数：4 镜
声音：不要配乐，只要环境声、自然音效和对白
输出：分镜表格 + 最终可复制 Prompt

内容：
【粘贴内容】
```

## 2. 垫图模式

用来提取角色、道具、石像、场景或关键画面，生成一张后续视频参考图。

```text
$seedance-storyboard-prompt 垫图模式

垫图对象：老祭司石像
用途：后续 Seedance 生视频参考图
画幅：16:9
输出：
1. 场景档案
2. 英文 Prompt
3. Negative

内容：
【粘贴分镜/原文】
```

常见对象：

- 角色垫图
- 石像垫图
- 关键道具
- 场景氛围
- 某个镜头的定帧画面

## 3. 反馈修复模式

当视频生成结果不对时，把问题说出来，让它改 Prompt。

```text
$seedance-storyboard-prompt

下面这个 Prompt 生成出来有问题，帮我修。

问题：
1. 女主前后长相不一致
2. 镜头 2 和镜头 3 空间接不上
3. 出现了字幕和水印

修改目标：
1. 固定女主外貌、服装、发型
2. 强化前后镜头动作连续性
3. 明确禁止字幕、logo、水印

原 Prompt：
【粘贴 Prompt】
```

## 4. 证据模式

当你希望它说明“为什么这样改”，用证据模式。

```text
$seedance-storyboard-prompt 证据模式

问题：这段声音怪，流泪也很生硬，帮我查资料后改。

要求：
1. 先列问题结论
2. 标注依据来源
3. 区分【资料明确依据】【当前内容依据】【AI 推理判断】【经验优化建议】
4. 最后给修复版 Prompt

当前 Prompt：
【粘贴 Prompt】
```

如果没有可读资料，它会明确说没有直接文件依据，不会把经验判断伪装成资料结论。

## 4.1 资料库 / 来源整合

当你给新的 PDF、zip、网页、项目包或手册时，可以说：

```text
$seedance-storyboard-prompt

这是 Seedance 的补充资料。
请和当前 GitHub 里的 skill 对比整合：
1. 不要覆盖现有文件
2. 不要原样复制大文件
3. 只抽取可复用规则
4. 更新资料来源索引
5. 告诉我改了哪些文件
```

整合时会优先更新：

- `docs/MANIFEST.md`
- `docs/sources/`
- `docs/web/`
- `docs/cases/`
- `references/source-library-workflow.md`
- `references/seedance-2-multimodal.md`
- 和已有的 evidence / output / troubleshooting 规则

如果只是想在某个项目中长期保存资料，推荐项目里建立：

```text
docs/MANIFEST.md
docs/sources/
docs/web/
docs/cases/
```

新增资料后说：

```text
把这个文档加入资料库，更新 MANIFEST，以后遇到声音、字幕、水印、人物漂移问题时优先参考。
```

也可以用脚本：

```bash
python3 seedance-storyboard-prompt/scripts/ingest_file.py path/to/source.pdf --root . --kind sources
python3 seedance-storyboard-prompt/scripts/search_docs.py 字幕 水印 人物漂移 --root .
```

## 4.2 Seedance 2.0 多模态提示词

当你有图片、视频、音频参考时，不要只堆素材名。给每个素材分配角色：

```text
$seedance-storyboard-prompt

使用 Seedance 2.0 全能参考模式。
素材映射：
@图片1 = 主体外观
@图片2 = 场景空间
@视频1 = 动作节奏和运镜
@音频1 = 音乐卡点

目标：生成 10 秒一镜到底视频。
要求：输出可直接复制的 Seedance Prompt。
```

如果只是首帧/尾帧控制，可以说：

```text
@图片1 作为首帧，@图片2 作为尾帧，中间生成角色从门口走到窗边的连续动作。
```

## 5. 推荐输入信息

越具体越稳：

```text
故事/场次：____
画幅：16:9 / 9:16
风格：写实短剧 / 古风 / 悬疑 / 电影感
总时长：____ 秒
镜头数：____
角色设定：姓名、年龄、发型、服装、身份
场景：地点、时间、天气、光线
对白规则：中文转英文 / 保留中文 / 无对白
声音规则：环境声 / 同期声 / 不要配乐
禁止项：字幕、logo、水印、多人同脸、现代物件
```

## 6. 常用短句

```text
用 Seedance 分镜 Skill，把这段原文生成前两个分镜。
```

```text
用垫图模式，提取老祭司石像。
```

```text
这个 Prompt 生成出来人物变脸，帮我按反馈修。
```

```text
SC_3_6 和 SC_3_7 接不上，帮我强化动作和空间连续性。
```

## 7. 输出格式建议

默认让它输出两份：

1. 分镜表格版：方便检查镜头、动作、声音和对白。
2. 最终可复制 Prompt：方便直接粘贴到视频生成工具。

如果只想要最终版：

```text
只给我最终可复制 Prompt，不要解释。
```

如果要方便逐镜修改：

```text
先给分镜表格，不要急着合成最终 Prompt。
```

## 8. 最终 Prompt 自包含

最终给 Seedance 的 Prompt 不要写：

- 承接上一镜
- 承接 SC_3_6
- 参考前文
- 根据资料
- 当前内容依据
- AI 推理判断

要把这些改成模型能直接执行的画面信息。

错误：

```text
承接 SC_3_6 镜头C，保持莉迪亚背后视角。
```

正确：

```text
镜头位于@莉迪亚身后偏侧位置，画面前景只见@莉迪亚的肩背、半侧脸轮廓与按在腹部附近的手；画面前方是@美杜莎背对镜头端坐在@钢刃王座上的背影。
```
