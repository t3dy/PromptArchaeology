# SKILLSRIFFING — Composing your skill apparatus for tired-mode, exploratory, learning-rich sessions

**Date:** 2026-04-25
**Reframe:** Your skills are not a shipping pipeline. They are a toolkit for getting useful work done under variable energy, with the AI as a thinking partner. This document maps which skills + native commands to compose for which mental state, with prebuilt riffs (skill chains) you can memorize.

---

## The core principle

Your skills are instruments. You don't pick a "right" skill — you **riff** on them. Some skills are loud (architecture-level decisions); some are quiet (single-page captures). Tired-mode sessions need quiet skills. Fresh-mode sessions can handle loud ones. Between them you can build short *riffs* — 2–4 skill chains — that turn an aimless hour into a small, durable artifact: a journal entry, a parked idea, a compressed transcript, a cleaned-up file.

This is not a skills reference manual. This is a tactical guide for *which combinations actually work under what conditions*.

---

## The energy ladder

Sort skills by what you can do at each energy level. **Match skill weight to your weight.**

### LOW (Wiped — post-school, evening, half-attention)

These skills require minimal generation. You react, you read, you let the AI synthesize.

- `/plan-abendsen-parking` — capture without evaluation. **Crown jewel of tired mode.**
- `/plan-fat-compress` — squash a sprawling doc into something small. Receptive work.
- `/plan-arctor-retro` — look back at what you did. No new generation required.
- `/write-isidore-critique` — AI critiques something you already wrote. Read, react.
- `/write-archer-evaluate` — same shape, evaluator mode.
- `anthropic-skills:consolidate-memory` — pure janitorial: prune, dedupe, fix dates.
- Native: `/clear` — reset and walk away. A legitimate move.

### MEDIUM (Coherent, low-creative)

You can hold a small structure in your head; you can react to medium-length output.

- `/plan-tagomi-briefing` — briefing on a project. AI synthesizes; you read.
- `/plan-runciter-audit` — failure audit. Reads existing work, surfaces issues.
- `/plan-mayerson-prereq` — prereq check. Diagnostic.
- `/plan-buckman-critic` — prompt review. Refines without committing.
- `/plan-isidore-tokens` — token-budget review of a context.
- `/plan-mercer-reframe` — reframe a request. Light cognitive load.
- `/plan-regan-simplify` — simplify a thing. Subtractive, low-effort.
- `/write-runciter-ux` — UX audit of a website you already built.
- Built-in: `prompt-review`, `complexity-brake`, `failure-audit`, `simplify`.

### HIGH (Fresh, can hold structure in head, can decide what you'll live with)

These are commitment-level skills. Use only when rested. Outputs become load-bearing.

- `/plan-joe-chip-scope` — scope a new thing. Real decisions.
- `/plan-runciter-slice` — design vertical slices.
- `/plan-deckard-boundary` — AI/LLM boundary calls.
- `/plan-bohlen-constraint` — constraint-first design.
- `/plan-buckman-execute` — convert plan to task list.
- `/plan-steiner-gate` — phase gate. Load-bearing decisions.
- `/plan-kevin-pipeline` + `/plan-isidore-tokens` — pipeline architecture.
- `/plan-rosen-artifact` — define what artifact you're producing.
- `/plan-freck-narrative` — narrative architecture.
- `/plan-brady-graph` — graph design.
- `/plan-bulero-refactor` — refactor design (planning, not executing).
- `/plan-eldritch-swarm` — multi-agent design.
- Native: `/init`, `/review`, `/security-review`, `vertical-slice`, `constraint-first`, `scope-check`.

**Rule of thumb:** Tired-you using `/plan-deckard-boundary` produces a doc you'll regret tomorrow. Tired-you using `/plan-abendsen-parking` produces an idea preserved without commitment, which is exactly what you wanted.

---

## Session archetypes (and their riffs)

