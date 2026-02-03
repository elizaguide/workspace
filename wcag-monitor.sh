#!/bin/bash
URL="https://elizaguide.github.io/workspace/mindvalley/wcag/"
while true; do
    if curl -s --head "$URL" | head -n 1 | grep -q "200 OK"; then
        echo "WCAG site is LIVE at $(date)!"
        exit 0
    else
        echo "Still waiting... $(date)"
    fi
    sleep 180  # 3 minutes
done
