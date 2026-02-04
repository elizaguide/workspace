#!/bin/bash

# Quick Cross-Session Memory Update Helper
# Usage: ./update-cross-session.sh "Project Name" "Context" "Status" "Platform" "Action Required"

if [ $# -lt 3 ]; then
    echo "Usage: $0 \"Project Name\" \"Context\" \"Status\" [Platform] [Action Required]"
    echo "Example: $0 \"Executive Presentation\" \"Vishen requested slide deck for tomorrow\" \"IN PROGRESS\" \"Desktop\" \"Get current slides\""
    exit 1
fi

PROJECT_NAME="$1"
CONTEXT="$2"
STATUS="$3"
PLATFORM="${4:-Unknown}"
ACTION="${5:-None specified}"

TODAY=$(date +%Y-%m-%d)
CROSS_SESSION_FILE="memory/cross-session-$TODAY.md"

# Check if project already exists in file
if grep -q "### $PROJECT_NAME" "$CROSS_SESSION_FILE" 2>/dev/null; then
    echo "Project '$PROJECT_NAME' already exists in cross-session memory. Please update manually or use a different name."
    exit 1
fi

# Add new project entry
cat >> "$CROSS_SESSION_FILE" << EOF

### $PROJECT_NAME
- **Context:** $CONTEXT
- **Status:** $STATUS
- **Platform:** $PLATFORM
- **Action Required:** $ACTION
- **Updated:** $(date '+%Y-%m-%d %H:%M GMT')
EOF

echo "Added '$PROJECT_NAME' to cross-session memory"
echo "File: $CROSS_SESSION_FILE"