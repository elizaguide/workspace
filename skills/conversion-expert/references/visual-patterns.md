# Visual Patterns for Conversion

Design principles that guide visitors toward action.

---

## Eye Flow Patterns

### F-Pattern (Information-Heavy Pages)

Best for: Curriculum sections, feature lists, FAQ pages

```
┌─────────────────────────────────┐
│ ████████████████████ ←─ Scan   │
│ █████████████████    ←─ Scan   │
│ █████████                      │
│ █████████████████    ←─ Scan   │
│ ███████                        │
│ ██████████████       ←─ Scan   │
└─────────────────────────────────┘
```

**Design implications:**
- Left-align headlines and key content
- Front-load important information in first 2 words
- Use clear visual hierarchy (H2 → H3 → body)
- Break up dense text with subheadings

### Z-Pattern (Landing Pages)

Best for: Hero sections, simple landing pages, CTAs

```
┌─────────────────────────────────┐
│ LOGO ─────────────────────► CTA │  ← Top bar
│   ↘                             │
│        ████████████             │  ← Visual focus
│             ↘                   │
│ BENEFITS ────────────────► CTA  │  ← Bottom bar
└─────────────────────────────────┘
```

**Design implications:**
- Logo top-left, CTA top-right
- Central visual anchors the page
- Key benefits left, CTA right
- Natural diagonal eye movement

### Gutenberg Diagram (Balanced Layouts)

```
┌─────────────────────────────────┐
│ PRIMARY          │    STRONG    │
│ OPTICAL AREA     │    FALLOW    │
│                  │              │
├──────────────────┼──────────────┤
│ WEAK             │   TERMINAL   │
│ FALLOW           │   AREA ←CTA  │
└─────────────────────────────────┘
```

**Key insight:** Terminal area (bottom-right) is where eye naturally lands. Place CTA there.

---

## Hero Section Patterns

### Pattern 1: Full-Width Image + Overlay

```
┌─────────────────────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│ ░░░░ EYEBROW TEXT ░░░░░░░░░░░░░░░░░░░░░░░░░ │
│ ░░░░ HEADLINE ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│ ░░░░ Subheadline text here ░░░░░░░░░░░░░░░░ │
│ ░░░░ [  CTA BUTTON  ]  ░░░░░░░░░░░░░░░░░░░░ │
│ ░░░░ 12M+ Students  ░░░░░░░░░░░░░░░░░░░░░░░ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
└─────────────────────────────────────────────┘
```

**CSS approach:**
- Background image with gradient overlay
- Text positioned left (60% width)
- Dark gradient: `rgba(15,19,26,0.7)` → `transparent`

### Pattern 2: Split Layout (Text + Image)

```
┌──────────────────────┬──────────────────────┐
│                      │                      │
│  EYEBROW             │     ┌──────────┐     │
│  HEADLINE            │     │          │     │
│  Subheadline         │     │  IMAGE   │     │
│                      │     │          │     │
│  [CTA]  [Secondary]  │     └──────────┘     │
│                      │                      │
│  ★★★★★ 12M students  │                      │
└──────────────────────┴──────────────────────┘
```

**Best for:** Product-aware audiences where you want to show the product/teacher immediately.

### Pattern 3: Centered Minimal

```
┌─────────────────────────────────────────────┐
│                                             │
│              EYEBROW TEXT                   │
│                                             │
│          BOLD HEADLINE HERE                 │
│                                             │
│     Supporting text that explains the       │
│     value proposition in one sentence.      │
│                                             │
│            [  CTA BUTTON  ]                 │
│                                             │
│         Powered by Mindvalley • 12M+        │
│                                             │
└─────────────────────────────────────────────┘
```

**Best for:** Premium/luxury positioning, simple offers.

---

## CTA Design Principles

### Color Psychology

| Color | Emotion | Best For |
|-------|---------|----------|
| **Orange** | Urgency, energy, action | Primary CTAs, "Buy Now" |
| **Green** | Trust, safety, go | "Start Free", trials |
| **Purple** | Premium, creativity | Brand accent, secondary |
| **Blue** | Trust, calm | Corporate, B2B |

**Mindvalley standard:**
- Primary CTA: Orange gradient (`#f97316` → `#ea580c`)
- Secondary CTA: Purple outline (`#7a12d4`)

### CTA Button Anatomy

```
┌─────────────────────────────────┐
│                                 │
│   →   Start My Transformation   │  ← Icon + Action + Benefit
│                                 │
└─────────────────────────────────┘
     ↑        ↑           ↑
   Icon    Action      Benefit
```

