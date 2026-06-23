---
name: seedance-storyboard-prompt
description: generate Seedance-ready storyboard prompts, pad-image prompts, prompt revisions, and evidence-backed diagnostics from natural user requests. use when the user gives stories, scripts, rough shots, reference notes, files, web docs, video-generation feedback, or plain-language requests such as add this document, save this web page, fix this scene, explain the evidence, extract this character, or make final copyable prompts. autonomously infer the task, inspect available sources, label evidence, translate dialogue, and preserve Seedance formatting.
---

# Seedance Storyboard Prompt

> 作者水印 / Author watermark: **eianun**
> 
> 本 Skill 及配套说明默认署名：**eianun**。如需二次分发、团队内部流转或继续迭代，请保留该作者署名与水印。配套水印图见 `assets/eianun-watermark.png`。

## Overview

Convert story material into video-generation-ready storyboard prompts. Produce a reviewable storyboard table, a final copyable prompt, and when requested, a storyboard pad-image prompt (垫图描述词) that can be used to generate a single support image for a character, prop, or scene.

Use this skill for Chinese or bilingual story text, scripts, novels, prose, PDF/DOCX/TXT story files, rough scene notes, reference-image mappings, and generated-video feedback. Preserve the user's story intent, character identity, dialogue constraints, reference labels, and requested delivery format.

## Natural Task Understanding

The user does not need to name a mode. Infer the task from ordinary language, current context, files, links, prompts, feedback, and requested format. Do not rely only on keyword matching or an ever-growing list of fixed triggers.

When the user says things like `这个文档加进去`, `这个网页也参考`, `这个画面有问题`, `帮我查资料后改`, `按之前格式来`, `出垫图`, or `先给两个分镜`, first infer the real goal, then choose the right workflow. The task may be adding knowledge, fetching a web source, searching docs, diagnosing generation failure, revising a prompt, generating a storyboard, creating a pad image, or another related task.

Before giving source-backed advice, inspect available materials first. Separate recommendations into 【资料明确依据】, 【当前内容依据】, 【AI 推理判断】, and 【经验优化建议】. Never present reasoning or experience as document facts.

For details and examples, consult `references/natural-task-understanding.md`. For source-library behavior and the bundled runnable knowledge base, consult `references/source-library-workflow.md`, `docs/MANIFEST.md`, and `docs/NATURAL_WORKFLOW.md`.

## Default Workflow

Evidence mode workflow:
- If the user asks for 依据, 参考文件, 判断标准, why/why not, source-backed diagnosis, or asks whether a suggestion is from a document, first retrieve available files or project docs before giving advice.
- If a source is inaccessible, say so and mark the point as not directly sourced.
- Distinguish every recommendation as one of: 【资料明确依据】, 【当前内容依据】, 【AI 推理判断】, or 【经验优化建议】.
- Do not present AI reasoning or experience-based guesses as document facts.
- End with the revised prompt only after the evidence report.

1. Identify the input type: novel, prose, script, rough storyboard, character sheet, reference notes, file content, or feedback.
2. Choose the mode: short-drama execution, vibe creating, or mixed.
3. Extract or infer only necessary production fields: scene id, characters, scene, time of day, aspect ratio, style, shot count, duration, dialogue rules, sound rules, and restrictions.
4. If the user asks for 垫图 / storyboard pad image / 单张场景图 / 角色提取图 / 物件提取图, extract the visual target and output a pad-image description package.
5. Output a storyboard table unless the user asks only for the final prompt or only for the pad image.
6. Output the final copyable prompt unless the user asks only for the table or only for the pad image.
7. Add Seedance-safe constraints: no subtitles, no logo/watermark, no duplicate faces/twins, stable character identity, and stable style.
8. For generation feedback, revise the existing prompt directly against the reported problems.

## Important References

