# PROJECT_BRIEFINGS — Drop-in templates that re-orient future-you cold

**Date:** 2026-04-25
**Use:** Each active project should have a 1-page briefing that future-tired-you can read in 90 seconds and know exactly where to start. This file gives you the template, the questions to ask yourself, and stub briefings for each active project that need YOUR input to complete.

---

## The template

Every project's briefing fits this shape. Save as `BRIEFING.md` in the project root, or as a 1-paragraph block at the top of `CLAUDE.md`.

```markdown
# [Project] Briefing — last updated YYYY-MM-DD

## In one sentence
[What this project is and who it's for. Don't be poetic; be functional.]

## State right now
- Phase: [exploration / building / shipping / frozen]
- Last commit: [date + 5-word description]
- What's hot: [the one or two files I'm actively touching]
- What's stuck: [the blocker, if any]

## Tired-mode entry
"When I open this project tired, the smallest useful thing is: [one sentence]."

## Fresh-mode entry  
"When I open this project rested, the next real move is: [one sentence]."

## Don't touch
[Files / directories that look inviting but are speculative or load-bearing.]

## Smoke test
[One command that tells me if the project still works.]

## Open questions for me
- [Question 1 — what I haven't decided yet]
- [Question 2]
```

---

## Why this works

It compresses the project's load-bearing context into something that fits in working memory. Without it, future-Ted has to:
- Read CLAUDE.md
- Read PHASESTATUS.md
- Skim the most recent commits
- Guess

With it: 90 seconds. One paragraph. Move.

The two "modes" matter — having both tired and fresh entry points means tired-you doesn't have to *decide* what to do; the briefing already chose.

---

## Stub briefings — fill these in yourself (questions for you below each)

### MTGSLIDER

```
In one sentence: An MTG slide-deck generator that pairs themes with esoteric/alchemical research overlays, intended to inform [???].

State right now:
- Phase: building (slice 1 done; slice 2 parked)
- Last commit: [check git]
- What's hot: writing/100_magical_keywords.md, deck regeneration
- What's stuck: [???]

Tired-mode entry: "Open writing/100_magical_keywords.md and add one keyword."
Fresh-mode entry: "Pick one of the 98 generated decks and edit speaker notes by hand."

Don't touch: PARKING_LOT.md (only as reference), the slideshow compiler architecture.

Smoke test: pytest tests/

Open questions:
- [???]
```

**Open questions for YOU:**
- Who is this project for, when you're being honest? Yourself? MTG creators? An imaginary audience? The honest answer goes in the "for [???]" slot.
- What's actually stuck in MTGSLIDER right now? (Or is it just slow because it's deprioritized?)

---

### Claudiens

```
In one sentence: A digital humanities site presenting H.M.E. De Jong's scholarship on Michael Maier's Atalanta Fugiens (1618), modeled on HPMarginalia's architecture.

State right now:
- Phase: building (3A done, 5A done, 3B+4 ready but not started)
- Last commit: [check git]
- What's hot: [??? — phase 3B work?]
- What's stuck: phase 3B/4 are READY but not built — why?

Tired-mode entry: "Add one missing image to an existing text page."
Fresh-mode entry: "Start phase 3B per docs/PIPELINE.md."

Don't touch: ONTOLOGY.md (the schema is decided), the SQLite → static-HTML pipeline architecture.

Smoke test: [???]

Open questions:
- [???]
```

**Open questions for YOU:**
- What's actually blocking phase 3B? Time, decisions, or interest?
- Does Claudiens have a smoke command? If not, building one is a 30-minute job that pays for itself.

---

### EmeraldTablet

```
In one sentence: A hermetic/alchemical reference database (biographies, concepts, eras, scholars, texts) with a static site frontend.

State right now:
- Phase: building (5 content types at varying completion)
- Last commit: [check git]
- What's hot: [???]
- What's stuck: cross-references aren't queryable; no rebuild-smoke command

Tired-mode entry: "Add one entry to whichever content type is closest to 70% populated."
Fresh-mode entry: "Pick a target % per content type. Audit current state. Decide which to push."

Don't touch: HERMETICDB schema (working as-is), cross-references with Claudiens (parked).

Smoke test: [???]

Open questions:
- Which content type is closest to ready?
- Are you going to ship this as standalone or fold parts into Claudiens?
```

**Open questions for YOU:**
- Which content type is closest to "fully populated"? Biographies, concepts, eras, scholars, or texts?
- Do you want EmeraldTablet to merge with Claudiens eventually, or stay distinct?

---

### NSFRIPPER

