# ESOTERIC_CS_MAPPING — Where your interests in alchemy / PKD / Marxism actually map onto CS concepts

**Date:** 2026-04-25
**Use:** You aestheticize your CS work with hermetic / PKD vocabulary. The previous critique called this "cosplay." Both readings are partly right. This file tries the *constructive* reading: where do these traditions genuinely illuminate CS concepts? Where are they decorative? When you know which is which, the aesthetic stops being a cost.

---

## The honest distinction

Not all aesthetic naming is the same. There are three categories:

1. **Genuinely illuminating.** The metaphor *teaches you something* about the CS concept that a literal name wouldn't. Worth keeping; the cost is real but the benefit is too.
2. **Mnemonically helpful.** The metaphor doesn't teach the concept but helps you *remember* it under fatigue. Acceptable. Costs real but small.
3. **Decorative.** The metaphor is just dress-up; nothing about the CS concept becomes clearer or stickier. Pure cost.

Most of your aesthetic naming is currently in category 3. Some is in 2. A surprising amount could be moved into 1 with a little rigor.

---

## Genuine mappings (Category 1) — keep these and lean in

### Alchemy → Compilation / Transformation pipelines

The alchemical *opus* is a multi-stage transformation: prima materia → nigredo → albedo → rubedo. Each stage has a state, a process, and a verification.

CS analog: a compiler. Source → AST → IR → optimized IR → bytecode → machine code. Each stage has a representation, a transformation, a verification.

**Why this is real:** Both traditions explicitly think about *what intermediate representations make sense*. Alchemists argued about whether nigredo had to precede albedo, just as compiler engineers argue about IR design. Your NSFRIPPER and REAPERBEYONDNES Frame IR work is *literally* in this register — choosing a canonical intermediate form is the alchemical move.

**Use it like this:** Next time you design an IR, ask "what is the state being transmuted, what's the visible color of this stage's output, what verification proves transmutation occurred." Not silly — these are the right questions. The alchemical vocabulary makes them memorable.

### Hermeticism → Symbol → Reference → Resolution

Hermetic correspondences: *as above, so below*. A symbol on one plane stands for something on another. The interpretive work is in the mapping.

CS analog: name resolution. Variable scopes. Symbol tables. Pointers. URI resolution.

**Why this is real:** Hermeticism gave Western thought a vocabulary for "this thing stands for that thing in a different domain." That's pointer thinking. That's symbolic linking. It's not metaphor; it's the same cognitive move.

**Use it like this:** When debugging a name-resolution bug (wrong variable found, wrong file imported), the question "where does this symbol find its referent" is hermetic exegesis. Naming the move helps.

### Philip K. Dick → Distributed systems / Concurrency / Consistency

PKD's obsessions: which version of reality is the real one? Whose memories can be trusted? When two characters disagree about what just happened, who's right?

CS analog: distributed consensus. CRDTs. Vector clocks. Read-your-own-writes. Consistency models.

**Why this is real:** PKD spent a career intuiting problems that the distributed-systems literature later formalized. *A Scanner Darkly* is essentially about an agent whose two views of the world fail to converge — a CAP-theorem story. *Ubik* is about replicated state with corrupting writes. These aren't decorative parallels; they're the same problem shape.

**Use it like this:** When you face an eventual-consistency problem, ask "what's the *Ubik* version of this?" The PKD framing makes you remember the question because it's a question you actually care about.

### Marxism → Resource economics / Performance accounting

Capital's labor theory + commodity fetishism: where does *value* come from in a system, and what hides it?

CS analog: performance accounting. Where do CPU cycles go? Where does latency get spent? What costs are hidden by abstraction layers?

**Why this is real:** Both traditions ask "where is the work *actually* happening, and what abstractions disguise it." When you profile a Python program and find that 80% of time is in an unexpected place, that's the same epistemic move as Marx asking where value is in a commodity.

**Use it like this:** When optimizing, ask explicitly "what abstraction is hiding the labor here." The Marxian framing makes the question feel important rather than tedious.

### Atalanta Fugiens emblems → Visualization / dashboards

Each emblem of *Atalanta Fugiens* combines motto + image + epigram + score — four redundant encodings of one alchemical idea.