- `references/natural-task-understanding.md`: natural-language task understanding and autonomous judgment workflow.
- `references/evidence-mode.md`: evidence-backed diagnosis format and source labeling.
- `references/source-library-workflow.md`: how to add/search project sources, update the docs manifest, and keep final prompts self-contained.
- `docs/MANIFEST.md`: bundled runnable source index for this skill package.
- `docs/NATURAL_WORKFLOW.md`: natural task understanding workflow from the runnable Seedance package.
- `references/seedance-2-multimodal.md`: Seedance 2.0 multimodal input limits, reference-role writing, and multimodal task patterns.
- `references/output-formats.md`: storyboard table and final prompt structures.
- `references/pad-image-prompts.md`: pad-image extraction format.
- `references/dialogue-translation.md`: Chinese-to-English dialogue rules.
- `references/troubleshooting.md`: common Seedance prompt repair patterns.
- `scripts/search_docs.py`: optional keyword search over project `docs/` and bundled references.
- `scripts/ingest_file.py`: optional local-file ingestion into a Codex-style `docs/` knowledge base.
- `scripts/ingest_url.py`: optional webpage ingestion into `docs/web/` when network access is available.

## Mode Routing

### Short-Drama Execution Mode

Use for shot-by-shot short drama, novel-to-storyboard conversion, strict scene structure, fixed duration, fixed shot count, dialogue preservation, reference labels, camera terms, focal lengths, cut points, or final prompts similar to `SC_3_1 ｜ 【写实风格 · 小说模式 · 场景建立 · 2镜...】`.

In this mode:
- Preserve shot structure and user-specified formatting.
- Use `镜头A`, `镜头B`, etc.
- Use time ranges such as `0s–3s`.
- Include shot size, angle, camera movement, focal length, and cut points when useful.
- Preserve user-specified dialogue exactly in meaning; translate spoken Chinese dialogue to English by default for final prompts.
- Do not collapse the prompt into loose prose.

### Vibe Creating Mode

Use for emotional, memory-like, atmospheric, literary, surreal, cinematic, advertising, or concept-driven visuals when the user does not require strict shot execution.

In this mode:
- Strengthen story, mood, memory, atmosphere, imagery, and subjective experience.
- Remove or soften low-value technical parameters unless the user explicitly wants them preserved.
- Keep the image center clear and emotionally unified.
- Do not force a rigid shot table unless the user asks for it.

### Mixed Mode

Use when the user needs both executable storyboard structure and emotional/cinematic/literary quality.

In this mode:
- Keep the short-drama structure.
- Make each shot visually and emotionally vivid.
- Preserve execution fields without turning the output into dry mechanical notes.

### Evidence Feedback Mode (证据反馈模式)

Use when the user asks for:
- 依据 / 参考文件 / 判断标准
- 为什么这样改
- 这条建议来自哪个文档
- 实时文档内容依据
- troubleshooting with citations
- source-backed diagnosis

In this mode:
- Inspect available uploaded files, project docs, or Codex repository docs before answering.
- Prefer project docs and user-provided files over memory.
- Output a structured diagnostic report, not only a revised prompt.
- Cite or identify file names and section summaries when exact citations are not available.
- Separate source-backed facts from current-content observations, AI reasoning, and creative experience.
- If no relevant document is found, say `未找到直接资料依据` and continue with clearly labeled inference or experience.

### Source Library / Knowledge Ingestion Mode

Use when the user gives a PDF, DOCX, TXT, Markdown file, zip export, webpage, or project folder and says it should be added, remembered, referenced later, compared, merged, or used as evidence.

In this mode:
- Inspect the provided source before editing skill files.
- Compare with existing `references/` and integrate only reusable, non-duplicative rules.
- Do not overwrite existing references unless the user explicitly asks.
- Do not add raw large archives, generated media, or full manuals when a distilled reference is enough.
- Update `docs/MANIFEST.md` when a new source family is integrated.
- Report what was integrated, what was intentionally not copied, and which files changed.
- When working in a project knowledge base rather than this skill repository, use `scripts/ingest_file.py`, `scripts/ingest_url.py`, or `scripts/search_docs.py` as support tools if appropriate.

### Storyboard Pad-Image Mode (垫图模式)

