#!/usr/bin/env python3
"""
YouTube Transcript Scraper for Mindvalley RAG

Extracts transcripts from YouTube videos using yt-dlp and 
whisper (or YouTube's auto-generated captions when available).

Usage:
    python youtube_scraper.py --url "https://youtube.com/watch?v=..."
    python youtube_scraper.py --channel "@vishenlakhiani" --limit 50
    python youtube_scraper.py --batch urls.txt
"""

import argparse
import json
import os
import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

# Import YouTube transcript libraries
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api.formatters import TextFormatter
    TRANSCRIPT_API_AVAILABLE = True
except ImportError:
    TRANSCRIPT_API_AVAILABLE = False
    print("Warning: youtube-transcript-api not installed. Will use yt-dlp fallback.")

try:
    import yt_dlp
    YT_DLP_AVAILABLE = True
except ImportError:
    YT_DLP_AVAILABLE = False
    print("Error: yt-dlp is required. Install with: pip install yt-dlp")


def extract_video_id(url: str) -> str:
    """Extract video ID from various YouTube URL formats."""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'(?:watch\?v=)([0-9A-Za-z_-]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return ""


def get_video_metadata(video_id: str) -> dict:
    """Get video metadata using yt-dlp."""
    if not YT_DLP_AVAILABLE:
        return {}
    
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f'https://youtube.com/watch?v={video_id}', download=False)
            return {
                'title': info.get('title', ''),
                'description': info.get('description', ''),
                'upload_date': info.get('upload_date', ''),
                'uploader': info.get('uploader', ''),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
            }
    except Exception as e:
        print(f"Error getting metadata: {e}")
        return {}


def get_transcript_youtube_api(video_id: str) -> str:
    """Get transcript using YouTube Transcript API."""
    if not TRANSCRIPT_API_AVAILABLE:
        return ""
    
    try:
        # Create API instance and fetch transcript
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=['en'])
        
        # Get raw data and format as text
        transcript_data = transcript.to_raw_data()
        
        full_text = ""
        for entry in transcript_data:
            text = entry['text'].replace('\n', ' ').strip()
            if text:
                full_text += text + " "
        
        return full_text.strip()
        
    except Exception as e:
        print(f"Transcript not available for {video_id}: {e}")
        return ""


def get_channel_videos(channel_url: str, limit: int = 50) -> list[str]:
    """Get video URLs from a YouTube channel."""
    if not YT_DLP_AVAILABLE:
        return []
    
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
        'playlist_items': f'1:{limit}',  # Changed format
    }
    
    video_urls = []
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(channel_url, download=False)
            
            if 'entries' in info:
                for entry in info['entries']:
                    if entry and entry.get('id'):
                        video_urls.append(f"https://youtube.com/watch?v={entry['id']}")
            elif info.get('id'):  # Single video case
                video_urls.append(f"https://youtube.com/watch?v={info['id']}")
            
    except Exception as e:
        print(f"Error extracting channel videos: {e}")
    
    return video_urls


def save_transcript(video_id: str, metadata: dict, transcript: str, output_dir: str) -> str:
    """Save transcript as .txt file."""
    if not transcript:
        return ""
    
    title = metadata.get('title', f'Video-{video_id}')
    # Clean title for filename
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')[:50]
    
    filename = f"{video_id}-{safe_title}.txt"
    filepath = Path(output_dir) / filename
    
    # Format with metadata
    upload_date = metadata.get('upload_date', '')
    if upload_date:
        try:
            upload_date = datetime.strptime(upload_date, '%Y%m%d').strftime('%Y-%m-%d')
        except:
            pass
    
    content = f"""Title: {title}
Video ID: {video_id}
URL: https://youtube.com/watch?v={video_id}
Upload Date: {upload_date}
Uploader: {metadata.get('uploader', '')}
Duration: {metadata.get('duration', 0)} seconds
Views: {metadata.get('view_count', 0)}
Date Scraped: {datetime.now().isoformat()}
Source: YouTube

---

Description:
{metadata.get('description', '')[:500]}

---

Transcript:
{transcript}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(filepath)


def process_video(url: str, output_dir: str) -> bool:
    """Process a single YouTube video."""
    video_id = extract_video_id(url)
    if not video_id:
        print(f"Could not extract video ID from: {url}")
        return False
    
    print(f"Processing video: {video_id}")
    
    # Get metadata
    metadata = get_video_metadata(video_id)
    title = metadata.get('title', video_id)
    print(f"  Title: {title}")
    
    # Check if already processed
    existing_files = list(Path(output_dir).glob(f"{video_id}-*.txt"))
    if existing_files:
        print(f"  Already processed: {existing_files[0]}")
        return True
    
    # Get transcript
    transcript = get_transcript_youtube_api(video_id)
    
    if transcript:
        filepath = save_transcript(video_id, metadata, transcript, output_dir)
        print(f"  Saved: {filepath}")
        return True
    else:
        print(f"  No transcript available")
        return False


def main():
    parser = argparse.ArgumentParser(description="Scrape YouTube transcripts for RAG")
    parser.add_argument("--url", help="Single YouTube video URL")
    parser.add_argument("--channel", help="YouTube channel URL or @handle")
    parser.add_argument("--limit", type=int, default=50, 
                        help="Max videos from channel (default: 50)")
    parser.add_argument("--batch", help="Text file with video URLs")
    parser.add_argument("--output-dir", 
                        default="/Users/vishen/clawd/transcripts/youtube",
                        help="Output directory")
    
    args = parser.parse_args()
    
    if not (TRANSCRIPT_API_AVAILABLE and YT_DLP_AVAILABLE):
        print("Missing dependencies. Install with:")
        print("pip install yt-dlp youtube-transcript-api")
        return
    
    # Create output directory
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    
    videos_to_process = []
    
    if args.url:
        videos_to_process = [args.url]
    elif args.channel:
        print(f"Getting videos from channel: {args.channel}")
        channel_url = args.channel if args.channel.startswith('http') else f"https://youtube.com/{args.channel}"
        videos_to_process = get_channel_videos(channel_url, args.limit)
        print(f"Found {len(videos_to_process)} videos")
    elif args.batch:
        with open(args.batch, 'r') as f:
            videos_to_process = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    else:
        parser.print_help()
        return
    
    # Process videos
    successful = 0
    for i, video_url in enumerate(videos_to_process, 1):
        print(f"\n[{i}/{len(videos_to_process)}]")
        if process_video(video_url, args.output_dir):
            successful += 1
    
    print(f"\nCompleted: {successful}/{len(videos_to_process)} videos processed successfully")


if __name__ == "__main__":
    main()