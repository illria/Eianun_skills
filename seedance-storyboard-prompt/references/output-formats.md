# Output Formats

## Storyboard Table

Use this table by default:

| 镜头 | 时长 | 景别 | 角度 | 运镜 | 焦段 | 画面内容 | 中文对白 | 英文对白 | 声音 | 剪接点 |
|---|---:|---|---|---|---|---|---|---|---|---|
| 镜头A | 0s–3s | 近景 | 平视偏低 | 固定轻微呼吸感 | 标准50mm | ... | ... | ... | ... | ... |

## Final Prompt Skeleton

```text
SC_x_x ｜ 【写实风格 · 小说模式 · 场景功能 · 2镜 · 轻运镜激活 · 5600K · @场景名（室内 · 晨） · 竖屏9:16】

【小说激活模式已启动 · 输入材质：小说/散文/剧本 · 旁白已全量转化为演绎 · 人物对白已自动翻译为英文 · 英文对白作为实际说出口台词】
【竖屏短剧模式已激活 · 开场钩子类型：近景惊醒钩子】
场景人物清单：主动：@人物A ｜静默：@人物B ｜背景存在：@人物C

镜头A ｜ 0s–3s ｜ 近景 · 平视偏低 · 固定轻微呼吸感 · 标准50mm
画面描述…… @人物A 低声说：{English spoken dialogue.}
[剪接点 3s — xxx时切]

【切镜】镜头B ｜ 3s–6s ｜ 中近景转中景 · 平视 · 缓慢后拉 · 35mm
画面描述……
【本单元结束】

备注：
1、不要配乐，仅允许同期对白、环境声、自然音效。
2、保持无字幕，避免画面生成任何文字或字幕。
3、不要生成 logo，不要生成水印，不要出现平台标识。
4、视频全程禁止出现外形、着装、配饰完全相同的两个人，杜绝双胞胎同款人物，不要多人同脸。
5、保持人物身份稳定，避免换脸、ID 漂移、年龄漂移、服装漂移。
6、保持指定风格、画幅、色温和场景统一，不要突然跳转为无关风格。
```

## Final Prompt Self-Containment

The final copyable prompt must be understandable without the diagnostic report, project docs, previous messages, or source labels.

Do not include:

- `承接上一镜`
- `承接 SC_x_x`
- `参考前文`
- `根据资料`
- `根据官方指南`
- evidence labels such as 【资料明确依据】 or 【AI 推理判断】

Instead, convert context into concrete scene information:

- camera location
- foreground/background relation
- character positions
- character action
- prop state
- time-coded movement
- sound behavior

When continuity depends on a previous shot, restate the needed visual layout inside the current shot.


## Evidence Mode Output

Use this structure when the user asks for diagnosis with sources:

```markdown
## 问题结论

## 参考资料
- `文件路径或文件名`: 相关内容摘要

## 依据拆解
| 建议 | 类型 | 依据 | 判断标准 |
|---|---|---|---|

## 当前分镜结构依据

## 优化方案

## 优化后的 Prompt
```

Required labels:
- 【资料明确依据】
- 【当前内容依据】
- 【AI 推理判断】
- 【经验优化建议】
