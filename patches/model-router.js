/**
 * Model Router — auto-classifies messages as simple/complex
 * and returns the appropriate model for each.
 *
 * Simple messages → Ollama (local, free, fast)
 * Complex messages → Sonnet (cloud, capable)
 *
 * Uses keyword/heuristic scoring (sub-millisecond, no network calls).
 */

const SONNET = { provider: "anthropic", model: "claude-sonnet-4-0" };
const OLLAMA = { provider: "ollama", model: "llama3.1:8b" };

// --- Complexity indicators (push score UP → Sonnet) ---

const COMPLEX_KEYWORD_LIST = [
  "create", "build", "write", "generate", "implement", "design",
  "analyze", "research", "debug", "fix", "refactor", "code",
  "script", "function", "deploy", "publish", "compare", "evaluate",
  "summarize", "translate", "convert", "calculate", "plan",
  "architect", "optimize", "migrate", "configure", "integrate",
  "automate", "explain", "page", "website", "html",
];

const COMPLEX_PHRASES = /\b(step by step|in detail|detailed|comprehensive|thorough|compare and contrast|pros and cons)\b/i;

const HAS_CODE_BLOCK = /```[\s\S]*```|`[^`]+`/;

const HAS_URL = /https?:\/\/\S+/;

function countKeywordMatches(text) {
  const lower = text.toLowerCase();
  let count = 0;
  for (const kw of COMPLEX_KEYWORD_LIST) {
    if (new RegExp(`\\b${kw}\\b`).test(lower)) count++;
  }
  return count;
}

// --- Simplicity indicators (push score DOWN → Ollama) ---

const GREETING = /^\s*(hi|hello|hey|hola|good\s*(morning|afternoon|evening|night)|what'?s\s*up|yo|sup)\s*[!?.]*\s*$/i;

const CONFIRMATION = /^\s*(yes|no|yeah|nah|yep|nope|ok|okay|sure|thanks|thank\s*you|cool|great|got\s*it|alright|fine|np|ty|thx|k)\s*[!?.]*\s*$/i;

const SINGLE_EMOJI = /^\s*[\p{Emoji}\u200d\ufe0f]{1,8}\s*$/u;

/**
 * Classify message complexity.
 * @param {string} text — the user's message
 * @returns {{ provider: string, model: string }}
 */
export function classifyComplexity(text) {
  if (!text || typeof text !== "string") return SONNET; // safety default

  const trimmed = text.trim();
  if (!trimmed) return OLLAMA;

  let score = 0;

  // --- Simplicity signals ---
  if (GREETING.test(trimmed))       score -= 3;
  if (CONFIRMATION.test(trimmed))   score -= 3;
  if (SINGLE_EMOJI.test(trimmed))   score -= 3;
  if (trimmed.length < 50)          score -= 2;

  // --- Complexity signals ---
  if (trimmed.length > 500)         score += 3;
  else if (trimmed.length > 200)    score += 2;

  if (HAS_CODE_BLOCK.test(trimmed)) score += 3;
  if (HAS_URL.test(trimmed))        score += 1;

  // Each distinct action keyword adds +2 (capped at +8)
  const kwHits = countKeywordMatches(trimmed);
  score += Math.min(kwHits * 2, 8);

  if (COMPLEX_PHRASES.test(trimmed))  score += 2;

  // Multiple sentences suggest a multi-part request
  const sentences = trimmed.split(/[.!?]+/).filter(s => s.trim().length > 5);
  if (sentences.length > 3) score += 1;

  return score > 0 ? SONNET : OLLAMA;
}
