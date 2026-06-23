# Direct Title -> Thumbnail Playbook

Use this when the user already supplies the title and wants to see the thumbnail effect immediately.

## Goal

Turn a full video title into a shorter thumbnail text hierarchy that reads clearly at YouTube thumbnail size, then render it as a PS/Canva-like manually designed thumbnail.

The title is the source of truth, but the visible canvas text should usually be shorter than the title.

## Decomposition rule

Break the title into four possible layers.

1. Header / badge
   - brand name
   - review/tutorial/version label
   - short angle marker
   - example: `Neverless | 深度评测`

2. Main hook
   - the shortest high-value concept
   - usually 3-8 Chinese characters or one short brand phrase
   - example: `数字货币`

3. Secondary hook
   - the main promise or differentiator
   - usually the part containing `零手续费`, `开户`, `教程`, `自建节点`, `保号`, `免费 CDN`, `美股`, `实体卡`
   - example: `零手续费交易美股`

4. Support strip
   - one concise proof point
   - examples: `自带同名 IBAN`, `无损出金 Wise`, `大陆可用`, `保姆级教程`

## What to keep visible

Prefer this priority order:

1. product / promise
2. strongest differentiator
3. one proof point
4. brand marker

Do not place every clause from the long title onto the thumbnail if that harms readability.

## Layout recipe

Default high-performing recipe for these Chinese tutorial thumbnails:

- top-left small brand/header pill
- center-left huge main + secondary text across 2 lines
- one or two rounded support chips below
- right side product hero: app dashboard, phone UI, bank card, product screenshot, logo, or concept object, pasted in simply like a human-made PS layout
- simple background metaphors such as chart line, cloud, phone, network, or map when relevant; avoid cinematic glow/world-map poster look

## Color recipe

- derive the main accent from the product/brand if obvious
- finance / banking: green, teal, deep blue, white
- crypto: green or gold accent on dark background works well when paired with UI cards
- keep contrast very strong

## Text safety rule

If the generator struggles with Chinese text accuracy:

- shorten the text hierarchy
- reduce to 2 large text groups + 1 support chip
- prefer exact short strings over long sentences
- if needed, generate a clean background first and add text in the editable SVG/source workflow

## Example decomposition

Input title:
`Neverless深度评测：数字货币零手续费交易美股，自带同名IBAN | 无损出金Wise`

Suggested visible hierarchy:

- Header / badge: `Neverless | 深度评测`
- Main hook: `数字货币`
- Secondary hook: `零手续费交易美股`
- Support strip 1: `自带同名 IBAN`
- Support strip 2: `无损出金 Wise`
- Right-side product cue: `Neverless app dashboard + global account card + growth chart + crypto/finance cue`

## Revision mapping

- `更像教程封面` -> simplify layout, boost text dominance, reduce decorative detail
- `更高级` -> cleaner spacing, stronger color hierarchy, better typography, not more AI shine
- `再突出 Wise` -> move Wise into a support chip or product cue, increase logo visibility
- `右边太花` -> reduce number of cards/icons, keep one main product hero
- `AI味太重` -> use PS/Canva style guide, remove cinematic lighting/3D/glassmorphism, use flatter color blocks and pasted assets
