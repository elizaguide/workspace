---
name: mindvalley-design
description: Create Mindvalley-branded pages and UI using the official design system. Use this skill when building landing pages, web components, or any UI that should follow Mindvalley's brand guidelines. Triggers on requests mentioning "Mindvalley", "landing page", "Self Reset", "wellness page", or when creating pages using mindvalley-font.css or @mindvalley/design-system. This skill MUST invoke the frontend-design skill for implementation while enforcing Mindvalley brand standards. Works with nano-banana skill for image generation.
---

# Mindvalley Design System

Create distinctive, brand-aligned pages and UI using Mindvalley's design system. This skill enforces brand consistency and delegates implementation to the `frontend-design` skill.

## Critical Requirements

**ALWAYS:**
1. Invoke `frontend-design` skill for all page/component creation
2. Use `public/mindvalley-font.css` for typography (Google Sans Flex)
3. Use brand colors defined below
4. Follow section patterns from `references/components.md`
5. Use `nano-banana` skill for custom images when needed

**NEVER:**
- Use generic fonts (Arial, system-ui, etc.) - only Google Sans Flex
- Use non-brand colors without explicit user request
- Create generic/bland AI-looking UI
- Skip the responsive design patterns

## Brand Colors

**IMPORTANT: Use purple sparingly - only for action items!**

| Token | Hex | Usage |
|-------|-----|-------|
| Primary Purple | `#7a12d4` | **ACTION ITEMS ONLY:** CTAs, buttons, links, eyebrow text |
| Body Text | `#0f131a` | Default text |
| Muted Text | `#4b5563` | Subheadlines, secondary text |
| Footer Gray | `#6b7280` | Captions, footer text |
| Light Gray | `#f9fafb` | Alternating section backgrounds (use instead of lavender) |
| Card Background | `#ffffff` | Cards, content areas |
| Border Gray | `#e5e7eb` | Subtle borders, dividers |

**Purple Usage Rules:**
- ✅ Primary CTA buttons (purple background)
- ✅ Secondary CTA borders and text
- ✅ Eyebrow/overline text
- ✅ Text links
- ✅ Active/hover states
- ❌ NO purple section backgrounds
- ❌ NO purple cards or containers
- ❌ NO purple decorative elements
- ❌ NO lavender/purple tinted backgrounds

## Typography (from mindvalley-font.css)

**Always link the stylesheet:**
```html
<link rel="stylesheet" href="public/mindvalley-font.css" />
```

### Heading Classes (Responsive)
| Class | Mobile | Desktop | Usage |
|-------|--------|---------|-------|
| `title-bold-1` | 48px | 72px | Hero H1 |
| `title-bold-2` | 36px | 60px | Major sections |
| `title-bold-3` | 30px | 48px | Section headings |
| `title-bold-4` | 28px | 36px | Subsections |
| `title-bold-5` | 24px | 28px | Card titles |
| `title-bold-6` | 22px | 24px | Feature titles |
| `title-bold-7` | 20px | 22px | Labels |

### Body Classes (Fixed)
| Class | Size | Usage |
|-------|------|-------|
| `body-lg` | 20px | Large body, hero subtext |
| `body` | 16px | Default paragraphs |
| `body-sm` | 14px | Small text |
| `body-italic` | 16px | Testimonial quotes |
| `overline-text` | 14px | Eyebrows (uppercase) |

## Page Structure

Every page must include:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>[Page Title] — Mindvalley</title>
  <meta name="description" content="[150-160 chars]" />
  <meta name="theme-color" content="#7a12d4" />
  <link rel="stylesheet" href="public/mindvalley-font.css" />
</head>
<body>
  <!-- Content sections using .mv-container -->
  <footer class="mv-container" style="padding: 4rem 0; color: #6b7280;">
    © Mindvalley • [Page Name]
  </footer>