**Best practices:**
- Height: 48-56px (touch-friendly)
- Padding: 16px 32px minimum
- Border-radius: 999px (fully rounded)
- Font-weight: 600-700
- Subtle shadow for depth

### CTA Copy Formulas

**Action + Benefit:**
- "Start My Transformation"
- "Get Instant Access"
- "Join 12M+ Students"

**Action + Timeframe:**
- "Start My 28-Day Journey"
- "Begin Today"
- "Enroll Now"

**Curiosity:**
- "See What's Inside"
- "Discover the Method"

**Avoid:**
- "Submit" (clinical)
- "Click Here" (vague)
- "Buy" (harsh)

---

## Mobile-First Patterns

### Critical Stats (2025)
- **70%+** of traffic is mobile
- **53%** bounce if load time > 3s
- **44px** minimum touch target

### Mobile Hero Adaptations

**Desktop:**
```
┌────────────────────────────────┐
│ [Text]            [Image]      │
└────────────────────────────────┘
```

**Mobile:**
```
┌────────────────┐
│    [Image]     │
│                │
│    [Text]      │
│                │
│     [CTA]      │
└────────────────┘
```

### Thumb Zone

```
     ┌─────────────────┐
     │   Hard to       │  ← Avoid placing CTAs here
     │   Reach         │
     ├─────────────────┤
     │   Okay          │  ← Secondary actions
     │                 │
     ├─────────────────┤
     │   Easy          │  ← Primary CTAs here
     │   ████████████  │
     └─────────────────┘
           👍
```

### Sticky CTA Pattern

For sales pages, use sticky bottom CTA on mobile:

```
┌─────────────────┐
│                 │
│   Page content  │
│   scrolls here  │
│                 │
├─────────────────┤
│ $199  [Enroll]  │  ← Sticky bar
└─────────────────┘
```

---

## Visual Hierarchy

### Size Scale

| Element | Size Range | Purpose |
|---------|------------|---------|
| H1 (Hero) | 48-72px | Primary headline, one per page |
| H2 (Section) | 36-48px | Section headings |
| H3 (Subsection) | 24-30px | Card titles, feature headings |
| Body Large | 18-20px | Subheadlines, important text |
| Body | 16px | Default paragraph text |
| Caption | 14px | Supporting text, labels |

### Contrast & Weight

```
High contrast (dark + bold)    → Headlines, CTAs
Medium contrast (dark + regular) → Body text
Low contrast (gray + regular)    → Captions, secondary info
```

### White Space Rules

| Element | Vertical Spacing |
|---------|------------------|
| Between sections | 80-128px (5-8rem) |
| Between elements in section | 24-48px (1.5-3rem) |
| Between lines (line-height) | 1.5-1.7 |

**Rule of thumb:** When in doubt, add more white space.

---

## Social Proof Placement

### Above-the-Fold Indicators

```
┌─────────────────────────────────┐
│ Hero headline here              │
│                                 │
│ [CTA]                           │
│                                 │
│ ★★★★★ 12M+ students • 195 countries │  ← Trust bar
└─────────────────────────────────┘
```

### Testimonial Layouts

**Featured testimonial (large quote):**
```
┌─────────────────────────────────────────────┐
│                                             │
│    "This program transformed how I          │
│     approach every challenge in life."      │
│                                             │
│           [Photo]  Name, Title              │
│                                             │
└─────────────────────────────────────────────┘
```

**Grid testimonials (social proof volume):**
```
┌─────────────┬─────────────┐
│   Quote 1   │   Quote 2   │
│   [Photo]   │   [Photo]   │
├─────────────┼─────────────┤
│   Quote 3   │   Quote 4   │
│   [Photo]   │   [Photo]   │
└─────────────┴─────────────┘
```

**Best practice:** One featured testimonial + grid of 2-4 supporting testimonials.

---

## Anti-Patterns to Avoid

### Visual Clutter
- ❌ Multiple CTAs competing for attention
- ❌ Decorative elements that don't serve conversion
- ❌ Busy backgrounds that reduce readability

### Inconsistency
- ❌ Multiple button styles on same page
- ❌ Inconsistent spacing between sections
- ❌ Mixed typography (stick to system classes)

### False Urgency Signals
- ❌ Fake countdown timers that reset
- ❌ "Only 3 left!" when inventory is unlimited
- ❌ "Limited time!" with no actual deadline

### Mobile Neglect
- ❌ Tiny tap targets
- ❌ Horizontal scrolling
- ❌ Text too small to read
- ❌ Forms with too many fields
