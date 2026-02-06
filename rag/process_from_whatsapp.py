#!/usr/bin/env python3
"""
WhatsApp Integration Helper

Processes URLs sent via WhatsApp messages into the RAG system.
Automatically detects YouTube vs Newsletter URLs and processes appropriately.

Usage:
    python process_from_whatsapp.py "URL1 URL2 URL3"
    python process_from_whatsapp.py --file message.txt
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


def extract_urls_from_text(text: str) -> list[str]:
    """Extract all URLs from text."""
    url_pattern = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?'
    urls = re.findall(url_pattern, text)
    return urls


def classify_url(url: str) -> str:
    """Classify URL as youtube, newsletter, or unknown."""
    domain = urlparse(url).netloc.lower()
    
    if any(yt in domain for yt in ['youtube.com', 'youtu.be', 'm.youtube.com']):
        return 'youtube'
    elif any(news in domain for news in ['mindvalley.com', 'blog.', 'newsletter', 'substack.com']):
        return 'newsletter'
    else:
        return 'newsletter'  # Default to newsletter scraper


def process_urls(urls: list[str]) -> dict:
    """Process URLs and return results."""
    results = {
        'youtube': {'processed': 0, 'failed': 0, 'urls': []},
        'newsletter': {'processed': 0, 'failed': 0, 'urls': []},
    }
    
    # Group URLs by type
    youtube_urls = []
    newsletter_urls = []
    
    for url in urls:
        url_type = classify_url(url)
        if url_type == 'youtube':
            youtube_urls.append(url)
            results['youtube']['urls'].append(url)
        else:
            newsletter_urls.append(url)
            results['newsletter']['urls'].append(url)
    
    print(f"Found {len(youtube_urls)} YouTube URLs and {len(newsletter_urls)} newsletter URLs")
    print()
    
    # Process YouTube URLs
    if youtube_urls:
        print("🎥 Processing YouTube videos...")
        for i, url in enumerate(youtube_urls, 1):
            print(f"  [{i}/{len(youtube_urls)}] {url}")
            try:
                cmd = [
                    sys.executable, 'youtube_scraper.py', 
                    '--url', url
                ]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                
                if result.returncode == 0:
                    results['youtube']['processed'] += 1
                    print(f"    ✅ Success")
                else:
                    results['youtube']['failed'] += 1
                    print(f"    ❌ Failed: {result.stderr.strip()}")
                    
            except subprocess.TimeoutExpired:
                results['youtube']['failed'] += 1
                print(f"    ⏰ Timeout")
            except Exception as e:
                results['youtube']['failed'] += 1
                print(f"    ❌ Error: {e}")
    
    # Process Newsletter URLs
    if newsletter_urls:
        print("\n📰 Processing newsletters...")
        for i, url in enumerate(newsletter_urls, 1):
            print(f"  [{i}/{len(newsletter_urls)}] {url}")
            try:
                cmd = [
                    sys.executable, 'newsletter_scraper.py', 
                    '--url', url
                ]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                
                if result.returncode == 0:
                    results['newsletter']['processed'] += 1
                    print(f"    ✅ Success")
                else:
                    results['newsletter']['failed'] += 1
                    print(f"    ❌ Failed: {result.stderr.strip()}")
                    
            except subprocess.TimeoutExpired:
                results['newsletter']['failed'] += 1
                print(f"    ⏰ Timeout")
            except Exception as e:
                results['newsletter']['failed'] += 1
                print(f"    ❌ Error: {e}")
    
    return results


def reindex_new_content(results: dict):
    """Reindex the newly processed content."""
    print("\n🔄 Indexing new content...")
    
    index_commands = []
    if results['youtube']['processed'] > 0:
        index_commands.append(['--youtube'])
    if results['newsletter']['processed'] > 0:
        index_commands.append(['--newsletters'])
    
    for cmd_args in index_commands:
        try:
            cmd = [sys.executable, 'enhanced_indexer.py'] + cmd_args
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print(f"  ✅ Indexed {' '.join(cmd_args)} content")
            else:
                print(f"  ❌ Indexing failed for {' '.join(cmd_args)}: {result.stderr.strip()}")
                
        except Exception as e:
            print(f"  ❌ Indexing error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Process URLs from WhatsApp into RAG")
    parser.add_argument("urls", nargs="?", help="Space-separated URLs or text containing URLs")
    parser.add_argument("--file", help="File containing URLs or text")
    parser.add_argument("--no-index", action="store_true", help="Don't automatically index after processing")
    
    args = parser.parse_args()
    
    # Get text content
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text_content = f.read()
    elif args.urls:
        text_content = args.urls
    else:
        # Read from stdin
        text_content = sys.stdin.read()
    
    if not text_content.strip():
        print("No content provided. Usage:")
        print("  python process_from_whatsapp.py 'https://youtube.com/watch?v=... https://blog.mindvalley.com/...'")
        print("  python process_from_whatsapp.py --file urls.txt")
        print("  echo 'URLs here' | python process_from_whatsapp.py")
        return
    
    # Extract URLs
    urls = extract_urls_from_text(text_content)
    if not urls:
        print("No URLs found in the provided text.")
        return
    
    print(f"Extracted {len(urls)} URLs:")
    for url in urls:
        print(f"  - {url}")
    print()
    
    # Process URLs
    results = process_urls(urls)
    
    # Summary
    total_processed = results['youtube']['processed'] + results['newsletter']['processed']
    total_failed = results['youtube']['failed'] + results['newsletter']['failed']
    
    print(f"\n📊 Summary:")
    print(f"  YouTube:    {results['youtube']['processed']} processed, {results['youtube']['failed']} failed")
    print(f"  Newsletter: {results['newsletter']['processed']} processed, {results['newsletter']['failed']} failed")
    print(f"  Total:      {total_processed} processed, {total_failed} failed")
    
    # Auto-index if content was processed
    if total_processed > 0 and not args.no_index:
        reindex_new_content(results)
        print(f"\n🎉 Successfully added {total_processed} new items to your RAG system!")
    elif total_processed > 0:
        print(f"\n✅ Processing complete. Run indexing manually:")
        if results['youtube']['processed'] > 0:
            print(f"  python enhanced_indexer.py --youtube")
        if results['newsletter']['processed'] > 0:
            print(f"  python enhanced_indexer.py --newsletters")


if __name__ == "__main__":
    main()