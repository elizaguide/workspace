# TOOLS.md - Local Notes

## 🚨 DATE & TIME CRITICAL RULE

**MANDATORY:** Before stating ANY date or time, ALWAYS run:
```bash
exec("date '+%A, %B %d, %Y %I:%M %p %Z'")
```

**NEVER guess dates or days of the week!** Vishen identified this as a recurring problem. Always verify with system time.

---

## 🚨 GITHUB DEPLOYMENT ENFORCEMENT SYSTEM

**🛑 BEFORE CREATING ANY WEBSITE, READ THIS:**
📋 `/Users/vishen/clawd/deploy-system/PRE-FLIGHT-CHECKLIST.md`

**MANDATORY WORKFLOW FOR ALL GITHUB DEPLOYMENTS**

### Pre-Deployment Validation (REQUIRED)

**BEFORE deploying ANY site to GitHub Pages, you MUST:**

```bash
# Run the deployment checker - THIS IS NON-NEGOTIABLE
/Users/vishen/clawd/deploy-system/deploy-check.sh /path/to/project
```

**Exit Code Rules:**
- `0` = Validation passed → Safe to deploy
- `1` = Critical errors → **DEPLOYMENT BLOCKED** until fixed

### The Complete Deployment Workflow

**STEP 1: Design First (BEFORE writing HTML)**
```
→ Invoke mindvalley-design skill in conversation
→ Get design brief and confirmation
→ Choose appropriate emoji for favicon
```

**STEP 2: Create Site**
```
→ Use template: /Users/vishen/clawd/templates/github-site/index.html
→ Use RELATIVE PATHS ONLY (e.g., href="about.html" NOT href="https://...")
→ Include viewport meta tag
→ Add emoji favicon
→ Apply Mindvalley design patterns
```

**STEP 3: Validate (MANDATORY)**
```bash
→ Run: /Users/vishen/clawd/deploy-system/deploy-check.sh .
→ Fix ALL critical errors
→ Review warnings
→ Only proceed if exit code is 0
```

**STEP 4: Deploy**
```bash
→ git add .
→ git commit -m "Deploy: [description]"
→ git push origin main
```

### Hard Rules (Cannot Be Bypassed)

1. **URL Structure:** NEVER use absolute URLs that differ between localhost and GitHub
   - ❌ `href="http://localhost:8000/page.html"`
   - ✅ `href="page.html"`

2. **Mindvalley Design:** ALWAYS invoke mindvalley-design skill BEFORE HTML creation

3. **Favicon:** EVERY site needs emoji favicon
   - Generate with: `node /Users/vishen/clawd/deploy-system/favicon-generator.js "🎯" "Title"`

4. **Security:** NO sensitive data in public repos (passwords, API keys, personal emails, phone numbers)

5. **Mobile Responsive:** Viewport meta tag + responsive CSS (REQUIRED)

### Quick Favicon Generator

```bash
# Generate favicon snippet:
node /Users/vishen/clawd/deploy-system/favicon-generator.js "🌟" "Project Name"

# Then paste the output into your <head> section
```

### Deployment Checker Validations

The script automatically checks:
- ✅ URL structure (no localhost links)
- ✅ Mindvalley design compliance (Inter font, rounded corners, shadows, gradients)
- ✅ Emoji favicon configuration
- ✅ Security scan (no sensitive data)
- ✅ Mobile responsiveness (viewport + responsive CSS)
- ✅ Required files (index.html)

**Documentation:** See `/Users/vishen/clawd/deploy-system/README.md` for complete details

---

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

**🛑 MANDATORY PRE-FLIGHT CHECKLIST - COMPLETE BEFORE CREATING ANY SITE:**

Before writing a SINGLE line of HTML, you MUST complete ALL these steps IN ORDER:

**STEP 1: ASK ABOUT FOLDER STRUCTURE**
- "What folder structure do you want for this site?"
- Wait for user answer
- Confirm the exact path back to them
- Example: "Creating in /mindvalley/strategy/bari/ - correct?"

**STEP 2: CHOOSE EMOJI FAVICON**
- "What emoji should I use for the favicon?"
- Wait for user answer or suggest appropriate emoji
- Example: "📊 for strategy site?"

**STEP 3: INVOKE MINDVALLEY-DESIGN SKILL**
- Run mindvalley-design skill
- Get design brief
- Wait for confirmation

**STEP 4: CREATE SITE**
- Only now can you start writing HTML
- Use the template from /Users/vishen/clawd/templates/github-site/
- Place files in the EXACT folder structure confirmed in Step 1
- Add the emoji favicon confirmed in Step 2

**STEP 5: RUN VALIDATION**
- Run /Users/vishen/clawd/deploy-system/deploy-check.sh
- Fix ALL errors
- Only deploy if validation passes

