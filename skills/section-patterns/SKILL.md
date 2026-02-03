---
name: section-patterns
description: Pre-built, conversion-optimized HTML section patterns for Mindvalley landing pages and sales pages. Use this skill when building landing pages, sales pages, program pages, or any marketing page that needs Hero sections, Benefits grids, Testimonial sections, FAQ accordions, Pricing tables, or CTA sections. Triggers on "landing page", "sales page", "hero section", "benefits section", "testimonials", "FAQ section", "pricing section", "CTA section", or requests to build complete marketing pages. This skill MUST invoke the mindvalley-design skill for brand compliance.
---

# Section Patterns

Pre-built HTML section patterns for Mindvalley marketing pages. All patterns follow mindvalley-design brand guidelines.

## Workflow

### Step 1: Invoke mindvalley-design

Before using any patterns, ensure mindvalley-design skill is active for:
- Typography classes (`title-bold-*`, `body`, etc.)
- Brand colors (`mv-purple`, `mv-lavender`, etc.)
- Layout utilities (`.mv-container`)

### Step 2: Select Section Pattern

Choose the appropriate reference file based on what you're building:

| Section Type | Reference File | When to Use |
|--------------|----------------|-------------|
| Hero | `references/hero-sections.md` | Page opener with headline, subheadline, CTA |
| Benefits | `references/benefits-sections.md` | Feature grids, icon lists, value propositions |
| Testimonials | `references/testimonial-sections.md` | Social proof, quotes, video testimonials |
| FAQ | `references/faq-sections.md` | Accordion with Schema.org markup |
| CTA | `references/cta-sections.md` | Final call-to-action sections |

### Step 3: Customize Pattern

Replace placeholders in the pattern:
- `{{HEADLINE}}` - Main heading text
- `{{SUBHEADLINE}}` - Supporting text
- `{{CTA_TEXT}}` - Button label
- `{{CTA_URL}}` - Button destination
- `{{IMAGE_URL}}` - Image source (use placehold.co for drafts)

## Quick Reference

### Section Spacing

All sections use consistent vertical padding:
```css
/* Standard section */
padding: 5rem 0;

/* Hero section */
padding: 6rem 0 5rem 0;

/* Footer */
padding: 4rem 0;
```

### Background Alternation

Alternate backgrounds for visual rhythm:
```
Section 1 (Hero): white or gradient
Section 2: #f9f7fc (mv-lavender)
Section 3: white
Section 4: #f9f7fc (mv-lavender)
...
```

### Common Patterns by Page Type

**Sales Page:**
1. Hero (centered or split)
2. Problem/Pain (benefits-sections.md → problem-agitation)
3. Solution (benefits-sections.md → features)
4. Benefits Grid
5. Curriculum/What's Included
6. Teacher Bio (testimonial-sections.md → authority)
7. Testimonials
8. FAQ
9. Final CTA

**Landing Page (Lead Capture):**
1. Hero with form
2. Benefits (3-column)
3. Social proof strip
4. Final CTA

**Event Page:**
1. Hero with date/location
2. What You'll Learn (benefits)
3. Speaker(s)
4. Schedule/Agenda
5. Testimonials
6. Pricing/Register CTA

## Integration with Other Skills

- **order-menu**: For checkout/pricing components, invoke order-menu skill
- **nano-banana**: For generating hero images or visual assets
- **figma:implement-design**: When implementing from Figma designs

## Anti-Patterns: Avoid AI-Looking Designs

**CRITICAL**: The patterns in reference files are starting points, NOT copy-paste templates. Every page must feel unique and handcrafted.

### DO NOT:

1. **Overuse brand purple** - Purple should be accent only (CTAs, eyebrows, highlights). Not every icon, card border, and background.

2. **Create identical card grids** - 3 cards in a row with same structure/colors is AI's signature. Instead:
   - Vary card sizes (one large, two small)
   - Use different visual treatments per card
   - Mix card layouts with inline content
   - Skip cards entirely and use prose with occasional emphasis

3. **Use formulaic problem-agitation** - Red-tinted cards listing pain points is overused. Better alternatives:
   - Simple text paragraph with powerful question
   - Single compelling story/scenario
   - Conversational "Does this sound familiar?" followed by prose, not cards

4. **Repeat the same section structure** - If you have 3 benefit cards, don't follow with 3 testimonial cards then 3 result cards. Mix formats.

5. **Add decorative elements to every section** - Not every section needs icons, badges, or visual flourishes.

### DO:

1. **Let content breathe** - Some sections should just be text. A well-written paragraph beats a card grid.

2. **Create visual hierarchy through variety** - One featured item + supporting items, not 3 equal items.

3. **Use white/neutral space** - White backgrounds with black text are not boring, they're sophisticated.

4. **Make each section distinct** - Different layout, different visual treatment, different rhythm.

5. **Trust typography** - A powerful headline doesn't need an icon, gradient, or card wrapper.

## Output Checklist

Before finalizing any page:
- [ ] Uses mindvalley-design typography classes (not Tailwind text-*)
- [ ] Proper heading hierarchy (H1 → H2 → H3)
- [ ] All sections have `.mv-container`
- [ ] Backgrounds alternate for visual rhythm
- [ ] Mobile responsive (check reference patterns)
- [ ] Images have alt text
- [ ] CTAs are prominent and above-the-fold
- [ ] FAQ has Schema.org FAQPage markup
- [ ] **NO identical card grids in consecutive sections**
- [ ] **Purple used sparingly as accent only**
- [ ] **At least 2 sections use prose instead of cards/grids**
- [ ] **Each section has distinct visual treatment**
