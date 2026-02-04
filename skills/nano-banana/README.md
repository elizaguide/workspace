# Nano Banana Pro

Generate images using Google's Gemini API (Imagen model) for web pages, UI designs, and visual assets.

**Author:** Chef
v 0.1.0

---

## Installation

1. Place the `nano-banana` folder in your `.claude/skills/` directory
2. Add your Google Gemini API key to `.env` in your project root:
   ```
   GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Via Claude Code

Simply ask Claude to generate images:

```
"Generate a hero image for my wellness landing page"
"Create an icon for meditation"
"Make a feature image showing mindfulness"
```

### Via Script Directly

```bash
# Basic usage
python .claude/skills/nano-banana/scripts/generate_image.py "your prompt" -o output.png

# With options
python .claude/skills/nano-banana/scripts/generate_image.py \
  "serene gradient with purple tones" \
  --size landscape \
  --style hero \
  -o public/assets/hero-bg.png

# Generate multiple variations
python .claude/skills/nano-banana/scripts/generate_image.py \
  "abstract wellness background" \
  --size landscape \
  -n 3 \
  -o variations.png
```

## Options

### Sizes
| Size | Ratio | Use Case |
|------|-------|----------|
| `square` | 1:1 | Icons, avatars |
| `landscape` | 16:9 | Hero sections |
| `portrait` | 9:16 | Mobile screens |
| `wide` | 3:2 | Feature cards |
| `tall` | 2:3 | Sidebars |

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

## Integration

Works seamlessly with:
- **mindvalley-design** - Automatically applies Mindvalley brand colors
- **frontend-design** - Generates images for pages being created

## Examples

```bash
# Hero background for wellness page
python scripts/generate_image.py \
  "Abstract flowing gradient with purple and lavender tones, serene atmosphere" \
  --size landscape --style hero -o hero.png

# Feature illustration
python scripts/generate_image.py \
  "Person meditating in nature, minimal illustration, purple accents" \
  --size wide --style illustration -o feature.png

# App icon
python scripts/generate_image.py \
  "Lotus flower icon, minimal flat design, purple #7a12d4" \
  --style icon -o icon.png
```

## Requirements

- Python 3.8+
- Google Gemini API key
- Dependencies auto-install on first run: `google-generativeai`, `Pillow`

## License

MIT
