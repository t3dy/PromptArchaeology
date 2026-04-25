# CS_CURRICULUM_TED — A personalized path tuned to your interests and projects

**Date:** 2026-04-25
**Use:** Stop reading random tutorials. Pick a path. Each path connects to a project you already have, so learning compounds with building.

---

## The principle

Generic CS curricula don't fit you. You're not trying to get hired; you're not trying to follow a formal degree path. You're a builder with strong aesthetic interests (PKD, alchemy, esoterica), real Python/SQLite chops, and 8 active projects. The right curriculum is one that turns each existing project into a vehicle for learning a specific CS area.

Six paths. Pick ONE. Run it for 8 weeks before adding another.

---

## Path 1 — PARSERS (vehicle: NSFRIPPER, MTGSLIDER decklist parsing)

**Why this fits you:** You already write driver-family parsers for NES games. You parse decklists. You ingest scholarly databases. Parsing is a core CS skill you do constantly without naming it.

**The book:** *Crafting Interpreters* by Bob Nystrom (free online).

**The 8-week arc:**
- Weeks 1–2: Parts I + II (tree-walk interpreter for Lox)
- Weeks 3–4: Apply to NSFRIPPER — rewrite one driver-family parser using a proper lexer/parser split
- Weeks 5–6: Build a tiny DSL for MTG decklist queries — `cards where mana_cost <= 3 and color contains W`
- Weeks 7–8: Either continue Crafting Interpreters Part III (bytecode VM) or apply patterns elsewhere

**Prompts to fire weekly:**
- `Read my [parser file]. Identify which parts are doing tokenization vs parsing vs evaluation. Are they tangled?`
- `Take this regex-based parser: [paste]. Rewrite as recursive descent. Show me the tradeoffs.`
- `Quiz me on the difference between LL and LR parsing. Use my NSFRIPPER drivers as examples.`

**Endpoint:** You can read any parser in any codebase with confidence and write a clean one when needed.

---

## Path 2 — DATABASES (vehicle: EmeraldTablet, Claudiens, Megabase, MTGSLIDER, your "federated SQLite" idea)

**Why this fits you:** You have at least 6 SQLite databases across projects. You've written FTS, you've sketched federated queries, you've mused about vector stores. You're a database person who hasn't read the database book.

**The book:** *Designing Data-Intensive Applications* by Martin Kleppmann.

**The 8-week arc:**
- Weeks 1–2: Chapters 1–4 (foundations, encoding, replication basics)
- Weeks 3–4: Apply — design a real federated query layer across two of your DBs (alchemy_scryfall + Claudiens, say)
- Weeks 5–6: Chapters 5–9 (replication deep, partitioning, transactions). Apply: implement WAL-aware backups across your DBs.
- Weeks 7–8: Chapters 10–12 (batch, stream, future). Apply: an event-sourced micro-architecture for DOGSGAME.

**Prompts to fire weekly:**
- `Read my schema [path]. Identify the third normal form violations. Tell me which ones are actually fine and which need fixing.`
- `Walk me through how SQLite's WAL works. Use my [project] as a case study.`
- `Explain CAP theorem using my projects as examples. Which ones are CP, which are AP, which are CA-by-being-single-node?`
- `Show me how an event-sourced DOGSGAME differs from a state-storing DOGSGAME, in concrete schema terms.`

**Endpoint:** You can choose between datastores knowingly. You can talk about consistency models. Your SQLite use becomes deliberate, not habitual.

---

## Path 3 — DSP & AUDIO (vehicle: NSFRIPPER, REAPERBEYONDNES)

**Why this fits you:** You've spent months on chiptune extraction. You've hit hard problems (non-linear DAC mix, length-counter idiosyncrasies). You're already inside DSP without the formal underpinnings.

**The books/resources:**
- *The Scientist and Engineer's Guide to Digital Signal Processing* by Steven W. Smith (free online)
- *Audio Programming Book* (Boulanger, Lazzarini, eds.) — chapters on synthesis
- ChibiAkumas chiptune resources (informal but on-topic)

**The 8-week arc:**
- Weeks 1–2: DSP basics (sampling, aliasing, FFT). Apply: write a tiny WAV analyzer that prints fundamental frequencies.
- Weeks 3–4: Filter design (FIR, IIR, biquads). Apply: write a biquad lowpass in Python and one in JSFX. Compare outputs against `scipy.signal`.
- Weeks 5–6: Synthesis (additive, subtractive, FM, wavetable). Apply: build a 30-line wavetable synth that matches your NES triangle channel.
- Weeks 7–8: Mix & master fundamentals. Apply: master one NSFRIPPER track to broadcast loudness standards.

**Prompts to fire weekly:**
- `Explain why my non-linear DAC mix is approximate. Show me the math.`
- `Why does the NES triangle channel "hold" DAC value on gate-off? What's the physics?`
- `Walk me through how a biquad coefficient set encodes a filter response. Use my JSFX code.`
- `Compare my JSFX synth to my Python stems for one frame. Where exactly do they diverge?`

