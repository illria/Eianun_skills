# Troubleshooting Prompt Revisions

Use this reference when the user reports problems after video generation.

## Subtitles or Text Appears

Add or strengthen:
`保持无字幕，避免画面生成任何文字、字幕、标题、说明字、贴纸文字。不要把对白显示为屏幕文字，只作为声音出现。`

## Logo or Watermark Appears

Add:
`不要生成 logo，不要生成水印，不要出现平台标识、电视台角标、品牌标识、视频平台水印。`

## Character ID Drift

Add:
`保持@角色人物身份稳定，五官、年龄、发型、服装、体态和气质保持一致，避免换脸、ID 漂移、年龄漂移、服装漂移。`

If reference images exist, specify:
`@角色 的脸部参考@图片1，服装参考@图片2。`

If using Seedance 2.0 multimodal references, make the material role explicit:
`@图片1 作为@角色外观参考，@视频1 只参考动作节奏和运镜，不改变@角色身份。`

## Duplicate Character / Twins

Add:
`视频全程禁止复制相同人物，禁止双胞胎同款人物，不要多人同脸。同一时刻画面中只保留一个@角色。`

## Character Must Not Show Face

Add:
`@角色 全程背对画面，不露正脸，不直视镜头，不让其他角色看到眼睛。只允许背影、侧后方轮廓或局部剪影。`

## Action Too Fast

Break the action into intermediate states:
- hesitation
- breath pause
- hand movement
- eye movement
- partial body shift
- delayed reaction

## Scene Not Strong Enough

Add stronger anchors:
- foreground object
- background object
- light source
- space layout
- repeated visual motif
- scale comparison
- environmental texture

## Continuity Depends on Previous Shot

Do not write `承接上一镜` in the final prompt. Restate the actual visual relationship:

- camera is behind / beside / above which character
- what is in foreground and background
- where each character is looking
- what action starts the shot
- what object or body part anchors continuity

If a single prompt mixes too many spatial actions, split it into separate shots.

## Multimodal Reference Confusion

When output ignores or mixes up uploaded material roles:

- add a material map before the prompt
- repeat the role near the relevant action
- avoid ambiguous pronouns
- specify whether a source controls appearance, action, camera movement, style, sound, or timing

Example:
`@图片1 控制主体1外观；@视频1 只控制打斗动作和镜头节奏；@音频1 只控制音乐卡点，不改变画面主体。`
