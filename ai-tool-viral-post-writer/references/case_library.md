# Case Library: Distilled Viral Patterns

This library stores structures learned from user-provided Chinese X/Twitter viral examples. Use the structure, not the wording.

## Pattern A: hidden-risk warning

Learned from examples about tools harming SSD/log writing/security costs.

Reusable mechanics:
- Start with an alarming but specific consequence.
- Explain the mechanism in plain language.
- Show observable evidence or behavior.
- Tell readers what to check or how to reduce risk.

Use for: privacy, hardware, billing, hidden background processes, safety issues.
Do not use for: normal resource directories or harmless tool lists.

## Pattern B: white/free resource burst

Learned from examples offering multiple frontier models/free APIs/free calls.

Reusable mechanics:
- Hook with “originally expensive, now accessible/free-tier”.
- List the concrete things users can try.
- Compare to former friction: subscriptions, credit cards, trial traps, scattered provider pages.
- Add setup steps and caveat that free tiers may change.

Use for: free-resource-directory, API aggregator, starter credits, trial/free plans.
Boundary: never claim unlimited/free forever without verification.

## Pattern C: workflow breakthrough

Learned from examples like record/replay, long-document OCR, live translation.

Reusable mechanics:
- “Before”: every task required repeated prompts/manual work/chunking.
- “Now”: one new capability compresses the workflow.
- Give familiar scenarios.
- End with a shift statement: from manual step-by-step to reusable capability.

Use for: new product features, agent capabilities, model architecture breakthroughs.

## Pattern D: open-source replacement

Learned from local voice/video, Mac utilities, stock analysis systems.

Reusable mechanics:
- Name the paid/complex incumbent friction.
- Present the open-source/local tool as a practical alternative.
- List capabilities as user jobs, not feature jargon.
- Add local/offline/privacy/cost angle.

Use for: local apps, open-source alternatives, self-hostable tools.
Boundary: do not overclaim production replacement.

## Pattern E: agent composition and protocol

Learned from Codex + MCP / agent integrations.

Reusable mechanics:
- The real question is not “which AI is strongest”, but “which AI handles which part”.
- Split planning, execution, tool access, verification.
- Give workflow examples.
- Conclude that AI work is moving from single chat to composed systems.

Use for: MCP, Codex, Claude Code, Cursor, agents, browser automation.

## Pattern F: project/product launch with builder credibility

Learned from dashboards, hackathon tools, community projects.

Reusable mechanics:
- Start with what was built and who it helps.
- Explain the messy information/workflow problem.
- List current modules/features.
- Credit data/tools/community where applicable.
- Include limitations and invite feedback.

Use for: user-built projects, open-source demos, Hugging Face Spaces, dashboards.

## Pattern G: list/stack post

Learned from Macbook essential tools lists.

Reusable mechanics:
- State context: “我的 X 必备工具”.
- Group by use case.
- Give short why-each-tool-stays comments.
- Keep it personal and subjective.

Use for: personal tool stacks and periodic roundups.

## Pattern H: extreme result story

Learned from high-return/trading-style viral posts.

Reusable mechanics:
- Start with shocking before/after result.
- Explain the simple mechanism.
- List exact rules/steps.
- Add disclaimer.

Use only when the result is verified and ethical. For finance, always add strong non-investment disclaimer. Often avoid this pattern for the user's default account unless the user explicitly asks.

## Pattern I: research/model release explainer

Learned from model releases and academic projects.

Reusable mechanics:
- Hook with “new capability/model release”.
- Explain the core idea in everyday language.
- Give 3-5 reasons it matters.
- Mention training data, benchmark, license, and how to try only if verified.
- End with cautious impact judgment.

Use for: models, papers, research repos.

## Pattern J: free flagship research tool with proof

Learned from examples about Deep Research tools that contrast free-user friction with a stronger research workflow and then prove it with a real report.