Fifteen pre-composed riffs. Memorize the shape; vary the contents.

### 1. Tired Tuesday — "I have an hour and zero brain"
```
/plan-abendsen-parking [whatever idea is rattling]
→ /plan-fat-compress [today's voice notes if any]
→ append one line to LEARNING_JOURNAL.md
→ /clear → done
```
Output: one parked idea, one compressed transcript, one journal line. Total cognitive cost: low.

### 2. Capture & Compress — "I'm full of half-thoughts"
```
voice notes / dump / paste raw thoughts
→ /plan-fat-compress
→ /plan-mercer-reframe (if the dump has a flawed premise)
→ save to project's IDEAS.md or PARKING.md
```
Use when you've been thinking *at* a project for days without sitting with it. Get thoughts out without trying to act on them.

### 3. Archaeology — "What was I doing in [old project]?"
```
/plan-tagomi-briefing [old project path]
→ /plan-arctor-retro
→ note what surprised you in LEARNING_JOURNAL.md
→ /plan-abendsen-parking [any next steps]
```
Best tired-mode visit to dormant projects. Re-orient without committing to advance.

### 4. Learning Loop — "Teach me what I'm doing"
```
read or write code with AI
→ "annotate what you just wrote and why"
→ "quiz me on what you just taught"
→ append answers + corrected misconceptions to LEARNING_JOURNAL.md
→ /plan-fat-compress weekly journal entries
```
The durable-CS-education riff. Pair every coding session with tutoring. Token-burn = knowledge.

### 5. Constraint Cone — "I want to start something but not big"
```
/plan-bohlen-constraint [problem]
→ if fresh: /plan-joe-chip-scope
→ if tired: /plan-abendsen-parking
→ tomorrow: /plan-runciter-slice
```
The constraint-first move is your guard against tired-Ted designing bloated v1s. If you can't articulate the constraint cleanly, park it.

### 6. Curriculum Builder — "I want to deliberately learn X"
```
/plan-taverner-curriculum [topic, e.g. "database internals"]
→ /plan-pris-pedagogy (what kind of learner am I for this?)
→ create LEARNING_PLAN_<topic>.md
→ schedule short sessions via /loop or /schedule
```
Converts vague "I should learn databases" into a concrete pedagogical plan. AI produces the curriculum; you execute in tired-mode-friendly chunks.

### 7. Cold Open — "I just want to play"
```
open a "warm" project (one that's always ready to extend)
→ make one tiny change
→ /write-chip-copy or /write-dekany-style if writing prose
→ commit with a real message ("playing with X")
→ done — no skills, no plan, just play
```
**Skills are optional.** Sometimes the right move is no skill at all. Protect your "having a million laughs."

### 8. Janitorial — "I can't think but want to feel productive"
```
anthropic-skills:consolidate-memory
→ /plan-isidore-tokens (review a CLAUDE.md, trim)
→ /plan-fat-compress an old sprawling doc
→ delete one stale file
→ commit "housekeeping"
```
Pure pruning. Zero creative load. Genuinely useful — your apparatus benefits from sweeping.

### 9. Reframe-and-Park — "I'm pulled in a new direction mid-build"
```
/plan-mercer-reframe [the new direction]
→ /plan-abendsen-parking
→ keep going on the old direction
```
The discipline you most need mid-session. The reframe captures the new idea legitimately; the park keeps it from derailing.

### 10. Audit Pass — "I have a bad feeling about this project"
```
/plan-runciter-audit
→ /plan-buckman-critic on the current plan
→ failure-audit (built-in)
→ note conclusions; do not act yet
```
Diagnostic, not corrective. Tired-you should never *act* on an audit — that's a fresh-day task. Auditing tired is fine.

### 11. Briefing-for-Tomorrow — "Set up future-fresh-me"
```
/plan-tagomi-briefing [current project state]
→ save as RESUME.md or NEXT.md
→ next morning: read it instead of cold-starting
```
Tired-you's best gift to fresh-you is a one-page briefing. This riff is specifically for tired-mode *preserving* fresh-mode productivity.

