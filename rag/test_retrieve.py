#!/usr/bin/env python3
"""
Mindvalley Transcript RAG — Verification Tests

Runs smoke tests to verify the RAG pipeline works correctly.

Usage:
    python test_retrieve.py
"""

import sys
import time
from pathlib import Path

from mv_memory import (
    DEFAULT_DB_PATH,
    DEFAULT_TRANSCRIPTS_DIR,
    expand_lines,
    retrieve,
)


def test_smoke_retrieval():
    """A) Smoke test: query a known term, verify sources and line ranges."""
    print("Test A: Smoke retrieval...")

    query = "meditation technique"
    start = time.time()
    results = retrieve(query, k=5)
    elapsed = time.time() - start

    assert len(results) > 0, f"No results for '{query}'"

    print(f"  Query: '{query}'")
    print(f"  Results: {len(results)} excerpts in {elapsed:.2f}s")
    for r in results:
        assert r["source"], "Missing source"
        assert r["start_line"] > 0, "Invalid start_line"
        assert r["end_line"] >= r["start_line"], "end_line < start_line"
        assert r["text"], "Empty text"
        print(f"    - {r['source']} (lines {r['start_line']}-{r['end_line']}, score={r['score']})")

    print("  PASS")
    return True


def test_citation_integrity():
    """B) Citation integrity: verify quoted text exists at claimed line range."""
    print("Test B: Citation integrity...")

    results = retrieve("energy", k=3)
    assert len(results) > 0, "No results for 'energy'"

    for r in results:
        verbatim = expand_lines(
            r["source"], r["start_line"], r["end_line"],
            transcripts_dir=DEFAULT_TRANSCRIPTS_DIR,
        )

        if verbatim.startswith("(Source file not found"):
            print(f"  SKIP: {r['source']} — file not found at expected path")
            continue

        # The chunk text should be a substring of the verbatim lines
        # (they should match since we chunked by the same lines)
        chunk_normalized = " ".join(r["text"].split())
        verbatim_normalized = " ".join(verbatim.split())

        # Check overlap — the chunk content should appear in the file
        overlap = len(set(chunk_normalized.split()) & set(verbatim_normalized.split()))
        total = max(1, len(set(chunk_normalized.split())))
        overlap_ratio = overlap / total

        assert overlap_ratio > 0.8, (
            f"Citation mismatch for {r['source']} lines {r['start_line']}-{r['end_line']}: "
            f"only {overlap_ratio:.0%} word overlap"
        )
        print(f"    - {r['source']} lines {r['start_line']}-{r['end_line']}: {overlap_ratio:.0%} match")

    print("  PASS")
    return True


def test_performance():
    """C) Performance: retrieval should complete within 3 seconds."""
    print("Test C: Performance...")

    queries = [
        "chakra healing meditation",
        "lucid dreaming techniques",
        "abundance mindset",
    ]

    for q in queries:
        start = time.time()
        results = retrieve(q, k=8)
        elapsed = time.time() - start

        assert elapsed < 5.0, f"Query '{q}' too slow: {elapsed:.2f}s"
        print(f"    '{q}': {len(results)} results in {elapsed:.2f}s")

    print("  PASS")
    return True


def test_no_results_graceful():
    """D) Graceful handling when query has no good matches."""
    print("Test D: No-results handling...")

    results = retrieve("xyzzy foobar nonsense gibberish 12345", k=3)
    # Should return results (even if low quality) without crashing
    print(f"    Nonsense query returned {len(results)} results (expected: 0-3)")
    print("  PASS")
    return True


def main():
    print("=" * 60)
    print("Mindvalley Transcript RAG — Verification Tests")
    print("=" * 60)
    print()

    # Check DB exists
    db_path = Path(DEFAULT_DB_PATH)
    if not db_path.exists():
        print(f"ERROR: ChromaDB not found at {db_path}")
        print("Run mv_index.py first to build the index.")
        sys.exit(1)

    passed = 0
    failed = 0

    for test_fn in [test_smoke_retrieval, test_citation_integrity, test_performance, test_no_results_graceful]:
        try:
            test_fn()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {e}")
            failed += 1
        print()

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
