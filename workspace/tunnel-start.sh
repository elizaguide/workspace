#!/bin/bash
# Cloudflared quick tunnel for Eliza's web publishing
# Proxies https://*.trycloudflare.com → http://127.0.0.1:18850
#
# The assigned URL is written to ~/.clawdbot/tunnel-url.txt
# so Eliza can read it and share links.

URL_FILE="$HOME/.clawdbot/tunnel-url.txt"
LOG_FILE="$HOME/.clawdbot/logs/tunnel.log"

# Start cloudflared, tee output to log, and capture the URL
/opt/homebrew/bin/cloudflared tunnel --url http://127.0.0.1:18850 --no-autoupdate 2>&1 | while IFS= read -r line; do
  echo "$line" >> "$LOG_FILE"
  # Extract the trycloudflare URL when it appears
  if echo "$line" | grep -qo 'https://[a-z0-9-]*\.trycloudflare\.com'; then
    URL=$(echo "$line" | grep -o 'https://[a-z0-9-]*\.trycloudflare\.com')
    echo "$URL" > "$URL_FILE"
    echo "$(date -Iseconds) Tunnel URL: $URL" >> "$LOG_FILE"
  fi
done
