#!/bin/bash
# Reapply Eliza memory-lancedb patches after clawdbot update
#
# What this patches (vs upstream defaults):
#   - Auto-recall: 3 → 8 memories per query, threshold 0.3 → 0.15
#   - Auto-capture: 3 → 8 memories per conversation
#   - shouldCapture max text: 500 → 1000 chars
#   - Emoji filter: >3 → >8 (Eliza uses emojis naturally)
#   - Removed markdown filter that was blocking Eliza's formatted output
#   - Added 10 new trigger patterns (project, family, health, learning, feedback)
#
# Usage:
#   bash ~/clawd/patches/apply-memory-patches.sh
#
# After running, restart the gateway:
#   npx clawdbot gateway restart

set -e

PLUGIN_DIR="/opt/homebrew/lib/node_modules/clawdbot/extensions/memory-lancedb"
PATCH_SOURCE="$(dirname "$0")/memory-lancedb-index.ts"
TARGET="$PLUGIN_DIR/index.ts"

if [ ! -f "$PATCH_SOURCE" ]; then
  echo "ERROR: Patch source not found: $PATCH_SOURCE"
  exit 1
fi

if [ ! -d "$PLUGIN_DIR" ]; then
  echo "ERROR: Plugin directory not found: $PLUGIN_DIR"
  echo "Is clawdbot installed at /opt/homebrew?"
  exit 1
fi

# Backup original before overwriting
BACKUP="$PLUGIN_DIR/index.ts.original"
if [ ! -f "$BACKUP" ]; then
  cp "$TARGET" "$BACKUP"
  echo "Backed up original to: $BACKUP"
fi

# Apply patch
cp "$PATCH_SOURCE" "$TARGET"
echo "Patched: $TARGET"
echo ""
echo "Changes applied:"
echo "  - Auto-recall: 8 memories, 0.15 threshold"
echo "  - Auto-capture: 8 per conversation"
echo "  - Text length: 10-1000 chars (was 10-500)"
echo "  - Emoji threshold: >8 (was >3)"
echo "  - Markdown filter: removed"
echo "  - Triggers: 19 patterns (was 9)"
echo ""
echo "Now restart the gateway:"
echo "  npx clawdbot gateway restart"