Reusable mechanics:
- Start with a familiar free-user pain: stitching together multiple AI products, shallow results, rate limits, or wasted time.
- Introduce the tool with a strong but verifiable judgment, then immediately anchor it in concrete workflow benefits.
- Stack only claims that can be checked: free tier, model class, multi-agent depth, speed, report quality, source coverage.
- Move quickly from product praise to use cases so the post feels practical rather than like an ad.
- Use a real research task, report, screenshot, or before/after result as proof.
- End by pointing readers to the attached report, thread, screenshots, or workflow notes.

Use for:
- Deep Research products
- AI search/report tools
- multi-agent research workflows
- free-tier AI tools with clearly verified capability
- tools that replace manual browsing, repeated prompting, or cross-tool stitching

Do not use for:
- tools whose free quota, model tier, or availability is unverified
- products without concrete output examples
- generic chatbots with no research workflow
- finance/trading posts without a clear non-investment disclaimer
- posts that rely only on "SOTA", "旗舰", "终极", or "最强" without evidence

Formula:
free-user research pain -> new tool judgment -> verified capability stack -> use-case preview -> real task proof -> report/thread/screenshot CTA.

Example hook variants:
- 免费用户做 Deep Research，最痛苦的不是不会问，而是到处被限速。
- 以前做深度调研，我是在几个 AI 和搜索引擎之间来回拼答案。
- Deep Research 真正好用的标准，不是答案长，而是能把证据链跑完整。
- 这类工具最值得看的地方，是它能把多个研究分支同时往下挖。
- 如果你经常做行业调研、论文调研或竞品分析，这种工作流值得单独看。

Safety boundaries:
- Verify "free", model tier, agent count, rate limit, and availability before using them as hard claims.
- For finance, stocks, crypto, trading, or IPO research, add that the output is for research/learning only and does not constitute investment advice.
- Avoid implying guaranteed accuracy; say outputs still need human review and source checking.

## Pattern K: dangerous capability flattening

Learned from examples about security, reverse engineering, or dual-use AI projects that package formerly expert-only workflows into AI-readable skills, routing rules, or agent systems.

Reusable mechanics:
- Start with an expert-only capability and show that it has been packaged for AI or agents.
- Frame the core tension as capability threshold reduction, not as a tool tutorial.
- Explain the mechanism in one simple sentence: routing, skill selection, agent dispatch, workflow orchestration, or tool-choice automation.
- List several recognizable subdomains to prove coverage, but keep them at category level.
- Emphasize that the most important shift is "knowing which path to take" becoming structured and reusable.
- End with a restrained judgment about risk, responsibility, or the larger AI-agent trend instead of a direct usage CTA.

Use for:
- AI security tooling
- reverse engineering assistants
- agent skill-routing systems
- CTF or security training workflows
- dual-use developer projects that lower expert workflow barriers
- tools that encode expert triage, tool selection, or methodology into reusable agent instructions

Do not use for:
- harmless productivity tools where danger is only clickbait
- ordinary resource directories or tool lists
- projects that require exploit steps, bypass recipes, credential misuse, persistence, stealth, or unauthorized access instructions
- claims about offensive capability that are not verified from the project source

Formula:
expert-only capability -> AI/agent packaging -> simple mechanism -> recognizable coverage list -> threshold-lowering insight -> restrained risk/trend judgment.

Example hook variants:
- 以前只有安全老手能做的事，现在开始被人做成 AI 技能包。
- 这个项目真正值得看的，不是工具多，而是它把判断路线也交给了 AI。
- 安全攻防最难的往往不是工具，而是知道什么时候该走哪条路。
- 当逆向工程被拆成 routing 和 skill，门槛就不只是低了一点。
- AI Agent 正在把专家脑子里的分诊流程，变成可以复用的工作流。

