# Evidence Mode Reference

Use this reference when the user asks for source-backed Seedance prompt diagnosis, document-based judgments, or reasons behind a prompt revision.

## Natural Entry

Do not require the user to say `evidence mode`. Enter this workflow whenever the task benefits from source-backed judgment, including when the user gives generation feedback, asks for revision with reasons, asks to check documents, gives a file/web source, or wants to know why a prompt should be changed. Trigger phrases such as `依据是什么`, `参考了哪个文件`, `判断标准`, and `帮我查资料后改` are examples, not a complete list.

## Required Retrieval Behavior

Before answering, inspect available information sources in this priority order:

1. The user's current prompt, scene, or feedback.
2. Uploaded files in the conversation.
3. Codex project docs when available:
   - `docs/MANIFEST.md`
   - `docs/sources/`
   - `docs/web/`
   - `docs/cases/`
4. Bundled skill references.
5. Web search only when the user requests latest public documentation or the fact may have changed.

If a source cannot be accessed, state that limitation clearly.

## Evidence Classification

Every important recommendation should be labeled as one of these types:

- 【资料明确依据】: a document, web page, uploaded file, or knowledge-base entry directly supports the recommendation.
- 【当前内容依据】: the user's current prompt, scene, neighboring scene, timing, shot count, dialogue, camera continuity, or feedback directly shows the issue.
- 【AI 推理判断】: reasoning from the available sources and current content.
- 【经验优化建议】: practical prompt/video-production advice without direct source support.

Never present experience-based advice as a document fact.

## Output Template

```markdown
## 问题结论
- ...

## 参考资料
- `path/to/file.md`: relevant section or summary

## 依据拆解
| 建议 | 类型 | 依据 | 判断标准 |
|---|---|---|---|
| ... | 【资料明确依据】 | ... | ... |

## 当前分镜结构依据
- 当前镜头 / 时长 / 台词 / 切点观察

## 优化方案
### 方案 A：最佳方案
### 方案 B：原生降级方案

## 优化后的 Prompt
...
```

## Handling Weak Evidence

If no direct file evidence exists, write:

`未找到直接资料依据；以下为基于当前内容、AI 推理和生成经验的判断。`

Then label the recommendation as 【当前内容依据】, 【AI 推理判断】, or 【经验优化建议】.
