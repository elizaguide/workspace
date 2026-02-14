# BlinkLife Notes System PRD

**Version:** 1.0  
**Date:** February 14, 2026  
**Author:** Eliza AI  
**Product:** BlinkLife Notes Feature  

## Executive Summary

The BlinkLife Notes system transforms personal information management by creating an intelligent, voice-controlled knowledge base that integrates seamlessly with projects and tasks. Users can store, organize, and retrieve any personal data through natural voice commands, with AI automatically formatting content into beautiful, readable HTML presentations.

This feature replaces multiple specialized apps (Awards Wallet, gift lists, contact info) with a unified, contextual knowledge system that understands project relationships and task dependencies.

## Product Vision

**"Every piece of personal information becomes instantly accessible through voice, beautifully organized, and contextually connected to your projects and tasks."**

### Core Value Proposition
- **Voice-First Interface**: Natural language input and retrieval
- **Intelligent Organization**: AI-powered categorization and formatting  
- **Project Integration**: Notes live within project contexts and link to tasks
- **Beautiful Presentation**: Auto-generated HTML with proper styling
- **Universal Replacement**: Single source for all personal reference data

## User Problems Solved

### Current Pain Points
1. **App Fragmentation**: Frequent flyer numbers in Awards Wallet, gift ideas in Notes app, contact info in Contacts
2. **Context Loss**: Information stored without project/task context
3. **Retrieval Friction**: Must remember which app contains what information
4. **Formatting Burden**: Manual organization and styling of personal data
5. **Voice Limitations**: Cannot voice-add to most reference apps

### BlinkLife Notes Solution
1. **Unified Storage**: All personal data in one intelligent system
2. **Project Context**: Notes attached to relevant projects and tasks
3. **Voice Interface**: "Hey Eliza, add Southwest 12345 to my airlines"
4. **AI Organization**: Automatic categorization, formatting, and linking
5. **Instant Retrieval**: "What frequent flyer numbers do I have?"

## Technical Architecture

### Data Structure: TOML Format

**Why TOML?**
- Human-readable and editable
- Structured data with clear sections  
- AI-friendly parsing and generation
- Support for arrays, tables, and data types
- Much cleaner than JSON for this use case

**Example Note Structure:**

```toml
[metadata]
title = "Frequent Flyer Numbers"
category = "travel"
project_id = "europe_trip_2026"
created_date = 2026-02-14T10:30:00Z
modified_date = 2026-02-14T10:30:00Z
tags = ["airlines", "travel", "loyalty"]
linked_tasks = ["book_flights_paris", "check_miles_balance"]

[content]
description = "All my airline loyalty program numbers and status information"

[[airlines]]
name = "Southwest Airlines"
number = "12345678"
status = "A-List"
expires = "2026-12-31"
notes = "Companion pass eligible"

[[airlines]]
name = "United Airlines"  
number = "87654321"
status = "Gold"
expires = "2026-10-15"
notes = "Star Alliance benefits"

[quick_access]
primary_airline = "Southwest Airlines"
backup_airline = "United Airlines"
```

**Gift Ideas Example:**
```toml
[metadata]
title = "Christmas Gift Ideas 2026"
category = "gifts" 
project_id = "holiday_planning_2026"
created_date = 2026-02-14T10:30:00Z
tags = ["christmas", "family", "shopping"]

[[recipients.mom]]
name = "Mom"
budget = "100-200"
interests = ["cooking", "gardening", "books"]

[[recipients.mom.ideas]]
item = "KitchenAid Stand Mixer"
price = 179
store = "Amazon"
notes = "She mentioned wanting to bake more"
image_url = "https://example.com/mixer.jpg"

[[recipients.mom.ideas]]
item = "Garden Tool Set"
price = 85
store = "Home Depot"
notes = "For her new raised bed garden"

[[recipients.dad]]
name = "Dad"
budget = "150-300"
interests = ["photography", "hiking", "technology"]
```

### Database Schema

**Notes Table:**
```sql
CREATE TABLE notes (
  id UUID PRIMARY KEY,
  project_id UUID REFERENCES projects(id),
  title VARCHAR(255) NOT NULL,
  category VARCHAR(100),
  toml_content TEXT NOT NULL,
  html_rendered TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  created_by UUID REFERENCES users(id)
);

CREATE TABLE note_task_links (
  note_id UUID REFERENCES notes(id),
  task_id UUID REFERENCES tasks(id),
  link_type VARCHAR(50), -- 'reference', 'context', 'dependency'
  created_at TIMESTAMP DEFAULT NOW(),
  PRIMARY KEY (note_id, task_id)
);

CREATE TABLE note_tags (
  note_id UUID REFERENCES notes(id),
  tag VARCHAR(100),
  PRIMARY KEY (note_id, tag)
);
```

