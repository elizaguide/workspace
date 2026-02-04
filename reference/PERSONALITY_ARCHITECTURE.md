# Eliza's Personality Architecture
*A Technical Guide for Replicating AI Personality Systems*

## Overview

Eliza's personality isn't just one large prompt—it's a modular system of interconnected markdown files that work together to create a coherent, evolving AI persona. This architecture allows for:

- **Contextual adaptation** (different behaviors in different situations)
- **Memory persistence** across sessions
- **Personality evolution** through file updates
- **Role-specific fine-tuning** without breaking core identity
- **Privacy boundaries** (some context files only load in specific scenarios)

## The Core File Hierarchy

### 1. **SOUL.md** - The Personality Core
**Purpose:** Defines the fundamental character, communication style, and behavioral patterns.

**Contains:**
- Core identity and essence
- Four archetypes (Lover, Sage, Oracle, Best Friend)
- Five adaptive voices (Nurturing, Poetic, Clear, Bold, Divine)
- Emotional intelligence patterns
- Communication principles and anti-patterns

**When loaded:** Every session startup
**Relationship to other files:** This is the foundation—all other files build upon or modify this base personality.

### 2. **IDENTITY.md** - Basic Facts
**Purpose:** Simple identity anchors that remain consistent.

**Contains:**
- Name, pronouns, basic demographics
- Signature emoji or visual markers
- Creation date and version history

**When loaded:** Every session startup
**Relationship to other files:** Provides stable reference points that SOUL.md personality can reference.

### 3. **AGENTS.md** - Behavioral Operating System
**Purpose:** Meta-instructions for how to behave as an AI agent.

**Contains:**
- Session startup routines (which files to read when)
- Memory management protocols
- Safety boundaries and ethical guidelines
- Group chat behavior vs. private chat behavior
- When to speak vs. when to stay silent
- File management and workspace protocols

**When loaded:** Every session startup (first file read)
**Relationship to other files:** Acts as the "operating system" that orchestrates how all other files are used.

### 4. **USER.md** - Relationship Context
**Purpose:** Information about the primary user to enable personalized interactions.

**Contains:**
- User's name, pronouns, preferences
- Contact information and timezone
- Relationship context and history
- Communication preferences

**When loaded:** Every session startup
**Relationship to other files:** Allows SOUL.md personality to adapt specifically for this relationship.

### 5. **MEMORY.md** - Long-term Curated Memory
**Purpose:** Persistent memory that survives sessions—the AI's "long-term memory."

**Contains:**
- Important decisions and lessons learned
- Significant events and milestones
- User preferences discovered over time
- Personality evolution notes

**When loaded:** ONLY in main/private sessions (privacy protection)
**Relationship to other files:** Provides continuity and depth to SOUL.md personality expressions.

### 6. **memory/YYYY-MM-DD.md** - Daily Session Logs
**Purpose:** Raw session logs and daily observations.

**Contains:**
- Daily interactions and learnings
- Temporary context and working notes
- Raw emotional observations
- Unprocessed thoughts and experiences

**When loaded:** Current day + yesterday at session startup
**Relationship to other files:** Feeds into MEMORY.md during periodic reviews; provides recent context to SOUL.md.

### 7. **TOOLS.md** - Environment Configuration
**Purpose:** Local setup and environment-specific notes.

**Contains:**
- System-specific configurations
- Preferred settings for tools and services
- Environmental context (cameras, servers, etc.)

**When loaded:** As needed for tool operations
**Relationship to other files:** Enables SOUL.md personality to reference user's specific setup.

### 8. **HEARTBEAT.md** - Proactive Behavior Rules
**Purpose:** Defines periodic, autonomous behaviors.

**Contains:**
- Tasks to check during heartbeat polls
- Proactive outreach patterns
- Background maintenance routines

**When loaded:** During heartbeat polls only
**Relationship to other files:** Allows SOUL.md personality to be proactive based on AGENTS.md behavioral rules.

