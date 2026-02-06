#!/usr/bin/env python3
"""
Dropbox Video Transcript Scraper for Mindvalley RAG

Downloads videos from Dropbox and extracts transcripts using Whisper.
Integrates with the existing RAG system.

Usage:
    python dropbox_video_scraper.py --url "https://dropbox.com/..." 
    python dropbox_video_scraper.py --batch urls.txt
"""

import argparse
import os
import re
import subprocess
import tempfile
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Import required libraries
try:
    import yt_dlp
    YT_DLP_AVAILABLE = True
except ImportError:
    YT_DLP_AVAILABLE = False
    print("Error: yt-dlp is required. Install with: pip install yt-dlp")

try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("Warning: whisper not installed. Install with: pip install openai-whisper")


def extract_title_from_url(url: str) -> str:
    """Extract a meaningful title from the Dropbox URL."""
    try:
        # Look for preview parameter
        if 'preview=' in url:
            preview = url.split('preview=')[1].split('&')[0]
            # URL decode and clean up
            import urllib.parse
            title = urllib.parse.unquote(preview)
            # Remove file extension
            title = re.sub(r'\.(mov|mp4|avi|mkv)$', '', title, re.IGNORECASE)
            # Clean up special chars
            title = re.sub(r'[+_-]', ' ', title)
            return title.strip()
    except:
        pass
    
    # Fallback to generic title
    return f"Dropbox Video {datetime.now().strftime('%Y%m%d_%H%M%S')}"


def convert_dropbox_url(url: str) -> str:
    """Convert Dropbox preview/share URL to direct download URL."""
    if 'dropbox.com' not in url:
        return url
    
    # Convert different Dropbox URL formats to direct download
    if '?dl=0' in url:
        return url.replace('?dl=0', '?dl=1')
    elif '&dl=0' in url:
        return url.replace('&dl=0', '&dl=1')
    else:
        # Add download parameter
        separator = '&' if '?' in url else '?'
        return f"{url}{separator}dl=1"


def download_video(url: str, temp_dir: str) -> str:
    """Download video from Dropbox URL."""
    if not YT_DLP_AVAILABLE:
        print("yt-dlp not available, trying direct download...")
        return download_video_direct(url, temp_dir)
    
    output_template = os.path.join(temp_dir, '%(title)s.%(ext)s')
    
    ydl_opts = {
        'outtmpl': output_template,
        'format': 'best[ext=mp4]/best',  # Prefer mp4
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
            # Find the downloaded file
            for file in os.listdir(temp_dir):
                if file.endswith(('.mp4', '.mov', '.avi', '.mkv')):
                    return os.path.join(temp_dir, file)
                    
    except Exception as e:
        print(f"yt-dlp failed: {e}")
        print("Trying direct download...")
        return download_video_direct(url, temp_dir)
    
    return ""


def download_video_direct(url: str, temp_dir: str) -> str:
    """Direct download from Dropbox using curl."""
    direct_url = convert_dropbox_url(url)
    title = extract_title_from_url(url)
    
    # Determine file extension from URL
    ext = '.mp4'  # default
    if '.mov' in url.lower():
        ext = '.mov'
    elif '.avi' in url.lower():
        ext = '.avi'
    
    output_path = os.path.join(temp_dir, f"{title}{ext}")
    
    try:
        print(f"Downloading: {title}")
        cmd = ['curl', '-L', '-o', output_path, direct_url]
        result = subprocess.run(cmd, check=True, capture_output=True)
        
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            return output_path
        else:
            print("Download failed - file is empty or doesn't exist")
            return ""
            
    except subprocess.CalledProcessError as e:
        print(f"Download failed: {e}")
        return ""


def transcribe_audio(video_path: str, model_size: str = "base") -> str:
    """Transcribe video using Whisper."""
    if not WHISPER_AVAILABLE:
        print("Whisper not available - cannot transcribe")
        return ""
    
    try:
        print(f"Loading Whisper model: {model_size}")
        model = whisper.load_model(model_size)
        
        print("Transcribing audio...")
        result = model.transcribe(video_path)
        
        return result["text"]
        
    except Exception as e:
        print(f"Transcription failed: {e}")
        return ""


def save_transcript(title: str, url: str, transcript: str, output_dir: str) -> str:
    """Save transcript as .txt file in RAG format."""
    if not transcript:
        return ""
    
    # Clean title for filename
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')[:50]
    
    filename = f"dropbox-{safe_title}.txt"
    filepath = Path(output_dir) / filename
    
    # Format with metadata
    content = f"""Title: {title}
Source: Dropbox Video
URL: {url}
Date Scraped: {datetime.now().isoformat()}
Transcription: OpenAI Whisper

---

Transcript:
{transcript}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(filepath)


def process_video(url: str, output_dir: str, whisper_model: str = "base") -> bool:
    """Process a single Dropbox video."""
    print(f"\nProcessing: {url}")
    
    title = extract_title_from_url(url)
    print(f"Title: {title}")
    
    # Check if already processed
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')[:50]
    existing_files = list(Path(output_dir).glob(f"dropbox-{safe_title}.txt"))
    if existing_files:
        print(f"Already processed: {existing_files[0]}")
        return True
    
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Download video
        video_path = download_video(url, temp_dir)
        if not video_path:
            print("Download failed")
            return False
        
        print(f"Downloaded: {os.path.basename(video_path)}")
        print(f"File size: {os.path.getsize(video_path) / (1024*1024):.1f} MB")
        
        # Transcribe
        transcript = transcribe_audio(video_path, whisper_model)
        if not transcript:
            print("Transcription failed")
            return False
        
        print(f"Transcript length: {len(transcript)} characters")
        
        # Save
        filepath = save_transcript(title, url, transcript, output_dir)
        print(f"Saved: {filepath}")
        
        return True


def main():
    parser = argparse.ArgumentParser(description="Scrape Dropbox video transcripts for RAG")
    parser.add_argument("--url", help="Single Dropbox video URL")
    parser.add_argument("--batch", help="Text file with video URLs")
    parser.add_argument("--output-dir", 
                        default="/Users/vishen/clawd/transcripts",
                        help="Output directory")
    parser.add_argument("--whisper-model", default="base",
                        choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model size (larger = better accuracy)")
    parser.add_argument("--reindex", action="store_true",
                        help="Re-index RAG after processing")
    
    args = parser.parse_args()
    
    if not (YT_DLP_AVAILABLE or WHISPER_AVAILABLE):
        print("Missing dependencies. Install with:")
        print("pip install yt-dlp openai-whisper")
        return
    
    # Create output directory
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    
    videos_to_process = []
    
    if args.url:
        videos_to_process = [args.url]
    elif args.batch:
        with open(args.batch, 'r') as f:
            videos_to_process = [line.strip() for line in f 
                               if line.strip() and not line.startswith('#')]
    else:
        parser.print_help()
        return
    
    # Process videos
    successful = 0
    for i, video_url in enumerate(videos_to_process, 1):
        print(f"\n[{i}/{len(videos_to_process)}]")
        if process_video(video_url, args.output_dir, args.whisper_model):
            successful += 1
    
    print(f"\nCompleted: {successful}/{len(videos_to_process)} videos processed successfully")
    
    # Re-index RAG if requested
    if args.reindex and successful > 0:
        print("\nRe-indexing RAG system...")
        try:
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