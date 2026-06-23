# Storyboard Pad-Image Prompts

Use this reference when the user asks for a 垫图, storyboard still, extracted character image, extracted prop image, or extracted scene support image.

## Purpose

A pad image is a single generated image used as a support asset for later video generation. It should capture the most stable visual identity of a character, prop, statue, or scene.

## Mandatory Output Contract

For every pad-image request, output the full package. Do not stop at a role summary. The response must include:

1. title line: `【@目标名称】16:9场景分镜垫图` or requested aspect ratio
2. `场景档案：`
3. `Prompt：` in English
4. `Negative：`

Incomplete outputs are not acceptable: role name only, use case only, Chinese description only, constraints only, or no Prompt / no Negative.

## Default Output Format

```markdown
【@目标名称】 16:9场景分镜垫图

场景档案：
· 画面主体：……
· 外形与材质：……
· 姿态与表情（核心反差）：……
· 核心道具：……
· 环境与光影：……

Prompt：
16:9 horizontal cinematic single-panel scene,
...

Negative:
...
```

## How to Extract

When the source is a video prompt or script scene:
1. identify one main target
2. extract appearance details
3. extract material or texture
4. extract gesture / expression
5. extract the strongest prop contrast
6. extract environment and light
7. convert everything into one still-image prompt

## High-Value Visual Anchors

Use as many as needed:
- age / body type / face category
- hair / beard / headpiece
- clothing and fabric
- body material (stone, bronze, wet skin, silk, scales, etc.)
- emotional expression
- hand position and prop interaction
- background scene identity
- key light and shadow behavior

## Common Aspect Ratio Defaults

- 16:9: default for scene pad images and environment stills
- 9:16: use when the user explicitly wants a vertical support image
- 1:1: use for centered character or prop concept sheets if requested

## Example: Petrified Priest Statue

### Chinese archive
- 画面主体：@老祭司石像（前雅典娜神庙祭司）
- 外形与材质：头发与胡须花白，全身石化，灰白岩石质感，粗糙颗粒与轻微风化
- 姿态与表情：仪式性恭敬姿态，但面部凝固为极度恐惧
- 核心道具：握着一把仪式用金匕首，匕首保留黯淡古旧金属光泽
- 环境与光影：幽暗洞穴，一束冷硬顶光打在面部与匕首上

### English prompt skeleton
`16:9 horizontal cinematic single-panel scene, medium shot, three-quarter front view of a hyper-realistic petrified stone statue of an elderly priest...`

### Negative ideas
- living person
- flesh skin
- colorful clothes
- multiple main statues
- cartoon
- anime
- plastic 3d look
- text overlay
- watermark

## Negative Prompt Guidance

For stone / statue targets, commonly suppress:
- living person
- human flesh
- real skin
- alive eyes
- modern clothing
- bright cheerful lighting
- multiple main subjects
- cartoon
- anime
- plastic 3d render
- text overlay
- watermark
- multi-panel layout
