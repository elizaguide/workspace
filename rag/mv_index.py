#!/usr/bin/env python3
"""
Mindvalley Transcript Indexer

Recursively loads .txt files from the transcripts directory,
chunks them by line count, embeds with Ollama nomic-embed-text,
and stores in a persistent ChromaDB.

Usage:
    python mv_index.py [--transcripts-dir PATH] [--db-path PATH]
    python mv_index.py --clear   # wipe and rebuild from scratch

Re-running is safe: uses stable chunk IDs so duplicates are skipped.
"""

import argparse
import sys
import time
from pathlib import Path

from mv_memory import (
    DEFAULT_DB_PATH,
    DEFAULT_TRANSCRIPTS_DIR,
    chunk_file,
    get_chroma_client,
    get_collection,
)


def find_transcript_files(transcripts_dir: str) -> list[Path]:
    """Recursively find all .txt files."""
    root = Path(transcripts_dir).resolve()
    files = sorted(root.rglob("*.txt"))
    return files


def index_transcripts(transcripts_dir: str, db_path: str, clear: bool = False):
    """Index all transcripts into ChromaDB."""
    print(f"Transcripts dir: {transcripts_dir}")
    print(f"ChromaDB path:   {db_path}")
    print()

    client = get_chroma_client(db_path)

    if clear:
        try:
            client.delete_collection("mv_transcripts")
            print("Cleared existing collection.")
        except Exception:
            pass

    collection = get_collection(client=client)

    files = find_transcript_files(transcripts_dir)
    if not files:
        print("No .txt files found.")
        return

    print(f"Found {len(files)} transcript files.")
    print()

    total_chunks = 0
    skipped = 0
    start = time.time()

    # Get existing IDs to skip duplicates
    existing_ids = set()
    try:
        existing = collection.get()
        if existing and existing["ids"]:
            existing_ids = set(existing["ids"])
    except Exception:
        pass

    for filepath in files:
        chunks = chunk_file(str(filepath), transcripts_dir=transcripts_dir)
        if not chunks:
            continue

        # Filter out already-indexed chunks
        new_chunks = [c for c in chunks if c["id"] not in existing_ids]
        skip_count = len(chunks) - len(new_chunks)
        skipped += skip_count

        if not new_chunks:
            print(f"  {filepath.name}: {len(chunks)} chunks (all already indexed)")
            continue

        # Batch add to ChromaDB (small batches to avoid embedding context overflow)
        batch_size = 10
        for i in range(0, len(new_chunks), batch_size):
            batch = new_chunks[i : i + batch_size]
            collection.add(
                ids=[c["id"] for c in batch],
                documents=[c["text"] for c in batch],
                metadatas=[
                    {
                        "source": c["source"],
                        "start_line": c["start_line"],
                        "end_line": c["end_line"],
                    }
                    for c in batch
                ],
            )

        total_chunks += len(new_chunks)
        print(f"  {filepath.name}: {len(new_chunks)} new chunks indexed"
              + (f" ({skip_count} skipped)" if skip_count else ""))

    elapsed = time.time() - start

    print()
    print(f"Indexing complete.")
    print(f"  Files:          {len(files)}")
    print(f"  New chunks:     {total_chunks}")
    print(f"  Skipped (dup):  {skipped}")
    print(f"  Total in DB:    {collection.count()}")
    print(f"  Time:           {elapsed:.1f}s")
    print(f"  DB path:        {db_path}")


def main():
    parser = argparse.ArgumentParser(description="Index Mindvalley transcripts into ChromaDB")
    parser.add_argument("--transcripts-dir", default=DEFAULT_TRANSCRIPTS_DIR,
                        help="Path to transcripts directory")
    parser.add_argument("--db-path", default=DEFAULT_DB_PATH,
                        help="Path to ChromaDB persistence directory")
    parser.add_argument("--clear", action="store_true",
                        help="Clear existing index and rebuild from scratch")
    args = parser.parse_args()

    index_transcripts(args.transcripts_dir, args.db_path, args.clear)


if __name__ == "__main__":
    main()
