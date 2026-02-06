# RAG System Expansion Guide

## Overview

This expansion adds **newsletters** and **YouTube transcripts** to your existing RAG system, creating a comprehensive knowledge base of Vishen's content across all formats.

## Quick Setup

### 1. Install New Dependencies
```bash
cd /Users/vishen/clawd/rag
source .venv/bin/activate
pip install -r requirements-enhanced.txt
```

### 2. Make Scripts Executable
```bash
chmod +x newsletter_scraper.py
chmod +x youtube_scraper.py  
chmod +x enhanced_indexer.py
```

## Newsletter Integration

### Step 1: Get Newsletter Links from Ramya
When Ramya shares the newsletter links in WhatsApp, you can process them:

**Single Newsletter:**
```bash
python newsletter_scraper.py --url "https://..." --title "Newsletter Title"
```

**Batch Processing:**
1. Create a file with URLs (one per line):
```bash
echo "https://newsletter1.com" > newsletter_urls.txt
echo "https://newsletter2.com" >> newsletter_urls.txt
```

2. Process all:
```bash
python newsletter_scraper.py --batch newsletter_urls.txt
```

### Step 2: Index Newsletters
```bash
python enhanced_indexer.py --newsletters
```

## YouTube Integration

### Step 1: Extract All Your YouTube Content

**Your Entire Channel (50 most recent):**
```bash
python youtube_scraper.py --channel "@vishenlakhiani" --limit 50
```

**Specific Video:**
```bash
python youtube_scraper.py --url "https://youtube.com/watch?v=VIDEO_ID"
```

**Batch Processing:**
```bash
python youtube_scraper.py --batch youtube_urls.txt
```

### Step 2: Index YouTube Transcripts
```bash
python enhanced_indexer.py --youtube
```

## Complete Reindexing

To rebuild everything with the enhanced system:
```bash
python enhanced_indexer.py --all --clear
```

## New RAG Features

### Enhanced Search with Content Types
The retrieval system now includes content type metadata:

```python
# Example: Search with content type filtering
results = retrieve("entrepreneurship mindset", k=10)
for result in results:
    print(f"Source: {result['source']} (Type: {result.get('content_type', 'unknown')})")
```

### Available Content Types:
- `quest` - Original Mindvalley quest transcripts
- `book` - Your published books
- `newsletter` - Newsletter content
- `youtube` - YouTube video transcripts
- `unknown` - Unclassified content

## Automation Workflow

### Daily Newsletter Processing
Set up a cron job or manual process:

1. **Receive links** from Ramya via WhatsApp
2. **Save to file:** `today_newsletters.txt`
3. **Process:** `python newsletter_scraper.py --batch today_newsletters.txt`
4. **Index:** `python enhanced_indexer.py --newsletters`

### Weekly YouTube Update
```bash
# Get latest videos
python youtube_scraper.py --channel "@vishenlakhiani" --limit 10

# Index new content
python enhanced_indexer.py --youtube
```

## Directory Structure

Your expanded transcripts directory:
```
transcripts/
├── soul/                    # Original quest transcripts
├── vishen-books/           # Your books
├── newsletters/            # Newsletter content (NEW)
│   ├── 2026-02-06-newsletter-title.txt
│   └── 2026-02-07-another-newsletter.txt
└── youtube/               # YouTube transcripts (NEW)
    ├── VIDEO_ID-title.txt
    └── ANOTHER_ID-title.txt
```

## Testing the Expansion

### 1. Test Newsletter Scraper
```bash
python newsletter_scraper.py --url "https://mindvalley.com/blog/some-article" --title "Test Article"
```

### 2. Test YouTube Scraper
```bash
python youtube_scraper.py --url "https://youtube.com/watch?v=dQw4w9WgXcQ"
```

### 3. Test Enhanced Indexing
```bash
python enhanced_indexer.py --newsletters --youtube
```

### 4. Test Retrieval
```bash
python test_retrieve.py --query "your test query"
```

## Content Quality Notes

### Newsletter Content:
- Extracts main article content
- Filters out navigation/footer elements  
- Preserves formatting and structure
- Includes metadata (URL, scrape date, title)

### YouTube Content:
- Uses YouTube's auto-generated transcripts when available
- Includes video metadata (title, description, upload date)
- Handles multiple language transcripts
- Skips videos without transcripts

## Troubleshooting

### Common Issues:

**"No transcript available":**
- YouTube video has transcripts disabled
- Try different video or wait for auto-generation

**"Failed to extract newsletter content":**
- Website blocking scrapers
- Try different URL or manual copy-paste

**"ChromaDB embedding errors":**
- Check Ollama is running: `ollama serve`
- Verify nomic-embed-text model: `ollama pull nomic-embed-text`

### Performance Optimization:
- Process content in batches of 10-20 items
- Index incrementally (new content only)
- Monitor disk space (transcripts can be large)

## Next Steps

1. **Get newsletter links from Ramya**
2. **Run YouTube channel scrape**
3. **Test retrieval with expanded content**
4. **Set up regular update workflow**

Your RAG system will now have 4x the content with much richer context for answering questions about your teachings, philosophy, and business insights!