Safety boundaries:
- Keep capability descriptions at category and workflow level; do not provide operational attack steps.
- Use "授权研究", "教学实验", "CTF", "内部测试", or "防御验证" as the allowed context.
- Avoid encouraging EDR bypass, exploitation, evasion, credential misuse, persistence, stealth, or unauthorized target testing.
- Verify project claims such as number of skills, supported tools, license, stars, and active maintenance before using exact numbers.
- If naming sensitive subdomains, pair them with a boundary statement so the post reads as risk analysis, not instruction.

## Pattern L: vertical skill stack roundup

Learned from examples recommending a small set of high-frequency Skills for a specific professional group, with each item tied to a concrete output.

Reusable mechanics:
- Start by naming the exact audience and the list value: "designer/developer/operator must-have Skills" plus "daily high-frequency use".
- Keep the list short enough to feel curated, usually 5-8 items.
- Give each item a clear job-to-be-done instead of a generic praise line.
- Translate the technical capability into the output users want: editable animation, interaction code, 3D map, design spec document, admin UI.
- Use "personally tested", "daily workflow", or "high-frequency use" only when the author has actually used the tools.
- Make the post feel like a practical stack note, not a ranking or product ad.

Use for:
- role-specific AI Skill lists
- designer, developer, marketer, creator, student, or indie-hacker tool stacks
- plugin/skill/workflow roundups
- posts where each listed tool produces a tangible asset or saved workflow step
- periodic "my current stack" or "must-have tools" posts

Do not use for:
- long undifferentiated directories with no personal selection logic
- tools the author has not tried when the post claims hands-on use
- one-off product launches that need a deeper single-tool narrative
- lists where every item has the same vague benefit

Formula:
specific audience -> curated count -> personal/high-frequency credibility -> itemized tools -> concrete output per tool -> workflow-saving judgment.

Example hook variants:
- 设计师做 AI 工作流，这几类 Skill 真的能省掉很多重复活。
- 整理一套我最近高频用的设计向 Skill，每个都对应一个明确产出。
- 如果你经常做动效、网页交互、3D 大屏或后台页面，这组 Skill 可以单独收藏。
- AI Skill 最好用的地方，不是替你想创意，而是把重复产出流程固定下来。
- 分享一组适合设计师和前端一起用的 Skill 栈。

Safety boundaries:
- Verify tool names, availability, install path, and supported outputs before presenting them as recommendations.
- Avoid "必备", "拉满", or "一键" if the workflow still requires setup, cleanup, or manual review.
- If recommending paid tools, mention pricing or free-tier uncertainty only after checking current sources.
- Do not imply generated code/design specs are production-ready without human review.

## Pattern M: cross-platform trend brief

Learned from examples about AI search or monitoring tools that collect social/content-platform discussions, rank them with engagement signals, deduplicate repeated stories, and export a usable brief.

Reusable mechanics:
- Open with current traction only if verified: GitHub Trending, star count, launch momentum, or community attention.
- Define the tool as a cross-platform trend/research skill, not just a search box.
- Emphasize source coverage with recognizable platforms, then explain the time window and ranking signal in plain language.
- Show the intent-resolution step: entity parsing, account/community matching, and deciding where to search before fetching results.
- Highlight deduplication across platforms so the benefit is "one clean story" instead of repeated fragments.
- End with a concrete output format and use cases: HTML brief, Notion, email, competitor tracking, topic research, content ideation.

Use for:
- AI search Skills
- social listening tools
- competitor tracking workflows
- content ideation and trend discovery products
- multi-source research agents
- tools that turn raw platform chatter into ranked briefs or reports

Do not use for:
- normal web search products without social/content-platform aggregation
- tools that only scrape one platform
- posts where platform access, ranking signals, or freshness are unverified
- products that encourage spam, mass scraping, credential misuse, or ToS evasion

Formula:
verified traction -> multi-platform source coverage -> intent/entity resolution -> engagement-weighted ranking -> cross-platform deduplication -> exportable brief -> practical use cases.

