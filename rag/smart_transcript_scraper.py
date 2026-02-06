#!/usr/bin/env python3
"""
Smart Transcript Scraper - Gets transcripts efficiently without video downloads

For YouTube: Uses auto-generated captions via youtube-transcript-api
For Dropbox: First tries to find the video on YouTube, then falls back to download if needed

Usage:
    python smart_transcript_scraper.py --url "https://youtube.com/watch?v=..."
    python smart_transcript_scraper.py --batch urls.txt --reindex
"""

import argparse
import re
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Import YouTube transcript libraries
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    TRANSCRIPT_API_AVAILABLE = True
except ImportError:
    TRANSCRIPT_API_AVAILABLE = False
    print("Error: youtube-transcript-api not installed. Install with: pip install youtube-transcript-api")

try:
    import yt_dlp
    YT_DLP_AVAILABLE = True
except ImportError:
    YT_DLP_AVAILABLE = False
    print("Warning: yt-dlp not available for metadata extraction")


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


def get_youtube_metadata(video_id: str) -> dict:
    """Get basic video metadata from YouTube."""
    if not YT_DLP_AVAILABLE:
        return {"title": f"Video-{video_id}", "description": "", "uploader": ""}
    
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f'https://youtube.com/watch?v={video_id}', download=False)
            return {
                'title': info.get('title', f'Video-{video_id}'),
                'description': info.get('description', ''),
                'upload_date': info.get('upload_date', ''),
                'uploader': info.get('uploader', ''),
                'duration': info.get('duration', 0),
                'view_count': info.get('view_count', 0),
            }
    except Exception as e:
        print(f"Warning: Could not get metadata for {video_id}: {e}")
        return {"title": f"Video-{video_id}", "description": "", "uploader": ""}


def get_youtube_transcript(video_id: str) -> str:
    """Get transcript using YouTube's auto-generated captions."""
    if not TRANSCRIPT_API_AVAILABLE:
        return ""
    
    try:
        # Create API instance and fetch transcript
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=['en', 'en-US'])
        
        # Get raw data and format as text
        transcript_data = transcript.to_raw_data()
        
        full_text = ""
        for entry in transcript_data:
            text = entry['text'].replace('\n', ' ').strip()
            if text and not text.startswith('['):  # Skip [Music] type annotations
                full_text += text + " "
        
        return full_text.strip()
        
    except Exception as e:
        print(f"No transcript available for {video_id}: {e}")
        return ""


