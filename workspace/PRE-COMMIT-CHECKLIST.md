# 🚨 PRE-COMMIT CHECKLIST FOR WEB CONTENT
**MANDATORY CHECK BEFORE EVERY GIT COMMIT WITH WEB FILES**

---

## ⚠️ STOP! Before you commit, verify ALL items below:

### 📁 Structure & Organization
- [ ] **Local folder:** Content is in `/websites/PROJECT_NAME/` locally
- [ ] **GitHub structure:** Projects go directly in repo root as `/PROJECT_NAME/`
- [ ] **Clean paths:** No scattered files, everything properly organized
- [ ] **README updated:** Project README reflects new content

### 🎨 Design Requirements (NON-NEGOTIABLE)
- [ ] **FAVICON ADDED:** Every HTML page has appropriate favicon 
- [ ] **Emojis in titles:** Page titles include relevant emojis as design fabric
- [ ] **Visual hierarchy:** Emojis used throughout for emotional connection
- [ ] **Responsive design:** Pages work on mobile and desktop

### 🌐 Publishing Rules
- [ ] **GitHub Pages only:** Will publish to elizaguide.github.io/workspace/PROJECT_NAME/
- [ ] **No external services:** No rawgithack, netlify, or other domains
- [ ] **Proper links:** All internal links use relative paths that will work on GitHub Pages
- [ ] **No local paths:** No references to localhost or local file paths

### 📝 Content Quality
- [ ] **Meaningful titles:** Descriptive, emoji-enhanced page titles
- [ ] **Navigation works:** All links functional and logical
- [ ] **Loading test:** Pages load properly with all assets
- [ ] **Team accessibility:** Content ready for team members to access

### 🔄 Pre-Share Process  
- [ ] **Commit first:** Always commit and push BEFORE sharing links
- [ ] **Wait for propagation:** GitHub Pages may need 5-10 minutes
- [ ] **Test the public URL:** Verify link works before sending to teams
- [ ] **Proper message:** Team communications include context and next steps

---

## 🚫 INSTANT FAIL CONDITIONS
**If ANY of these are true, DO NOT COMMIT:**
- Missing favicon on any HTML page
- Local file paths in team communications  
- Content not in proper /workspace/ structure
- External domain dependencies
- Broken or incomplete navigation

---

## ⚡ AUTOMATION TRIGGER
**This checklist MUST run automatically when I detect:**
- HTML file modifications
- New web content creation  
- Team link sharing requests
- Publishing/deployment tasks
- Any mention of "commit," "push," or "deploy"

---

*💜 Created: 2026-02-03*
*This checklist prevents rule violations and ensures quality web deployment*