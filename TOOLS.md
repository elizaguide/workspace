# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Website Development Checklist

**Always include when building websites:**
- ✅ **Mobile responsive design** (minimum: grid layouts that stack on mobile, readable text sizes, touch-friendly buttons)
- ✅ **Clean typography** with proper hierarchy
- ✅ **Fast loading** (optimize images, minimal dependencies)  
- ✅ **Accessibility** basics (alt tags, proper contrast)
- ✅ **Cross-browser compatibility**

**V's Priority:** Mobile responsiveness is critical - many people check sites on their phones first!

## 🚨 MUST RULES for Website Development

**🎨 DESIGN SYSTEM - CHECK FIRST, ALWAYS:**
**STEP 1: BEFORE writing ANY HTML, ask yourself:**
- "Is this for Mindvalley?" → **INVOKE mindvalley-design skill FIRST**
- "Does this need branding?" → **INVOKE mindvalley-design skill FIRST** 
- "Am I creating a webpage?" → **INVOKE mindvalley-design skill FIRST**

**🎯 DESIGN MANDATE (NON-NEGOTIABLE):**
- ✅ **ALL WEB PAGES use Mindvalley design by default** - No exceptions
- ✅ **ALWAYS invoke mindvalley-design skill BEFORE coding**
- ✅ **Use mindvalley-core.css + mindvalley-utilities.css** - Speed-optimized utility system
- ✅ **Professional, clean aesthetic** matching brand guidelines

**WhatsApp vs Gateway Deployment:**
- **WhatsApp messages:** ALWAYS use GitHub URLs (remote access for travel)
- **Gateway/computer messages:** localhost URLs OK

**IMAGE RULES - NEVER IGNORE:**
- 🚫 **ZERO CIRCULAR CROPS** - NEVER crop any image into circles
- 🚫 **ZERO IMAGE MANIPULATION** - Use images exactly as provided
- ✅ **Keep original aspect ratios** - Landscape stays landscape, portrait stays portrait
- ✅ **Human judgment over AI** - Vishen's visual preferences always win
- ✅ **If image is perfect as-is, leave it alone** - Don't "fix" what isn't broken

**FOLDER ORGANIZATION RULES:**
- ✅ **Always ask WHERE to put the website** if not specified
- ✅ **Default location:** `/Users/vishen/clawd/projects/[descriptive-name]/`
- ✅ **Never assume** - Different projects need different homes
- ✅ **Create proper structure:** index.html, assets/, css/, js/ folders
- ✅ **Commit to git** immediately after creation

**Required Elements:**
- ✅ **Emoji favicon** matching the topic (🧠 for AI, 🎓 for education, etc.)
- ✅ **GitHub deployment** for remote access
- ✅ **Mobile responsive design**

## 🚀 Mindvalley Utility CSS - Speed Development

**NEW: Utility-First Framework** - Build pages 10x faster with pre-built classes!

### Essential Imports (Always Include):
```html
<link rel="stylesheet" href="mindvalley-core.css">
<link rel="stylesheet" href="mindvalley-utilities.css">
```

### ⚡ Quick Page Patterns:
```html
<!-- Hero Section (1 line) -->
<section class="mv-hero-quick">
  <div class="mv-container">
    <h1 class="title-bold-1 mv-mb-4">Your Title</h1>
    <p class="body-lg mv-mb-8">Your subtitle</p>
    <a href="#" class="mv-btn mv-btn-primary">Call to Action</a>
  </div>
</section>

<!-- Feature Grid (Auto-responsive) -->
<div class="mv-features">
  <div class="mv-card">Feature 1</div>
  <div class="mv-card">Feature 2</div>
  <div class="mv-card">Feature 3</div>
</div>

<!-- Mobile Stack (Column mobile, row desktop) -->
<div class="mv-mobile-stack">
  <div>Content 1</div>
  <div>Content 2</div>
</div>
```

### 🎨 Color System:
- **Purple brand:** `mv-text-purple` `mv-bg-purple` `mv-bg-gradient-purple`
- **Dark text:** `mv-text-dark` `mv-bg-dark` `mv-bg-gradient-dark`
- **Status:** `mv-text-success` `mv-text-warning` `mv-text-error`

### 📱 Mobile-First Grid:
- **Base:** `mv-grid-1` `mv-grid-2` `mv-grid-3` `mv-grid-4`
- **Responsive:** `md:mv-grid-2` `lg:mv-grid-3` (breakpoints: 768px, 1024px)
- **Example:** `mv-grid-1 md:mv-grid-2 lg:mv-grid-3` = 1 col mobile, 2 col tablet, 3 col desktop

### 📏 Spacing (Mobile-optimized):
- **Margin:** `mv-mt-4` `mv-mb-8` `mv-mx-auto`
- **Padding:** `mv-p-4` `mv-px-6` `mv-py-8`
- **Gaps:** `mv-gap-4` `mv-gap-8`

### ⚡ Instant Components:
- **Buttons:** `mv-btn mv-btn-primary` or `mv-btn mv-btn-secondary`
- **Cards:** `mv-card` (auto-padding, shadows, rounded)
- **Hero:** `mv-hero-quick` (gradient background, centered)
- **Section:** `mv-section` or `mv-section-lg` (responsive padding)

