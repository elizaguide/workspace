---
name: nano-banana
description: Generate images using Google Gemini API (Imagen/Nano Banana Pro). Use this skill when creating images for web pages, UI designs, landing pages, hero backgrounds, feature images, icons, avatars, or any visual assets. Automatically integrates with frontend-design workflows to replace placeholder images with generated visuals. Triggers on requests like "generate an image", "create a hero image", "make an icon", "generate visuals for this page", or when building UI that needs custom imagery. Requires GOOGLE_GEMINI_API_KEY in .env file.
---

# Nano Banana Pro Image Generator

Generate high-quality images using Google's Gemini API for web pages, UI components, and design assets.

## Prerequisites

Ensure `.env` file exists in the project root with:
```
GOOGLE_GEMINI_API_KEY=your_api_key_here
```

## Quick Reference

### Generate via Script
```bash
python scripts/generate_image.py "prompt" --size landscape --style hero -o output.png
```

### Sizes
| Size | Ratio | Use Case |
|------|-------|----------|
| `square` | 1:1 | Icons, avatars, thumbnails |
| `landscape` | 16:9 | Hero sections, banners |
| `portrait` | 9:16 | Mobile screens, stories |
| `wide` | 3:2 | Feature images, cards |
| `tall` | 2:3 | Sidebar images |

### Styles
| Style | Best For |
|-------|----------|
| `hero` | Website hero backgrounds |
| `feature` | Product/feature images |
| `icon` | Minimal icons, logos |
| `avatar` | Profile pictures |
| `photo` | Photorealistic images |
| `illustration` | Vector-style artwork |
| `3d` | 3D rendered visuals |
| `abstract` | Abstract backgrounds |

## Integration with Mindvalley Design

When used with `mindvalley-design` skill, automatically apply brand styling:
- Use purple tones (#7a12d4) and lavender accents
- Include "wellness", "serene", "transformative" mood keywords
- Match placeholder colors (e8e0f0 background, 7a12d4 accent)

## Integration with Frontend Design

When generating images for pages created with `frontend-design` skill:

### 1. Identify Image Needs
Scan the page for placeholder images or TODO comments:
```html
<!-- TODO: Replace with actual hero background -->
<img src="https://placehold.co/1920x800/e8e0f0/7a12d4?text=Hero" ...>
```

### 2. Generate Contextual Images
Match image generation to the page's purpose:

| Page Element | Size | Style | Prompt Pattern |
|--------------|------|-------|----------------|
| Hero background | `landscape` | `hero` | "Hero background for [page purpose], [mood/aesthetic]" |
| Feature cards | `wide` | `feature` | "Feature image showing [concept], clean modern style" |
| Speaker/host photo | `square` | `avatar` | "Professional portrait, [description], neutral background" |
| Icons | `square` | `icon` | "Minimal icon representing [concept], flat design" |
| Testimonial photos | `square` | `avatar` | "Friendly person portrait, natural lighting" |

### 3. Save to Assets Directory
```bash
python scripts/generate_image.py "prompt" -o public/assets/hero-bg.png --size landscape --style hero
```

## Prompt Engineering

### Effective Prompts

**Be specific about:**
- Subject matter and composition
- Color palette (match brand: purple #7a12d4, lavender tones)
- Mood and atmosphere
- Style and aesthetic

**Hero Background Example:**
```
"Serene abstract gradient background with soft purple and lavender tones,
flowing organic shapes, calm and wellness-focused atmosphere,
suitable for meditation app hero section"
```

**Feature Image Example:**
```
"Clean illustration of person meditating in nature,
minimal style with purple accent colors,
peaceful morning atmosphere, modern wellness aesthetic"
```

**Icon Example:**
```
"Minimal flat icon of a lotus flower,
simple geometric shapes, purple color #7a12d4,
clean lines, suitable for web UI"
```

### Brand-Aligned Prompts

For Mindvalley-style pages, include:
- Color references: "purple tones", "lavender accents", "#7a12d4"
- Mood: "serene", "transformative", "uplifting", "wellness"
- Style: "modern", "clean", "professional", "minimal"

## Workflow Examples

### Example 1: Landing Page Images
```bash
# Hero background
python scripts/generate_image.py \
  "Abstract flowing gradient with purple and gold tones, serene wellness atmosphere, soft lighting" \
  --size landscape --style hero -o assets/hero-bg.png

# Feature images
python scripts/generate_image.py \
  "Person practicing mindfulness in nature, illustration style, purple accents" \
  --size wide --style illustration -o assets/feature-mindfulness.png

# Speaker photo placeholder
python scripts/generate_image.py \
  "Professional portrait of wellness coach, warm smile, neutral studio background" \
  --size square --style avatar -o assets/speaker.png
```

### Example 2: Multiple Variations
```bash
# Generate 3 variations to choose from
python scripts/generate_image.py \
  "Meditation retreat hero image, mountains at sunrise, peaceful" \
  --size landscape --style photo -n 3 -o assets/hero-option.png
```

### Example 3: Icon Set
```bash
python scripts/generate_image.py "Heart icon, minimal flat design, purple" --style icon -o assets/icon-heart.png
python scripts/generate_image.py "Brain icon, minimal flat design, purple" --style icon -o assets/icon-brain.png
python scripts/generate_image.py "Lotus icon, minimal flat design, purple" --style icon -o assets/icon-lotus.png
```

## Replacing Placeholders

After generating images, update HTML:

**Before:**
```html
<img src="https://placehold.co/1920x800/e8e0f0/7a12d4?text=Hero+Background"
     alt="[PLACEHOLDER: Hero background]" ...>
```

**After:**
```html
<img src="assets/hero-bg.png"
     alt="Serene gradient background with flowing shapes" ...>
```

## Troubleshooting

### API Key Issues
- Verify `.env` file exists in project root
- Check key format: `GOOGLE_GEMINI_API_KEY=AIza...`
- Ensure no quotes around the key value

### Generation Failures
- Simplify complex prompts
- Remove potentially problematic content
- Try different style options
- Check API quota/limits

### Quality Issues
- Add more specific style descriptors
- Include composition guidance
- Specify lighting and mood
- Reference the intended use case

## Resources

- Prompt patterns: See `references/prompt-patterns.md`
- Script options: Run `python scripts/generate_image.py --help`
