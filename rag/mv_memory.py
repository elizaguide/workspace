"""
Mindvalley Transcript RAG — Core Library

Provides chunking, embedding, indexing, and retrieval for
Mindvalley quest transcripts stored as .txt files.

Uses:
- ChromaDB for local vector persistence
- Ollama nomic-embed-text for embeddings
- Line-based chunking for precise citations
"""

import hashlib
import os
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction

# ── Defaults ─────────────────────────────────────────────────────────

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "mv_chroma_db")
DEFAULT_TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "..", "transcripts")
COLLECTION_NAME = "mv_transcripts"
EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_URL = "http://localhost:11434"
CHUNK_LINES = 30
CHUNK_OVERLAP = 5
MAX_CHUNK_CHARS = 4000  # nomic-embed-text context limit safe margin


# ── ChromaDB helpers ─────────────────────────────────────────────────

def get_embedding_fn():
    """Return Ollama embedding function for nomic-embed-text."""
    return OllamaEmbeddingFunction(
        model_name=EMBEDDING_MODEL,
        url=OLLAMA_URL,
    )


def get_chroma_client(db_path=None):
    """Open or create a persistent ChromaDB client."""
    db_path = db_path or DEFAULT_DB_PATH
    os.makedirs(db_path, exist_ok=True)
    return chromadb.PersistentClient(path=db_path)


def get_collection(client=None, db_path=None):
    """Get or create the transcript collection."""
    client = client or get_chroma_client(db_path)
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=get_embedding_fn(),
        metadata={"hnsw:space": "cosine"},
    )


# ── Chunking ─────────────────────────────────────────────────────────

def make_chunk_id(source: str, start_line: int, end_line: int) -> str:
    """Stable ID from source + line range for idempotent re-indexing."""
    raw = f"{source}:{start_line}-{end_line}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def chunk_file(
    filepath: str,
    chunk_lines: int = CHUNK_LINES,
    overlap: int = CHUNK_OVERLAP,
    transcripts_dir: str = None,
) -> list[dict]:
    """
    Split a text file into line-based chunks with metadata.

    Returns list of dicts:
      - text: chunk content
      - source: relative path from transcripts root
      - start_line: 1-indexed
      - end_line: 1-indexed (inclusive)
      - id: stable hash
    """
    transcripts_dir = transcripts_dir or DEFAULT_TRANSCRIPTS_DIR
    filepath = Path(filepath)
    transcripts_root = Path(transcripts_dir).resolve()

    try:
        source = str(filepath.resolve().relative_to(transcripts_root))
    except ValueError:
        source = filepath.name

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    if not lines:
        return []

    chunks = []
    step = max(1, chunk_lines - overlap)
    i = 0

    while i < len(lines):
        end = min(i + chunk_lines, len(lines))
        chunk_text = "".join(lines[i:end])

        if chunk_text.strip():
            # Truncate if exceeds embedding model context limit
            if len(chunk_text) > MAX_CHUNK_CHARS:
                chunk_text = chunk_text[:MAX_CHUNK_CHARS]

            start_line = i + 1  # 1-indexed
            end_line = end      # inclusive
            chunks.append({
                "text": chunk_text,
                "source": source,
                "start_line": start_line,
                "end_line": end_line,
                "id": make_chunk_id(source, start_line, end_line),
            })

        i += step

    return chunks


# ── Retrieval ────────────────────────────────────────────────────────

def retrieve(query: str, k: int = 8, db_path: str = None) -> list[dict]:
    """
    Search ChromaDB for relevant transcript chunks.

    Returns list of dicts sorted by relevance:
      - text, source, start_line, end_line, score
    """
    collection = get_collection(db_path=db_path)
    results = collection.query(query_texts=[query], n_results=k)

    excerpts = []
    if results and results["documents"] and results["documents"][0]:
        docs = results["documents"][0]
        metas = results["metadatas"][0] if results["metadatas"] else [{}] * len(docs)
        dists = results["distances"][0] if results["distances"] else [0.0] * len(docs)

        for doc, meta, dist in zip(docs, metas, dists):
            excerpts.append({
                "text": doc,
                "source": meta.get("source", "unknown"),
                "start_line": meta.get("start_line", 0),
                "end_line": meta.get("end_line", 0),
                "score": round(1.0 - dist, 4),  # cosine distance → similarity
            })

    return excerpts


# ── Context & citation formatting ────────────────────────────────────

def build_context(excerpts: list[dict]) -> str:
    """Format retrieved excerpts into a context block for the LLM."""
    if not excerpts:
        return "(No relevant excerpts found.)"

    parts = []
    for i, ex in enumerate(excerpts, 1):
        header = f"[Excerpt {i}] {ex['source']} (lines {ex['start_line']}-{ex['end_line']})"
        parts.append(f"{header}\n{ex['text']}")

    return "\n---\n".join(parts)


def build_citations(excerpts: list[dict], max_quote: int = 200) -> str:
    """Format citation bullets with short quotes."""
    if not excerpts:
        return "(No citations.)"

    bullets = []
    for ex in excerpts:
        quote = " ".join(ex["text"].split())[:max_quote]
        if len(" ".join(ex["text"].split())) > max_quote:
            quote += "..."
        bullet = f'- ({ex["source"]}, lines {ex["start_line"]}-{ex["end_line"]}) "{quote}"'
        bullets.append(bullet)

    return "\n".join(bullets)


def expand_lines(
    source: str,
    start_line: int,
    end_line: int,
    transcripts_dir: str = None,
) -> str:
    """Read exact lines from a source transcript file."""
    transcripts_dir = transcripts_dir or DEFAULT_TRANSCRIPTS_DIR
    filepath = Path(transcripts_dir) / source

    if not filepath.exists():
        return f"(Source file not found: {source})"

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Convert to 0-indexed
    start_idx = max(0, start_line - 1)
    end_idx = min(len(lines), end_line)

    return "".join(lines[start_idx:end_idx])
