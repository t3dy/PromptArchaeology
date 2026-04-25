# TIREDPROMPTS — A copy-paste library for token-burn when fried

**Date:** 2026-04-25
**Use:** When you sit down post-school and need a prompt fast. Pick by energy level + intent. Paste, react, walk away.

---

## LOW energy — read & react (you generate ~10 words)

1. `Read [file path]. Tell me in 3 bullet points what it does. End with one question I should ask myself about it.`
2. `git log --since="1 week ago" --oneline. Summarize the past week in 100 words. What's the throughline?`
3. `I'm tired. In 200 words, walk me through what we did in our last session and where we left off.`
4. `Take my last voice note: [paste]. Compress to 5 bullet points. Don't add anything.`
5. `Look at C:\Dev\<project>. Tell me what's stale and what's hot. No advice — just observations.`
6. `Read [file]. Roast it gently. Three things that are weak.`
7. `Quiz me on [topic I claimed to learn last week]. Five questions. I'll guess; you grade.`
8. `Diff my LEARNING_JOURNAL.md from a month ago vs today. What did I learn?`
9. `Pick the most over-engineered file in [project] and explain in plain English why.`
10. `What's the smallest possible thing I could do in [project] in 20 minutes?`
11. `Read this paragraph I wrote: [paste]. Translate it into something a smart 10-year-old would understand.`
12. `Show me the first 30 lines of [unfamiliar file]. Annotate every block.`
13. `Look at my MEMORY_INDEX.md. Which entries feel stale? Just list them.`
14. `Open [project]/PARKING_LOT.md. Which 3 entries should I delete because they're dead?`
15. `Read the 5 most recent files in [dir]. What was I obsessed with?`

## MEDIUM energy — analyze & decide (you generate ~50 words)

16. `Read [project]/CLAUDE.md. Identify the 3 instructions that are too vague to act on. Suggest tighter wording.`
17. `Compare these two files [A] [B]. What's redundant? What's contradictory?`
18. `Look at my git history for [project]. Identify the moment I switched directions and explain why I might have.`
19. `Read [doc]. Now read [doc 2]. Are they consistent? Where do they diverge?`
20. `Take this rough idea: [paste]. Draft three different framings — minimal, ambitious, esoteric. I'll pick.`
21. `Survey the tools/ directory in [project]. Which scripts have I never run? Which look broken?`
22. `Audit the SQLite schema in [project]/db.sqlite. What field is misnamed? What table should be split?`
23. `Look at this Python file: [path]. Suggest one refactor under 20 lines that would meaningfully improve it.`
24. `Read [old planning doc]. Write a 3-sentence "what we should have done" retrospective.`
25. `My bash history shows I ran [X] command 12 times this week. Why might I be doing that? Suggest a script.`

## HIGH energy — design & commit (save these for fresh days)

26. `I want to add [feature] to [project]. Run /plan-joe-chip-scope. Frozen scope only — no extras.`
27. `Run /plan-deckard-boundary on [decision]. I need to know what's in vs. out of LLM territory.`
28. `Design a vertical slice for [feature]. Use /plan-runciter-slice format. Include acceptance gate.`
29. `I'm choosing between [A] and [B] architecturally. Run /plan-bohlen-constraint to surface what constrains the decision.`
30. `Stand up the smallest end-to-end version of [project] in one file. Constraint: under 150 lines.`

## Crisis prompts — when the urge to start something new hits

31. `I want to start a new project called [X]. Talk me out of it. Be specific about what existing project this rhymes with.`
32. `I'm about to make a new skill called /plan-[name]. Steel-man and then attack. Should I park it instead?`
33. `I want to add a THE_*.md to [project]. Diagnose the urge. What am I avoiding?`
34. `I keep wanting to refactor [X]. Is the urge real or aesthetic? Five questions to clarify.`
35. `I'm tempted to rebuild [project] from scratch. Read the existing version first. Veto if appropriate.`

## Joy prompts — for the laughs

36. `Show me three weird Magic cards from MTG history I probably don't know. Tell me what's funny about each.`
37. `Pick a PKD novel I haven't mentioned. Pitch me a one-paragraph adaptation set in [random domain].`
38. `Generate a fake hermetic axiom that sounds Renaissance but is actually about software bugs.`
39. `Translate one of my existing Python functions into a parable. Keep it short.`
40. `What would [my project] look like if it were a Bach fugue? Map components to voices.`
41. `Roast my project naming choices in the style of a 17th-century alchemist who is unimpressed.`
42. `Write a 4-line poem in the voice of one of my dogs about my coding habits.`
43. `Generate one absurd MTG card whose mechanic depends on knowing my CLAUDE.md instructions.`
44. `Imagine a future archeologist excavating C:\Dev. Write their field notes.`
45. `Give me a tarot card whose meaning is "this PR has too many files."`

## Archaeology prompts — visiting old work

46. `What's in [old project] that I've forgotten? Briefing in 300 words.`
47. `Pick the most interesting file in [old project] I haven't touched in 3 months. Tell me why it's interesting.`
48. `Read [old conversation log]. What was I trying to figure out? Did I figure it out?`
49. `Diff [old project]'s structure 6 months ago vs now. What got abandoned?`
50. `What promise did I make myself in [old README] that I haven't kept? No judgment, just observation.`

## Cleaning prompts — useful junk-drawer work

51. `Find all TODO and FIXME comments across [project]. Bucket them: real, dead, aspirational. I'll triage your buckets.`
52. `Find duplicate-ish files across [project]. Suggest merges.`
53. `Look at my dependencies. Which ones could I remove?`
54. `Find files I've imported but never actually use.`
55. `Generate a .gitignore review — what should be in it that isn't?`

## Tutoring prompts — convert tokens to knowledge

56. `Explain [CS concept] using a metaphor from my interests (PKD / alchemy / MTG / NES audio).`
57. `Show me three different ways to write [function I just wrote]. Explain tradeoffs.`
58. `Walk me through how SQLite stores a B-tree. Use diagrams in ASCII.`
59. `Read [Python file in my project]. Quiz me on what it does. Five questions.`
60. `Pick a design pattern I'm probably using accidentally. Name it and show me how to use it deliberately.`

---

## Usage rules

- Don't pick more than ONE prompt per session.
- If a prompt's output makes you want to start something — `/plan-abendsen-parking` it.
- Save outputs you like into `LEARNING_JOURNAL.md` or `IDEAS.md`.
- If you're tempted to "just one more prompt" past 90 minutes, `/clear` instead.
- These prompts are tools, not assignments. Most of them you'll never use. The point is to have them ready when the brain fog says "what should I even do."
