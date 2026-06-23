# Codex Native Image Workflow

Use this workflow when the environment provides native image generation, including Codex image generation or ChatGPT image generation. Use native generation as the renderer, but default to a PS/Canva-like human-made thumbnail aesthetic.

## 1. Intake

Collect or infer:

- video topic
- target audience
- user's opinions or angle
- must-include keywords
- title style preference
- thumbnail text language
- brands/products/logos allowed
- examples or screenshots
- things to avoid
- whether the user already supplied the final title

Default avoid list:

- bottom red progress bar
- crowded small text
- thin fonts
- generic stock-photo look
- exact cloning of another creator's thumbnail
- cinematic AI poster look

## 2. Choose the correct entry mode

### A. Title ideation first

Create candidates in three buckets:

1. Search traffic: keyword-dense and explicit.
2. CTR hook: shorter, higher tension, more curiosity.
3. Tutorial clarity: direct, beginner-friendly, promise-oriented.

Ask the user to pick, unless they requested autonomous selection.

### B. Direct title to thumbnail

If the user already supplied the title:

1. keep that title as the source of truth
2. shorten it into badge / main hook / secondary hook / support strip
3. use `references/direct-title-thumbnail-playbook.md`
4. create the brief directly

## 3. Brief

Create a JSON brief before generating the image. The brief is the stable source of truth for iterations.

Minimum fields:

- selected title
- title bucket
- main thumbnail text
- secondary text
- badge text
- support text
- audience
- keywords
- visual focal object
- brand/logo usage
- color direction
- avoid list

## 4. Native image generation

Use the native image-generation tool as the final renderer. Prompt for a complete thumbnail, not a flat mockup.

Prompt must include:

- 16:9 YouTube thumbnail, 1280x720
- Chinese tech/tutorial thumbnail style
- exact visible Chinese text from the brief
- 2-3 oversized text groups only, plus optional support chips
- strong contrast, flat/2D color blocks, restrained shadows, rounded badges
- brand/product visuals if allowed, shown like pasted assets or simple product cards
- clear mobile readability
- no bottom red progress bar
- no glossy 3D render, cinematic lens flare, hologram, or over-detailed AI dashboard by default

When Chinese text accuracy matters, ask the generator to render fewer, larger characters. If the generated text is wrong, regenerate with shorter text or create a text-safe background and add text separately in an external editor.

## 5. Editable source pack

Save these files with the final image:

- brief JSON
- prompt markdown
- source SVG blueprint
- revision notes
- final image

The source SVG is a layout blueprint. It is not expected to match the generated art perfectly.

## 6. Revisions

On feedback such as `more premium`, `less crowded`, `bigger title`, `change to blue`, or `more like the last test image`, update the brief and prompt, then regenerate. If the image feels too AI-like, regenerate with `references/ps-made-style-guide.md` and a stronger anti-AI negative prompt before doing any local patching.
