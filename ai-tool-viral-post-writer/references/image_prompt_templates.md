# Image Prompt Templates

Use these templates to generate visual prompts that match the written post. Fill placeholders from the copy spine.

## Universal cover prompt template

Create a clean modern SaaS/developer style cover image for a Chinese X/Twitter post about {PROJECT_NAME}. The visual theme is {CORE_VALUE}. Use a polished product UI composition with rounded cards, subtle gradients, developer-tool aesthetics, organized information hierarchy, and enough whitespace. Show conceptual modules for {FEATURE_CHIPS}. Make it feel practical, credible, and useful for builders, not exaggerated advertising. No people, no cartoon style, no fake screenshots, no misleading official logos. If text is included, keep it minimal and large: title “{IMAGE_TITLE}”, subtitle “{SUBTITLE}”. Aspect ratio {ASPECT_RATIO}.

## Chinese infographic text-accurate prompt template

Use this template when the user asks for direct image generation and wants readable Chinese text inside the image. Keep the number of text strings limited and list every string exactly.

这张信息图采用 {STYLE_AND_PALETTE}，整体是清晰、现代、适合中文 X/Twitter 首图的横版信息图。画布比例为 {ASPECT_RATIO}。整体排版分为 {LAYOUT_DESCRIPTION}，所有文字必须清晰锐利、字号足够大、不得模糊、不得错字、不得替换为其他文字、不得出现乱码或额外文字。

顶部主标题区域：
- 主标题文字：“{IMAGE_TITLE}”
- 副标题文字：“{SUBTITLE}”

{SECTION_1_NAME}：
- 区块标题：“{SECTION_1_TITLE}”
- 视觉元素：{SECTION_1_VISUAL}
- 标签文字：{SECTION_1_LABELS}

{SECTION_2_NAME}：
- 区块标题：“{SECTION_2_TITLE}”
- 视觉元素：{SECTION_2_VISUAL}
- 标签文字：{SECTION_2_LABELS}

{SECTION_3_NAME}：
- 区块标题：“{SECTION_3_TITLE}”
- 视觉元素：{SECTION_3_VISUAL}
- 标签文字：{SECTION_3_LABELS}

底部提示文字：“{FOOTER_TEXT}”

负面约束：不要真实品牌 Logo，不要伪造截图，不要小字段落，不要代码长段落，不要水印，不要英文乱字，不要额外中文，不要乱码。所有出现的中文只能来自上面列出的文字。

## Official-style three-column infographic prompt template

Use this as the preferred Sensenova/NewAPI prompt when the image needs readable Chinese. It follows the user's official example structure and should be written as a complete design-spec narrative, not a short keyword prompt.

这张信息图采用 {STYLE_AND_PALETTE}，整体呈现 {MOOD_AND_GENRE}。主标题位于 {TITLE_POSITION}，采用清晰醒目的无衬线粗体：“{IMAGE_TITLE}”，其下方紧跟副标题：“{SUBTITLE}”。

整体排版从左到右分为三个主要区块，分别介绍 {SECTION_1_PURPOSE}、{SECTION_2_PURPOSE} 和 {SECTION_3_PURPOSE}。以下是图表中各区块的详细结构和全部文字内容：

1. 左侧区块：{SECTION_1_TITLE}。该区块主要展示 {SECTION_1_DESCRIPTION}。{SECTION_1_CONTAINER_STYLE}。其中包含三项内容：
1. {SECTION_1_ITEM_1}（图标为 {SECTION_1_ICON_1}）。
2. {SECTION_1_ITEM_2}（图标为 {SECTION_1_ICON_2}）。
3. {SECTION_1_ITEM_3}（图标为 {SECTION_1_ICON_3}）。

2. 中间区块：{SECTION_2_TITLE}。该区块通过 {SECTION_2_VISUAL_STRUCTURE} 串联核心流程。流程节点依次为：
步骤一：{SECTION_2_STEP_1}（图标为 {SECTION_2_ICON_1}）。
步骤二：{SECTION_2_STEP_2}（图标为 {SECTION_2_ICON_2}）。
步骤三：{SECTION_2_STEP_3}（图标为 {SECTION_2_ICON_3}）。

3. 右侧区块：{SECTION_3_TITLE}。该区块被设计成 {SECTION_3_CONTAINER_STYLE}。其中包含三条结果或规则：
规则一：{SECTION_3_ITEM_1}（图标为 {SECTION_3_ICON_1}）。
规则二：{SECTION_3_ITEM_2}（图标为 {SECTION_3_ICON_2}）。
规则三：{SECTION_3_ITEM_3}（图标为 {SECTION_3_ICON_3}）。

底部总结栏文字为：“{FOOTER_TEXT}”

所有文字必须清晰、锐利、完整、无错字，文字像真实信息图设计稿一样可读。不要出现未列出的额外文字，不要水印，不要英文乱码，不要小字段落，不要长段代码，不要真实品牌 Logo，不要伪造真实截图。

## No-text background prompt template

Create a clean modern SaaS/developer style background illustration for an AI tool post about {PROJECT_NAME}. Represent {CORE_VALUE} using abstract UI cards, workflow nodes, code/API panels, and organized category chips. No readable text, no people, no logos, no screenshots. Leave clear empty space for later Chinese title overlay. Aspect ratio {ASPECT_RATIO}.

## Resource map prompt template

Create a polished “AI resource map” cover image for Chinese X/Twitter. Show an organized grid of connected cards representing models, APIs, local inference tools, chat UIs, coding assistants, RAG, and agents. The mood is low-cost practical AI learning for indie builders and students. Dark navy or clean light SaaS style, clear hierarchy, subtle glow, rounded cards, no people, no fake brand logos. Minimal Chinese title: “{IMAGE_TITLE}”. Subtitle: “{SUBTITLE}”. Aspect ratio {ASPECT_RATIO}.

## Workflow diagram prompt template

Create a modern workflow diagram cover for an AI tool post. Show a left-to-right process: {BEFORE_STATE} → {TOOL_ACTION} → {OUTPUT_RESULT}. Use clean cards, arrows, agent nodes, browser/API/code panels, and a polished SaaS product feel. Keep text minimal: “{IMAGE_TITLE}”. No people, no cartoon, no misleading screenshots. Aspect ratio {ASPECT_RATIO}.

## Before/after prompt template

Create a clean before/after comparison card for Chinese X/Twitter. Left side: old workflow with scattered tabs/subscriptions/manual steps. Right side: new workflow using {PROJECT_NAME} with organized cards and a smoother path. Modern developer SaaS style, credible and restrained. Minimal text: “以前” and “现在”. Aspect ratio {ASPECT_RATIO}.

## Research proof prompt template

Create a modern research dashboard style cover image for an AI deep research tool post. Show multiple agent nodes collecting evidence into a structured report, with cards for sources, notes, and final summary. Practical professional style, not sci-fi. Minimal Chinese title: “{IMAGE_TITLE}”. Include no real company logos or unverified numbers. Aspect ratio {ASPECT_RATIO}.

## Warning card prompt template

Create a restrained technical warning card for Chinese X/Twitter. Show a developer dashboard with alert indicators, logs, disk/API/security panels, and a clear check/mitigation area. Serious but not panic-inducing. Minimal Chinese title: “{IMAGE_TITLE}”. No fake screenshots, no brand logos. Aspect ratio {ASPECT_RATIO}.
