#!/usr/bin/env python3
"""
Mindvalley Transcript Retriever — CLI entry point for Eliza

Called by Eliza's exec tool to search transcripts and return
relevant excerpts with citations.

Usage:
    python mv_retrieve.py --query "energy healing techniques" [--mode strict] [--k 8]

Output: JSON to stdout with excerpts, formatted context, and citations.
"""

import argparse
import json
import sys

from mv_memory import (
    DEFAULT_DB_PATH,
    DEFAULT_TRANSCRIPTS_DIR,
    build_citations,
    build_context,
    expand_lines,
    retrieve,
)

STRICT_PROMPT = """You are answering based ONLY on the provided transcript excerpts.
Rules:
- Use ONLY the information in the excerpts below. Do NOT use outside knowledge.
- If the excerpts do not contain enough information to answer, respond exactly:
  "I don't have that in the transcripts."
- Every key claim must have a citation: (Source, lines X-Y)
- Do not guess or infer beyond what is explicitly stated."""

CREATIVE_PROMPT = """You are answering based on the provided transcript excerpts.
Rules:
- Ground your answer in the excerpts below.
- You may synthesize across multiple excerpts and draw reasonable inferences.
- Any inference or synthesis MUST be labeled with "Inference:" at the start.
- Every factual claim must have a citation: (Source, lines X-Y)
- If the excerpts are insufficient, say so clearly."""


def main():
    parser = argparse.ArgumentParser(description="Retrieve from Mindvalley transcript index")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--mode", choices=["strict", "creative"], default="strict",
                        help="Response mode (default: strict)")
    parser.add_argument("--k", type=int, default=8, help="Number of excerpts to retrieve")
    parser.add_argument("--db-path", default=DEFAULT_DB_PATH, help="ChromaDB path")
    parser.add_argument("--transcripts-dir", default=DEFAULT_TRANSCRIPTS_DIR,
                        help="Transcripts directory (for line expansion)")
    parser.add_argument("--expand", action="store_true",
                        help="Include exact verbatim lines from source files")
    args = parser.parse_args()

    try:
        excerpts = retrieve(args.query, k=args.k, db_path=args.db_path)
    except Exception as e:
        json.dump({"error": str(e)}, sys.stdout)
        sys.exit(1)

    # Build output
    result = {
        "mode": args.mode,
        "system_prompt": STRICT_PROMPT if args.mode == "strict" else CREATIVE_PROMPT,
        "query": args.query,
        "excerpt_count": len(excerpts),
        "excerpts": [
            {
                "source": ex["source"],
                "start_line": ex["start_line"],
                "end_line": ex["end_line"],
                "score": ex["score"],
                "quote": " ".join(ex["text"].split())[:200],
            }
            for ex in excerpts
        ],
        "context": build_context(excerpts),
        "citations": build_citations(excerpts),
    }

    # Optionally expand exact verbatim lines
    if args.expand:
        for i, ex in enumerate(excerpts):
            result["excerpts"][i]["verbatim"] = expand_lines(
                ex["source"], ex["start_line"], ex["end_line"],
                transcripts_dir=args.transcripts_dir,
            )

    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()  # trailing newline


if __name__ == "__main__":
    main()
