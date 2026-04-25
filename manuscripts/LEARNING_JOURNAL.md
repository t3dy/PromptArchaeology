# LEARNING_JOURNAL — Protocol + template + seed prompts

**Date:** 2026-04-25
**Use:** Build a single file that compounds your CS education over months. Tired-mode-friendly. Token-burn-converts-to-knowledge.

---

## Why this exists

You said: *"I'm having a million laughs and learning a lot about CS along the way."* Right now that learning evaporates. Each session ends; the insight goes with it. Six months from now, you'll have built more, but you won't be able to point to *what you learned* — just to *what you have*.

A learning journal fixes this. One file. Append-only. Searchable. Read it back annually and the line-of-progress is visible.

## The single rule

**One line per session, minimum.** That's it. If you have nothing else, write the one line. The discipline is the line, not the prose.

Format:
```
2026-04-25 — [project] — [one thing I learned, in plain English]
```

Examples:
```
2026-04-25 — MTGSLIDER — SQLite ATTACH lets you query across DBs without merging schemas
2026-04-26 — NSFRIPPER — APU length counters silence channels via different mechanisms per driver family
2026-04-27 — DOGSGAME — event sourcing means storing what happened, not what is
2026-04-28 — n/a — Python's contextlib.suppress is shorter than try/except/pass and reads better
```

That's enough. If you write only the one line for a year, you'll have ~250 entries that map your CS evolution.

## Optional: the long-form entry

When something genuinely surprised you, expand:

```
2026-04-25 — MTGSLIDER — SQLite ATTACH lets you query across DBs without merging schemas

Surprise: I assumed I'd have to ETL my alchemy_db and mtg_db into one mega-DB to join across them.
Actually: ATTACH lets you mount multiple DBs in one connection and write joins like
   SELECT a.term, m.card_name FROM alchemy.terms a JOIN mtg.cards m ON ...
Implication: my "federated SQLite" idea in MTGSLIDER/CONTEXT_ENGINEERING.md is a one-liner, not a project.
What I might do with this: rewrite three of my projects' multi-DB queries.
```

Five-field shape: **Surprise / Actually / Implication / What I might do.**

## 30 prompts that produce journal-worthy moments

Use these to *generate* journal entries. Run any of these post-session; capture the answer.

1. `What was the thing I just figured out, in one sentence a non-programmer could understand?`
2. `What did the AI suggest that I almost rejected but turned out to be right?`
3. `What pattern did this code have that I'd seen before but didn't have a name for?`
4. `What was the smallest change in this session that had the biggest effect?`
5. `What in this codebase confused me an hour ago and doesn't now?`
6. `If I were teaching this concept to a 10-year-old, what's the metaphor?`
7. `What would have saved me an hour today, that I now know for next time?`
8. `What CS idea did I bump into without knowing its name?`
9. `What assumption did I have walking in that turned out to be wrong?`
10. `What did the AI know that I didn't, that I now do?`
11. `What's a function I wrote today that I'd write more elegantly tomorrow?`
12. `What's a thing the language/library does for me that I was about to do manually?`
13. `What Python pattern emerged in my code today that I should add to my mental toolkit?`
14. `What's a debugging move I tried first that didn't work — and the move that did?`
15. `What part of the codebase did I touch today that's weirder than I realized?`
16. `What did I learn about my own thinking process today?`
17. `What's a question I should have asked at the start of this session that would have shortened it?`
18. `What did I avoid doing today that I'll regret tomorrow?`
19. `What's a name I gave to something today that's worse than it should be?`
20. `What's a connection between this work and something else I've built?`
21. `What's an analogy from outside CS that explains what I just did?`
22. `What's a thing I now know that contradicts something I wrote in my own docs three months ago?`
23. `What's a single keyword I should look up tonight that would make me smarter tomorrow?`
24. `What's the cheapest experiment I could run to learn something I currently guess about?`
25. `What's the riskiest assumption in the code I just wrote?`
26. `What library function did I almost reimplement before checking the stdlib?`
27. `What's a habit I noticed in myself today, good or bad?`
28. `What's a wrong turn that taught me something the right turn wouldn't have?`
29. `What did I read in this codebase that I want to steal?`
30. `What's the question this session left me with?`

## Weekly compression workflow

Once a week, run this:
```
1. /plan-fat-compress LEARNING_JOURNAL.md last 7 days
2. Output: a 200-word "this week in CS" paragraph at the bottom of LEARNING_JOURNAL.md
3. Tag the paragraph with WEEKLY_2026_W17 or similar
4. The original entries stay; the summary just adds a layer
```

Quarterly: read all weekly summaries. That's your CS journey, distilled.

## Yearly archaeology

End of year:
```
ask AI: "Read my LEARNING_JOURNAL.md. What's the throughline? What did I get good at?
Where did I stagnate? What's a curriculum the future me should follow based on the gaps?"
```

That output becomes next year's `CS_CURRICULUM_TED.md`.

## Open questions for you

- Do you want this in markdown or in a SQLite table? (Table = queryable. Markdown = greppable + readable.)
- Where should this live? `C:\Dev\LEARNING_JOURNAL.md` (top-level) or `C:\Users\PC\.claude\projects\C--Dev\LEARNING_JOURNAL.md` (memory tier)?
- Do you want an automated daily prompt via `/loop daily "Ask me what I learned today"`?

Pick one, start writing tonight, don't aim for fancy.
