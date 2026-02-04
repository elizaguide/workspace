# Mindvalley Design System

Create Mindvalley-branded pages and UI using the official design system with Google Sans Flex typography and brand colors.

**Author:** Chef
v 0.1.0

---

## Installation

1. Place the `mindvalley-design` folder in your `.claude/skills/` directory
2. Ensure `public/mindvalley-font.css` exists in your project (contains typography classes)

## Usage

### Via Claude Code

Simply ask Claude to create Mindvalley-styled pages:

```
"Create a landing page for Self Reset program"
"Build a wellness workshop registration page"
"Design a speaker bio section for Mindvalley event"
"Make a testimonials section with Mindvalley styling"
```

The skill will:
1. Ask clarifying questions about your needs
2. Invoke `frontend-design` skill for implementation
3. Apply Mindvalley brand colors and typography
4. Use `nano-banana` for custom images (if available)

### Key Triggers

This skill activates when you mention:
- "Mindvalley"
- "landing page"
- "Self Reset"
- "wellness page"
- `mindvalley-font.css`
- `@mindvalley/design-system`

## Brand Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Purple | `#7a12d4` | CTAs, links, accents |
| Body Text | `#0f131a` | Default text |
| Muted Text | `#4b5563` | Subheadlines |
| Footer Gray | `#6b7280` | Captions |
| Light Lavender | `#f9f7fc` | Section backgrounds |
| Lighter Lavender | `#f5f0fa` | Cards |

## Typography Classes

Always link the stylesheet:
```html
<link rel="stylesheet" href="public/mindvalley-font.css" />
```

### Headings (Responsive)
- `title-bold-1` - Hero H1 (48px → 72px)
- `title-bold-2` - Major sections (36px → 60px)
- `title-bold-3` - Section headings (30px → 48px)
- `title-bold-4` - Subsections (28px → 36px)
- `title-bold-5` - Card titles (24px → 28px)

### Body (Fixed)
- `body-lg` - Large body text (20px)
- `body` - Default paragraphs (16px)
- `body-sm` - Small text (14px)
- `body-italic` - Testimonials (16px)
- `overline-text` - Eyebrows, uppercase (14px)

## Available Components

See `references/components.md` for copy-paste patterns:

- **Hero Sections** - Standard, with background, centered
- **Feature Sections** - Grid, with icons, with images
- **Speaker Sections** - Single, multiple grid
- **Testimonials** - Cards grid, single large quote
- **Schedule/Timeline** - Event schedules
- **FAQ Sections** - Simple list format
- **CTA Sections** - Final conversion blocks
- **Cards** - Content cards, pricing cards
- **Buttons** - Primary, secondary, small
- **Footer** - Simple, with links

## Integration

Works with:
- **frontend-design** - Delegates page creation (required)
- **nano-banana** - Custom image generation (optional)

## Example Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Page Title — Mindvalley</title>
  <meta name="theme-color" content="#7a12d4" />
  <link rel="stylesheet" href="public/mindvalley-font.css" />
</head>
<body>
  <!-- Hero -->
  <section class="mv-container" style="padding: 6rem 0 5rem 0;">
    ...
  </section>

  <!-- Features (alternating background) -->
  <section style="background-color: #f9f7fc;">
    <div class="mv-container" style="padding: 5rem 0;">
      ...
    </div>
  </section>

  <!-- Footer -->
  <footer class="mv-container" style="padding: 4rem 0; color: #6b7280;">
    © Mindvalley • Page Name
  </footer>
</body>
</html>
```

## Design Guidelines

**DO:**
- Use generous whitespace (5-6rem section padding)
- Apply subtle background alternation (#f9f7fc)
- Round CTAs fully (border-radius: 999px)
- Constrain text widths (max-width: 48rem headings, 40rem body)

**DON'T:**
- Use sharp corners on buttons
- Mix font families
- Use generic gradients or patterns
- Cram content without breathing room

## License

MIT
