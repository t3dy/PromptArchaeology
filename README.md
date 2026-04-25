# Promptarchaeology-Heldscalla

Distant-reading tool for your own LLM prompt history.

## Heldscalla

In Philip K. Dick's *Galactic Pot-Healer* (1969), the alien Glimmung summons skilled craftspeople from across the galaxy to help raise **Heldscalla** — an ancient cathedral sunk beneath the seas of Plowman's Planet. Joe Fernwright, the protagonist, is a pot healer: a restorer of broken ceramics. The work is patient, partial, and uncertain.

Your prompt corpus across `megabase.db` (5,271 conversations, ~1.45M prompts) is Heldscalla. This tool is Joe's craft — bringing one cascade at a time into the light, ignoring the AI's outputs to surface only your own writing.

## What this is

A read-only analytical layer over `C:\Dev\megabase\megabase.db`. Defines TEMP SQL views that present the user-prompt subset of the corpus as a clean object, plus saved queries that surface specific patterns:

- First prompts (pre-influence framing)
- Redirects ("no, actually I want...")
- "What I'm actually trying to do" reveals
- Cascade-length distribution
- Theme/obsession lines over months
- Interrupt-and-restart patterns
- 1000-page cascade anatomy
- Mood markers (fatigue, excitement, frustration)

## What this is NOT

- An ingestion pipeline. Megabase already has the data.
- An output-analyzer. We deliberately ignore assistant outputs to isolate your own writing.
- A modification of megabase. Read-only forever.

## Quick start

```bash
cd C:\Dev\promptarchaeology
python tools/run.py 01_first_prompts
```

Output lands in `reports/YYYY-MM-DD_01_first_prompts.md`.

To anatomize a single 1000-page cascade:

```bash
python tools/chunk_cascade.py <conversation_id>
```

Find conversation IDs via `python tools/run.py 08_thousand_page_anatomy`.

## Layout

```
promptarchaeology/
  README.md
  CLAUDE.md                     — agent instructions
  schema/
    views.sql                   — pa_prompts, pa_cascades (TEMP views)
  queries/
    01_first_prompts.sql
    02_redirects.sql
    03_what_im_actually.sql
    04_cascade_lengths.sql
    06_obsession_lines.sql
    07_interrupt_restarts.sql
    08_thousand_page_anatomy.sql
    09_mood_markers.sql
  tools/
    run.py                      — `python tools/run.py <query>`
    chunk_cascade.py            — break large cascades into prompt-only chunks
  reports/                      — dated query outputs (markdown)
  fixtures/                     — known-prompt validation
```

## Adding a query

1. Drop a `.sql` file in `queries/`. Use views from `schema/views.sql`.
2. Run via `python tools/run.py <basename>`.
3. Output goes to `reports/`.

That's the whole loop.

## Skill

This tool has a companion slash command at `~/.claude/skills/promptarchaeology-heldscalla/SKILL.md`. Invoke it when you want analysis without manually picking a query.