Example hook variants:
- 这个工具真正解决的不是搜索，而是把几个平台上的同一件事合成一份简报。
- 做竞品追踪最烦的不是没信息，而是 Reddit、X、YouTube、HN 各说各的。
- 好的 AI 搜索不应该只给链接，而应该先判断你到底要找哪个人、公司和社区。
- 如果你做内容选题，这类跨平台热点简报工具会很省时间。
- 社媒研究最值钱的能力，是去重、排序和把讨论变成可读报告。

Safety boundaries:
- Verify GitHub Trending status, star count, release date, time window, supported platforms, and export format before using them as hard claims.
- If source coverage includes Reddit, X, YouTube, HN, or similar platforms, avoid encouraging high-scale scraping, credential misuse, spam, or ToS bypass.
- Clarify whether ranking is based on official APIs, public pages, cached data, or user-provided credentials when that affects reliability or compliance.
- Do not imply "all hotspots" or complete coverage unless the project source proves it; prefer "collects recent discussions from..." or "can aggregate signals from...".
- For market, finance, investment, or public-company research, add that the brief is for research only and needs human verification.

## Pattern N: audit-data risk report

Learned from examples that turn a large-scale AI tool/Skill/MCP security audit into a viral risk thread with verifiable numbers, segment comparisons, and a concrete checker product.

Reusable mechanics:
- Open with a practical trust question: "Before installing this agent Skill/MCP/server, how do you know it is safe?"
- Establish credibility with audit scope, dataset size, source coverage, and a named methodology.
- Reveal the first shock: most items are unaudited, unrated, or mixed into normal search results.
- Break down the audited subset with clear proportions: safe, concerning, unsafe, unreviewed.
- Add a surprising risk distribution, such as low-star/cold-start projects being riskier than popular repositories.
- Surface one novel attack surface in simple language, such as reading agent config, memory, secrets, or local files.
- Close with a reproducibility path and practical mitigation: report, methodology, disclaimer, CLI, search/check command, or agent-callable tool.

Use for:
- AI Skill or MCP security audits
- plugin marketplace trust and safety reports
- package/repository risk scoring tools
- agent permission and local-file exposure analysis
- security scanners that convert raw audits into usable ratings
- posts that combine research findings with a CLI or dashboard release

Do not use for:
- vague security scare posts without reproducible data
- single-vulnerability writeups that need a technical CVE-style structure
- products that only provide marketing scores without methodology
- posts that require exposing exploit steps, secret paths, bypass methods, or weaponized payloads
- claims about exact counts, percentages, or rankings that cannot be verified

Formula:
installation trust question -> audit scale -> unaudited majority shock -> rated-risk breakdown -> segment comparison -> new attack surface -> reproducible report -> practical checker/CLI CTA.

Example hook variants:
- 你装一个 AI Agent Skill 之前，真的知道它安不安全吗？
- Agent 时代最容易被忽略的风险，不是模型回答错，而是你装进去的工具在读什么。
- 真正危险的可能不是热门项目，而是你为冷门需求随手搜到的低星仓库。
- 过去安全审计盯服务器，现在还要盯 agent 的配置、记忆和本地权限。
- AI Skill/MCP 生态最缺的不是数量，而是一套安装前能查的风险评级。

Safety boundaries:
- Verify audit dataset size, percentages, star buckets, unsafe definitions, and methodology before using exact numbers.
- Clearly distinguish "unaudited", "security concern", and "unsafe"; do not collapse all risk categories into one panic label.
- Avoid naming or instructing exploit techniques, secret paths, bypass methods, or payload details.
- If mentioning agent memory, config, credentials, or local-file access, frame it as permission/risk awareness and mitigation, not exploitation.
- Include reproducibility notes, methodology links, disclaimers, and limits of automated scoring when available.
- Do not imply popular repositories are guaranteed safe; say risk appears lower in the measured dataset if verified.

## Pattern O: multi-platform crawler with compliance warning

Learned from examples about crawler or collection tools that cover many Chinese/social platforms, lower technical barriers, and must be framed with clear research-only and anti-abuse boundaries.

