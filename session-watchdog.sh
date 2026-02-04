#!/bin/bash
# Session Watchdog — auto-recovers Eliza from stuck states
#
# Detects two failure modes:
#
# 1. FORMAT ERRORS — corrupted tool call history in session files
#    causes the agent to reject all new messages permanently.
#    Detection: grep "format error" in gateway.err.log
#
# 2. STUCK RUNS — agent starts processing but never finishes
#    (API timeout, context overflow, mid-run crash). The session
#    stays "active" so new messages queue but never get processed.
#    Detection: session file > 200KB AND not modified in > 15 minutes.
#    The size+staleness combo avoids killing active work (which was
#    the problem with a pure size check).
#
# Runs every 5 minutes via LaunchAgent.

LOG="/Users/vishen/.clawdbot/logs/gateway.err.log"
SESSIONS_DIR="/Users/vishen/.clawdbot/agents/main/sessions"
WATCHDOG_LOG="/Users/vishen/.clawdbot/logs/watchdog.log"
LOCKFILE="/tmp/clawdbot-watchdog.lock"

STALE_THRESHOLD=900    # 15 minutes with no writes = stuck
SIZE_THRESHOLD=204800  # 200KB = substantial conversation in progress

# Prevent concurrent runs
if [ -f "$LOCKFILE" ]; then
  exit 0
fi
touch "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

NEEDS_CLEAR=0
REASON=""

# --- Check 1: Format errors ---
if [ -f "$LOG" ]; then
  RECENT_ERRORS=$(tail -200 "$LOG" 2>/dev/null | grep -c "format error" 2>/dev/null || echo "0")
  if [ "$RECENT_ERRORS" -gt 0 ]; then
    NEEDS_CLEAR=1
    REASON="format error ($RECENT_ERRORS occurrences)"
  fi
fi

# --- Check 2: Stuck runs (large + stale session files) ---
if [ "$NEEDS_CLEAR" -eq 0 ]; then
  NOW=$(date +%s)
  for f in "$SESSIONS_DIR"/*.jsonl; do
    [ -f "$f" ] || continue

    SIZE=$(stat -f%z "$f" 2>/dev/null || echo 0)
    [ "$SIZE" -lt "$SIZE_THRESHOLD" ] && continue

    MTIME=$(stat -f%m "$f" 2>/dev/null || echo 0)
    AGE=$(( NOW - MTIME ))

    if [ "$AGE" -gt "$STALE_THRESHOLD" ]; then
      SIZE_KB=$(( SIZE / 1024 ))
      AGE_MIN=$(( AGE / 60 ))
      NEEDS_CLEAR=1
      REASON="stuck run (${SIZE_KB}KB session stale for ${AGE_MIN}m)"
      break
    fi
  done
fi

# --- Act ---
if [ "$NEEDS_CLEAR" -eq 1 ]; then
  TIMESTAMP=$(date -Iseconds)
  echo "$TIMESTAMP Watchdog: $REASON — clearing sessions" >> "$WATCHDOG_LOG"

  # Clear session files
  rm -f "$SESSIONS_DIR"/*.jsonl 2>/dev/null
  echo '{}' > "$SESSIONS_DIR/sessions.json"

  # Restart gateway
  /opt/homebrew/bin/npx clawdbot gateway restart >> "$WATCHDOG_LOG" 2>&1

  echo "$TIMESTAMP Watchdog: sessions cleared and gateway restarted" >> "$WATCHDOG_LOG"

  # Truncate the error log so we don't re-trigger on stale errors
  [ -f "$LOG" ] && echo "" > "$LOG"
fi
