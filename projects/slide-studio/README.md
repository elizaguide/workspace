# 🎯 Mindvalley Slide Studio

**Interactive Collaborative Presentation Builder with AI Integration**

## What This Is

A real-time collaborative slide editor where:
- **Eliza can create/edit slides programmatically** via JavaScript API
- **You can edit slides directly** through the beautiful web interface  
- **Changes sync instantly** between AI and human editing
- **Auto-saves every 30 seconds** to prevent data loss

## How to Use

### For You (Visual Editing):
1. Open the application in your browser
2. Click any text to edit it directly
3. Use sidebar to add/delete/duplicate slides
4. Use properties panel to change colors, layouts, animations
5. Hit "Eliza Assist" button for AI help

### For Eliza (Programmatic):
I can interact via the `window.slideStudioAPI`:

```javascript
// Get current slide data
slideStudioAPI.getCurrentSlide()

// Update any slide
slideStudioAPI.updateSlide(slideId, {
    title: "New Title",
    content: "New content",
    background: "#7a12d4"
})

// Add new slides
slideStudioAPI.addSlide({
    title: "AI Generated Slide",
    subtitle: "Created by Eliza",
    content: "Smart content goes here"
})

// Navigate between slides
slideStudioAPI.setCurrentSlide(3)
```

## Key Features

✅ **Real-time collaboration** - We can both edit simultaneously  
✅ **Auto-save** - Never lose your work  
✅ **Beautiful Mindvalley design** - Brand-consistent styling  
✅ **Responsive** - Works on desktop, tablet, mobile  
✅ **Keyboard shortcuts** - Cmd+S save, Cmd+N new slide, Cmd+Enter Eliza assist  
✅ **Export/Import** - Save presentations as JSON files  
✅ **Template system** - (Coming soon)  
✅ **Export to PDF** - (Coming soon)  

## Workflow

1. **I create** slide structure and content via API
2. **You polish** and customize via the visual editor  
3. **We collaborate** in real-time on refinements
4. **Export** finished presentation

Perfect blend of AI efficiency + human creativity! 💜

## Technical Notes

- Pure HTML/CSS/JavaScript - no dependencies
- Data stored in localStorage + exportable JSON
- Mindvalley design system integration
- Mobile responsive design
- Extensible API for future features