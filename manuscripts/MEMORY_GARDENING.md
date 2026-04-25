# MEMORY_GARDENING — A quarterly pruning protocol for your memory + apparatus

**Date:** 2026-04-25
**Use:** Your memory accumulates without garden-keeping. Skills proliferate. Docs go stale. CLAUDE.md files duplicate facts. This is the protocol for the seasonal cleanup that keeps the apparatus from rotting.

---

## Why a *quarterly* cadence

- Weekly is too often — you'll be cleaning the same files repeatedly
- Yearly is too rare — by then the rot is deep enough that pruning feels like demolition
- Quarterly maps to natural shifts in projects + interests; you'll have enough new material to evaluate but not so much that it's overwhelming

Schedule it. Treat it like daylight savings — a known recurring chore.

Suggested dates: solstices and equinoxes, if you like the aesthetic. Or 1st of January / April / July / October if you don't.

---

## The session shape (90 minutes, fresh-mode)

This is **not** tired-mode work. Memory gardening requires judgment about what's still true. Do it on a Saturday morning, coffee, no school.

Three passes, each 30 minutes:

### Pass 1 — Memory files (`C:\Users\PC\.claude\projects\C--Dev\memory\`)

For each file in the directory:

1. **Open it.**
2. **Read every entry.**
3. **For each entry, decide:**
   - **Keep as-is** — still accurate, still load-bearing
   - **Update** — partly true, needs correction (today's date, current state)
   - **Compress** — overstuffed, distill to essentials
   - **Move** — belongs in a project doc, not memory
   - **Delete** — no longer true, or never load-bearing

4. **Update `last_reviewed: YYYY-MM-DD`** on every kept file.

5. **Sync `MEMORY.md` index** — remove pointers to deleted files, add pointers to new ones.

**Specific entries you should always re-evaluate:**
- The "Pets" line in user_ted_profile.md — animals come and go (RIP Okie + Tex 2026)
- "Active project" lists in any memory — verify the project is still active
- "Current phase" in any project memory — phases shift
- Any retracted content (the Attila temperament case from MTGSLIDER Q24/Q25 — make sure it stayed reverted)

### Pass 2 — CLAUDE.md hierarchy (root + per-project)

Walk the CLAUDE.md tree:
- `C:\Dev\CLAUDE.md` (root — multi-project)
- Each project's CLAUDE.md (Claudiens, MTGSLIDER, NSFRIPPER, REAPERBEYONDNES, DOGSGAME, EmeraldTablet)
- Sub-project CLAUDE.md files if any

For each:
1. **Skim every section.** Is it still accurate? Still useful?
2. **Identify duplications.** What's said in this CLAUDE.md that's also in memory, in another doc, or in code? Pick ONE source of truth.
3. **Check the mandates.** Any rule that says "always run /plan-X first" — is it still being followed? If not, either reform yourself or remove the mandate.
4. **Trim cross-references.** Links to docs that no longer exist or have moved.
5. **Status block update.** If you have a status block, refresh it.
6. **Token-budget check.** Run `/plan-isidore-tokens` against the file. Trim if over budget.

### Pass 3 — Skills + scripts inventory

Walk `~/.claude/skills/` and your slash commands:

1. **List every PKD skill (`/plan-*`, `/write-*`).**
2. **For each, ask:** Have I used this in the last quarter? If yes — keep. If no — flag.
3. **For flagged skills:** Either delete, or confirm it's an "occasional but real" skill (e.g., once-a-year audits).
4. **Look for duplication across skills.** Two skills that do almost the same thing should merge.
5. **Look for missing skills.** Any task you've manually re-prompted 3+ times this quarter is a candidate for a skill — but **prefer parking** unless the recurrence is clear.
6. **Update skill descriptions** to reflect what they actually do, not what they were originally meant to do.

---

## Per-memory question template

For any memory entry you're uncertain about, ask:

- Is this still true?
- Is the date in the file recent?
- Have I referenced this memory in the last quarter (consciously or via Claude pulling it)?
- Does this memory contradict something I now believe?
- If a stranger read this, would they think it's load-bearing or trivia?
- Could this be three lines instead of fifteen?
- Does this belong in a project file instead of in memory?

---

## Suggested compression patterns

Most stale memory comes in these flavors. Here's how to prune each:

### Bloated narrative entries

Entry like: *"Project X is doing Y for reason Z, and last session we did A, B, C, and tomorrow we'll do D…"*

Compress to: *"Project X — current focus: Y. State as of [date]: ~50% complete on [thing]."*

The narrative belongs in git or in NEXT.md, not memory.

### Redundant project state

Memory says "phase 3A complete." Project's PHASESTATUS.md also says "phase 3A complete." Pick one location. Memory should point to the project doc, not duplicate.

### Stale "current project" lists

Lists of "currently active projects" decay fast. Move to a single `WHATS_HOT.md` at `C:\Dev` and update from there; don't list active projects in memory.

### Specific facts that are now wrong

When you find a fact that's wrong, fix it AND figure out why it persisted. If memory recorded a fact that you later contradicted in code, the contradiction is also data — what about your workflow let the contradiction live?

---

## A 5-minute mini-version (not a substitute for quarterly)

If you skipped a quarter and the full 90 minutes feels insurmountable, do this:

```
1. Open MEMORY.md
2. Pick ONE memory file at random
3. Open it. Read it. Update the date. Trim one paragraph.
4. /clear and walk away.
```

That's enough to keep rust from setting in. Better than nothing.

---

## The `consolidate-memory` skill workflow

Anthropic provides `anthropic-skills:consolidate-memory`. Use it as the *first* step in Pass 1:

```
1. Run anthropic-skills:consolidate-memory
2. It surfaces duplicates, stale entries, formatting issues
3. You decide what to act on
4. Then proceed with the manual passes above
```

This skill exists because memory hygiene is a known problem; lean on it.

---

## What to do with what you delete

Don't actually delete-delete. Use a `MEMORY_ARCHIVE/` directory:

```
C:\Users\PC\.claude\projects\C--Dev\memory\
  MEMORY.md
  user_ted_profile.md
  ...
  ARCHIVE/
    2026-04-25_session.md   ← bundle of deleted entries with date
    2026-07-15_session.md
```

Archive entries are searchable but don't affect current memory load. After 2 years in archive, evaluate again — may be safe to truly delete.

---

## Open questions for you

- Are you OK with quarterly cadence, or does monthly feel better?
- Should memory gardening be on a `/loop quarterly` reminder?
- Do you want me to do a first pass right now and surface candidates? I can run anthropic-skills:consolidate-memory and write up findings.
- The "Attila temperament" save/retract case — should we add a "retraction log" pattern to memory so future retractions leave a trail?
- Where should `WHATS_HOT.md` live if we adopt that pattern?

The first quarterly pass is the longest. Subsequent ones are 30 minutes. Worth doing.