CS analog: good dashboards combine multiple representations of one underlying state. A row in a database, a metric in Grafana, a chart, a colored cell — same data, different sensory channels.

**Why this is real:** Maier was solving a UX problem: how do you make an abstract idea memorable through multiple modalities? The emblem-book design is multimodal information design. So is a good observability dashboard.

**Use it like this:** When designing UI for any of your DH projects, think emblematically: motto (one-line label), image (visualization), epigram (caption), score (sortable metric). Strong design pattern.

---

## Mnemonic mappings (Category 2) — keep but don't oversell

### PKD characters → Slash command names

Joe Chip (broke, dignified, observant) → `/plan-joe-chip-scope`. The character is *useful* for remembering "scope means asking what minimal resources will let you proceed." But the character isn't *teaching* you scoping; it's helping you recall it.

This is fine. It's the same trick teachers use with mnemonic devices. As long as you remember the mnemonic isn't doing the teaching, you keep the benefit and avoid the trap.

**Where this becomes Category 3:** When you forget what `/plan-deckard-boundary` does and you have to look it up. Then the mnemonic isn't earning its keep.

**Diagnostic:** Skill descriptions you can't recall from the name = Category 3. Skill descriptions you *can* recall from the name = Category 2.

### Hermetic operational vocabulary in REAPERBEYONDNES

THE_LITURGY, THE_GAZETTEER, THE_MEMORY_PALACE — these are mnemonics for "the rules doc, the index, the memory store." They make the docs feel important and load-bearing.

This is borderline. The names *are* memorable. But "RULES.md, INDEX.md, MEMORY.md" would be just as memorable while being greppable. The cost-benefit tilts toward Category 3 because you sacrifice convention compatibility for atmosphere.

**Recommendation:** Either rename these to conventional names AND keep the hermetic atmosphere internal to the prose, OR commit to the bit and accept the search-friction cost.

---

## Pure decoration (Category 3) — fine to keep but don't pretend it's load-bearing

- Naming a project `EmeraldTablet` instead of `hermetic-database` — pure aesthetic. No CS insight gained.
- Calling a status doc `THE_LIMINAL_THRESHOLD.md` — atmosphere, not function.
- Skill names like `/plan-eldritch-swarm` — vibes-based.

**Honest reading:** Decoration is fine. You enjoy it. It's part of why you're still building. Don't apologize. Just don't oversell — these names aren't earning anything, and that's OK.

---

## A practical exercise

Go through your CLAUDE.md mandates and aesthetic vocabulary. For each named thing, ask:

- **Could a reader infer what this does from the name?** If no → Category 3.
- **Does the metaphor teach me something about the underlying concept?** If yes → Category 1.
- **Does the metaphor help me *remember* the concept under fatigue?** If yes → Category 2.

Keep Category 1. Audit Category 2 (do you actually remember it?). Be honest about Category 3 (it's decoration, not engineering).

---

## Reading list to deepen Category 1 mappings

Since some of your aesthetic naming is *almost* doing real work, these books would tighten the bridge:

- *The Reflective Practitioner* — Donald Schön. Why expert intuition is structured.
- *Computers as Theatre* — Brenda Laurel. Drama theory applied to UI.
- *Surfaces and Essences* — Hofstadter & Sander. Analogy as the core of cognition.
- *The Information* — James Gleick. History of "information" as a concept across disciplines.
- *Cybernetics and the Origin of Hermes* (working title; doesn't exist) — write it yourself someday.

These would let you tell the difference between "alchemy is metaphor for compilers" (Category 3) and "alchemy and compilation are both species of the broader cognitive pattern of staged symbolic transformation" (Category 1). The second framing is real.

---

## Open questions for you

- Which mappings feel *most* alive to you? Those are worth doubling down on; the others can be decoration.
- Is there a writing project lurking here? "Esoteric CS" is a real and underrepresented register — *Distant Reading meets Alchemy meets Compilers*. Could be one essay. Could be the thing you actually publish someday.
- Are there mappings I missed? Marxist computing has a literature (Kontonatsios, Gere, Steyerl) — your interest in capital might map to GPU / accelerator economics in interesting ways.
- Should this file become a regular practice — quarterly add new mappings as they emerge?

The aesthetic isn't the enemy of the engineering. They share more than the critique allowed. Just be honest about which mappings earn their keep.
