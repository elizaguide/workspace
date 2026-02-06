#!/usr/bin/env python3
"""
CSV Newsletter Processor for RAG

Processes CSV files containing newsletter content and adds them to the RAG system.
Designed for Mindvalley newsletter exports from Airtable.

Usage:
    python csv_to_rag.py --csv /path/to/newsletters.csv --reindex
"""

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def clean_filename(name: str) -> str:
    """Clean a string to be safe for use as a filename."""
    # Remove quotes and brackets, replace spaces with dashes
    name = re.sub(r'["\[\]()]', '', name)
    name = re.sub(r'\s+', '-', name.strip())
    # Remove other unsafe characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Limit length
    if len(name) > 100:
        name = name[:100]
    return name


def extract_newsletter_content(row: dict) -> dict:
    """Extract relevant content from a CSV row."""
    # Get the main content from the Email Proposal / Brief column
    content = row.get('Email Proposal / Brief', '').strip()
    
    # Skip if no content or if it's just metadata
    if not content or len(content) < 100:
        return None
        
    # Check if it's just a note about Google Docs access
    if "I am unable to access the content" in content:
        return None
    
    # Extract metadata
    title = row.get('Title', '') or row.get('Name', '')
    if not title:
        return None
        
    live_date = row.get('Live Date', '')
    topics = row.get('🌳 Topics', '')
    category = row.get('Category (from 🌳 Topics)', '')
    blog_link = row.get('Blog Link', '')
    
    return {
        'title': title,
        'content': content,
        'live_date': live_date,
        'topics': topics,
        'category': category,
        'blog_link': blog_link,
        'raw_row': row
    }


def create_newsletter_file(newsletter: dict, output_dir: Path) -> str:
    """Create a text file for the newsletter."""
    # Create a clean filename
    filename_base = clean_filename(newsletter['title'])
    if newsletter['live_date']:
        try:
            # Try to parse date and prepend it
            date_obj = datetime.strptime(newsletter['live_date'], '%d %B %Y')
            date_prefix = date_obj.strftime('%Y-%m-%d')
            filename_base = f"{date_prefix}-{filename_base}"
        except ValueError:
            pass  # If date parsing fails, just use title
    
    filename = f"{filename_base}.txt"
    filepath = output_dir / filename
    
    # Create the content with metadata header
    file_content = f"""TITLE: {newsletter['title']}
LIVE_DATE: {newsletter['live_date']}
TOPICS: {newsletter['topics']}
CATEGORY: {newsletter['category']}
BLOG_LINK: {newsletter['blog_link']}
SOURCE: Newsletter CSV Export
TIMESTAMP: {datetime.now().isoformat()}

---

{newsletter['content']}
"""
    
    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)
    
    return str(filepath)


def process_csv(csv_path: str, output_dir: Path) -> dict:
    """Process the CSV file and create newsletter text files."""
    results = {
        'processed': 0,
        'skipped': 0,
        'files_created': [],
        'errors': []
    }
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            # Use DictReader to handle the CSV
            reader = csv.DictReader(f)
            
            for i, row in enumerate(reader, 1):
                try:
                    # Extract newsletter data
                    newsletter = extract_newsletter_content(row)
                    
                    if newsletter is None:
                        results['skipped'] += 1
                        print(f"  [Row {i}] Skipped - no usable content")
                        continue
                    
                    # Create the file
                    filepath = create_newsletter_file(newsletter, output_dir)
                    results['files_created'].append(filepath)
                    results['processed'] += 1
                    
                    print(f"  [Row {i}] ✅ Created: {Path(filepath).name}")
                    
                except Exception as e:
                    results['errors'].append(f"Row {i}: {str(e)}")
                    print(f"  [Row {i}] ❌ Error: {e}")
    
    except Exception as e:
        results['errors'].append(f"CSV reading error: {str(e)}")
        print(f"❌ Error reading CSV: {e}")
    
    return results


def reindex_newsletters():
    """Reindex the newsletter content."""
    print("\n🔄 Indexing newsletter content...")
    try:
        cmd = [sys.executable, 'enhanced_indexer.py', '--newsletters']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("  ✅ Newsletter indexing complete")
        else:
            print(f"  ❌ Indexing failed: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"  ❌ Indexing error: {e}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Process newsletter CSV into RAG system")
    parser.add_argument("--csv", required=True, help="Path to the newsletter CSV file")
    parser.add_argument("--output-dir", help="Output directory (defaults to ../transcripts/newsletters)")
    parser.add_argument("--reindex", action="store_true", help="Automatically reindex after processing")
    parser.add_argument("--no-cleanup", action="store_true", help="Don't remove existing newsletter files")
    
    args = parser.parse_args()
    
    # Set up paths
    script_dir = Path(__file__).parent
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = script_dir.parent / "transcripts" / "newsletters"
    
    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"❌ CSV file not found: {csv_path}")
        return
    
    print(f"📊 Processing CSV: {csv_path}")
    print(f"📁 Output directory: {output_dir}")
    
    # Clean up existing files if requested
    if not args.no_cleanup and output_dir.exists():
        print(f"🧹 Cleaning up existing newsletter files...")
        for file in output_dir.glob("*.txt"):
            file.unlink()
            print(f"  Removed: {file.name}")
    
    print(f"\n📝 Processing newsletter data...")
    
    # Process the CSV
    results = process_csv(str(csv_path), output_dir)
    
    # Print summary
    print(f"\n📊 Processing Summary:")
    print(f"  ✅ Processed: {results['processed']} newsletters")
    print(f"  ⏭️  Skipped:   {results['skipped']} rows")
    if results['errors']:
        print(f"  ❌ Errors:    {len(results['errors'])}")
        for error in results['errors']:
            print(f"     - {error}")
    
    # Reindex if requested and we processed content
    if results['processed'] > 0:
        if args.reindex:
            success = reindex_newsletters()
            if success:
                print(f"\n🎉 Successfully added {results['processed']} newsletters to your RAG system!")
            else:
                print(f"\n⚠️  Content processed but indexing failed. Run manually:")
                print(f"     python enhanced_indexer.py --newsletters")
        else:
            print(f"\n✅ Content processed. To add to RAG, run:")
            print(f"     python enhanced_indexer.py --newsletters")
    
    print(f"\nFiles created in: {output_dir}")


if __name__ == "__main__":
    main()