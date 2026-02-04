#!/bin/bash
# Quick deployment script
cd www/ai-accelerator
echo "Starting deployment..."

# Try using a simple upload service
curl -F "file=@ai-accelerator-sales-page.html" -F "expires=24h" https://file.io/ || echo "Upload failed"