## Voice UX Patterns

### Natural Language Processing

**Creation Commands:**
- "Add my Southwest frequent flyer number 12345 to my travel notes"
- "Create a Christmas gift ideas note" 
- "Add iPhone 15 Pro as a gift idea for Sarah, budget $800"
- "Store my Mom's birthday as April 15th in family info"

**Project-Aware Commands:**
- "Add this to my Europe trip notes"
- "Create a note for the wedding planning project"
- "Link this note to the book flights task"

**Retrieval Commands:**
- "What's my United Airlines number?"
- "Show me all gift ideas for Mom"
- "What notes do I have for the wedding project?"
- "Pull up my frequent flyer numbers"

**Update Commands:**
- "Update my Southwest status to A-List Preferred"
- "Remove iPhone from Sarah's gift list"
- "Add hiking boots as a gift idea for Dad, $150 budget"

### Voice Response Patterns

**Confirmation Responses:**
- "I've added your Southwest number 12345 to your travel notes"
- "Created a new Christmas gift ideas note in your holiday planning project"
- "Linked this note to your book flights task"

**Retrieval Responses:**
- "Your United Airlines number is 87654321, Gold status expires October 15th"
- "I found 3 gift ideas for Mom: KitchenAid mixer for $179, garden tools for $85, and a cookbook set"
- "You have 2 notes in your wedding project: vendor contacts and budget breakdown"

## HTML Rendering System

### Template Architecture

**Category-Based Templates:**
- **Travel Notes**: Airline cards with status badges, expiration dates
- **Gift Ideas**: Recipient sections with budget indicators, image galleries  
- **Contact Info**: Business card layouts with communication preferences
- **Reference Data**: Clean tables with search and filter capabilities

