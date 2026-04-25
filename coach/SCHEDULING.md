# Scheduling the coach

You can wire coach offerings into a recurring schedule so company arrives without you having to ask. Use the `anthropic-skills:schedule` or the local `schedule` skill.

## Suggested schedules

### Tired Tuesday companion (weekday post-school)
**When:** Mon–Thu at 18:00 your time.
**Prompt to schedule:**
> Run promptarchaeology-heldscalla coach mode. Pick from `SESSION_OPENERS.md` light openers only. One offering, no elaboration unless I respond. If I don't respond within 30 minutes, ignore.

### Saturday morning briefing
**When:** Sat at 09:00.
**Prompt:**
> Run promptarchaeology-heldscalla coach mode. Pick from `SESSION_OPENERS.md` reflective openers. Fresh-mode: a slightly larger offering is OK. Maybe pull a random prompt from a year ago and ask me to react.

### Friday cool-down
**When:** Fri at 17:00.
**Prompt:**
> Coach: ask me what surprised me this week. Save my answer to `LEARNING_JOURNAL.md` with one line.

### Sunday garden hour
**When:** Sun at 10:00.
**Prompt:**
> Run promptarchaeology query 06_obsession_lines and tell me which themes shifted this month. Then ask me one question from `coach/QUESTIONS.md` reflective set.

### Monthly cathedral visit
**When:** First of each month at 09:00.
**Prompt:**
> Pick a 1000-page cascade I haven't visited in 30+ days. Generate a one-paragraph briefing and ask if I want to read one chunk tonight.

## Anti-patterns

- Never schedule "did you ship?" prompts. The coach has zero shipping mandate.
- Don't schedule during family time, school hours, or sleep.
- Don't schedule more than 5 recurring coach prompts. The corpus rewards low-frequency.
- Don't schedule the same opener type every day; let the random pull do its work.

## Setup snippet

When ready, ask Claude:
> "Set up a scheduled trigger using anthropic-skills:schedule. Cron: weekdays at 18:00. Prompt body: invoke promptarchaeology-heldscalla coach mode with a Light Opener."

The schedule skill will write the entry; coach offerings will arrive on cadence.

## Manual override

Any time you want a coach moment outside the schedule, just say "coach me" or run `python tools/coach.py`.
