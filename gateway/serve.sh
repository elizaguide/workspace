#!/bin/bash
# Simple HTTP server for Eliza UI
cd "$(dirname "$0")"
echo "Eliza UI running at: http://localhost:8080"
echo "Press Ctrl+C to stop"
python3 -m http.server 8080
