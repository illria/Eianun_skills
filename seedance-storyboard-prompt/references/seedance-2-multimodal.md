# Seedance 2.0 Multimodal Reference

This file distills reusable operational rules from the reviewed 即梦 Seedance 2.0 usage manual. Use it when the user asks about Seedance 2.0, multimodal references, `@图片/@视频/@音频`, extension, editing, one-take continuity, music beat matching, or reference-material planning.

## Input capabilities and limits

Seedance 2.0 supports text, image, video, and audio inputs. Treat exact limits as source-backed but potentially changeable; if the user needs current production limits, verify against the live product.

Reviewed limits:

| Input | Supported details |
|---|---|
| image | jpeg, png, webp, bmp, tiff, gif; up to 9 images; each under 30 MB |
| video | mp4, mov; up to 3 videos; total duration 2-15s; each under 50 MB; reviewed pixel range roughly 480p to 720p |
| audio | mp3, wav; up to 3 audio files; total duration up to 15s; each under 15 MB |
| text | natural language prompt |
| generated duration | reviewed range 4-15s |
| mixed inputs | reviewed combined upper bound: 12 files |

## Interaction routes

Use the route based on material type:

- `首尾帧`: when the user mainly gives a first frame / end frame plus prompt.
- `全能参考`: when the user combines image, video, audio, and text references.

If the user only gives a story or prompt, continue using the normal storyboard workflow and do not pretend multimodal materials exist.

## Reference-role writing

When the user provides multiple materials, assign explicit roles. Do not simply list `@图片1 @视频1 @音频1`.

Good role patterns:

- `@图片1 作为首帧`
- `@图片2 作为尾帧`
- `@图片1 作为主体1的人物外观参考`
- `@图片3 作为主体1的武器参考`
- `@视频1 参考镜头语言、动作节奏和转场方式`
- `@音频1 用于音乐节奏/氛围/配乐参考`

When materials are many, add a compact material map before the prompt:

```text
素材映射：
@图片1 = 主体1外观
@图片2 = 场景空间
@视频1 = 动作节奏与运镜
@音频1 = 情绪节拍
```

## Prompt structure for multimodal tasks

Use this order:

1. Identify each referenced material and its role.
2. State target output: edit, extension, multi-reference generation, one-take, beat-matched video, emotional acting, etc.
3. Write a time-coded story line.
4. Specify continuity: subject identity, movement transition, spatial relation, and style.
5. Specify sound/music only if desired.
6. Add restrictions: no subtitles, no watermark, no duplicate faces, stable identity.

## Common Seedance 2.0 task patterns

### Edit existing video

Use when the user wants to change an action, emotion, plot, product, hair, prop, or short segment while preserving the original video logic.

Write:

- which video is being edited
- what must be preserved
- what must change
- time range and sequence
- emotional state per phase

### Extend video

Use when the user says 延长 / 接着拍.

Write:

- original video subject
- target extension duration
- note that selected generation duration should match the added segment when relevant
- what happens before, during, after the extension
- how motion and camera continue naturally from the source video

### Multi-reference generation

Use when combining character images, props, scenes, video motion, and audio.

Write:

- each subject and prop separately
- which reference controls appearance, which controls motion, which controls scene, which controls sound
- avoid ambiguous labels such as `她` when multiple characters exist

### One-take continuity

Use when the user wants 一镜到底 / no cuts / continuous transition.

Write:

- camera path
- subject path
- occlusion/transition moments
- spatial anchors
- transformation or scene transition logic
- forbid unintended cuts if the user wants one-take

### Music beat matching

Use when the user wants 音乐卡点 / rhythm sync.

Write:

- which audio/video provides beat reference
- key beat moments
- visual changes at each beat
- whether camera framing may change with rhythm

### Emotional acting

Use when the user wants crying, fear, breakdown, hesitation, shock, tenderness, or other subtle acting.

Write emotional transitions as visible steps:

- stillness
- breath
- eye movement
- micro-expression
- hand/shoulder/body tension
- delayed reaction
- final expression

Avoid asking the model to jump directly from neutral to extreme emotion.

## Consistency and limitations

Seedance 2.0 improves consistency, but prompts should still explicitly preserve:

- identity
- costume
- prop details
- scene layout
- camera style
- text/logo handling
- sound role

Important limitation from the reviewed manual:

- Uploading materials containing realistic human faces may be blocked or unsupported by platform compliance rules. If the user relies on real-person face references, warn that this may fail and suggest non-realistic, stylized, or non-identifying alternatives when appropriate.

## Repair hints from the manual

When a result has common issues:

- identity changes: strengthen reference roles and repeat stable identity attributes.
- action unlike reference: specify `@视频1` controls action rhythm and camera movement, not just style.
- extension unnatural: write the transition from original motion into added motion.
- scene jumps: add spatial anchors and a time-coded sequence.
- sound mismatch: state whether sound comes from source video, audio file, or should be natural environmental sound only.
- music not on beat: map visual changes to beat moments.
