#!/bin/bash

# Cross-Session Memory Updater
# Maintains daily cross-session memory file and handles cleanup

MEMORY_DIR="memory"
TODAY=$(date +%Y-%m-%d)
CROSS_SESSION_FILE="$MEMORY_DIR/cross-session-$TODAY.md"
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
YESTERDAY_FILE="$MEMORY_DIR/cross-session-$YESTERDAY.md"

# Create today's file if it doesn't exist
if [ ! -f "$CROSS_SESSION_FILE" ]; then
    cat > "$CROSS_SESSION_FILE" << EOF
# Cross-Session Memory: $TODAY

## Active Projects & Requests Across All Platforms

### [Project Name]
- **Context:** [What Vishen requested and where]
- **Status:** [IN PROGRESS/COMPLETED/BLOCKED]
- **Platform:** [WhatsApp Group/Desktop/Terminal/etc]
- **Action Required:** [Next steps]

---

## Memory Gaps to Address
- [ ] [List any missing context]

## System Notes
- **Created:** $(date '+%Y-%m-%d %H:%M GMT')
- **Purpose:** Track work across WhatsApp groups, desktop sessions, and all platforms
- **Auto-cleanup:** Will archive to daily memory and reset every 24h
- **Update trigger:** Significant project completion or new requests
EOF
    echo "Created new cross-session memory file: $CROSS_SESSION_FILE"
fi

# Archive yesterday's file if it exists
if [ -f "$YESTERDAY_FILE" ]; then
    # Append to daily memory
    echo "" >> "$MEMORY_DIR/$YESTERDAY.md"
    echo "## Cross-Session Summary" >> "$MEMORY_DIR/$YESTERDAY.md"
    tail -n +3 "$YESTERDAY_FILE" >> "$MEMORY_DIR/$YESTERDAY.md"
    
    # Remove old cross-session file
    rm "$YESTERDAY_FILE"
    echo "Archived and cleaned up: $YESTERDAY_FILE"
fi

echo "Cross-session memory system ready: $CROSS_SESSION_FILE"