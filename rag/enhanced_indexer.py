#!/usr/bin/env python3
"""
Enhanced Mindvalley RAG Indexer

Indexes all content types: transcripts, books, newsletters, YouTube videos, Summit Playbook
with improved metadata and source tracking.

Usage:
    python enhanced_indexer.py --all             # Index everything
    python enhanced_indexer.py --newsletters     # Just newsletters
    python enhanced_indexer.py --youtube         # Just YouTube
    python enhanced_indexer.py --books           # Just books
    python enhanced_indexer.py --transcripts     # Just quest transcripts
    python enhanced_indexer.py --summit-playbook # Just Summit Mastery Playbook
"""

import argparse
import time
from pathlib import Path

from mv_memory import (
    DEFAULT_DB_PATH,
    DEFAULT_TRANSCRIPTS_DIR,
    chunk_file,
    get_chroma_client,
    get_collection,
)


def get_content_type(file_path: Path, transcripts_root: Path) -> str:
    """Determine content type based on file location."""
    try:
        relative_path = file_path.relative_to(transcripts_root)
        parts = relative_path.parts

        if 'newsletters' in parts:
            return 'newsletter'
        elif 'youtube' in parts:
            return 'youtube'
        elif 'vishen-books' in parts:
            return 'book'
        elif 'soul' in parts:
            return 'quest'
        elif 'summit-mastery-playbook' in parts:
            return 'summit-playbook'
        else:
            return 'transcript'
    except ValueError:
        return 'unknown'


def enhanced_chunk_file(filepath: str, transcripts_dir: str = None) -> list[dict]:
    """Enhanced chunking with content type detection and metadata."""
    chunks = chunk_file(filepath, transcripts_dir=transcripts_dir)
    
    transcripts_root = Path(transcripts_dir or DEFAULT_TRANSCRIPTS_DIR).resolve()
    file_path = Path(filepath)
    content_type = get_content_type(file_path, transcripts_root)
    
    # Add content type and enhanced metadata to each chunk
    for chunk in chunks:
        chunk['content_type'] = content_type
        
        # Extract additional metadata from file content if available
        if content_type in ['newsletter', 'youtube']:
            lines = chunk['text'].split('\n')[:10]  # First 10 lines for metadata
            
            for line in lines:
                if line.startswith('Title: '):
                    chunk['title'] = line.replace('Title: ', '').strip()
                elif line.startswith('URL: '):
                    chunk['url'] = line.replace('URL: ', '').strip()
                elif line.startswith('Upload Date: ') or line.startswith('Date Scraped: '):
                    chunk['date'] = line.split(': ', 1)[1].strip()
                elif line.startswith('Uploader: '):
                    chunk['author'] = line.replace('Uploader: ', '').strip()
    
    return chunks