</body>
</html>
```

## Section Patterns

### Hero Section
```html
<section class="mv-container" style="padding: 6rem 0 5rem 0;">
  <div class="overline-text" style="margin-bottom: 1rem; color: #7a12d4;">
    EYEBROW TEXT
  </div>
  <h1 class="title-bold-2" style="max-width: 48rem; margin: 0 0 1.25rem 0;">
    Compelling headline here
  </h1>
  <p class="body-lg" style="max-width: 40rem; color: #4b5563; margin-bottom: 0;">
    Supporting subheadline text.
  </p>
  <div style="display: flex; gap: 1rem; margin-top: 2.5rem; flex-wrap: wrap;">
    <!-- Primary CTA -->
    <a href="#" class="button" style="
      display: inline-flex; align-items: center; justify-content: center;
      padding: 1rem 2rem; background-color: #7a12d4; color: white;
      font-weight: 700; border-radius: 999px; text-decoration: none;
    ">Primary CTA</a>
    <!-- Secondary CTA -->
    <a href="#" class="button" style="
      display: inline-flex; align-items: center; justify-content: center;
      padding: 1rem 2rem; background-color: transparent; color: #7a12d4;
      border: 2px solid #7a12d4; font-weight: 500; border-radius: 999px;
      text-decoration: none;
    ">Secondary CTA</a>
  </div>
</section>
```

### Feature Grid
```html
<section class="mv-container" style="padding: 5rem 0;">
  <h2 class="title-bold-4" style="margin-bottom: 2.25rem;">Section Title</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 2rem;">
    <div>
      <h3 class="title-bold-7" style="margin-bottom: 0.5rem;">Feature Title</h3>
      <p class="body">Feature description.</p>
    </div>
    <!-- More items -->
  </div>
</section>
```

### Alternating Background
```html
<section style="background-color: #f9fafb;">
  <div class="mv-container" style="padding: 5rem 0;">
    <!-- Content -->
  </div>
</section>
```

## Image Handling

### With nano-banana skill (preferred for custom images)
When images are needed, use the `nano-banana` skill:
```bash
# Hero background - use neutral, warm, or nature-inspired tones
python scripts/generate_image.py "serene natural landscape, soft warm tones, wellness atmosphere" \
  --size landscape --style hero -o public/assets/hero-bg.png

# Feature images - clean, modern, minimal
python scripts/generate_image.py "person meditating in nature, clean modern style, warm lighting" \
  --size wide --style feature -o public/assets/feature.png
```

### Placeholder images (when real images unavailable)
Use placehold.co with neutral colors:
```html
<!-- Hero: 1920x800 -->
<img src="https://placehold.co/1920x800/f3f4f6/6b7280?text=Hero" alt="[PLACEHOLDER: description]" />

<!-- Feature: 600x400 -->
<img src="https://placehold.co/600x400/f9fafb/6b7280?text=Feature" alt="[PLACEHOLDER: description]" />

<!-- Avatar: 200x200 -->
<img src="https://placehold.co/200x200/f3f4f6/6b7280?text=Speaker" alt="[PLACEHOLDER: name]"
     style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover;" />
```

## Workflow

1. **Receive request** → Identify page type and requirements
2. **Ask clarifying questions** if needed (goal, sections, CTAs, assets)
3. **Invoke frontend-design skill** with Mindvalley constraints:
   - Pass brand colors and typography requirements
   - Specify section patterns needed
   - Request responsive implementation
4. **Generate images** with nano-banana if custom visuals needed
5. **Review output** for brand compliance

## Design Quality Guidelines

To avoid generic AI-generated aesthetics:

**DO:**
- Use generous whitespace (5-6rem section padding)
- Apply subtle neutral background alternation (#f9fafb)
- Round CTAs fully (border-radius: 999px)
- Constrain text widths (max-width: 48rem headings, 40rem body)
- Use purple (#7a12d4) **ONLY for action items** (buttons, links, eyebrows)
- Keep backgrounds white or light gray
- Use clean, minimal aesthetics

**DON'T:**
- Use purple backgrounds or purple-tinted sections
- Use lavender or purple cards/containers
- Use sharp corners on buttons
- Cram content without breathing room
- Mix font families
- Use stock gradients or generic patterns
- Add unnecessary decorative elements
- Overuse the brand purple color

## Resources

- Component patterns: See `references/components.md`
- Typography reference: `public/mindvalley-font.css`
- Image generation: `nano-banana` skill
