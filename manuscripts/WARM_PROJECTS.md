# WARM_PROJECTS — Which of your projects can be "always-ready-to-extend"

**Date:** 2026-04-25
**Use:** A warm project is one where, on a tired evening, you can open the directory, add 30–100 lines, commit, and walk away feeling good. It needs no mental warm-up. This file maps which of your projects qualify, what their extension menus look like, and what's needed to warm up the cold ones.

---

## Criteria for warmth

A project is **warm** if all of these are true:

1. **Cheap startup.** `cd` + open editor + you know what to do, in under 60 seconds.
2. **Modular extension.** Adding one item (a deck, an entry, a card, a behavior) doesn't require touching architecture.
3. **Trustworthy state.** You can run a smoke command and know if it still works in <30 seconds.
4. **Bounded change.** A typical session adds <200 lines / 1 file / 1 row, not "refactor the engine."
5. **Low cognitive entry tax.** You don't need to re-read CLAUDE.md, MEMORY.md, or any planning doc to start.

If any one is false, the project is **lukewarm**. If multiple are false, **cold**.

---

## Per-project assessment

### MTGSLIDER — WARM ✓

- ✓ Cheap startup: `cd MTGSLIDER && python tools/regen_one.py` (if built)
- ✓ Modular extension: each theme is independent
- ✓ Trustworthy state: 29 tests pass; `pytest` is your smoke
- ✓ Bounded change: add one theme spec → bulk_generate produces new deck
- ✗ Cognitive tax: still has a PARKING_LOT, REFRAME_NOTES, and Q-log culture pulling you into meta-mode

**Extension menu (do any in 30 min):**
- Add one new theme spec to `tools/theme_specs.py` based on a card you played this week
- Add one new keyword to `writing/100_magical_keywords.md`
- Write one esoteric copy piece in `writing/`
- Improve one existing deck's speaker notes
- Run `mtg-historical-trip` skill on a card you're curious about
- Add one new style preset to the slideshow compiler

**To make warmer:** Build `tools/regen_one.py --theme NAME`. Stop authoring Q-log files for trivial sessions.

---

### Claudiens — LUKEWARM

- ✓ Cheap startup: cd, edit a markdown
- ✓ Modular extension: per-text, per-image, per-biography entries
- ~ Trustworthy state: pipeline rebuilds the site, but no smoke command
- ~ Bounded change: phase work creeps; "just one more feature" pattern
- ✗ Cognitive tax: DOCUMENTAIRTRAFFICCONTROL, PHASESTATUS, ONTOLOGY all front-load

**Extension menu:**
- Add one biography entry
- Add one missing image to an existing text
- Write one short paragraph for a concept page
- Tag one text with cross-references to others

**To make warmer:** Build `python scripts/smoke.py` that builds + serves the site locally with one command. Move PHASESTATUS into a 3-line block in CLAUDE.md.

---

### EmeraldTablet — LUKEWARM

- ✓ Cheap startup
- ✓ Modular extension
- ✗ Trustworthy state: "rebuild from db" smoke missing
- ~ Bounded change
- ✗ Cognitive tax: 5 content types each at unknown completion

**Extension menu:**
- Add one biography
- Add one concept entry
- Cross-reference two existing entries
- Improve one weak entry

**To make warmer:** Pick ONE content type as the warm one (concepts? biographies?). Make extending that type the trivial path. Other types stay lukewarm and that's fine.

---

### NSFRIPPER — COLD

- ✗ Startup is heavy: ROM acquisition, driver detection, environment setup
- ✗ Modular extension: each new game requires nontrivial driver work
- ~ Trustworthy state: rendering works, but no fixture suite to verify nothing broke
- ✗ Unbounded change: every fix is "one more rule"
- ✗ Heavy cognitive tax: many docs, two DSP codebases

**Tired-mode access via:** read existing outputs, listen to BESTOUTPUT/ samples, write listening notes. Don't try to *extend* NSFRIPPER tired.

---

### REAPERBEYONDNES — COLD

- ✗ Whole project is currently architecture and vision; no warm extension surface
- THE_LITURGY mandates pre-load — anti-warmth by design

**Tired-mode access:** none recommended. Don't open this when tired.

---

### DOGSGAME — COLD (becomes WARM after v1 ships)

Currently planning-only. After a v1 prototype exists:
- ✓ Adding a new behavior (B011, B012...) becomes warm
- ✓ Extending dialogue lines becomes warm
- ✓ Adding new yard tiles becomes warm

**Tired-mode access right now:** Capture a new dog observation as a B### file in `canon/behaviors/`. That's it. Don't touch design/.

---

### Megabase — LUKEWARM

- Depends on what's currently built (you should write STATUS.md to clarify)
- Once a query interface exists, adding new saved queries is warm

**Extension menu (once interface exists):**
- Add a new saved query
- Tag corpus entries
- Run a query and capture insights

---

### PKD Fest 2026 site — LUKEWARM

- ✓ Cheap startup
- ✓ Modular extension (events, schedule items, speaker bios)
- ~ Trustworthy state depends on Vercel preview being stable
- ✓ Bounded change (text edits mostly)
- ~ Cognitive tax minimal

**Extension menu:**
- Add one schedule item
- Add or polish one section of copy
- Tweak one design token in the VALIS palette
- Add one image asset

---

### dungeon-architect — UNKNOWN (probably cold)

You haven't touched it recently per memory. Run `/plan-tagomi-briefing` on it before declaring warmth.

---

## Strategy: pick ONE warm-by-default project

**Recommendation:** Make MTGSLIDER your default warm project.

Reasons:
- It's the warmest already
- Each addition (theme spec, keyword, deck regen) is bounded
- The PKD/alchemy/MTG aesthetic is the part of your work that produces "the laughs"
- Adding to it doesn't fight the urge-to-architect

**Discipline:** When you sit down post-school and feel cooked, the default move is `cd MTGSLIDER`. Only deviate when there's a specific reason. That single rule prevents a lot of drift.

---

## What converts a cold project to warm

For any cold project, three concrete moves warm it up:

1. **One smoke command.** `make smoke` or `python tools/smoke.py` that exits 0 if the project still works.
2. **One extension entry point.** A single command that adds one new item (deck, entry, behavior, etc.) without touching architecture.
3. **A `WARM_MENU.md` at the project root.** A 1-page list of "things you can do in this project in 30 minutes when tired." When you open the project, you read this first.

Do this once per project; the warmth lasts for months.

---

## Open questions for you

- Is MTGSLIDER actually the right default? Or does Claudiens give you more dopamine when you extend it?
- Are there projects I missed that should be assessed (e.g., MarxistTradition, capital_interpreter, BachStudies)?
- Would a `WARM_MENU.md` per project actually help, or is one global file better?
- What's your post-school energy floor? If it's truly zero on some days, "warm" might still be too high a bar — what would `EVEN_COLDER_MODE.md` look like?

Pick one warm-by-default project. Stop trying to keep all 8 warm. Heat is a budget.