### 12. Aesthetic Pass — "I want the words to feel right"
```
/write-rachael-aesthetic [doc or page]
→ /write-dekany-style
→ /write-isidore-critique
→ revise prose
```
Pure prose riff. Good post-school activity if you're more in a wordsmith than coder mood.

### 13. UX Sweep — "I want to look at a website I built"
```
/write-runciter-ux [site or page]
→ note issues to PARKING.md
→ /plan-abendsen-parking the bigger ones
```
Read-only inspection. Don't fix tonight; capture for tomorrow.

### 14. Refactor Stub — "I see something ugly but won't fix it tonight"
```
/plan-bulero-refactor [target]
→ output goes into REFACTORS.md
→ do NOT refactor; just plan
```

### 15. Skill Forge — "I want to make a new skill" (RARE)
```
anthropic-skills:skill-creator
→ ONLY if a real recurring need exists, AND
→ run /plan-buckman-critic on the proposed skill spec FIRST
```
Be skeptical. New-skill-creation is itself a drift signal. Most "I should make a skill for this" tired-thoughts evaporate by morning. Park first.

---

## Native Claude Code slash commands as your harness

The native commands are infrastructure-level. Use them to shape the *session container*, not the work itself.

- **`/clear`** — your most underused tool. End a session by clearing rather than continuing into incoherence. Tired-you continuing past an hour produces messes.
- **`/init`** — bootstrap a new project's CLAUDE.md. One-shot. Use when starting a project, then never again.
- **`/loop <interval> <prompt>`** — recurring prompts. Tired-friendly uses:
  - `/loop daily "Ask me what surprised me today"` — one-line journal habit
  - `/loop weekly "Walk through C:\Dev and identify dormant projects"` — housekeeping
  - `/loop 30m "Time check — am I still on the original task?"` — drift-guard mid-session
- **`/schedule`** — heavier cron for background prompts. Pair with `anthropic-skills:schedule` if needed.
- **`/fast`** — toggle Opus 4.6 fast mode. Use for tired-mode reactive work where speed > depth.
- **`/help`**, **`/review`**, **`/security-review`** — situational. `/review` is the right move when looking at your own old code with fresh eyes.
- **`update-config`** — when a setting is annoying you. Tired-friendly: complain about something specific, get a config patch.
- **`less-permission-prompts`** — once a quarter, run this. Reduces friction for future sessions.
- **`keybindings-help`** — for shortcut tweaks. Low-energy quality-of-life work.

---

## Anthropic skills as utilities

Treat these as *boring infrastructure*, not creative tools.

- **`anthropic-skills:consolidate-memory`** — your memory directory needs garden-keeping. Run quarterly.
- **`anthropic-skills:setup-cowork`** — only when adding new tooling.
- **`anthropic-skills:pdf` / `pptx` / `docx` / `xlsx`** — file-operation utilities. Reach for these by file extension, not by feel. If you have a PDF: use the PDF skill. Don't compose a custom workflow.
- **`anthropic-skills:skill-creator`** — see Riff #15 caveat.

---

## A warm-up routine (3 minutes, every session)

```
1. Read NEXT.md or RESUME.md for the project (one paragraph).
2. Skim LEARNING_JOURNAL.md last 3 entries — what were you learning?
3. Decide energy level honestly: LOW / MEDIUM / HIGH.
4. Pick ONE riff above that matches that level.
5. Set a 30- or 60-minute timer.
```

This deliberately delays the urge to "just start" — which is when tired-you commits to overscoped work. Three minutes of orientation pays back the rest of the session.

---

## A cool-down routine (3 minutes, every session)