**Endpoint:** The "two DSP codebases drift apart" problem becomes a *measurable* problem you can characterize and solve, not a fogged hard problem.

---

## Path 4 — DISTANT READING / CORPUS NLP (vehicle: Megabase, your ChatGPT/Claude exports)

**Why this fits you:** You want to understand your own intellectual evolution. You have years of LLM chats. You've sketched megabase. This is the path that turns introspection into method.

**The books/resources:**
- *Speech and Language Processing* by Jurafsky & Martin (3rd ed., free online)
- Franco Moretti's *Distant Reading* (the humanities side)
- Voyant Tools / spaCy / Hugging Face docs as reference

**The 8-week arc:**
- Weeks 1–2: Tokenization, basic stats (TF-IDF, word frequencies). Apply: top-50 words in your ChatGPT exports per quarter.
- Weeks 3–4: Topic modeling (LDA, BERTopic). Apply: produce a topic-shift chart across 24 months of your output.
- Weeks 5–6: Embeddings + similarity. Apply: build a semantic search across all your project README files.
- Weeks 7–8: One real essay: *"What Distant Reading of My Own LLM Sessions Reveals."* 1,500 words. Anchored in actual data.

**Prompts to fire weekly:**
- `Walk me through TF-IDF using my own corpus as the example.`
- `What's the difference between LSA and BERTopic, and which fits my "introspect my chats" use case?`
- `Read this paragraph from one of my old chats. What latent assumptions does it carry?`

**Endpoint:** Megabase becomes a real tool, not a planned tool. You produce one essay other humans could read about your own thinking.

---

## Path 5 — GAME LOGIC & EVENT SOURCING (vehicle: DOGSGAME, dungeon-architect)

**Why this fits you:** You sketch games but don't ship them. The blocker isn't "I don't know how to code games." It's that you haven't internalized the patterns (entity-component, event sourcing, fixed-timestep update). Once those click, DOGSGAME could be 200 lines.

**The book/resources:**
- *Game Programming Patterns* by Robert Nystrom (free online)
- Roguelike Development resources at /r/roguelikedev FAQ

**The 8-week arc:**
- Weeks 1–2: Read patterns 1–8. Apply: refactor DOGSGAME's planned architecture to one named pattern.
- Weeks 3–4: Implement DOGSGAME v1 (Okie + bush) in 200 lines using event sourcing.
- Weeks 5–6: Add the second behavior (Tex belly-roll) and notice what generalizes.
- Weeks 7–8: Implement a bare bones save/replay using event log alone. The whole game state is a fold over events.

**Prompts to fire weekly:**
- `Explain entity-component-system using DOGSGAME's four dogs as a worked example.`
- `Show me three ways to implement DOGSGAME's event bus, weakest to strongest.`
- `Why is event sourcing perfect for a game where dogs have moods that depend on history?`

**Endpoint:** A playable DOGSGAME prototype. Pattern fluency that transfers to dungeon-architect, MTG simulators, and anything else game-like.

---

## Path 6 — STATIC SITES & BUILD PIPELINES (vehicle: Claudiens, EmeraldTablet, MTGSLIDER, PKD Fest)

**Why this fits you:** You have ~5 sites that should deploy cleanly. The shared substrate is "data → templates → static HTML." Doing this *well* once unlocks all of them.

**The books/resources:**
- Eleventy / Astro / Hugo docs — pick one
- *The Pragmatic Programmer* (Hunt & Thomas) on build pipelines
- GitHub Actions docs for CI

**The 8-week arc:**
- Weeks 1–2: Pick a static site generator (recommend Eleventy for Python-friendliness). Build a tiny dummy site.
- Weeks 3–4: Migrate ONE existing project (e.g., EmeraldTablet) to it. Notice what generalizes.
- Weeks 5–6: Set up GitHub Actions to build + deploy automatically.
- Weeks 7–8: Apply the pattern to a second site. The third is a copy job.

**Prompts to fire weekly:**
- `Compare Eleventy / Astro / Hugo for my use case. Pick one. Defend it.`
- `Walk me through how my SQLite → static HTML pipeline could be expressed as Eleventy data files.`
- `Show me the GitHub Actions YAML for a pipeline that runs python scripts THEN builds the site.`

**Endpoint:** A unified deploy story across your DH sites. Future sites take a day, not a month.

---

## Open questions for you

- Which path resonates first? My guess: **Path 2 (Databases)** because it touches the most projects, OR **Path 1 (Parsers)** because it builds a fundamental skill you exercise weekly without naming.
- Are 8 weeks the right cadence? Could be 12 if energy is variable.
- Do you want a `/loop weekly` reminder to do the prompts? Easy to set up.
- Should the curriculum live as one file per path or one combined file?

Pick a path. Set up `LEARNING_JOURNAL.md` first. Run the curriculum's prompts in tired-mode sessions; do the project work in fresh-mode sessions. Compounds over months.