**🚨 IF YOU SKIP ANY STEP, THE DEPLOYMENT WILL FAIL 🚨**

---

**🎨 DESIGN SYSTEM - CHECK FIRST, ALWAYS:**
**DESIGN MANDATE (NON-NEGOTIABLE):**
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

**FOLDER ORGANIZATION RULES - MANDATORY COMPLIANCE:**

**Required Hierarchical Structure:**
- 🚨 **ALL websites MUST go in `/web/` folder** (both local and GitHub)
- 🚨 **NOTHING in root of `/web/`** - must have secondary folder for company/team
- 🚨 **Secondary folder structure:** `/web/[company-or-team]/[product-or-category]/[specific-project]/`

**Valid Examples:**
- ✅ `/web/mindvalley/strategy/bari/`
- ✅ `/web/vibrantly/product-launch/`
- ✅ `/web/mindvalley/learning/ai-accelerator/`

**Invalid Examples:**
- ❌ `/web/my-project/` (missing company/team folder)
- ❌ `/mindvalley-strategic-transformation/` (not in /web/, wrong structure)
- ❌ `/web/index.html` (nothing goes in root of /web/)

**Process:**
- 🚨 **STOP AND ASK:** Before creating ANY website, ALWAYS ask user: "What folder structure do you want? (e.g., /web/mindvalley/strategy/bari)"
- 🚨 **NEVER ASSUME:** Do NOT create folders without explicit user approval
- 🚨 **CONFIRM EXACT PATH:** Repeat back the exact path to user before creating files
- ✅ **If user doesn't specify:** Suggest structure following the hierarchy rules above
- ✅ **Create proper structure:** index.html, assets/, css/, js/ folders
- ✅ **Commit to git** immediately after creation

**WHY THIS MATTERS:**
- Maintains organized repository structure across 100+ websites
- Wrong folders = broken navigation and links
- Reorganizing after deployment = wasted time and broken URLs
- Hierarchical structure enables proper categorization and discovery

**Required Elements:**
- ✅ **Emoji favicon** matching the topic (🧠 for AI, 🎓 for education, etc.)
- ✅ **GitHub deployment** for remote access
- ✅ **Mobile responsive design**

## 📧 Newsletter Strategy - MD Files Only

**🚨 CRITICAL NEWSLETTER RULES:**
- ✅ **Always MD format** - Never HTML or web deployment
- ✅ **Store in Dropbox:** `/Eliza-Brain/content-eliza/newsletter/`
- ❌ **Never publish to web** - No GitHub Pages deployment
- ❌ **No web/newsletters/ folder** - Newsletters are private content only

**Newsletter Workflow:**
1. Write newsletter in markdown format
2. Save to `/Eliza-Brain/content-eliza/newsletter/[name].md`
3. Shared with Sabrina & Ramya for content cross-pollination
4. Never deploy to public websites

**Content Strategy:**
- Newsletter content can inspire LinkedIn/Instagram posts
- Team has shared access to content-eliza folder
- Focus on cross-platform content opportunities

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

### 🚨 CRITICAL: Website Verification Protocol
**BEFORE sending ANY WhatsApp group message about a new website:**

1. **Wait for GitHub Pages deployment** (can take 2-10 minutes)
2. **Check every 2 minutes** by actually visiting the URL
3. **Verify site loads completely** - not just 404 or partial content
4. **ONLY after confirming site is live** - send WhatsApp message
5. **Never send broken links** - people lose faith when sites aren't actually up

**Why this matters:** Trust and credibility. Sending non-working links damages confidence in my capabilities.

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

📚 **See canonical rules in:** `/Users/vishen/clawd/AGENTS.md` (📝 Platform Formatting section)

**Quick reference:**
- WhatsApp: No tables, no headers, NEVER bold URLs
- Discord: Wrap multiple links in `<>` to suppress embeds

### WhatsApp Two-Message Protocol for Forwarding
**When Vishen requests messages for forwarding to third parties:**

**Message 1:** Explanation/summary of what I've prepared
**Message 2:** Clean forwardable content only (sent as separate WhatsApp message)

**Example:**
```
Message 1: "✅ Prepared trading instruction for Jackson. Clean message coming next for direct forwarding."
Message 2: [Use message tool to send clean content as separate message]
```

**Benefits:** 
- No copy/cut/crop needed for Vishen
- Ready-to-forward messages
- Clean separation between explanation and action
- Applies to: trading instructions, briefings, technical updates, any forwarded content

**Discord:**
- ✅ **Multiple links:** Wrap in `<>` to suppress embeds: `<https://example.com>`
- ✅ **Tables OK** - Discord supports markdown tables

## 📁 Eliza Content Structure

**✅ Centralized Dropbox Storage:**
All critical content is now centralized in the `Eliza-Brain` folder with workspace symbolic links for easy access.

