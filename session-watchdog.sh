#!/bin/bash
# Session Watchdog — auto-clears corrupted/stuck sessions
#
# Checks for two failure modes:
#   1. "format error" in gateway error log (corrupted tool call history)
#   2. Session files > 500KB (bloated sessions that cause silent failures)
#
# Runs every 5 minutes via LaunchAgent.

LOG="/Users/vishen/.clawdbot/logs/gateway.err.log"
SESSIONS_DIR="/Users/vishen/.clawdbot/agents/main/sessions"
WATCHDOG_LOG="/Users/vishen/.clawdbot/logs/watchdog.log"
LOCKFILE="/tmp/clawdbot-watchdog.lock"
MAX_SESSION_KB=500

# Prevent concurrent runs
if [ -f "$LOCKFILE" ]; then
  exit 0
fi
touch "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

NEEDS_RESET=0
REASON=""

# Check 1: format errors in error log
if [ -f "$LOG" ]; then
  RECENT_ERRORS=$(tail -200 "$LOG" 2>/dev/null | grep -c "format error" 2>/dev/null || echo "0")
  if [ "$RECENT_ERRORS" -gt 0 ]; then
    NEEDS_RESET=1
    REASON="format error ($RECENT_ERRORS occurrences)"
  fi
fi

# Check 2: any session file over 500KB (bloated = about to break)
if [ "$NEEDS_RESET" -eq 0 ]; then
  LARGE_FILES=$(find "$SESSIONS_DIR" -name "*.jsonl" -size +${MAX_SESSION_KB}k 2>/dev/null | wc -l | tr -d ' ')
  if [ "$LARGE_FILES" -gt 0 ]; then
    NEEDS_RESET=1
    REASON="$LARGE_FILES session files over ${MAX_SESSION_KB}KB"
  fi
fi

if [ "$NEEDS_RESET" -eq 1 ]; then
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
