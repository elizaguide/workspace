#!/bin/bash
# Reapply ALL Eliza patches after clawdbot update
#
# Usage:
#   bash ~/clawd/patches/apply-all-patches.sh
#   npx clawdbot gateway restart

set -e
DIR="$(dirname "$0")"

echo "=== Applying Eliza patches ==="
echo ""

# 1. Memory-LanceDB plugin
MEMORY_SRC="$DIR/memory-lancedb-index.ts"
MEMORY_DST="/opt/homebrew/lib/node_modules/clawdbot/extensions/memory-lancedb/index.ts"
if [ -f "$MEMORY_SRC" ] && [ -d "$(dirname "$MEMORY_DST")" ]; then
  BACKUP="$MEMORY_DST.original"
  [ ! -f "$BACKUP" ] && cp "$MEMORY_DST" "$BACKUP"
  cp "$MEMORY_SRC" "$MEMORY_DST"
  echo "[1/2] Memory plugin patched"
  echo "  - Auto-recall: 8 memories, 0.15 threshold"
  echo "  - Auto-capture: 8 per conversation"
  echo "  - Relaxed filters, 19 trigger patterns"
else
  echo "[1/2] SKIPPED: Memory plugin files not found"
fi

echo ""

# 2. TTS pronunciation
TTS_SRC="$DIR/tts.js"
TTS_DST="/opt/homebrew/lib/node_modules/clawdbot/dist/tts/tts.js"
if [ -f "$TTS_SRC" ] && [ -d "$(dirname "$TTS_DST")" ]; then
  BACKUP="$TTS_DST.original"
  [ ! -f "$BACKUP" ] && cp "$TTS_DST" "$BACKUP"
  cp "$TTS_SRC" "$TTS_DST"
  echo "[2/2] TTS pronunciation patched"
  echo "  - Vishen → vishion (correct pronunciation)"
else
  echo "[2/2] SKIPPED: TTS files not found"
fi

echo ""
echo "Done! Now restart the gateway:"
echo "  npx clawdbot gateway restart"