### 🏃‍♂️ Speed Tips:
1. **Start with layout:** `mv-container` → `mv-mobile-stack` or `mv-features`
2. **Add typography:** `title-bold-3` `body` `mv-text-center`
3. **Apply colors:** `mv-text-purple` `mv-bg-white`
4. **Fine-tune spacing:** `mv-mb-8` `mv-px-4`

**Example Page in 5 minutes:**
```html
<section class="mv-hero-quick">
  <div class="mv-container">
    <h1 class="title-bold-1 mv-mb-4">Amazing Product</h1>
    <p class="body-lg mv-mb-8">Transform your life today</p>
    <a href="#" class="mv-btn mv-btn-primary">Get Started</a>
  </div>
</section>

<div class="mv-section">
  <div class="mv-container">
    <div class="mv-features">
      <div class="mv-card">
        <h3 class="title-bold-6 mv-text-purple mv-mb-4">Feature 1</h3>
        <p class="body">Amazing feature description</p>
      </div>
      <div class="mv-card">
        <h3 class="title-bold-6 mv-text-purple mv-mb-4">Feature 2</h3>
        <p class="body">Another great feature</p>
      </div>
    </div>
  </div>
</div>
```

**Files:**
- Reference: `web/skills/mindvalley-design/utility-example.html`
- Framework: `web/skills/mindvalley-design/mindvalley-utilities.css`

## 🧩 Mindvalley Component Library - Pre-Built Components

**NEW: JavaScript Component System** - Generate complete sections with one function call!

### Essential Includes:
```html
<link rel="stylesheet" href="mindvalley-core.css">
<link rel="stylesheet" href="mindvalley-utilities.css">
<script src="mindvalley-components.js"></script>
```

### ⚡ One-Line Components:
```javascript
// Complete hero section in 1 line
document.getElementById('hero').innerHTML = MV.hero({
  title: "Transform Your Life",
  subtitle: "Discover your potential", 
  cta: "Start Now"
});

// Auto-responsive features grid
document.getElementById('features').innerHTML = MV.features({
  features: [
    {title: "Feature 1", description: "Benefit", icon: "🚀"},
    {title: "Feature 2", description: "Value", icon: "⚡"}
  ]
});

// Complete landing page
const page = MV.landingPage({
  hero: {title: "Your Title"},
  features: {features: [...]},
  cta: {title: "Ready?"}
});
```

### 🎯 Available Components:
- **MV.hero()** - Hero sections with gradients and CTAs
- **MV.features()** - Auto-responsive feature grids  
- **MV.testimonial()** - Social proof sections
- **MV.cta()** - Call-to-action with conversions
- **MV.benefits()** - Benefits + pricing boxes
- **MV.faq()** - Interactive FAQ accordions
- **MV.stats()** - Numbers/metrics displays
- **MV.media()** - Video sections with thumbnails
- **MV.landingPage()** - Complete page generator

### 🏃‍♂️ Speed Gains:
- **Landing page:** 15 minutes → **3 minutes** (80% faster)
- **Component sections:** 10 minutes → **30 seconds** (95% faster)
- **Complex pages:** 45 minutes → **8 minutes** (82% faster)

**Live Demo:** https://elizaguide.github.io/web/mindvalley-components-demo.html
**Documentation:** `web/skills/mindvalley-design/COMPONENTS.md`

**Deployment Flow:**
1. **ASK:** "Where should I create this website?" (if not specified)
2. Create proper folder structure in chosen location
3. Add emoji favicon  
4. Commit & push to GitHub
5. Share GitHub URL (not localhost) for WhatsApp

## 🔗 Website Sharing Rules for WhatsApp

**🚨 CRITICAL RULES - NEVER BREAK THESE:**

### URL Formatting
- 🚫 **NEVER BOLD URLS** - **https://example.com** breaks the link!
- ✅ **Plain URLs only** - https://example.com works perfectly
- ✅ **Format description separately** - **Main Landing Page:** (new line) https://example.com
- ✅ **Test every link** - Ensure URLs are clickable before sending

### URL Type Selection  
- ✅ **WhatsApp messages:** ALWAYS use GitHub URLs (remote access for travel)
- ❌ **Never localhost** on WhatsApp - http://localhost:3000 won't work remotely
- ✅ **GitHub Pages format:** https://elizaguide.github.io/web/project-name/
- ✅ **Verify deployment** - Check GitHub Pages is live before sharing

### Website Sharing Format
```
🎯 **Project Name** 

Brief description of what it does

https://elizaguide.github.io/web/project-name/

✨ **Key features:**
- Feature 1
- Feature 2  
- Feature 3
```

### Common Mistakes to Avoid
- ❌ `**https://example.com**` - Breaks the link completely
- ❌ `Here's the site: **https://example.com**` - Still breaks it
- ❌ `http://localhost:3000` - Won't work on mobile/travel
- ❌ Forgetting to commit/push to GitHub before sharing

## 💬 Platform Formatting Rules

**WhatsApp Specific:**
- ✅ **No markdown tables** - Use bullet lists instead
- ✅ **No headers** - Use **bold** or CAPS for emphasis
- ✅ **Keep it clean** - WhatsApp doesn't need fancy formatting

**Discord:**
- ✅ **Multiple links:** Wrap in `<>` to suppress embeds: `<https://example.com>`
- ✅ **Tables OK** - Discord supports markdown tables

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
