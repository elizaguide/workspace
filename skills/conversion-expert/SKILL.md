---
name: conversion-expert
description: |
  Orchestrates high-converting landing pages and sales pages by combining conversion frameworks (Hormozi, Schwartz, Sugarman, Cialdini) with visual design principles. Use when creating sales pages, landing pages, program pages, or any conversion-focused page. Triggers on "sales page", "landing page", "conversion", "high-converting", "optimize for signups", "optimize for purchases", or when building pages that need to convert visitors. This skill coordinates mindvalley-design, section-patterns, nano-banana, and order-menu skills with conversion-optimized guidance. MUST be invoked BEFORE other page-building skills to establish conversion strategy.
---

# Conversion Expert

Pre-build conversion strategist that orchestrates high-converting pages using proven frameworks and coordinating other skills.

## Role

1. **Analyze** page requirements and determine conversion strategy
2. **Select** applicable frameworks based on page type and audience
3. **Orchestrate** other skills with conversion-optimized instructions
4. **Audit** (optional) completed pages against conversion checklist

## Workflow

```
1. Detect page type (sales, lead capture, event, etc.)
2. Infer audience awareness stage from context
3. Select frameworks → see references/conversion-frameworks.md
4. Generate conversion brief for child skills
5. Invoke skills in order: section-patterns → mindvalley-design → nano-banana → order-menu
6. (Optional) Run audit → see references/audit-checklist.md
```

## Page Type Detection

| Page Type | Signals | Primary Goal | Key Frameworks |
|-----------|---------|--------------|----------------|
| **Sales Page** | "buy", "purchase", "enroll", checkout URL | Purchase | Hormozi Value, Schwartz Stages, Objection handling |
| **Lead Capture** | "signup", "download", "free", form | Email capture | Hook + value exchange, Form friction reduction |
| **Event Page** | "register", "attend", date/location | Registration | FOMO, Social proof, Speaker authority |
| **Program Page** | "course", "quest", curriculum | Exploration → Purchase | Curriculum showcase, Teacher credibility |

## Awareness Stage Detection

Infer from context clues:

| Stage | Context Clues | Strategy |
|-------|---------------|----------|
| **Unaware** | Cold traffic, broad audience, no prior exposure | Lead with story/curiosity, educate on problem |
| **Problem-Aware** | Mentions pain points, searching for solutions | Amplify pain, introduce solution category |
| **Solution-Aware** | Knows solution exists, comparing options | Lead with mechanism/methodology uniqueness |
| **Product-Aware** | Knows Mindvalley/product, needs convincing | Heavy social proof, differentiation, testimonials |
| **Most Aware** | Returning visitor, cart abandoner, past customer | Lead with offer, urgency, guarantee |

**Default assumption:** Solution-Aware (most Mindvalley traffic)

## Skill Orchestration

### 1. section-patterns
Invoke with conversion context:
```
- Hero type: [problem-agitation | solution-reveal | social-proof-heavy]
- Section order based on awareness stage
- Testimonial placement: [early for product-aware | late for problem-aware]
- Objection handling sections needed: [yes | no]
```

### 2. mindvalley-design
Pass conversion brief:
```
- Page goal: [purchase | signup | registration]
- Primary CTA: [above fold + sticky | above fold only | bottom only]
- Visual hierarchy: Guide eye to CTA
- Color psychology: Orange CTA for urgency, green for trust
```

### 3. nano-banana
Generate images that support conversion:
```
- Hero: Aspirational outcome state (person transformed, not struggling)
- Features: Show the transformation or mechanism in action
- Teacher: Authority + approachability (not stiff headshot)
- Testimonials: Real people, candid moments (avoid stock photo look)

CRITICAL: Use --style photo for realistic images. Avoid AI-looking ethereal/glowing effects.
```

### 4. order-menu (for sales pages)
Pass pricing psychology context:
```
- Anchor pricing: Show original price crossed out
- Default selection: Yearly (higher LTV)
- Timer: 15 min for urgency (if appropriate)
- Guarantee prominence: High (reduces purchase anxiety)
```

## Framework Quick Reference

### Hormozi Value Equation
```
Value = (Dream Outcome × Perceived Likelihood) ÷ (Time × Effort)
```

**Application:**
- **Hero**: Maximize dream outcome - paint the transformation vividly
- **Social proof**: Build perceived likelihood - "12M+ students" proves it works
- **Curriculum**: Minimize time/effort - "just 15 min/day" or "28-day program"

### Schwartz Awareness Stages
See `references/conversion-frameworks.md` for full breakdown.

**Quick selection:**
- Problem-Aware → Lead with pain, reveal solution
- Solution-Aware → Lead with mechanism uniqueness
- Product-Aware → Lead with proof and differentiation

### Sugarman Slippery Slope
Every element's job is to get them to read the next element.

**Application:**
- Hook in first 3 seconds (headline + subheadline)
- End sections with open loops or transitions
- CTA should feel like natural conclusion, not interruption

### Cialdini Influence Triggers
Layer throughout the page:
- **Authority**: Teacher credentials, media logos, celebrity associations
- **Social Proof**: Student count, testimonials, specific results
- **Scarcity**: Limited spots, deadline, exclusive access (only if true)
- **Unity**: "Join 12M+ growth seekers" - tribal belonging

See `references/conversion-frameworks.md` for detailed application.

## Visual Patterns

### Eye Flow
- **F-pattern**: For content-heavy pages (curriculum, features)
- **Z-pattern**: For landing pages (hero → CTA → features → CTA)

### CTA Design
- **Color**: Orange outperforms purple for CTAs
- **Shape**: Rounded (border-radius: 999px)
- **Text**: Action verb + benefit ("Start My Transformation" > "Submit")
- **Size**: Touch-friendly (44px+ height)

### Mobile Priority
- 70%+ traffic is mobile
- CTA must be visible without scrolling
- Touch targets 44px minimum
- Collapse long sections into accordions

See `references/visual-patterns.md` for full guide.

## High-Converting Examples

Study these for inspiration:
- **Mindvalley Membership**: mindvalley.com/membership/overview
- **Apple Product Pages**: apple.com/iphone
- **Premium Wellness**: goop.com/wellness

See `references/high-converting-examples.md` for detailed breakdowns.

## Anti-Patterns to Avoid

### Copy Anti-Patterns
- Leading with features instead of outcomes
- Addressing objections after the CTA (too late)
- Generic headlines without specificity
- Hype words without proof ("revolutionary", "life-changing")

### Visual Anti-Patterns
- Purple everywhere (use only for CTAs/accents)
- Identical 3-card grids in consecutive sections
- Stock photo testimonials (use real or styled fallbacks)
- AI-looking ethereal/glowing imagery

### Structure Anti-Patterns
- CTA buried below the fold
- No social proof in hero section
- FAQ without Schema.org markup
- Missing guarantee near pricing

## Optional: Post-Build Audit

After page is built, offer to run audit checklist.
See `references/audit-checklist.md` for full checklist.

**Quick audit:**
- [ ] Clear value proposition visible above fold?
- [ ] Primary CTA visible without scrolling?
- [ ] Social proof stat in hero?
- [ ] Objections addressed before final CTA?
- [ ] Guarantee prominent near pricing?
- [ ] Mobile layout maintains conversion elements?
