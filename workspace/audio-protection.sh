#!/bin/bash

# Audio Protection Script for Presentations
# Protects presentation audio files from automatic cleanup for 1 month

# Set the base directory for presentation audio files
AUDIO_BASE_DIR="$HOME/clawd/audio"

# Find and protect all presentation audio files less than 30 days old
if [ -d "$AUDIO_BASE_DIR" ]; then
    # Find all mp3 files in presentation directories modified in the last 30 days
    find "$AUDIO_BASE_DIR" -name "*.mp3" -path "*/presentation*" -mtime -30 -type f | while read -r file; do
        # Set file attributes to protect from deletion
        chflags uchg "$file" 2>/dev/null || true
        echo "Protected: $file"
    done
    
    # Also protect any files in executive-presentation or similar directories
    find "$AUDIO_BASE_DIR" -name "*.mp3" -path "*executive*" -mtime -30 -type f | while read -r file; do
        chflags uchg "$file" 2>/dev/null || true
        echo "Protected: $file"
    done
fi

# Unprotect files older than 30 days
find "$AUDIO_BASE_DIR" -name "*.mp3" -path "*/presentation*" -mtime +30 -type f | while read -r file; do
    chflags nouchg "$file" 2>/dev/null || true
    echo "Unprotected (30+ days old): $file"
done

echo "Audio protection script completed at $(date)"