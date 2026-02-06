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
- ✅ **Use mindvalley-font.css and Mindvalley brand colors** (#7a12d4, #0f131a, etc.)
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