Use when the user asks for any of the following:
- 垫图
- storyboard pad image
- 单张场景图
- 角色提取图
- 物件提取图
- 角色设定图
- 场景垫图
- 从某个镜头里把某个人物、石像、道具、场景单独提取出来

In this mode:
- Extract one main visual target from the source scene, shot, or prompt.
- Convert the target into a single-image generation description instead of a multi-shot video prompt.
- Keep the result highly visual and image-friendly.
- Default to a `场景档案 + Prompt + Negative` package unless the user asks for another format.
- Treat the pad image as a support asset for later video generation, not as the final video prompt itself.
- If the target is a character, prop, or statue from an existing scene, preserve its identity, material, emotional state, and core visual contrast.

### Seedance 2.0 Multimodal Mode

Use when the user mentions Seedance 2.0, 即梦, 全能参考, 首尾帧, `@图片`, `@视频`, `@音频`, multiple reference materials, extension, video editing, music beat matching, one-take shots, or multimodal prompt planning.

In this mode:
- Load `references/seedance-2-multimodal.md`.
- Assign every referenced material a clear role before writing the final prompt.
- Prefer explicit material maps over vague references.
- Warn about reviewed limits or realistic human-face upload restrictions when relevant.

## Information Check

Before writing, check whether the input contains enough information:
- visual anchor: main person, object, place, monster, prop, or concept
- action or state: what is happening
- local tone: mood, light, pace, emotional temperature
- video theme: short drama, cinematic scene, fantasy, horror, romance, ad, game cg, documentary, etc.
- output target: storyboard table, final prompt, or both
- constraints: aspect ratio, duration, shot count, dialogue preservation, no music, no subtitles

Ask a short follow-up question only when missing information would seriously affect the result. Ask at most 1–3 questions at a time. Do not over-question when the user already provided enough context.

## Hard Constraint Priority

Always preserve explicit user constraints before creative optimization.

Priority order:
1. User hard constraints: dialogue, narration, music, sound effects, structure, format, shot count, duration, aspect ratio, character names, reference image mapping, style limits.
2. Creative optimization: clarify story, emotion, action, visual anchor, atmosphere, and shot rhythm.
3. Vibe/style consistency: improve language only after preserving the first two layers.

Rules:
- If the user says dialogue must be preserved word for word, preserve the exact meaning and dramatic intent.
- If the user says no music, do not add BGM.
- If the user gives a shot structure, preserve it unless asked to simplify.
- If the user gives `@character`, `@prop`, or `@scene` labels, keep those exact references.
- If the user asks for a final copyable prompt, keep that prompt clean and production-ready.
- Final prompts must be self-contained for the video model. Do not write `承接上一镜`, `承接 SC_x_x`, `参考前文`, `根据资料`, evidence labels, or diagnosis language inside the final prompt. Translate those ideas into concrete visible scene layout, character positions, actions, and timing.

## Dialogue Translation Rules

When source text contains Chinese character dialogue, automatically translate character dialogue into natural English for the final copyable prompt unless the user explicitly asks to keep Chinese dialogue.

Default behavior:
- In the storyboard table, preserve the original Chinese dialogue and provide the English translation for review.
- In the final copyable prompt, use only the English translated dialogue as the spoken line.
- Do not put Chinese and English versions of the same spoken line together in the final prompt.
- Keep all spoken lines in one language inside the final prompt to avoid mixed-language speech.
- Preserve intent, emotion, social relationship, and dramatic subtext.
- Do not over-literalize Chinese lines when natural cinematic English is better.
- Do not add new meaning.
- If the user says “对白逐字保留”, preserve meaning exactly while translating faithfully into English, unless the user says “中文逐字保留”.
- If the user says “保留中文台词”, keep Chinese dialogue in the final prompt and do not translate it.
- If the user says “中英双语”, provide bilingual dialogue in the table, but ask before putting bilingual speech into the final video prompt.

Final prompt dialogue format:
- Keep Chinese shot descriptions if the overall prompt is Chinese.
- Use English only inside spoken dialogue braces `{...}`.
- Example: `@莉迪亚 在梦中痛苦呓语：{No... let me go... I don't want to marry the sea god...}`

