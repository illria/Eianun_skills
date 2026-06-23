# Thumbnail Brief Schema

Use this JSON structure as the editable source of truth.

```json
{
  "video_topic": "",
  "audience": "",
  "selected_title": "",
  "title_bucket": "search|ctr|tutorial|custom|direct_title",
  "keywords": [],
  "user_angle": "",
  "thumbnail": {
    "main_text": "",
    "secondary_text": "",
    "badge_text": "",
    "support_text": "",
    "language": "zh-CN",
    "visual_focal_object": "",
    "brand_logos": [],
    "color_direction": "",
    "composition": "left-text-right-product|center-title-product-cards|split-panels|custom",
    "mood": "ps/canva-made, clear, high-trust, punchy",
    "style_mode": "ps_made"
  },
  "image_generation": {
    "mode": "codex-native",
    "aspect_ratio": "16:9",
    "size": "1280x720",
    "style_reference_assets": [],
    "must_include": [],
    "avoid": ["bottom red progress bar", "tiny text", "flat template look"]
  },
  "revision_history": []
}
```

## Rules

- Thumbnail text should be shorter than the video title.
- Use exact visible text strings in the prompt.
- Keep `avoid` persistent across revisions.
- Add user feedback to `revision_history` before building the next prompt.
- For direct-title mode, keep the user title in `selected_title` and store the shortened visible hierarchy in `thumbnail` fields.
- Default `style_mode` to `ps_made` unless the user explicitly asks for cinematic/3D/AI-poster style.