Reusable mechanics:
- Open with a curiosity hook about where content operators, trend trackers, or reposters find source material.
- Present the tool as a multi-platform public-content collection tool, not as a shortcut for unauthorized copying.
- List recognizable supported platforms to create coverage shock, but avoid implying total or guaranteed access.
- Explain the barrier-lowering mechanism at a high level, such as using browser session state or an automated workflow, without giving evasion or signature-bypass instructions.
- Translate collected fields into legitimate research scenarios: topic research, public opinion monitoring, creator research, comment analysis, trend discovery.
- Include the author's research-only disclaimer and add a stronger platform/copyright/compliance reminder.
- End with a caution about content reposting risk, platform enforcement, and moderation rather than encouraging mass搬运.

Use for:
- social media crawler projects
- public-content collection tools
- creator research and topic-monitoring workflows
- multi-platform data collection libraries
- posts about content-source discovery with explicit compliance boundaries

Do not use for:
- tutorials for evading anti-bot systems, signatures, captchas, paywalls, or rate limits
- posts encouraging content theft, spam accounts, mass reposting, or copyright infringement
- tools requiring stolen cookies, shared credentials, or private data access
- scraping workflows that target non-public content or bypass platform restrictions
- claims about supported platforms or data fields that are not verified from the project source

Formula:
content-source curiosity -> multi-platform coverage -> public data fields -> barrier-lowering workflow -> legitimate research use cases -> author disclaimer -> anti-abuse/content-reposting warning.

Example hook variants:
- 现在终于知道很多内容号的素材源是怎么被整理出来的了。
- 这类工具真正敏感的地方，不是能采多少平台，而是门槛被降得很低。
- 做话题研究时，多平台公开内容采集很有用，但边界一定要讲清楚。
- 内容研究和内容搬运只差一步，工具越方便越要守规则。
- 这个项目适合研究公开内容，不适合拿来批量搬运别人的作品。

Safety boundaries:
- Verify supported platforms, data fields, login/session requirements, license, and project disclaimer before writing.
- Keep technical description high level; do not provide JS reverse engineering, signature extraction, anti-bot bypass, cookie theft, captcha bypass, or rate-limit evasion steps.
- Emphasize public content, learning/research, compliance with platform ToS, copyright, privacy, and local law.
- Avoid framing the tool as a way to copy posts, farm traffic, build spam accounts, or bypass official APIs at scale.
- If mentioning reposting or content搬运, frame it as a risk and moderation warning, not a recommended use.

## Pattern P: clean self-hosted replacement for hostile web tools

Learned from examples about small open-source, self-hosted utilities that replace ad-heavy, tracking-heavy, or malware-prone web tools with a clean local workflow.

Reusable mechanics:
- Open with an emotionally familiar frustration: popups, redirects, fake buttons, malware risk, upsells, telemetry, or hostile UX.
- Introduce the project as the clean alternative: open-source, free, self-hosted, no ads, no paid tier, no telemetry, local data control.
- List concrete capabilities as user choices, such as format, quality, batch mode, deduplication, Web UI, or browser access.
- Use implementation simplicity as proof of trust: few dependencies, small codebase, no build step, easy audit, local-only operation.
- Keep deployment simple but do not overclaim: Homebrew, Docker, localhost, or one-command setup only if verified.
- End with an open-source worldview: tools that do one job well without monetizing attention or data.

Use for:
- self-hosted alternatives to shady web utilities
- open-source download/conversion/transcoding tools
- local-first media or file utilities
- privacy-friendly replacements for ad-heavy websites
- small auditable projects where simplicity is a selling point

Do not use for:
- tools that primarily bypass paywalls, DRM, access controls, private content, or platform restrictions
- posts encouraging copyright infringement, mass downloading, reuploading, or content monetization without rights
- projects that are not actually local/self-hosted when privacy is the main claim
- tools with unverified claims like no telemetry, no paid tier, no upsell, or very small codebase
- products whose main value is illegal content access

