# Mindvalley Transcripts

This folder contains quest transcripts that Eliza can search and cite.

## Current transcripts

22 quest transcripts in the `soul/` subfolder (~10MB total).

## Adding new transcripts

1. Save the transcript as a `.txt` file (UTF-8 encoding).

2. Copy it into the `soul/` folder:

```bash
cp "/path/to/Your Transcript.txt" ~/clawd/transcripts/soul/
```

To copy multiple files at once:

```bash
cp /path/to/folder/*.txt ~/clawd/transcripts/soul/
```

3. Re-index so Eliza can search the new content:

```bash
~/clawd/rag/.venv/bin/python3 ~/clawd/rag/mv_index.py
```

This only indexes new chunks. Existing ones are skipped automatically.

4. To verify the new transcript was indexed:

```bash
~/clawd/rag/.venv/bin/python3 ~/clawd/rag/mv_retrieve.py --query "a topic from your new transcript" --k 3
```

## Rebuilding the full index from scratch

If you need to wipe and rebuild everything:

```bash
~/clawd/rag/.venv/bin/python3 ~/clawd/rag/mv_index.py --clear
```

## File format requirements

- Plain text `.txt` files only
- UTF-8 encoding (standard for most text editors)
- Files can be nested in subfolders if needed
- Any filename works, but descriptive names help with citations (e.g., `Unlocking Transcendence (Jeffrey Allen).txt`)

## Where things are stored

| Path | What |
|------|------|
| `~/clawd/transcripts/soul/` | Transcript text files |
| `~/clawd/mv_chroma_db/` | Vector database (auto-generated) |
| `~/clawd/rag/` | Python scripts (indexer, retriever, tests) |