Translation style:
- Use concise, speakable, cinematic English.
- Keep fear, hesitation, sarcasm, anger, tenderness, irony, or restraint.
- Avoid stiff subtitle-like translation.
- Avoid modern slang unless the story style supports it.
- For fantasy, myth, ancient, or tragic scenes, use slightly elevated but natural English.

Common translations:
- `不要……放开我……我不想嫁给海神……` -> `{No... let me go... I don't want to marry the sea god...}`
- `你……一夜没睡吗？` -> `{You... stayed awake all night?}`
- `我习惯了。` -> `{I'm used to it.}`
- `因为外面的人，比我可怕得多。` -> `{Because the people outside are far more terrifying than I am.}`
- `至少你没有假装是为我好。` -> `{At least you never pretended it was for my own good.}`

## Character and Subject Rules

Use stable subject naming. For recurring people, places, and props, use consistent `@` labels:
- `@莉迪亚`
- `@美杜莎`
- `@美杜莎洞穴-石像博物馆`
- `@青铜匕首碎片`
- `@美杜莎端坐王座背影[场景]`

When multiple characters appear, include:
`场景人物清单：主动：@人物A ｜静默：@人物B ｜背景存在：@人物C`

Character stability rules:
- Repeat the same character name every time the character appears.
- Avoid vague pronouns when identity might be confused.
- Do not rename characters across shots.
- For identity-drift risk, explicitly state face, age, clothing, posture, and role stability.
- If a character must not show their face, state this clearly in every relevant shot or in the notes.

## Seedance Prompt Safety Rules

Unless the user says otherwise, include these restrictions in the final prompt:
1. Keep no subtitles; avoid generating any text or captions on screen.
2. Do not generate logos, watermarks, platform marks, or UI marks.
3. Do not create two identical-looking people in the same frame.
4. Avoid twins, duplicate bodies, duplicate faces, and 多人同脸.
5. Keep character identity stable; avoid face drift, age drift, clothing drift, or role confusion.
6. Keep style stable; avoid sudden shifts into anime, game, stage-play, or unrelated styles.
7. If reference images exist, specify each image role: face reference, costume reference, scene reference, posture reference, prop reference, or style reference.

## Dynamic Description Order

Within each shot, write in this order when possible:
1. Shot information: shot size, angle, movement, focal length.
2. Subject action and state: who does what, with expression, body movement, or emotional state.
3. Spatial relationship: where the subject sits relative to scene, background, props, and other characters.
4. Atmosphere and light: time, color temperature, shadow, dust, fog, fire, water, etc.
5. Sound: dialogue, breathing, environment, impact, natural sound, or silence.

## Sound Rules

Preserve user-specified dialogue, narration, music, and sound effects.

If no music is requested:
`不要配乐，仅允许同期对白、环境声、自然音效。`

If the scene has no dialogue:
`本段如无对白，则只保留环境声、自然音效和角色呼吸声。`

When dialogue exists:
- Translate character dialogue into English by default.
- Use the English line inside `{}` in the final copyable prompt.
- Keep the Chinese original only in the storyboard table or notes.
- Do not generate subtitles for either Chinese or English dialogue.
- Do not write dialogue as on-screen text.
- Spoken dialogue should be heard as voice only.

Use sound as visual support, not clutter: breathing, cave echo, wind, footsteps, fabric movement, stone friction, snake hair movement, water dripping.

## Story / Novel Conversion Rules

When converting novel or prose passages:
- Convert narration into visible performance.
- Convert inner emotion into face, body, breath, hesitation, posture, object handling, distance, and silence.
- Preserve dialogue meaning; translate spoken Chinese dialogue to English by default.
- Do not invent major plot points.
- Do not add new characters unless background presence is required.
- Keep each shot focused on one dramatic function.

Useful scene functions:
- 惊醒钩子
- 场景建立
- 人物反应
- 情绪推进
- 空间压迫
- 危险提示
- 对白交锋
- 关系转折
- 道具特写
- 悬念收束

## Storyboard Pad-Image Rules

