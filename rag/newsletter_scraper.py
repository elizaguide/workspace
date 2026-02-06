#!/usr/bin/env python3
"""
Newsletter Scraper for Mindvalley RAG

Scrapes newsletters from web links and converts them to 
the same .txt format used by the RAG system.

Usage:
    python newsletter_scraper.py --url "https://..." --title "Newsletter Title"
    python newsletter_scraper.py --batch urls.txt  # process multiple URLs from file
"""

import argparse
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    """Clean and normalize extracted text."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove weird characters
    text = re.sub(r'[^\w\s\.\,\;\:\!\?\-\'\"\(\)\[\]\/\@\#\$\%\&\*\+\=]', '', text)
    return text.strip()


def extract_newsletter_content(url: str) -> tuple[str, str]:
    """
    Extract newsletter content from URL.
    Returns (title, content) tuple.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Try to get title
        title = ""
        if soup.title:
            title = soup.title.string.strip()
        
        # Extract main content
        # Try common newsletter container selectors
        content_selectors = [
            'article', 
            '.newsletter-content',
            '.email-content', 
            '.main-content',
            '.post-content',
            '[role="main"]',
            'main'
        ]
        
        content = ""
        for selector in content_selectors:
            container = soup.select_one(selector)
            if container:
                content = container.get_text(separator='\n', strip=True)
                break
        
        # Fallback: extract from body if no container found
        if not content:
            content = soup.body.get_text(separator='\n', strip=True) if soup.body else ""
        
        # Clean up the content
        content = clean_text(content)
        
        return title, content
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "", ""


def save_newsletter(title: str, content: str, url: str, output_dir: str) -> str:
    """Save newsletter as .txt file in transcripts format."""
    if not content:
        return ""
    
    # Create safe filename
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')
    
    # Add date prefix
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{safe_title[:50]}.txt"
    
    filepath = Path(output_dir) / filename
    
    # Format content with metadata header
    formatted_content = f"""Title: {title}
URL: {url}
Date Scraped: {datetime.now().isoformat()}
Source: Newsletter

---

{content}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(formatted_content)
    
    return str(filepath)


def process_batch_file(batch_file: str, output_dir: str):
    """Process multiple URLs from a text file."""
    with open(batch_file, 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        print(f"Processing {i}/{len(lines)}: {line}")
        
        title, content = extract_newsletter_content(line)
        if content:
            filepath = save_newsletter(title or f"Newsletter-{i}", content, line, output_dir)
            print(f"  → Saved: {filepath}")
        else:
            print(f"  → Failed to extract content")
        
        # Be nice to servers
        time.sleep(2)


def main():
    parser = argparse.ArgumentParser(description="Scrape newsletters for RAG system")
    parser.add_argument("--url", help="Single newsletter URL to scrape")
    parser.add_argument("--title", help="Custom title for the newsletter")
    parser.add_argument("--batch", help="Text file with multiple URLs (one per line)")
    parser.add_argument("--output-dir", 
                        default="/Users/vishen/clawd/transcripts/newsletters",
                        help="Output directory for newsletter files")
    
    args = parser.parse_args()
    
    # Create output directory
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    
    if args.batch:
        process_batch_file(args.batch, args.output_dir)
    elif args.url:
        print(f"Scraping: {args.url}")
        title, content = extract_newsletter_content(args.url)
        
        if content:
            custom_title = args.title or title or "Newsletter"
            filepath = save_newsletter(custom_title, content, args.url, args.output_dir)
            print(f"Saved: {filepath}")
        else:
            print("Failed to extract content")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()