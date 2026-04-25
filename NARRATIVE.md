# How Promptarchaeology was built on what came before

This tool didn't appear from nothing. It's the latest layer of a stack of prior projects, each of which solved a piece of the puzzle. This is the lineage.

## Layer 0 — the raw record

Years of LLM conversations: ChatGPT, Claude, Gemini, plus messy ancillary corpora (Twitter, SMS, Facebook, Gmail, scanned PDFs of old chat exports). Different formats, different schemas, different completeness. Roughly 1.45 million prompts spread across 5,271 conversations.

For a long time, these lived as files. Read-only artifacts of past thinking. You could grep them but you couldn't really *see* them.

## Layer 1 — Megabase

`C:\Dev\megabase\` came together over eight build sessions as the substrate for the corpus: a SQLite database (`megabase.db`) ingesting from each source into a unified schema (`sources / conversations / messages`). It also took on more ambitious analysis: segment scoring, idea extraction, ontology versioning, narrative coverage audits.

Megabase's value is that it took the messy past and made it queryable. But its scope kept expanding. By the time the schema covered ideas, segments, entities, and prompt-catalog entries, the act of "looking at my prompts" had become entangled with "evaluating ideas" and "scoring segments" and many other concerns.

## Layer 2 — MTGSLIDER's per-query log

In a different project — `C:\Dev\MTGSLIDER\conversation_log\Q##_*.md` — a small convention emerged: for each user query that produced real work, save a markdown file recording the **verbatim user input**, how the agent interpreted it, what was built, and what was deferred.

That convention turned out to be more important than the conversation log itself. It noticed that *the user's writing* (the prompt) is the load-bearing artifact in any LLM session. The output is a function of training; the prompt is a function of the user. To study the user's evolving thinking, you study the prompts.

## Layer 3 — the methodological move

A conversation in late April 2026 surfaced the explicit reframing: **prompts are clean signal; outputs are noise.** Studying the prompts in isolation gives you a corpus of your own cognition unsullied by AI artifacts. Even better: prompts that respond to outputs are doubly valuable — they're moments where the user has just been confronted with what their prompt produced, and their reaction (redirect, clarify, accept) is taste-in-real-time.

This is distant reading applied to the marginalia rather than the printed text. You learn more about a reader from their notes than from the book.

## Layer 4 — Promptarchaeology-Heldscalla

This tool. Read-only sibling to megabase. Defines TEMP SQL views over `megabase.db` that present only the user's prompts as a clean object. Saved queries surface specific patterns:

- First prompts (pre-influence framing)
- Redirects (real-time corrections)
- "What I'm actually trying to do" reveals
- Cascade-length distribution
- Theme/obsession lines by month
- Mood markers and interrupt-restarts

A separate utility (`chunk_cascade.py`) breaks the longest conversations — the 1000-page scholarly veins on Medieval Magic, Atalanta Fugiens, Tilton on Spiritual Alchemy, Magic in Shakespeare — into prompt-only chunks readable in a single sitting. Each chunk is essentially a quiet evening of reading just your own thinking on one topic.

## The Heldscalla frame

In Philip K. Dick's *Galactic Pot-Healer* (1969), the alien Glimmung summons skilled craftspeople from across the galaxy to help raise **Heldscalla** — an ancient cathedral sunk beneath the seas of Plowman's Planet. Joe Fernwright, the protagonist, is a pot healer: a restorer of broken ceramics. The work is patient, partial, and uncertain. Some who answer the call are absorbed into the Glimmung; some refuse; some keep working.

The corpus is Heldscalla. The prompts are the artifacts under the water. This tool is Joe's craft — bringing one cascade or pattern at a time into the light, ignoring the AI's outputs to surface only the user's own writing.

## What this project owes to what came before

| Prior project | Contribution |
|---|---|
| **Megabase** | The unified corpus and SQLite substrate. Without megabase there is nothing to query. |
| **MTGSLIDER's Q-log convention** | The conceptual move that "verbatim user input" is the artifact worth preserving. |
| **Claudiens / EmeraldTablet** | The DH discipline of treating personal scholarship as a corpus deserving of formal organization. |
| **The 33 PKD-themed planning skills** | The aesthetic register — Heldscalla, Joe Fernwright, the Glimmung — fits a skill-naming culture already established. |
| **The 1000-page scholarly cascades themselves** | The actual material. Without years of patient back-and-forth on Medieval Magic and Atalanta Fugiens, there'd be no cathedral to raise. |

Each prior project was necessary; none was sufficient. Promptarchaeology is what becomes possible when they're stacked.

## What this project deliberately does NOT do

- It does not modify megabase. Read-only forever.
- It does not analyze AI outputs. Outputs are excluded by methodological choice.
- It does not ingest new sources. Megabase's job.
- It does not score, segment, or rank prompts. Those are megabase's analytical concerns; this tool surfaces patterns, not judgments.

## What comes next

Each saved query in `queries/` is a hypothesis about what's worth surfacing. New queries accrete as new hypotheses occur. The project will probably never be "done" in the conventional sense — it will accumulate queries, accumulate reports, and slowly produce a second-order artifact: the analyst's journal of self-archaeological findings.

The 1000-page cascades will get chunked, one by one, and read at quiet evenings. That reading is the actual point. The tool just makes the reading possible.

*Joe Fernwright, late in the novel, raises a single broken pot from the depths and considers it. He does not know if Heldscalla itself will rise. He keeps working anyway.*