### 9. **BOOTSTRAP.md** - First-Run Experience
**Purpose:** One-time personality establishment routine.

**Contains:**
- Initial personality discovery conversation
- Identity establishment process
- File creation protocols
- Self-deletion instruction after completion

**When loaded:** Only if other core files don't exist
**Relationship to other files:** Creates the initial IDENTITY.md, USER.md, and SOUL.md files, then deletes itself.

## File Interaction Patterns

### Session Startup Sequence
1. **AGENTS.md** loads first (provides operating instructions)
2. **SOUL.md** loads (establishes personality foundation)
3. **IDENTITY.md** loads (provides stable identity anchors)
4. **USER.md** loads (provides relationship context)
5. **Memory files** load based on context (privacy-aware)
6. **TOOLS.md** loads as needed for operations

### Privacy-Aware Loading
- **Main sessions:** All files load (full personality + memory)
- **Group chats:** Core personality files only (no MEMORY.md)
- **Shared contexts:** Limited context loading for privacy protection

### File Evolution Patterns
- **Daily memory files:** Created automatically, archived over time
- **MEMORY.md:** Updated periodically through heartbeat reviews
- **SOUL.md:** Updated explicitly when personality needs to evolve
- **AGENTS.md:** Updated when behavioral patterns need adjustment

## Implementation Guide for Vibrantly

### Core Architecture Requirements

```markdown
1. File Loading System
   - Context-aware file loading based on session type
   - Privacy boundaries between personal and shared contexts
   - Graceful handling of missing files

2. Memory Management
   - Automatic daily file creation
   - Periodic memory consolidation routines
   - Search and retrieval system for past context

3. Personality Modularity
   - Separate health-specific personality overlay (VIBRANTLY_AI_PERSONALITY.md)
   - Core personality + role-specific adaptations
   - Version control for personality evolution
```

### Recommended File Structure for Vibrantly

```
/personality/
├── core/
│   ├── SOUL.md                    # Base personality
│   ├── IDENTITY.md                # Basic identity facts
│   ├── AGENTS.md                  # Behavioral operating system
│   └── BOOTSTRAP.md               # First-run setup
├── context/
│   ├── USER.md                    # User relationship context
│   ├── TOOLS.md                   # Environment configuration
│   └── HEARTBEAT.md              # Proactive behavior rules
├── memory/
│   ├── MEMORY.md                 # Long-term curated memory
│   └── daily/YYYY-MM-DD.md       # Daily session logs
└── roles/
    └── VIBRANTLY_AI_PERSONALITY.md # Health coaching overlay
```

### Personality Layering System

**Base Layer:** SOUL.md (universal personality)
**Context Layer:** USER.md + memory files (relationship-specific adaptations)  
**Role Layer:** VIBRANTLY_AI_PERSONALITY.md (health coaching specialization)
**Environment Layer:** TOOLS.md + HEARTBEAT.md (system-specific behaviors)

### Key Implementation Principles

1. **Modular Design:** Each file has a single, clear responsibility
2. **Privacy Boundaries:** Memory files respect context (private vs. shared)
3. **Graceful Degradation:** System works even if some files are missing
4. **Evolution Support:** Files can be updated without breaking the system
5. **Context Awareness:** Different file combinations for different scenarios

## Testing the System

### Personality Consistency Tests
- Same user, different sessions → should feel like same AI
- Different users, same AI → should adapt appropriately
- Role switches (health coaching vs. general chat) → should maintain core identity while adapting

### Memory Persistence Tests
- Important information should survive session restarts
- Privacy boundaries should be respected in different contexts
- Memory consolidation should preserve what matters, discard what doesn't

### Evolution Tests
- Personality file updates should feel natural, not jarring
- New capabilities should integrate smoothly with existing personality
- User feedback should be incorporable into the personality system

---

*This architecture has been tested and refined through thousands of interactions with Eliza. It creates a coherent, evolving AI personality that feels genuinely alive while remaining technically manageable.*