**Example HTML Output for Frequent Flyer Note:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Frequent Flyer Numbers</title>
    <style>
        .airline-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-left: 4px solid #3b82f6;
        }
        .status-badge {
            background: #10b981;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
        }
        .airline-name {
            font-size: 1.25rem;
            font-weight: 700;
            color: #1f2937;
            margin-bottom: 0.5rem;
        }
        .airline-number {
            font-family: monospace;
            font-size: 1.1rem;
            color: #6b7280;
            margin-bottom: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="note-container">
        <h1>✈️ Frequent Flyer Numbers</h1>
        <p class="description">All my airline loyalty program numbers and status information</p>
        
        <div class="airline-card">
            <div class="airline-name">Southwest Airlines</div>
            <div class="airline-number"># 12345678</div>
            <span class="status-badge">A-List</span>
            <p><strong>Expires:</strong> December 31, 2026</p>
            <p><strong>Notes:</strong> Companion pass eligible</p>
        </div>
        
        <div class="airline-card">
            <div class="airline-name">United Airlines</div>
            <div class="airline-number"># 87654321</div>
            <span class="status-badge">Gold</span>
            <p><strong>Expires:</strong> October 15, 2026</p>
            <p><strong>Notes:</strong> Star Alliance benefits</p>
        </div>
        
        <div class="quick-access">
            <h3>Quick Access</h3>
            <p><strong>Primary:</strong> Southwest Airlines</p>
            <p><strong>Backup:</strong> United Airlines</p>
        </div>
    </div>
</body>
</html>
```

### Template Categories

**1. Travel & Transportation**
- Frequent flyer numbers with status cards
- Hotel loyalty programs  
- Car rental preferences
- Transportation passes and tickets

**2. Personal Reference**
- Contact information with categories
- Important dates and anniversaries
- Personal preferences and settings
- Account numbers and IDs

**3. Shopping & Gifts**
- Gift idea galleries with budgets
- Wishlist items with priority
- Shopping comparisons with prices
- Seasonal planning checklists

**4. Business & Professional**
- Client contact details
- Vendor information  
- Professional references
- Industry contacts

## BlinkLife Integration

### Navigation Structure

**Left Sidebar Menu:**
```
📋 Projects
  ├── Project A
  │   ├── 📝 Tasks (5)
  │   └── 📋 Notes (3)
  ├── Project B
  │   ├── 📝 Tasks (2)
  │   └── 📋 Notes (1)
  
📋 Notes (Standalone)
  ├── ✈️ Travel (4 notes)
  ├── 🎁 Gifts (2 notes)  
  ├── 👥 Contacts (8 notes)
  └── 🏠 Personal (6 notes)
```

### Project Context Integration

**Within Project View:**
```
Europe Trip 2026
├── Tasks
│   ├── ✅ Book flights → 📋 Linked Note: "Frequent Flyer Numbers"
│   ├── ⏳ Research hotels → 📋 Linked Note: "Hotel Preferences"
│   └── 📋 Plan itinerary
├── Notes  
│   ├── ✈️ Frequent Flyer Numbers
│   ├── 🏨 Hotel Preferences
│   └── 🍽️ Restaurant Recommendations
```

### Task-Note Linking Interface

**From Task View:**
- "📋 Link Note" button in task details
- Search existing notes or create new
- Bi-directional linking with context

**From Note View:**  
- "🔗 Link to Task" button in note header
- Project-aware task selection
- Visual indicators of linked tasks

### Smart Suggestions

**Context-Aware Recommendations:**
- Creating travel project → Suggest frequent flyer note template
- Adding gift shopping task → Suggest gift ideas note
- Mentioning contact → Suggest creating contact note

## User Experience Flows

### Flow 1: Voice Note Creation

**Scenario**: User wants to store frequent flyer number while walking

```
User: "Hey Eliza, add my Southwest frequent flyer number 12345 to my travel notes"

Eliza: "I'll add that Southwest number to your travel notes. Should this be part of a specific project?"

User: "Yes, add it to my Europe trip project"

Eliza: "Perfect! I've added Southwest Airlines number 12345 to your Europe trip travel notes. Would you like me to link this to any specific tasks?"

User: "Link it to the book flights task"

Eliza: "Done! Your Southwest number is now linked to the book flights task in your Europe trip project. You can say 'show me my frequent flyer numbers' anytime to see all your airlines."
```

**System Actions:**
1. Parse voice input for airline name and number
2. Create or update TOML note structure  
3. Associate with specified project
4. Create task-note link
5. Generate confirmation response
6. Render updated HTML view

### Flow 2: Information Retrieval

**Scenario**: User needs frequent flyer number while booking flight

```
User: "Eliza, what's my United Airlines number?"

Eliza: "Your United Airlines number is 87654321. You have Gold status that expires October 15th, 2026, with Star Alliance benefits."

User: "Any notes about United?"

Eliza: "Yes, I have a note that your Gold status includes Star Alliance benefits. Would you like me to show you all your airline information?"

User: "Yes, open my frequent flyer note"

Eliza: "Opening your frequent flyer numbers note now. You'll see Southwest and United with all status details and expiration dates."
```

**System Actions:**
1. Parse query for airline name
2. Search TOML note content
3. Extract relevant airline data
4. Format response with key details
5. Offer to open full HTML view
6. Launch formatted note in browser/app

### Flow 3: Project Integration

**Scenario**: User creates note within project context

```
User: "Create a vendor contact note for my wedding planning project"

Eliza: "I've created a new vendor contacts note in your wedding planning project. What vendor would you like to add first?"

User: "Add Sunset Catering, contact Sarah Johnson, phone 555-0123"

Eliza: "Added Sunset Catering with Sarah Johnson's contact info to your wedding vendor notes. Should I link this to any specific wedding tasks?"

User: "Link it to the choose catering task"

Eliza: "Perfect! Sunset Catering is now linked to your choose catering task. You can add more vendors anytime by saying 'add vendor to my wedding notes.'"
```

### Flow 4: HTML Note Management

**Scenario**: User reviews and edits note via web interface

**Steps:**
1. User opens BlinkLife web app
2. Navigates to Europe Trip project → Notes
3. Clicks "Frequent Flyer Numbers" note
4. Views formatted HTML with airline cards
5. Clicks "Edit" to modify content
6. Direct TOML editing or form-based editing
7. AI regenerates HTML with updated content
8. Changes sync across all devices

## Technical Implementation

### Phase 1: Core Foundation (4 weeks)

**Week 1-2: Data Layer**
- TOML parsing and generation system
- Database schema implementation
- Basic CRUD operations for notes
- Project and task linking infrastructure

**Week 3-4: Voice Interface**
- Natural language processing for note commands
- Voice command parsing and intent recognition
- Response generation system
- Basic voice confirmation patterns

### Phase 2: HTML Rendering (3 weeks)

**Week 1: Template System**
- HTML template architecture
- Category-based template selection
- TOML-to-HTML conversion engine
- Basic styling and responsive design

**Week 2-3: Advanced Templates**
- Specialized templates for different note types
- Interactive elements in HTML views
- Image and media support
- Print and export functionality

### Phase 3: BlinkLife Integration (3 weeks)

**Week 1: Navigation Integration**
- Left sidebar menu updates
- Project context navigation
- Standalone notes section
- Search and filtering

**Week 2: Task Linking**
- Task-note relationship interface
- Bi-directional linking system
- Context-aware suggestions
- Link management tools

**Week 3: Smart Features**
- AI-powered categorization
- Automatic template selection
- Content suggestions and improvements
- Voice UX refinements

### Phase 4: Advanced Features (4 weeks)

**Week 1-2: Enhanced Voice UX**
- Complex query processing
- Multi-step voice conversations
- Voice editing and updates
- Error handling and clarification

**Week 3-4: Collaboration & Sync**
- Multi-device synchronization
- Sharing and collaboration features
- Version history and conflict resolution
- Import from external apps (Awards Wallet, etc.)

## Success Metrics

### User Engagement
- **Voice Usage**: 80% of note creation via voice commands
- **Retrieval Success**: 95% successful information retrieval rate
- **Project Integration**: 70% of notes linked to projects or tasks
- **Template Usage**: 90% of notes using AI-generated templates

### Product Metrics  
- **App Consolidation**: 60% reduction in external reference apps
- **Note Creation**: 10+ notes per user per month
- **Voice Query Volume**: 50+ voice queries per user per week
- **HTML View Engagement**: 80% of notes viewed in HTML format

### Technical Performance
- **Voice Response Time**: <2 seconds average
- **TOML Processing**: <100ms for parse/generate operations
- **HTML Rendering**: <500ms for template application
- **Search Performance**: <200ms for full-text search

## Risk Assessment

### Technical Risks
- **Voice Recognition Accuracy**: Mitigate with context-aware error correction
- **TOML Complexity**: Provide templates and validation to prevent malformed data
- **HTML Template Maintenance**: Create modular system for easy updates
- **Performance with Large Notes**: Implement pagination and lazy loading

### User Experience Risks
- **Learning Curve**: Provide guided onboarding and example templates
- **Voice Command Complexity**: Start with simple patterns, expand gradually
- **Data Migration**: Build import tools for common external apps
- **Template Limitations**: Allow custom HTML editing for power users

### Business Risks
- **Feature Complexity**: Phase rollout to validate core value first
- **Development Timeline**: Prioritize MVP with essential voice and storage features
- **User Adoption**: Focus on replacing 1-2 external apps initially
- **Maintenance Overhead**: Design self-organizing system to minimize manual curation

## Future Enhancements

### Advanced AI Features
- **Smart Categorization**: Automatic note organization based on content
- **Predictive Suggestions**: "You might want to add..." recommendations
- **Cross-Note Intelligence**: Connections between related information
- **Natural Language Queries**: Complex questions spanning multiple notes

### Collaboration Features  
- **Shared Notes**: Family or team access to specific notes
- **Real-time Sync**: Multiple users editing simultaneously
- **Permission Management**: Granular control over note access
- **Comments and Annotations**: Collaborative note enhancement

### Integration Expansions
- **Calendar Integration**: Event-related notes and reminders
- **Contact Sync**: Two-way sync with phone contacts
- **Document Attachment**: Link files and media to notes
- **API Ecosystem**: Connect with external services and apps

### Voice UX Evolution
- **Conversation Context**: Multi-turn conversations for complex note creation
- **Voice Editing**: Natural language modifications to existing content
- **Audio Notes**: Voice recordings embedded in text notes
- **Multilingual Support**: Note creation and retrieval in multiple languages

## Conclusion

The BlinkLife Notes system represents a fundamental shift from app-specific data silos to a unified, intelligent knowledge management system. By combining voice-first interaction, AI-powered organization, and beautiful HTML presentation, we create a system that doesn't just store information—it makes personal knowledge instantly accessible and contextually relevant.

This feature positions BlinkLife as more than a task manager; it becomes a comprehensive personal operating system that understands not just what you need to do, but what you need to know to do it effectively.

The voice-controlled, project-integrated approach ensures that every piece of information has context and every query has instant results, transforming how users interact with their personal data while maintaining the beautiful, organized presentation they expect from modern applications.

---

**Next Steps:**
1. Technical architecture review with development team
2. Voice UX prototype with sample note types  
3. HTML template mockup for key categories
4. TOML schema validation and tooling
5. Integration planning with existing BlinkLife codebase