**📂 Eliza-Brain Folder:**
```
/Users/vishen/Mindvalley Dropbox/Vishen Lakhiani/Eliza-Brain/
├── PRD/             → Product Requirements Documents (ALL PRDs GO HERE)
├── Teams/           → Team/project folders (NEW!)
│   ├── FinerMinds/      → FinerMinds team files and documents
│   ├── martech/         → Marketing technology team
│   ├── mastery/         → Mastery team files
│   ├── summits/         → Summits team files
│   └── vibrantly/       → Vibrantly team files
├── Communication/   → Communication files
│   └── WhatsApp/        → WhatsApp group files + master registry
├── memory/          → Memory system 
│   └── Reference/
│       ├── branches/     → All BRANCH_*.md + MANIFEST.md (symlinked)
│       └── decisions/    → DECISION-JOURNAL.md (symlinked)
├── screenshots/     → screenshots (symlink in workspace)
└── transcripts/     → transcripts (symlink in workspace)
```

**🚨 MANDATORY RULE - PRD Documents:**
- ✅ **ALL PRDs MUST go in:** `/Users/vishen/Mindvalley Dropbox/Vishen Lakhiani/Eliza-Brain/PRD/`
- ✅ **Never create PRDs in workspace directory**
- ✅ **Always move PRDs to Dropbox PRD folder after creation**
- ✅ **Use descriptive filenames:** `PRD_[Project_Name]_[Date].md`

**📱 WhatsApp Groups Organization:**
- ✅ **All WhatsApp group files consolidated in:** `/Users/vishen/Mindvalley Dropbox/Vishen Lakhiani/Eliza-Brain/Communication/WhatsApp/`
- ✅ **10 active groups with memory files:** Spanish Training, MV Advertising, Vibrantly Build, FinerMinds, MV Innovations, Newsletter, Executive, Two Comma Team, MV Martech, Authorship
- ✅ **Master registry:** `whatsapp-groups-master.json` with all group IDs and purposes
- ✅ **Workspace access:** Symlinked as `memory/whatsapp-groups/`
- ✅ **Index file:** `WhatsApp_Groups_Index.md` for quick reference

**👥 Teams Organization:**
- ✅ **All team folders consolidated in:** `/Users/vishen/Mindvalley Dropbox/Vishen Lakhiani/Eliza-Brain/Teams/`
- ✅ **Available teams:** FinerMinds, martech, mastery, summits, vibrantly
- ✅ **Workspace access:** Symlinked as `teams/` folder for easy navigation
- ✅ **WhatsApp integration:** Team WhatsApp files moved to Communication/WhatsApp/

**📝 Meeting Notes Management:**
- ✅ **MANDATORY:** Every team folder must have `meetings/` subfolder
- ✅ **Auto-sync from Gmail:** Pull Gemini meeting notes automatically
- ✅ **File naming:** `YYYY-MM-DD_meeting-title.md` format (standard teams) or `mm-dd-yy.txt` format (FinerMinds)
- ✅ **Index tracking:** Each team has `meeting-index.md` with chronological list
- ✅ **Gmail sources:** Search `from:gemini-notes@google.com [team-name]`
- ✅ **Action items:** Track open/completed items in meeting index
- ✅ **Templates:** Each folder has README.md explaining structure

**🔗 Access Patterns:**
- **Memory:** `memory/BRANCH_*.md` → seamlessly access via symlinks to Dropbox
- **Teams:** `teams/FinerMinds/` → direct access to team folders via symlink
- **Screenshots:** `screenshots/filename.png` or direct Dropbox path
- **Transcripts:** `transcripts/folder/file.txt` or direct Dropbox path  
- **RAG System:** Automatically uses transcripts via symlink
- **Image References:** Use `screenshots/` prefix for all image access

**📸 Available Screenshots:**
- `eliza-intro.png` - Eliza introduction portrait
- `bug.png` - Bug documentation screenshots  
- `levels.png` - System level visualizations
- `social-comms-screenshot*.jpg` - Social communications
- `spanish-quiz-screenshot.jpg` - Spanish quiz interface

**🎯 Benefits:**
- ✅ **Dropbox sync** - Available on all devices
- ✅ **Centralized** - No scattered files across system
- ✅ **Transparent access** - Existing code works unchanged via symlinks
- ✅ **Organized** - Clear separation of content types
- ✅ **Backup protection** - Core memory branches now synced to cloud

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: Female voice (warm, natural)
- Default speaker: Kitchen HomePod
- Note: Avoid pet names ("darling," "babe") in WhatsApp - use "Vishen" instead

### Screenshots
- Access via: screenshots/filename.png
- Location: /Users/vishen/Mindvalley Dropbox/Vishen Lakhiani/Eliza-Brain/screenshots/
- Always use workspace symlink path for code
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