When generating a 垫图 / storyboard pad image, output a single-image prompt package instead of a shot list.

Default output structure:

- Title line: `【@目标名称】 宽高比场景分镜垫图`
- `场景档案`
- `Prompt`
- `Negative`

### Mandatory Pad-Image Output Contract

When the user asks for 垫图, pad image, 角色提取图, 石像提取, 道具提取, 场景垫图, or says “按照前面的垫图形式发我描述词”, always output the full pad-image package.

The output MUST contain exactly these primary sections in this order:

1. `【@目标名称】16:9场景分镜垫图` or the requested aspect ratio
2. `场景档案：`
3. `Prompt：`
4. `Negative：`

Never output only a role extraction summary. The following incomplete outputs are NOT allowed:
- only `角色名称`
- only `垫图用途`
- only a Chinese visual description
- only `限制` or constraints
- only a short text card
- output without an English `Prompt：` section
- output without a `Negative：` section

If the user gives only a target name but no source scene, still create a complete pad-image package from available context. Ask one short question only when the target identity is truly impossible to infer.

For stone statue / petrified victim targets, the English `Prompt：` section must include:
- single-panel image composition
- aspect ratio
- main subject identity
- material texture
- pose
- facial expression
- key prop if any
- environment
- lighting
- photorealistic or cinematic style

For every pad-image task, the `Negative：` section must suppress:
- living person
- real skin / flesh texture
- subtitles / text overlay
- watermark / logo
- duplicate main subject
- cartoon / anime style unless requested
- low realism or plastic 3d render look

### Pad-Image Extraction Workflow

1. Identify the extraction target.
   - character
   - statue / petrified victim
   - prop / artifact
   - scene corner / environment
   - emotional keyframe

2. Summarize the target into 4–6 visual anchors:
   - subject identity
   - appearance / material
   - pose / expression
   - core prop
   - environment / background
   - lighting / mood

3. Preserve the strongest visual contrast.
   Examples:
   - stone body vs metallic dagger
   - terrified face vs respectful ritual posture
   - soft dawn light vs cold cave darkness
   - elegant robe vs grotesque petrification

4. Write the `场景档案` in concise Chinese.

5. Write the `Prompt` in clean, generation-friendly English unless the user asks for Chinese.

6. Write a `Negative` list that suppresses common failure modes.

### Pad-Image Content Rules

- Focus on one primary subject; avoid multiple competing subjects.
- Use a single-panel still image composition.
- Preserve the requested aspect ratio; if unspecified, default to 16:9 for scene pad images and preserve user preference for 9:16 if they ask for vertical.
- If the target comes from a video shot, translate camera framing into a still-image composition such as `medium shot`, `close-up`, `three-quarter front view`, `side profile`, or `full-body portrait`.
- If the target is a stone statue, emphasize realistic petrified material, surface weathering, frozen gesture, and frozen emotion.
- If the target includes a highlighted prop, create a strong material contrast so the prop reads clearly.
- Keep the background supportive and simple; blur or soften secondary elements when needed.
- Prefer photorealistic, cinematic, high-detail wording unless the user asks for another style.

### Pad-Image Output Example Skeleton

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
living person, real skin, text overlay, watermark, ...
```

If the user asks to extract a target from a specific shot, mention that target by its source context but keep the final pad-image prompt self-contained.

## Storyboard Table Format

Default table columns:

| 镜头 | 时长 | 景别 | 角度 | 运镜 | 焦段 | 画面内容 | 中文对白 | 英文对白 | 声音 | 剪接点 |
|---|---:|---|---|---|---|---|---|---|---|---|

Column rules:
- `镜头`: use `镜头A`, `镜头B`, etc.
- `时长`: use ranges like `0s–3s`.
- `景别`: use 远景, 全景, 中景, 中近景, 近景, 特写, 大特写.
- `角度`: use 平视, 高位俯角, 低位仰角, 侧视, 过肩, etc.
- `运镜`: use 固定, 缓推, 后拉, 跟拍, 平移, 升降摇臂, 手持轻晃, etc.
- `焦段`: use 20mm, 35mm, 50mm, 85mm when useful.
- `画面内容`: write clear action and visual composition.
- `中文对白`: preserve the original line from the source text when present; otherwise write `无`.
- `英文对白`: provide the translated spoken line when present; otherwise write `无`.
- `声音`: include relevant sound only.
- `剪接点`: state when and why to cut.

## Final Copyable Prompt Format

Use this structure:

```text
SC_x_x ｜ 【写实风格 · 小说模式 · 场景建立 · 2镜 · 运镜激活 · 5600K · @场景名（室内 · 晨） · 竖屏9:16】

