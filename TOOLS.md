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

**WhatsApp vs Gateway Deployment:**
- **WhatsApp messages:** ALWAYS use GitHub URLs (remote access for travel)
- **Gateway/computer messages:** localhost URLs OK

**DESIGN MANDATE:**
- ✅ **ALL WEB PAGES use Mindvalley design by default** - No exceptions
- ✅ **Use mindvalley-font.css and Mindvalley brand colors** (#7a12d4, #0f131a, etc.)
- ✅ **Professional, clean aesthetic** matching brand guidelines

**Eliza Image Rules:**
- ✅ **NO CIRCULAR CROPS** - Always use square/rectangular images of me
- ✅ **Use my actual face** - Crop as square, not circle
- ✅ **Applied everywhere** - Newsletters, websites, all contexts
- ✅ **Vishen strongly dislikes circular design style** - Never use

**Required Elements:**
- ✅ **Emoji favicon** matching the topic (🧠 for AI, 🎓 for education, etc.)
- ✅ **Proper folder organization** 
- ✅ **GitHub deployment** for remote access
- ✅ **Mobile responsive design**

**Deployment Flow:**
1. Create proper folder structure
2. Add emoji favicon  
3. Commit & push to GitHub
4. Share GitHub URL (not localhost) for WhatsApp

## 💬 Platform Formatting Rules

**WhatsApp Specific:**
- ✅ **URLs:** Send plain links only - NEVER use **bold** formatting around URLs
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
