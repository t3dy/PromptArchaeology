# VOICE_TO_ARTIFACT — A pipeline for tired-mode work driven by voice

**Date:** 2026-04-25
**Use:** When typing is too much but you can still talk. Voice notes → AI processing → durable artifacts. Most of your tired-mode best ideas die because you can't be bothered to type them. Fix that.

---

## Why voice

You already have the infrastructure: vosk model in `C:\Dev\vosk-model-small-en-us-0.15\`, a `voicenotes/` directory, `BARTONCONVO.txt` and several other voice-derived transcripts. You're not starting from zero.

Voice's tired-mode advantages:
- Lower activation energy than typing
- Catches half-formed thoughts that wouldn't survive typing
- Compatible with not-looking-at-screen (driving home, walking dogs, post-school recovery)
- Whisper or vosk transcribes well enough for AI processing downstream

Voice's hazards:
- Raw transcripts are noisy (filler, repetition, false starts)
- Without compression, voice-output fills up directories without becoming usable
- The temptation is to *only* talk and never write, which atrophies a different muscle

---

## The pipeline

```
[1] Speak into recorder (phone, laptop, voice notes app)
       ↓
[2] Transcribe (vosk locally OR Whisper API OR Otter.ai)
       ↓
[3] Compress (AI-assisted, /plan-fat-compress)
       ↓
[4] Triage (decide: park, journal, build, discard)
       ↓
[5] Land in destination (PARKING.md, LEARNING_JOURNAL.md, code, or trash)
```

Each step is short. The whole pipeline can run in under 15 minutes for a 10-minute voice note. **Most of the value is in steps 3–4** — raw transcripts are useless until compressed and triaged.

---

## Step-by-step prompts

### Step 1 — Capture

No prompt. Just talk. Suggested triggers:
- After dropping kids' parents at the door (or whatever your post-school equivalent is)
- Walking the dogs (Attila will probably interrupt you with a squeaky toy demand)
- Driving home — voice memos app
- Right before bed, lying down, lights off

Keep recordings under 10 minutes. Three short recordings beat one long one.

### Step 2 — Transcribe

Local with vosk:
```
python -m vosk_transcriber input.wav > transcript.txt
```
(Replace with your actual vosk wrapper script — you have the model installed.)

Or Whisper API if you're willing to spend the cents (you're not, per your subscription preference).

Or Otter.ai if you used it on your phone.

### Step 3 — Compress

Paste transcript. Run:
```
This is a raw voice note transcript. I was thinking out loud and it's noisy.
Compress to 5–10 bullet points capturing only the substantive thoughts.
Drop filler, repetition, and false starts.
Preserve any specific numbers, names, or technical terms exactly.
At the end, list any ideas that feel half-baked but worth parking.
```

That's the core compression prompt. Save it; reuse it.

### Step 4 — Triage

After compression, ask:
```
For each of the bullets above, classify as one of:
[P] Park — interesting idea, no immediate action
[J] Journal — a learning or insight, append to LEARNING_JOURNAL.md
[B] Build — actionable now or in next session
[D] Discard — said it, don't need it
[Q] Question — needs a decision I haven't made

Then write the destination text for each non-D item exactly as it should appear in the destination file.
```

The AI's output is paste-ready for your destination files.

### Step 5 — Land

Copy the [P] items to `PARKING.md` (project-specific) or `IDEAS.md` (cross-project).
Copy [J] items to `LEARNING_JOURNAL.md`.
Copy [B] items to `NEXT.md` for the relevant project.
Copy [Q] items to `OPEN_QUESTIONS.md`.

Done. The voice note's value is preserved in stable, queryable locations. The raw transcript can be archived or deleted.

---

## Specialized compression prompts

For different kinds of voice notes:

### "I was thinking about [project]"

```
This is a voice note about [project]. Compress to:
- 3 things I noticed
- 2 things I want to try
- 1 thing I'm uncertain about
Format each as a single sentence, plain English.
```

### "I was rambling about an idea"

```
Voice note of an idea I was working out loud. Distill into:
- The idea in one sentence (be charitable but accurate)
- The most interesting thing about it
- The most likely failure mode
- One concrete first experiment
- Whether this should go in PARKING_LOT.md or be acted on
```

### "I was teaching myself something"

```
This is me thinking through a concept I'm trying to learn. Output:
- The concept named precisely
- My current (possibly wrong) understanding
- What I correctly grasped
- What I'm confused about
- One follow-up question I should ask
Save as a draft LEARNING_JOURNAL.md entry.
```

### "I was venting about a project"

```
This is venting, not analysis. Compress to:
- What I'm frustrated about (1 sentence)
- The legitimate problem underneath the frustration
- The part that's just fatigue talking
- One small thing I could do that would help
Don't fix it. Just see it.
```

### "I had a half-finished thought"

```
Voice note of an unfinished thought. Don't try to finish it for me.
Output: the thought as I left it, in 2 sentences.
What I would need to know to finish it.
Save under PARKING.md / unfinished/.
```

---

## Tired-mode recipe: the 5-minute voice journal

Easiest possible tired-mode session:

```
1. Open phone voice memos.
2. Talk for 2 minutes about what was hard today.
3. Send transcript to Claude.
4. Run "compress + journal" prompt.
5. Paste to LEARNING_JOURNAL.md.
6. Done.
```

Total active typing: paste, paste. That's it. You captured a real thought. The day compounded.

---

## Anti-patterns

- **Letting raw transcripts pile up in `voicenotes/` without processing.** Either process within 24h or delete.
- **Trying to act on voice notes the same session you record them.** Voice → triage → cool-down → next session. Don't loop.
- **Talking for 30+ minutes.** Long monologues lose coherence. Three 5-minute notes > one 30-minute one.
- **Over-formatting the transcript.** Don't try to make voice notes read like prose. Compress, don't polish.
- **Ignoring the [D] discards.** Voice produces a lot of "actually never mind" which is fine. Discard freely.

---

## Open questions for you

- Are you still using vosk, or have you moved to Whisper / phone-native? The pipeline above assumes vosk; adjust if not.
- Do you want a script (`tools/voice_pipeline.py`) that runs steps 2–4 in one command? Could be a 100-line evening project.
- Where should LEARNING_JOURNAL.md, IDEAS.md, OPEN_QUESTIONS.md live — global at `C:\Dev\`, or per-project?
- Is there a project where voice-driven entry would be the killer feature? DOGSGAME's behavior catalog (you observe a dog, you talk into your phone) is a strong candidate.

The pipeline costs nothing to set up; the first voice → artifact loop is tonight if you want it.