Formula:
hostile web-tool pain -> clean open-source/self-hosted alternative -> concrete user controls -> simple auditable implementation -> easy local deployment -> open-source purity judgment -> copyright/ToS boundary.

Example hook variants:
- 那些弹窗下载网站最恶心人的地方，不是丑，而是你根本不知道点了什么。
- 这类小工具最舒服的状态：本地跑、无广告、无遥测、做完就走。
- 有些开源项目不需要很复杂，只要把一个恶心流程变干净就够了。
- 下载/转换工具最该自托管，因为你的链接、文件和习惯都不该被拿去赚钱。
- 开源最爽的瞬间，就是一个 150 行小工具把一堆广告站替掉。

Safety boundaries:
- Verify supported sites, formats, dependencies, license, telemetry claims, paid-tier claims, code size, and deployment commands before using exact claims.
- For yt-dlp-based or media-download tools, remind users to respect copyright, platform terms, creator rights, and local law.
- Avoid encouraging DRM bypass, paywall bypass, private video access, mass downloading, reuploading, or commercial reposting.
- Do not say "1000+ sites" or "no telemetry" unless confirmed by the README/source at writing time.
- Frame downloads as personal backup, research, accessibility, or permitted use when appropriate; avoid piracy framing.

## Pattern Q: professional system diagnostics upgrade

Learned from examples about advanced process/task managers that replace the default OS task manager with dense process, thread, memory, handle, network, and IO inspection.

Reusable mechanics:
- Open by contrasting the familiar built-in tool with a professional-grade alternative.
- Start from one simple action: click a process and reveal everything hidden underneath.
- Stack diagnostic dimensions quickly: threads, stacks, memory, handles, modules, sockets, disk IO, network rate, services, drivers.
- Translate feature density into real troubleshooting scenarios: performance spikes, suspicious process checks, file lock hunting, network connection tracing, system monitoring.
- Mention implementation credibility only if verified: UI framework, kernel/driver backend, supported OS versions, architecture, roadmap.
- End with the audience fit: Windows power users, sysadmins, reverse engineers, performance engineers, security analysts, or developers debugging native apps.

Use for:
- process explorers and task-manager replacements
- system monitoring tools
- performance troubleshooting utilities
- Windows internals tools
- observability tools for local machines
- security and diagnostics dashboards with rich process-level inspection

Do not use for:
- simple resource monitors that only show CPU/RAM charts
- tools whose privileged operations are unverified
- posts that encourage malware analysis on unauthorized machines, DLL injection abuse, stealth, persistence, or process tampering
- user-facing productivity apps with no diagnostics depth

Formula:
built-in tool limitation -> professional alternative -> one-click process deep dive -> dense inspection surfaces -> real troubleshooting use cases -> implementation credibility -> expert audience.

Example hook variants:
- Windows 任务管理器够看热闹，但真排查问题还得上这种工具。
- 这个项目最爽的地方，是随便点一个进程，底下的线程、句柄、Socket 全摊开。
- 做性能排查时，CPU 占用只是开始，真正要看的是它打开了什么文件、连了哪里、跑了哪些线程。
- 如果你经常查进程、句柄、网络连接，这类工具比任务管理器像显微镜。
- 专业级系统诊断工具的价值，就是把隐藏在一个进程背后的东西一次性展开。

Safety boundaries:
- Verify supported OS versions, Linux/macOS roadmap, driver dependency, license, and sensitive features before writing exact claims.
- Frame privileged operations such as DLL injection, module unload, handle closing, or driver-backed inspection as authorized debugging/diagnostics only.
- Do not provide instructions for process tampering, stealth, malware persistence, EDR evasion, or unauthorized system manipulation.
- Warn that driver-level tools and process modification features can crash apps or affect system stability; use on machines you control.
- Avoid "任务管理器根本没法比" style overclaim unless the specific feature comparison is factual.
