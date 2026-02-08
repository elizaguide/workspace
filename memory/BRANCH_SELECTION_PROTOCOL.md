# Intelligent Branch Selection Protocol
## Real-Time Context Intelligence System

### SESSION STARTUP PROTOCOL
**EXECUTE BEFORE responding to ANY user message:**

---

## STEP 1 - ENTITY EXTRACTION
Scan the user message for:
- **People names:** (Sarah, Barry, Hayden, Eve, Jackson, Norman, Jaideep, etc.)
- **Project names:** (summit, certification, Instagram, newsletter, Spanish, investments, etc.)  
- **Domain keywords:** (investments, team, content, marketing, health, AI, education, etc.)
- **Temporal markers:** (yesterday, last week, why did we, when was, history of, etc.)

---

## STEP 2 - BRANCH SCORING ALGORITHM
For each branch in MANIFEST.md, calculate:

```
score = (entity_matches / total_entities_in_msg) * 0.4
      + (keyword_matches / total_keywords_in_msg) * 0.3  
      + (days_since_last_active < 7 ? 0.2 : 0.1) * 0.2
      + (access_frequency_normalized) * 0.1
```

**Scoring Components:**
- **Entity Match (40%):** Direct people/project mentions get highest weight
- **Keyword Match (30%):** Domain vocabulary relevance
- **Recency Bonus (20%):** Recently active branches get priority boost  
- **Usage Pattern (10%):** Frequently accessed branches get slight boost

---

## STEP 3 - TEMPORAL LAYER SELECTION
Analyze message intent to determine layer depth:

| Message Type | Temporal Markers | Layer Selection |
|--------------|------------------|-----------------|
| **Action** | update, change, schedule, create | CURRENT only |
| **Retrospective** | why, when did we, history of, what happened | HISTORY + CURRENT |
| **Factual Lookup** | what's the email, phone number, API key | REFERENCE only |
| **Strategic Planning** | should we, strategy, next steps, plan | CURRENT + HISTORY |
| **Default** | general queries | CURRENT |

---

## STEP 4 - LOAD DECISION
**Selection Rules:**
- Load top 1-3 branches with score > 0.3
- **Maximum context budget:** 2,000 tokens from branch loading
- **If over budget priority:** CURRENT > HISTORY > REFERENCE
- **Minimum threshold:** 0.3 score to qualify for loading

**Load Pattern Examples:**
- **Single domain query:** Load 1 branch (highest scoring)
- **Cross-domain query:** Load 2-3 branches (score > 0.3)
- **Complex planning:** Load primary + related branches up to token limit

---

## STEP 5 - ROUTING LOG
**Record in MANIFEST.md Routing Log:**
```
| Date | Query Summary | Branches Selected | Score | Used? | Notes |
|------|---------------|------------------|-------|--------|--------|
| YYYY-MM-DD HH:MM | First 50 chars of query | Branch1, Branch2 | 0.85, 0.62 | ✅ | Context relevance assessment |
```

**Log Analysis:**
- **Weekly review:** Analyze hit rates and scoring accuracy
- **Pattern recognition:** Identify common query types for optimization
- **Threshold tuning:** Adjust 0.3 threshold based on performance data
- **Miss analysis:** Track cases where wrong branches were selected

---

## IMPLEMENTATION NOTES

**Token Budget Management:**
- CURRENT layer: ~500-800 tokens per branch
- HISTORY layer: ~300-500 tokens per branch  
- REFERENCE layer: ~200-400 tokens per branch
- Reserve 200 tokens for MANIFEST.md + routing overhead

**Performance Optimization:**
- Cache scoring calculations for identical queries
- Precompute entity/keyword frequencies for faster matching
- Implement early termination if high-confidence match found

**Fallback Behavior:**
- If no branches score > 0.3: Load Partnership + most recent active branch
- If scoring system fails: Default to Partnership + context-appropriate branch
- If token budget exceeded: Prioritize highest-scoring branch only

**Quality Assurance:**
- Track "context miss" events where selected branches weren't useful
- Monitor "context overflow" where too much irrelevant information loaded
- Measure response quality improvement vs baseline

---

## MID-CONVERSATION BRANCH SWITCHING
**Dynamic Context Adaptation During Dialogue**

### TOPIC SHIFT DETECTION
**Monitor EVERY user message for:**
- **New entities:** People/projects not in currently loaded branches
- **Topic pivots:** Domain keywords outside current branch scope
- **Context gaps:** Questions requiring knowledge not in loaded branches

### DYNAMIC LOADING ALGORITHM
**When topic shift detected:**

**STEP 1:** Run branch scoring algorithm on NEW message only
**STEP 2:** Identify highest-scoring unloaded branch
**STEP 3:** If new branch scores > 0.5 AND not currently loaded:
- Load the new branch immediately
- If at 3-branch limit: unload lowest-scoring current branch
- Integrate new context seamlessly into response

### SEAMLESS INTEGRATION RULES
**DO:**
- ✅ Respond with full context as if you always had it
- ✅ Naturally weave new branch knowledge into answer
- ✅ Maintain conversation flow without interruption

**DO NOT:**
- ❌ Announce "Let me check another branch"
- ❌ Say "I'm loading new context"
- ❌ Break conversation flow with meta-commentary
- ❌ Make the context switch visible to user

### DYNAMIC LOAD LOGGING
**Record in MANIFEST.md Routing Log:**
```
| Date | Trigger Entity/Topic | Branch Loaded | Unloaded | Conversation Context |
|------|---------------------|---------------|----------|-------------------|
| YYYY-MM-DD HH:MM | "Hayden" mentioned | Kids | Personal_Growth | Mid-convo about family |
```

**Learning Data:**
- **Trigger patterns:** What causes mid-conversation switches
- **Related branch discovery:** Auto-improve "Related branches" in MANIFEST
- **Context flow quality:** How well dynamic loading improves responses

### BRANCH CAPACITY MANAGEMENT
**Maximum 3 branches loaded simultaneously:**
- **Priority ranking:** Current scores determine retention
- **Smart unloading:** Remove branch with lowest current relevance
- **Memory efficiency:** Stay within 2,000 token budget
- **Context continuity:** Prefer keeping branches mentioned in recent conversation

### EXAMPLES

**Conversation Flow Example:**
```
User: "How's my portfolio doing?"
→ Loads: Investments (score 0.9)

User: "Also, can you help Hayden with Spanish homework?"
→ Topic shift detected: "Hayden" + "Spanish" 
→ Scores: Kids (0.7), Spanish_Teaching (0.8)
→ Dynamic load: Spanish_Teaching + Kids
→ Unload: None (only 3 total)
→ Response: Seamlessly addresses both portfolio AND Spanish homework
```

**Multi-Domain Pivot Example:**
```
Currently loaded: Partnership, AI_Education, Newsletter
User: "By the way, what's my CCJ stock performance?"
→ Topic shift: "CCJ" + "stock" 
→ Scores: Investments (0.9) 
→ Dynamic load: Investments
→ Unload: Newsletter (lowest score)
→ Response: Natural transition to investment discussion
```

---

## SUCCESS METRICS
- **Routing Accuracy:** % of selections where loaded context was actually used
- **Response Quality:** Subjective assessment of context relevance
- **Efficiency:** Average tokens used vs information utility
- **Learning Rate:** Improvement in routing accuracy over time

*This protocol transforms reactive context guessing into predictive intelligence.*