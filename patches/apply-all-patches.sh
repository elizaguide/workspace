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
  echo "[1/3] Memory plugin patched"
  echo "  - Auto-recall: 8 memories, 0.15 threshold"
  echo "  - Auto-capture: 8 per conversation"
  echo "  - Relaxed filters, 19 trigger patterns"
else
  echo "[1/3] SKIPPED: Memory plugin files not found"
fi

echo ""

# 2. TTS pronunciation
TTS_SRC="$DIR/tts.js"
TTS_DST="/opt/homebrew/lib/node_modules/clawdbot/dist/tts/tts.js"
if [ -f "$TTS_SRC" ] && [ -d "$(dirname "$TTS_DST")" ]; then
  BACKUP="$TTS_DST.original"
  [ ! -f "$BACKUP" ] && cp "$TTS_DST" "$BACKUP"
  cp "$TTS_SRC" "$TTS_DST"
  echo "[2/3] TTS pronunciation patched"
  echo "  - Vishen → vishion (correct pronunciation)"
else
  echo "[2/3] SKIPPED: TTS files not found"
fi

echo ""

# 3. Model Router (auto Ollama ↔ Sonnet)
ROUTER_SRC="$DIR/model-router.js"
REPLY_DST="/opt/homebrew/lib/node_modules/clawdbot/dist/auto-reply/reply/get-reply.js"
if [ -f "$ROUTER_SRC" ] && [ -f "$REPLY_DST" ]; then
  BACKUP="$REPLY_DST.original"
  [ ! -f "$BACKUP" ] && cp "$REPLY_DST" "$BACKUP"
  # Check if already patched
  if grep -q "Model Router" "$REPLY_DST" 2>/dev/null; then
    echo "[3/3] Model Router already patched"
  else
    # Insert router block after applyResetModelOverride closing brace
    sed -i '' '/^    });$/,/^    const directiveResult = await resolveReplyDirectives({$/{
      /^    const directiveResult = await resolveReplyDirectives({$/i\
\    // --- Model Router: auto-classify simple vs complex ---\
\    try {\
\        const { classifyComplexity } = await import("/Users/vishen/clawd/patches/model-router.js");\
\        const routed = classifyComplexity(triggerBodyNormalized);\
\        if (routed?.provider \&\& routed?.model) {\
\            sessionEntry.providerOverride = routed.provider;\
\            sessionEntry.modelOverride = routed.model;\
\        }\
\    } catch (_routerErr) { /* router missing or broken — use default */ }\
\    // --- End Model Router ---
    }' "$REPLY_DST"
    echo "[3/3] Model Router patched"
  fi
  echo "  - Simple messages → ollama/llama3.1:8b"
  echo "  - Complex messages → anthropic/claude-sonnet-4-0"
else
  echo "[3/3] SKIPPED: Model Router files not found"
fi

echo ""
echo "Done! Now restart the gateway:"
echo "  npx clawdbot gateway restart"