```
1. /plan-abendsen-parking anything that came up but didn't fit.
2. Update NEXT.md: "tomorrow, the smallest useful thing is X."
3. Append one line to LEARNING_JOURNAL.md: "I learned: [one thing]."
4. git commit with a real message (not "wip").
5. /clear.
```

The cool-down is what turns disconnected tired-mode sessions into a *coherent practice*. Without it, every session is amnesic. With it, sessions compound into something larger than any individual hour.

---

## Anti-riffs — combinations to AVOID when tired

- **`/plan-deckard-boundary` + `/plan-joe-chip-scope` + `/plan-runciter-slice`** in one tired session. Full-architecture mode. You will produce a beautiful doc you'll quietly abandon. Save for fresh hours.
- **Creating a new `THE_*.md` document of any kind.** Always a tired-mode tell.
- **Using `skill-creator` to make a new PKD skill.** Park the idea, don't build the tool. ~95% of tired-mode "I should make a skill for X" thoughts don't survive morning.
- **`/plan-buckman-execute` (plan → tasks) without first having a slice scoped fresh.** You'll produce tasks for vapor.
- **Long unbroken sessions.** >90 minutes without `/clear` is where mistakes compound. Set a timer.
- **Voice-dictating directly into a build session** without a `/plan-fat-compress` step in between. Voice unfiltered + fatigue = chaos. Always compress first.
- **Editing `MEMORY.md` directly** when tired. Use `consolidate-memory` (which mediates) or wait for morning.
- **Running `/plan-eldritch-swarm` ever, basically.** Multi-agent design is a high-energy decision; if you're considering swarm at 9pm you should park it.

---

## Two skills you have that are underused

- **`/plan-isidore-tokens`** — your apparatus is heavy (REAPERBEYONDNES requires reading THE_LITURGY + MEMORY + tradeoffs/INDEX + CODEENV + VISION pre-load). Run `/plan-isidore-tokens` on any project's CLAUDE.md once a month and trim aggressively.
- **`anthropic-skills:consolidate-memory`** — your memory directory accumulates without garden-keeping. The Attila save/retract was a symptom. This is the perfect tired-mode upkeep skill, and you almost never run it.

---

## Mode-specific quick reference card

| Energy / Goal | Reach for |
|---|---|
| Wiped, want to feel productive | Riff 8 (Janitorial) |
| Wiped, idea won't leave you alone | Riff 1 (Tired Tuesday) or Riff 2 (Capture & Compress) |
| Wiped, want to revisit old project | Riff 3 (Archaeology) |
| Medium, want to learn | Riff 4 (Learning Loop) |
| Medium, want a real plan but later | Riff 11 (Briefing-for-Tomorrow) |
| Medium, suspicious of a project | Riff 10 (Audit Pass) |
| Medium, prose-mood | Riff 12 (Aesthetic Pass) |
| Fresh, want to start small | Riff 5 (Constraint Cone) |
| Fresh, want to deliberately study X | Riff 6 (Curriculum Builder) |
| Any, just want to play | Riff 7 (Cold Open) |
| Mid-session derail | Riff 9 (Reframe-and-Park) |
| End of any session | Cool-down routine |

---

## Closing reframe

Your skill collection is a **toolkit for managing your own attention under variable energy**, more than it is a project-management apparatus. The PKD names — Joe Chip, Runciter, Abendsen, Mercer, Tagomi, Buckman, Isidore — were always characters who navigate broken or compromised states of consciousness. That's *exactly* the right register. You're tired. The skills help you do useful work anyway.

The riff catalog above is what your apparatus actually *does* once you stop framing it as a shipping pipeline. Three months of consistent use of these riffs — with the warm-up and cool-down attached — will give you a **practice**. Practices outlast projects. Practices accumulate competence in ways individual artifacts don't. And practices survive bad days, because they have a low-energy mode designed in.

Match weight to weight. Capture without judgment. Cool down before you crash. The rest is jamming.

---

*End of report. Saved 2026-04-25.*
