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
