# AUDIT_QUESTIONS — Diagnostic question bank for stuck or sprawling projects

**Date:** 2026-04-25
**Use:** When a project feels off but you can't articulate why, run these questions against it. Tired-mode-compatible: most are read-and-react. Pair with `/plan-runciter-audit` or run standalone.

---

## How to use

Pick ONE category that matches your hunch about what's wrong. Run those questions through the AI against the project. Capture answers in `AUDIT_<project>_<date>.md`. Don't act on findings tonight; review tomorrow.

---

## Category 1 — Scope drift

When a project has grown beyond what you remember agreeing to.

1. What was the original scope (per the earliest planning doc)? Quote it.
2. What's currently in the project that wasn't in that scope?
3. Which additions were deliberate decisions and which crept in?
4. Of the additions, which earned their keep? Which didn't?
5. If I deleted everything outside the original scope, would the project still be valuable?
6. Is there a decision log? If not, what should retroactively go in it?
7. What's the smallest version of this project that still does the core thing?
8. What was I hoping the additions would do, and did they do it?

---

## Category 2 — Architecture decay

When the code feels harder to reason about than it used to.

9. Where in the codebase do I keep "looking up the same thing"? That's where mental load is highest.
10. Which files have been touched most often in the last 3 months? `git log --name-only` then count.
11. Are there files that *should* change together but live apart?
12. Are there modules that do too much, or modules that exist only to forward calls?
13. What's the thing I'd do differently if I started over right now?
14. Of those things, which are cheap to fix retroactively? Which would require rewriting?
15. Is there a circular dependency I've been routing around?
16. Where do I have try/except that I added because something failed once?

---

## Category 3 — Documentation drift

When docs don't match the code.

17. Pick 3 random sections of CLAUDE.md. Are they still true?
18. Is there a doc that was important once and is now irrelevant?
19. Are there terms in docs that I now use differently in code?
20. What's been added to the project that no doc mentions?
21. What's deprecated in the docs but still in code?
22. Are the README's "how to run" instructions accurate today?
23. Do my code comments contradict my prose docs anywhere?
24. Which docs would be embarrassing if a stranger read them?

---

## Category 4 — Energy mismatch

When the project is taking more energy than it's giving back.

25. When was the last session where I left feeling good?
26. What in the project still excites me? What feels obligatory?
27. If I could outsource one part of this project, which part?
28. Is there a part of this I keep avoiding? What is it telling me?
29. Have I been working on parts that don't matter because they're easier?
30. What's the smallest thing that would re-spark my interest?
31. Is this project competing with something else for my attention?
32. What's the ratio of time spent thinking-about vs. working-on?

---

## Category 5 — AI-coding fragility

When sessions with the AI keep producing wrong-feeling output.

33. How much context do I load before doing any work? Is it under 30% of my window?
34. Where does the AI consistently get something wrong on this project? What do those mistakes have in common?
35. Are there facts in this project that exist in 3+ places (docs, code, memory)? Which is canonical?
36. Are there fixtures? Can I verify any output against expected?
37. When the AI proposes a change, can I test it cheaply, or do I have to read and judge?
38. What does my smoke test look like? If "doesn't have one" — that's the audit answer.
39. How often does the AI duplicate work because it doesn't know the existing function?
40. Is there an index/routing doc, or does the AI grep blindly?

---

## Category 6 — Dependency rot

When the boring stuff stops working.

41. When did I last update dependencies? `pip list --outdated`.
42. Is there a `requirements.txt` (or pyproject.toml, package.json) that matches what's installed?
43. Are there hardcoded paths that would break on another machine? `grep "C:" -r .`
44. Does the project have a `.python-version` or equivalent?
45. Are there scripts that work-only-by-luck?
46. What's the oldest piece of code in this project? Should it stay or be rewritten?
47. Are there imports that aren't used?
48. Are there packages I'm depending on that have alternatives I should consider?

---

## Category 7 — The "is this still mine" check

Every project should still feel like it belongs to you.

49. Could I explain this project to a friend without notes?
50. Do I know why each file exists?
51. Do I remember writing the code, or does it feel alien?
52. Is there a file I'm afraid to touch?
53. Is there architecture I inherited from the AI that I don't actually understand?
54. What would I do if all the AI assistance disappeared tomorrow?
55. Have I been following the AI's suggestions or my own taste?
56. What do I want this project to become that I haven't admitted yet?

---

## Category 8 — Closure readiness

When you suspect a project is done but haven't said so.

57. What hasn't changed in the last 3 months that you keep planning to change?
58. What part of the project would still be valuable if you stopped today?
59. What would have to be true for you to say "this is done"?
60. Is "done" actually attainable, or is it a moving target?
61. If a friend asked what this project does, what's the cleanest answer?
62. What would freezing this project look like in concrete terms?
63. What's the cost of keeping it active vs. freezing it?
64. Could parts be salvaged into another project if you froze the whole?

---

## Tired-mode subset

If you're running this audit tired, do ONLY these 10 questions. They produce useful output even at low energy:

- 1, 17, 25, 26, 33, 35, 38, 49, 57, 60

---

## Output template

When the AI runs an audit, ask it to format like this:

```markdown
# Audit: [project] — [date]

## Findings (max 5, ordered by severity)
1. [finding] — evidence: [where]
2. ...

## Surprises
- [things I expected to be problems but aren't]
- [things I didn't expect to be problems but are]

## Recommendations (DO NOT ACT TONIGHT)
- Quick wins (under 30 min each):
  - ...
- Meaningful changes (next fresh session):
  - ...
- Deep changes (require real planning):
  - ...

## Questions for me to answer
- ...
```

---

## Open questions for you

- Which of your projects is most overdue for an audit? Likely candidates: NSFRIPPER (drift acknowledged), REAPERBEYONDNES (vision-without-implementation), Megabase (state unknown).
- Do you want a `/loop monthly` reminder to audit the most stale project?
- Should audit findings auto-feed into PARKING_LOT.md per project?

Pick one project, one category, ten minutes. The audit habit is its own form of discipline.