def index_content_type(
    transcripts_dir: str, 
    db_path: str, 
    content_types: list[str] = None,
    clear: bool = False
):
    """Index specific content types."""
    print(f"Transcripts dir: {transcripts_dir}")
    print(f"ChromaDB path:   {db_path}")
    print(f"Content types:   {content_types or ['all']}")
    print()

    client = get_chroma_client(db_path)

    if clear:
        try:
            client.delete_collection("mv_transcripts")
            print("Cleared existing collection.")
        except Exception:
            pass

    collection = get_collection(client=client)
    transcripts_root = Path(transcripts_dir).resolve()
    
    # Find files based on content types
    files_to_process = []
    
    if not content_types or 'all' in content_types:
        content_types = ['newsletters', 'youtube', 'books', 'transcripts', 'summit-playbook']

    for content_type in content_types:
        if content_type == 'newsletters':
            pattern = transcripts_root / "newsletters" / "*.txt"
        elif content_type == 'youtube':
            pattern = transcripts_root / "youtube" / "*.txt"
        elif content_type == 'books':
            pattern = transcripts_root / "vishen-books" / "*.txt"
        elif content_type == 'transcripts':
            # Original quest transcripts
            pattern = transcripts_root / "soul" / "*.txt"
        elif content_type == 'summit-playbook':
            # Summit Mastery Playbook markdown files
            pattern = transcripts_root / "summit-mastery-playbook" / "*.md"
        else:
            continue

        files_to_process.extend(list(pattern.parent.glob(pattern.name)))
    
    # Remove duplicates and sort
    files_to_process = sorted(set(files_to_process))
    
    if not files_to_process:
        print("No files found for specified content types.")
        return

    print(f"Found {len(files_to_process)} files to process.")
    print()

    # Get existing IDs to skip duplicates
    existing_ids = set()
    try:
        existing = collection.get()
        if existing and existing["ids"]:
            existing_ids = set(existing["ids"])
    except Exception:
        pass

    total_chunks = 0
    skipped = 0
    start = time.time()

    for filepath in files_to_process:
        try:
            chunks = enhanced_chunk_file(str(filepath), transcripts_dir)
            if not chunks:
                continue

            # Filter out already-indexed chunks
            new_chunks = [c for c in chunks if c["id"] not in existing_ids]
            skip_count = len(chunks) - len(new_chunks)
            skipped += skip_count

            if not new_chunks:
                print(f"  {filepath.name}: {len(chunks)} chunks (all already indexed)")
                continue

            # Prepare metadata for ChromaDB
            metadatas = []
            for c in new_chunks:
                metadata = {
                    "source": c["source"],
                    "start_line": c["start_line"],
                    "end_line": c["end_line"],
                    "content_type": c.get("content_type", "unknown"),
                }
                
                # Add optional metadata
                for key in ['title', 'url', 'date', 'author']:
                    if key in c:
                        metadata[key] = c[key]
                
                metadatas.append(metadata)

            # Batch add to ChromaDB
            batch_size = 10
            for i in range(0, len(new_chunks), batch_size):
                batch = new_chunks[i : i + batch_size]
                batch_metadata = metadatas[i : i + batch_size]
                
                collection.add(
                    ids=[c["id"] for c in batch],
                    documents=[c["text"] for c in batch],
                    metadatas=batch_metadata,
                )

            total_chunks += len(new_chunks)
            content_type = new_chunks[0].get('content_type', 'unknown')
            print(f"  {filepath.name} ({content_type}): {len(new_chunks)} new chunks"
                  + (f" ({skip_count} skipped)" if skip_count else ""))
            
        except Exception as e:
            print(f"  Error processing {filepath.name}: {e}")

    elapsed = time.time() - start

    print()
    print(f"Indexing complete.")
    print(f"  Files:          {len(files_to_process)}")
    print(f"  New chunks:     {total_chunks}")
    print(f"  Skipped (dup):  {skipped}")
    print(f"  Total in DB:    {collection.count()}")
    print(f"  Time:           {elapsed:.1f}s")
    print(f"  DB path:        {db_path}")


def main():
    parser = argparse.ArgumentParser(description="Enhanced RAG indexing")
    parser.add_argument("--transcripts-dir", default=DEFAULT_TRANSCRIPTS_DIR)
    parser.add_argument("--db-path", default=DEFAULT_DB_PATH)
    parser.add_argument("--clear", action="store_true", help="Clear and rebuild")
    
    # Content type selection
    parser.add_argument("--all", action="store_true", help="Index all content types")
    parser.add_argument("--newsletters", action="store_true", help="Index newsletters")
    parser.add_argument("--youtube", action="store_true", help="Index YouTube videos")
    parser.add_argument("--books", action="store_true", help="Index books")
    parser.add_argument("--transcripts", action="store_true", help="Index quest transcripts")
    parser.add_argument("--summit-playbook", action="store_true", help="Index Summit Mastery Playbook")
    
    args = parser.parse_args()
    
    # Determine content types to process
    content_types = []
    if args.all:
        content_types = ['all']
    else:
        if args.newsletters:
            content_types.append('newsletters')
        if args.youtube:
            content_types.append('youtube')
        if args.books:
            content_types.append('books')
        if args.transcripts:
            content_types.append('transcripts')
        if args.summit_playbook:
            content_types.append('summit-playbook')
    
    if not content_types:
        content_types = ['all']  # Default to all if nothing specified
    
    index_content_type(args.transcripts_dir, args.db_path, content_types, args.clear)


if __name__ == "__main__":
    main()