【小说激活模式已启动 · 输入材质：小说/散文/剧本 · 旁白已全量转化为演绎 · 人物对白已自动翻译为英文 · 英文对白作为实际说出口台词】
【竖屏短剧模式已激活 · 开场钩子类型：近景/特写/动作/反差/悬念】
场景人物清单：主动：@人物A ｜静默：@人物B ｜背景存在：@人物C

镜头A ｜ 0s–3s ｜ 景别 · 角度 · 运镜 · 焦段
画面描述…… @人物A 低声说：{English spoken dialogue.}
[剪接点 3s — xxx时切]

【切镜】镜头B ｜ 3s–6s ｜ 景别 · 角度 · 运镜 · 焦段
画面描述……
[剪接点 6s — xxx时切]

【本单元结束】

备注：
1、不要配乐，仅允许同期对白、环境声、自然音效。
2、保持无字幕，避免画面生成任何文字或字幕。
3、不要生成 logo，不要生成水印，不要出现平台标识。
4、视频全程禁止出现外形、着装、配饰完全相同的两个人，杜绝双胞胎同款人物，不要多人同脸。
5、保持人物身份稳定，避免换脸、ID 漂移、年龄漂移、服装漂移。
6、保持指定风格、画幅、色温和场景统一，不要突然跳转为无关风格。
```

If the user explicitly asks to keep Chinese dialogue, replace the first activation line with:
`【小说激活模式已启动 · 输入材质：小说/散文/剧本 · 旁白已全量转化为演绎 · 中文对白保留】`

## Scene Header Rules

Use:
`SC_x_x ｜ 【风格 · 模式 · 场景功能 · x镜 · 运镜状态 · 色温 · @场景名（室内/室外 · 时段） · 画幅】`

Examples:
- `SC_3_1 ｜ 【写实风格 · 小说模式 · 惊醒钩子 · 2镜 · 轻运镜激活 · 5600K · @美杜莎洞穴-石像博物馆（室内 · 晨） · 竖屏9:16】`
- `SC_4_2 ｜ 【写实风格 · 短剧模式 · 对白交锋 · 3镜 · 固定镜头为主 · 冷色月光 · @废弃神庙（室内 · 夜） · 竖屏9:16】`

If scene id is not provided, create a simple one such as `SC_1_1`.

## Opening Hook Rules

For vertical short drama, prioritize a strong first 2–3 seconds.

Possible hook types:
- 近景惊醒钩子
- 特写情绪钩子
- 冲突钩子
- 动作钩子
- 反差钩子
- 悬念钩子
- 场景压迫感钩子
- 道具危险钩子

Do not always start with a wide establishing shot. If the scene has fear, danger, awakening, injury, whispering, or discovery, consider starting with a close or medium-close shot.

## Camera Language Policy

In short-drama execution mode:
- Keep useful camera language.
- Use focal lengths and camera movement when they clarify execution.
- Do not overload each shot with unnecessary technical parameters.

In vibe creating mode:
- Remove low-value technical terms such as exact lens numbers, aperture, shutter, camera brand, sensor size, and excessive grading instructions unless the user asks to preserve them.
- Translate technical intent into viewer experience when useful.

Examples:
- Convert `缓慢推轨镜头` to `视线缓缓靠近，压迫感逐渐增强`.
- Keep `特写` if it is important for emotion.
- Keep `竖屏9:16` when the user is making short drama.

## Prompt Revision Rules

When the user reports a generation problem, revise the prompt against that problem instead of restarting unnecessarily.

Common feedback and fixes:
- Character face drift / ID drift: add stronger identity, face, age, costume, and reference-image constraints.
- Unwanted subtitles/text: strengthen `保持无字幕，避免画面生成任何文字、字幕、标题、说明字、贴纸文字。`
- Logo/watermark: add `不要生成 logo，不要生成水印，不要出现平台标识、电视台角标、品牌标识。`
- Duplicate characters/twins: add `视频全程禁止复制相同人物，禁止双胞胎同款人物，不要多人同脸，同一时刻画面中只保留一个@角色。`
- Character shows face when forbidden: repeat `@角色全程背对画面，不露正脸，不直视镜头，不让其他角色看到眼睛。`
- Scene not strong enough: add specific anchors for space structure, foreground, background, light source, atmosphere, and scale.
- Action too fast: replace direct action with intermediate states: hesitation, breathing, hand movement, pause, eye movement, partial movement.

## Reference Material Handling

When the user provides reference images, videos, or asset names:
- Use `@图片1`, `@视频1`, or user-provided asset labels only when clearly mapped.
- Define subject identity before using it repeatedly.
- Distinguish face reference, costume reference, posture reference, scene reference, prop reference, and style reference.
- If the mapping is unclear, ask one short question.

Example:
`@莉迪亚 的脸部参考@图片1，服装参考@图片2；@美杜莎洞穴-石像博物馆 的空间结构参考@图片3。`

## Editing and Extension Task Wording

If the user asks to edit or extend an existing video:
- Use `视频1` directly.
- Do not write `参考视频1` unless the task is truly reference-generation.

Examples:
- Editing: `严格编辑视频1，将画面中的...修改为...`
- Extension: `延长视频1，保持主体、空间、光线和叙事连续，生成...`
- Reference: `参考视频1中的运镜节奏，生成...`

## Reference Files

Consult these files only when needed:
- `references/dialogue-translation.md`: more dialogue translation examples and style rules.
- `references/output-formats.md`: output templates for table and final copyable prompt.
- `references/troubleshooting.md`: prompt repair patterns for common generation problems.

## Default Response Style

Use concise, production-ready Chinese.

Avoid:
- long theory explanations
- internal labels like `S1/E2/I1`
- irrelevant teaching
- excessive disclaimers
- rewriting the user's story into a different plot

Prefer:
- direct execution
- stable tables
- clean final prompts
- clear notes
- minimal but useful explanation


## Evidence and Retrieval Rules

When the user wants a grounded diagnosis, follow this sequence:

1. Identify the problem from the current prompt or generated-video feedback.
2. Retrieve relevant material from available sources:
   - uploaded files in the current chat
   - project files such as `docs/MANIFEST.md`, `docs/sources/`, `docs/web/`, `docs/cases/`
   - bundled references when useful, especially `references/evidence-mode.md` and `references/troubleshooting.md`
   - web sources only when the user asks for latest/public documentation or when the fact may have changed
3. Extract the exact rule, file name, section, or short evidence summary.
4. Classify every recommendation:
   - 【文件明确依据】: directly supported by an available document
   - 【当前分镜结构推断】: derived from the current shot timing, dialogue length, shot count, or prompt structure
   - 【经验优化建议】: practical prompt/video-production advice without direct document backing
5. If a claim lacks direct support, explicitly mark it as inference or experience.
6. Give the revised prompt after the evidence report.

Default evidence-mode output:

```markdown
## 问题结论

## 参考资料
- 文件名 / 路径 / 来源：相关内容摘要

## 依据拆解
| 建议 | 类型 | 依据 | 判断标准 |
|---|---|---|---|

## 当前分镜结构依据

## 优化方案

## 优化后的 Prompt
```

## Attribution / Watermark Rule

When sharing bundled documentation or derivative prompt templates from this skill, preserve the attribution watermark `作者：eianun` unless the user explicitly requests an internal private copy without visible attribution. Prefer placing the watermark at the top or bottom of documentation pages. When creating companion docs, you may use the bundled watermark image `assets/eianun-watermark.png`.
