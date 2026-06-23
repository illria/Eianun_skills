# Seedance Knowledge Manifest

作者：eianun

This file is the index of local knowledge sources. Update it whenever a new source, webpage, or case is added.

## Source Types

- `docs/sources/`: official docs, FAQ, product guides, exported PDFs/DOCX/TXT/MD files.
- `docs/web/`: webpages saved as markdown.
- `docs/cases/`: project cases, failed generations, before/after prompt examples, evidence reports.

## Current Sources

### sources/README.md
- Type: folder guide
- Use: tells Codex where to store official or semi-official reference docs.
- Priority: high when documents are present.

### web/README.md
- Type: folder guide
- Use: stores copied/fetched webpage content.
- Priority: high when matching current question.

### cases/README.md
- Type: folder guide
- Use: stores project-specific troubleshooting and prompt examples.
- Priority: medium to high for recurring production problems.

## Evidence Policy

When answering, distinguish:
- 【文件明确依据】
- 【当前分镜结构推断】
- 【经验优化建议】

If no direct source exists, say so explicitly.

## 工作流说明

### NATURAL_WORKFLOW.md
- 类型：智能体行为规范 / 自然任务理解
- 重点：用户可以用白话给文档、网页、Prompt、反馈和格式要求；智能体自主判断任务、查资料、标明依据并完成输出。
- 优先级：高
