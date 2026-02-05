// 🤖 Eliza's Slide Studio API Demo
// This shows how I can programmatically create and edit slides

// Example: Create a complete presentation about "Employee Branding"
function elizaCreateEmployeeBrandingDeck() {
    console.log("🤖 Eliza: Creating Employee Branding presentation...");
    
    // Clear existing slides (keep first one)
    const currentSlides = window.slideStudioAPI.getAllSlides();
    currentSlides.slice(1).forEach(slide => {
        window.slideStudioAPI.deleteSlide(slide.id);
    });
    
    // Update the first slide
    window.slideStudioAPI.updateSlide(currentSlides[0].id, {
        title: "Employee Branding Mastery",
        subtitle: "Building Magnetic Workplace Culture",
        content: "The Complete Framework for Attracting Top Talent",
        background: "#7a12d4"
    });
    
    // Add Problem slide
    window.slideStudioAPI.addSlide({
        title: "The Problem",
        subtitle: "Traditional Hiring is Broken",
        content: "• 73% of companies struggle to attract top talent\n• Average time-to-hire: 42 days\n• Cost per hire: $4,700\n• 88% of hires are 'settling' decisions",
        background: "white",
        layout: "title-content"
    });
    
    // Add Four Quadrants slide  
    window.slideStudioAPI.addSlide({
        title: "The Four Pillars Framework",
        subtitle: "What Top Talent Really Wants",
        content: "🎯 MEANING: Purpose-driven mission\n💰 ABUNDANCE: Growth & prosperity\n😊 HAPPINESS: Positive culture & environment\n📈 GROWTH: Learning & development opportunities",
        background: "#f8f9fa",
        layout: "title-content"
    });
    
    // Add Bar of Awesomeness slide
    window.slideStudioAPI.addSlide({
        title: "Rule #1: Always Hire Above the Bar",
        subtitle: "Never Compromise on Excellence",
        content: "Every hire should elevate your team average.\n\nBetter to wait for A-players than settle for B-players.\n\nOne below-average hire affects everyone.",
        background: "#667eea",
        layout: "title-content"
    });
    
    // Add Results slide
    window.slideStudioAPI.addSlide({
        title: "Mindvalley Results",
        subtitle: "Magnetic Employer Brand in Action",
        content: "• 60 countries → Kuala Lumpur\n• 95% employee satisfaction\n• 40% faster hiring\n• Top talent approaches us\n• Global recognition as employer of choice",
        background: "#764ba2",
        layout: "title-content"
    });
    
    console.log("✅ Eliza: Employee Branding deck created! 5 slides ready for your editing.");
    
    // Navigate to first slide
    window.slideStudioAPI.setCurrentSlide(currentSlides[0].id);
}

// Example: Quick content optimization for current slide
function elizaOptimizeCurrentSlide() {
    const currentSlide = window.slideStudioAPI.getCurrentSlide();
    
    if (!currentSlide) {
        console.log("❌ No slide selected");
        return;
    }
    
    console.log("🤖 Eliza: Optimizing current slide for impact...");
    
    // Analyze and improve content
    const improvements = {
        title: makeMoreImpactful(currentSlide.title),
        content: addBulletPoints(currentSlide.content)
    };
    
    window.slideStudioAPI.updateSlide(currentSlide.id, improvements);
    console.log("✅ Content optimized for maximum impact!");
}

// Helper functions for content improvement
function makeMoreImpactful(title) {
    const powerWords = ["Ultimate", "Proven", "Essential", "Master", "Revolutionary"];
    const randomPower = powerWords[Math.floor(Math.random() * powerWords.length)];
    
    if (title && !powerWords.some(word => title.includes(word))) {
        return `${randomPower} ${title}`;
    }
    return title;
}

function addBulletPoints(content) {
    if (!content || content.includes("•")) return content;
    
    // Convert sentences to bullet points for better readability
    const sentences = content.split('. ').filter(s => s.length > 10);
    if (sentences.length > 1) {
        return sentences.map(s => `• ${s.trim()}`).join('\n');
    }
    return content;
}

// Example: Create slides from a topic
function elizaCreateSlidesFromTopic(topic) {
    console.log(`🤖 Eliza: Creating slides about "${topic}"...`);
    
    const slideTemplates = {
        "leadership": [
            { title: "Leadership in the Digital Age", subtitle: "Navigating Modern Challenges" },
            { title: "The 5 Leadership Archetypes", content: "Visionary • Coach • Servant • Transformational • Authentic" },
            { title: "Building High-Performance Teams", content: "Trust + Vision + Execution = Results" }
        ],
        "productivity": [
            { title: "Peak Performance Systems", subtitle: "Optimize Your Most Valuable Asset: Time" },
            { title: "The 4-Hour Focused Work Block", content: "Deep work beats busy work every time" },
            { title: "Energy Management > Time Management", content: "Work with your natural rhythms, not against them" }
        ]
    };
    
    const slides = slideTemplates[topic.toLowerCase()] || [
        { title: topic, subtitle: "Key Insights and Strategies" },
        { title: "The Challenge", content: "What problems are we solving?" },
        { title: "The Solution", content: "Our approach to " + topic },
        { title: "Next Steps", content: "How to implement these ideas" }
    ];
    
    slides.forEach(slideData => {
        window.slideStudioAPI.addSlide({
            background: "white",
            layout: "title-content",
            ...slideData
        });
    });
    
    console.log(`✅ Created ${slides.length} slides about ${topic}!`);
}

// Export functions to global scope so they can be called from browser console
window.elizaDemo = {
    createEmployeeBrandingDeck: elizaCreateEmployeeBrandingDeck,
    optimizeCurrentSlide: elizaOptimizeCurrentSlide,
    createSlidesFromTopic: elizaCreateSlidesFromTopic
};

console.log("🤖 Eliza Slide Studio API loaded!");
console.log("Try: elizaDemo.createEmployeeBrandingDeck()");
console.log("Or: elizaDemo.createSlidesFromTopic('leadership')");