def extract_title_from_dropbox_url(url: str) -> str:
    """Extract meaningful title from Dropbox URL."""
    try:
        # Try different patterns to extract filename
        patterns = [
            r'/([^/]+\.mp4)\?',  # Direct filename pattern
            r'/([^/]+\.mov)\?',  # Direct filename pattern  
            r'preview=([^&]+)',  # Preview parameter
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                title = match.group(1)
                import urllib.parse
                title = urllib.parse.unquote(title)
                # Clean up the title
                title = re.sub(r'\.(mov|mp4|avi|mkv)$', '', title, re.IGNORECASE)
                title = re.sub(r'[+_-]', ' ', title)
                title = re.sub(r'DAY\s*\d+\s*[-\s]*', '', title)  # Remove "DAY 11 -" type prefixes
                return title.strip()
    except:
        pass
    
    return f"Dropbox Video {datetime.now().strftime('%Y%m%d_%H%M%S')}"


def search_youtube_for_title(title: str) -> str:
    """Try to find the video on YouTube by searching for the title."""
    if not YT_DLP_AVAILABLE:
        return ""
    
    # Clean up title for search
    search_query = re.sub(r'[^\w\s-]', '', title.lower())
    search_query = re.sub(r'\s+', ' ', search_query).strip()
    
    # Add common keywords that might help
    if 'vishen' not in search_query.lower():
        search_query += " vishen"
    
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(
                f"ytsearch3:{search_query}",
                download=False
            )
            
            if search_results and 'entries' in search_results:
                for entry in search_results['entries']:
                    if entry and entry.get('id'):
                        # Basic similarity check
                        entry_title = entry.get('title', '').lower()
                        original_words = set(search_query.lower().split())
                        entry_words = set(entry_title.split())
                        
                        # If at least 2 important words match, consider it
                        common_words = original_words.intersection(entry_words)
                        if len(common_words) >= 2:
                            print(f"Found potential YouTube match: {entry_title}")
                            return entry['id']
        
    except Exception as e:
        print(f"YouTube search failed: {e}")
    
    return ""


def save_transcript(title: str, source_url: str, transcript: str, output_dir: str, source_type: str = "unknown") -> str:
    """Save transcript as .txt file."""
    if not transcript:
        return ""
    
    # Clean title for filename
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')[:50]
    
    if source_type == "youtube":
        filename = f"youtube-{safe_title}.txt"
    elif source_type == "dropbox":
        filename = f"dropbox-{safe_title}.txt"
    else:
        filename = f"{safe_title}.txt"
    
    filepath = Path(output_dir) / filename
    
    # Format content
    content = f"""Title: {title}
Source: {source_type.title()} Transcript
URL: {source_url}
Date Scraped: {datetime.now().isoformat()}
Method: Auto-generated captions

---

Transcript:
{transcript}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(filepath)


def process_youtube_url(url: str, output_dir: str) -> bool:
    """Process a YouTube video URL."""
    video_id = extract_video_id(url)
    if not video_id:
        print(f"Could not extract video ID from: {url}")
        return False
    
    print(f"Processing YouTube video: {video_id}")
    
    # Get metadata
    metadata = get_youtube_metadata(video_id)
    title = metadata.get('title', video_id)
    print(f"  Title: {title}")
    
    # Check if already processed
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')[:50]
    existing_files = list(Path(output_dir).glob(f"youtube-{safe_title}.txt"))
    if existing_files:
        print(f"  Already processed: {existing_files[0]}")
        return True
    
    # Get transcript
    transcript = get_youtube_transcript(video_id)
    
    if transcript:
        filepath = save_transcript(title, url, transcript, output_dir, "youtube")
        print(f"  Saved: {filepath}")
        print(f"  Length: {len(transcript)} characters")
        return True
    else:
        print(f"  No transcript available")
        return False


def process_dropbox_url(url: str, output_dir: str) -> bool:
    """Process a Dropbox video URL by first trying to find it on YouTube."""
    print(f"Processing Dropbox video: {url}")
    
    title = extract_title_from_dropbox_url(url)
    print(f"  Title: {title}")
    
    # Check if already processed
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')[:50]
    existing_files = list(Path(output_dir).glob(f"dropbox-{safe_title}.txt"))
    if existing_files:
        print(f"  Already processed: {existing_files[0]}")
        return True
    
    # Try to find on YouTube first
    print(f"  Searching YouTube for: {title}")
    youtube_video_id = search_youtube_for_title(title)
    
    if youtube_video_id:
        print(f"  Found on YouTube: {youtube_video_id}")
        transcript = get_youtube_transcript(youtube_video_id)
        if transcript:
            filepath = save_transcript(title, url, transcript, output_dir, "dropbox")
            print(f"  Saved from YouTube: {filepath}")
            print(f"  Length: {len(transcript)} characters")
            return True
    
    print(f"  Not found on YouTube or no transcript available")
    print(f"  Note: Would need to download and process manually")
    return False


def process_url(url: str, output_dir: str) -> bool:
    """Process any supported URL type."""
    if 'youtube.com' in url or 'youtu.be' in url:
        return process_youtube_url(url, output_dir)
    elif 'dropbox.com' in url:
        return process_dropbox_url(url, output_dir)
    else:
        print(f"Unsupported URL type: {url}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Smart transcript scraper")
    parser.add_argument("--url", help="Single video URL")
    parser.add_argument("--batch", help="Text file with video URLs")
    parser.add_argument("--output-dir", 
                        default="/Users/vishen/clawd/transcripts",
                        help="Output directory")
    parser.add_argument("--reindex", action="store_true",
                        help="Re-index RAG after processing")
    
    args = parser.parse_args()
    
    if not TRANSCRIPT_API_AVAILABLE:
        print("Error: youtube-transcript-api is required")
        return
    
    # Create output directory
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    
    urls_to_process = []
    
    if args.url:
        urls_to_process = [args.url]
    elif args.batch:
        with open(args.batch, 'r') as f:
            urls_to_process = [line.strip() for line in f 
                               if line.strip() and not line.startswith('#')]
    else:
        parser.print_help()
        return
    
    # Process URLs
    successful = 0
    for i, video_url in enumerate(urls_to_process, 1):
        print(f"\n[{i}/{len(urls_to_process)}]")
        if process_url(video_url, args.output_dir):
            successful += 1
    
    print(f"\nCompleted: {successful}/{len(urls_to_process)} videos processed successfully")
    
    # Re-index RAG if requested
    if args.reindex and successful > 0:
        print("\nRe-indexing RAG system...")
        try:
            import subprocess
            rag_dir = Path(__file__).parent
            subprocess.run([
                str(rag_dir / '.venv' / 'bin' / 'python3'),
                str(rag_dir / 'mv_index.py')
            ], check=True)
            print("RAG re-indexing completed!")
        except subprocess.CalledProcessError as e:
            print(f"RAG re-indexing failed: {e}")


if __name__ == "__main__":
    main()