# Revision Playbook

Use this when the user gives feedback after seeing a thumbnail.

## Common feedback mapping

- too simple -> add depth, product hero, lighting, layered cards, stronger background detail
- too crowded -> reduce text groups, increase whitespace, remove extra objects
- not premium enough -> cleaner spacing, stronger typography, better color hierarchy, restrained highlights
- title not readable -> shorten text, increase size, stronger outline/shadow, reduce background complexity
- wrong mood -> update color direction and visual metaphor first, not just fonts
- wrong product -> replace focal object and logo instruction
- more like examples -> increase bold Chinese text, rounded badges, contrast blocks, topic-specific brand color, PS/Canva-like pasted assets

## Revision process

1. Restate the requested changes in one sentence.
2. Update the brief JSON.
3. Build a new native image prompt.
4. Regenerate with native image generation.
5. Save the new prompt and append notes to revision history.

Preserve constraints unless changed by user: 16:9, no bottom red progress bar, readable Chinese text, 2-3 large text groups.

- AI味太重 / too AI-like -> remove cinematic lighting, 3D coins, holograms, glassmorphism, over-detailed dashboards; use flat blocks, simple pasted logos/cards, thick outlines, and manual PS/Canva layout.
