# WEEKLY_CADENCE — A working rhythm that fits a teacher's week

**Date:** 2026-04-25
**Use:** Tired-mode rules and warm-up routines work session-by-session. This file is the layer above: a *week shape* that protects energy, builds compounding practice, and respects that you have a real job that takes most of your daytime cognition.

---

## The core insight

You're not a full-time builder. Trying to follow a full-time builder's rhythm produces guilt and burnout. Your week has a real structure already (Monday–Friday school, weekends, evenings) — the cadence should match that, not fight it.

Most "developer productivity" advice assumes 35–45 hours of fresh focus per week. You have closer to 8–15 stolen hours, of variable quality. The shape that works is *very different*.

---

## The seven types of session

A week has different *kinds* of sessions, each with different goals. Naming them helps you pick the right type for the moment.

| Type | When | Length | Goal |
|---|---|---|---|
| **Tired Tuesday** | Weekday evening, low energy | 30–60 min | Capture, compress, archive |
| **Warm Wednesday** | Weekday evening, medium energy | 60 min | Extend a warm project (one thing) |
| **Learning Loop** | Anywhere, with energy for tutoring | 30–60 min | Burn tokens for CS knowledge |
| **Saturday Build** | Weekend morning, fresh | 2–4 hours | Real architecture, real building |
| **Sunday Garden** | Weekend, mellow | 60–90 min | Memory hygiene, audits, briefings |
| **Jam Night** | Whenever the spirit hits | ≤ 60 min | Pure play, no artifact required |
| **Recovery** | Whenever needed | n/a | NO coding. Walk dogs. Read. Sleep. |

---

## A baseline week

This is *one* possible shape. Adjust to your reality:

```
Mon evening   — Tired Tuesday riff (30 min cap, hard stop)
Tue evening   — Recovery OR Tired Tuesday (your call by 6pm)
Wed evening   — Warm Wednesday (60 min on warm project)
Thu evening   — Learning Loop OR Recovery
Fri evening   — Jam Night (let off steam, no goals)
Sat morning   — Saturday Build (2–4 hours, real work)
Sat afternoon — Recovery (walk, read, dogs)
Sun morning   — Sunday Garden (memory + audits + briefings)
Sun afternoon — Recovery
```

Total: ~8–10 hours of code, distributed across 6 of 7 days, with explicit recovery built in.

---

## Why this shape works for a teacher

- **Monday is the worst day.** You walked into Monday rested; Monday wiped you out. Tuesday is when the cumulative fatigue hits. Honor it. Don't book hard work on Tuesday.
- **Wednesday is the swing day.** You've adjusted to the school week's rhythm. Energy is medium. Warm Wednesday becomes the place where small but real progress lives.
- **Thursday is recovery or learning.** You're tired but the weekend is in sight. Reading mode, tutoring mode, journal mode.
- **Friday is psychic release.** Jam Night gives the laughs that compensate for the week. No goals = no failure mode.
- **Saturday morning is your one true builder window.** Treat it like sacred time. No errands until 11am. This is when real architecture or hard problems get attention.
- **Saturday afternoon is recovery.** Don't push two real-work blocks back-to-back. Walk. Pet dogs. Eat lunch slowly.
- **Sunday is hygiene + setup.** Memory garden, briefings, prepare yourself for the school week. A 90-minute Sunday morning here saves 2 hours of disorientation across the week.

---

## Weekly rituals (the load-bearing parts)

Three rituals that, if you do nothing else, hold the practice together.

### Friday afternoon — Honest week-in-review (10 minutes)

Before any Jam Night, do this:

```
Open LEARNING_JOURNAL.md. Skim this week's entries.
Open NEXT.md for each active warm project. Update them.
Run: git log --since="Monday" --shortstat (across all project dirs)
Write ONE sentence: "This week I learned X. I'm proud of Y. I'm carrying Z forward."
Save it as the week's marker in LEARNING_JOURNAL.md.
```

That single sentence is the week. Even a brutal week produces one true sentence.

### Saturday morning — Builder warm-up (5 minutes)

Before any Saturday Build:

```
Read NEXT.md for the project you're working on.
Run /plan-tagomi-briefing if more than 2 weeks have passed since last touch.
Set a timer (90 min for the first chunk).
Decide BEFORE starting: what's the artifact at the end of today?
```

The "decide before starting" line is the most important. Saturday Builds drift fastest because they're the longest sessions.

### Sunday afternoon — Set up the week (15 minutes)

Pick the warm project for next week. Write its NEXT.md as if for a stranger. Decide what days you'll likely have energy for what. (Schedule subject to change, but the *intention* matters.)

---

## Recovery is not optional

Coding 7 days a week post-school is how you broke yourself last quarter. The Recovery slots in this rhythm are *load-bearing*. They are not "wasted time"; they are the time that lets the other slots have value.

A week with 2 recovery evenings is *more productive* than a week with zero, because you don't reach Friday wiped enough to ruin the weekend.

If your evenings are consistently used for school prep, lesson planning, or family — that's also Recovery from the codebase's perspective. Don't double-book.

---

## What if a week falls apart

It will. Some weeks the cadence is impossible. School emergencies, sick dogs, family stuff, your own bad week. When it falls apart:

- **Skip to Sunday Garden** — even on a wrecked week, 30 minutes of memory hygiene Sunday morning resets the apparatus
- **Don't try to "make up" missed sessions** — that always produces a worse session
- **Write one journal line** — "Bad week, here's why, see you next week"
- **Trust the cadence to resume** — the *practice* survives bad weeks; only the *output* drops

---

## Seasonal arc

Beyond weekly: a quarterly arc.

- **Quarter 1:** Establish the cadence. Don't add ambitions. Just live in the shape.
- **Quarter 2:** Pick ONE curriculum path (CS_CURRICULUM_TED.md). Run it inside the existing shape.
- **Quarter 3:** Do a real audit (AUDIT_QUESTIONS.md) of one project. Either freeze, finish, or refactor.
- **Quarter 4:** Rest. Reflect. Plan next year.

Treat the year as four 12-week sprints with explicit themes. Each sprint has the same weekly cadence underneath.

---

## What this is NOT

- It's not a productivity system. It's a *practice* system. You're not optimizing throughput; you're maintaining a working rhythm.
- It's not rigid. The shape is a default; deviations are expected.
- It's not for everyone. It's tuned to a teacher with dogs and a coding hobby; it would feel wrong for a freelance dev or a researcher with grants.
- It's not a replacement for shipping discipline. (We're not doing that part now per your redirect — but if you ever want it, this cadence accommodates a "ship something monthly" sub-loop on Saturday Builds.)

---

## Open questions for you

- Is the weekly shape close to what your week already is, or does it require shifts?
- Does Saturday actually have a 2–4 hour fresh window for you, or is family/errands more dominant on weekends?
- Would having `/loop weekly` reminders for the three rituals help, or feel naggy?
- Is there a *daily* sub-rhythm worth specifying (e.g., evening start time, hard-stop time)?
- Are there seasonal patterns (school year vs summer break) that should change the cadence?

Pick a Sunday and try the cadence for one week. Adjust. Repeat for three more weeks. The shape becomes yours.