```
In one sentence: NES music extraction pipeline (ROM → frame IR → MIDI / REAPER / JSFX), 321 games extracted.

State right now:
- Phase: maintenance / asymptotic improvement
- Last commit: [check git]
- What's hot: [???]
- What's stuck: stems vs JSFX drift, driver coverage cap, disk management

Tired-mode entry: "Open BESTOUTPUT/, listen to one track, write 50 words on what's good and what isn't."
Fresh-mode entry: "Pick the next driver-family parser and decide if it's worth implementing."

Don't touch: REAPERBEYONDNES (sister project, leave alone), the stems/JSFX drift in tired hours.

Smoke test: [???]

Open questions:
- What does "done" look like for NSFRIPPER? Coverage? Quality? Audience?
- Is REAPERBEYONDNES the closure of NSFRIPPER or its replacement?
```

**Open questions for YOU:**
- Define "NSFRIPPER done" in one sentence. The most useful thing here is probably to declare it done at current state.
- Is the sister-project pattern (NSFRIPPER → REAPERBEYONDNES) actually working for you, or is it a way to avoid finishing?

---

### REAPERBEYONDNES

```
In one sentence: Multi-system chiptune extraction + arrangement + synthesis successor to NSFRIPPER.

State right now:
- Phase: vision-only; SN76489 vertical slice spec exists, not built
- Last commit: [check git]
- What's hot: [nothing — or be honest if something is]
- What's stuck: vision exceeds vertical slice progress

Tired-mode entry: DO NOT OPEN.
Fresh-mode entry: "Execute HANDOVER_03 (SN76489 slice). Stop adding vision docs."

Don't touch: THE_LITURGY, VISION.md, Memory Palace, Gazetteer (all done; revisiting them is procrastination).

Smoke test: [doesn't exist yet]

Open questions:
- Until the SN76489 slice runs end-to-end, is anything else worth adding?
```

---

### DOGSGAME

```
In one sentence: Text-adventure life sim of four real dogs in a real yard (Sultan, WA).

State right now:
- Phase: exploration (no code yet)
- Last commit: [check git]
- What's hot: behavior catalog, design dialogues
- What's stuck: no event schema, no renderer protocol, no exit criterion for exploration

Tired-mode entry: "Capture one new dog observation as canon/behaviors/B###_*.md."
Fresh-mode entry: "Define event-row shape OR write the 100-line v1 (Okie + bush + TEXT renderer)."

Don't touch: design/ docs that are pure speculation (NOIR_LENS, SHAMANIC_VOYAGES, K9_PATROL).

Smoke test: [doesn't exist yet]

Open questions:
- What's the trigger that ends exploration? A date? A satisfaction threshold? Pressure from outside?
- Is the v1 (Okie + bush) actually the smallest useful thing, or could it be smaller?
```

**Open questions for YOU:**
- What ends "exploration phase"? Right now this is open-ended.
- If you could only build ONE behavior, would it actually be Okie/bush, or is there a more interesting one?

---

### Megabase

```
In one sentence: Personal Knowledge Archaeology System — corpus-level ingestion + analysis of your own chats, docs, notes, voice notes.

State right now:
- Phase: built across 8 sessions, exact state unclear
- Last commit: [check git]
- What's hot: [???]
- What's stuck: [???]

Tired-mode entry: "Run a query. Capture one surprising result in LEARNING_JOURNAL.md."
Fresh-mode entry: "Write STATUS.md: what's ingested, what's queryable, what's broken."

Don't touch: new ingestion pipelines until existing ones are documented.

Smoke test: [???]

Open questions:
- What does megabase currently do that you've forgotten about?
- What corpus is fully ingested vs. partially?
```

**Open questions for YOU:**
- This briefing is the most blank because I have the least info. What does megabase actually do right now? A 5-bullet honest answer would let me write a proper briefing.

---

### PKD Fest 2026 site

```
In one sentence: Co-built site for PKD Fest 2026 (with Paul Shelton), Next.js / Vercel, VALIS-themed.

State right now:
- Phase: building
- Last commit: [check git]
- What's hot: [???]
- What's stuck: [???]

Tired-mode entry: "Polish copy on one section."
Fresh-mode entry: "Deploy a preview, ping Paul, react to his feedback."

Don't touch: VALIS palette decisions if Paul has signed off.

Smoke test: npm run build

Open questions:
- What's Paul's last feedback?
- What does Paul most need next?
```

**Open questions for YOU:**
- Is the site at C:\Dev\pkd-fest-site or pkd-planning-site? Or both?
- When does this need to be "done" — the actual fest date sets a deadline.

---

## Maintenance

Run a `BRIEFING.md` refresh every 4–6 weeks per active project, OR whenever you spend more than 5 minutes re-orienting at session start. The latter is a signal the briefing is stale.

Tired-mode-friendly refresh:
```
/plan-tagomi-briefing [project path]
→ output → save as updated BRIEFING.md
```

That's it. The briefing maintenance cost is low if you commit to it; the savings compound every session.
