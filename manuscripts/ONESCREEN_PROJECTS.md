# ONESCREEN_PROJECTS — Tiny project ideas that fit on one screen

**Date:** 2026-04-25
**Use:** When you want to *build something* but are too tired for architecture, pick one of these. Constraint: the whole project fits in one Python file under 200 lines, runs in one terminal, and produces output you can show to one human (or just yourself for the laughs).

---

## The constraint set

A one-screen project must satisfy:

- **One file.** No directory tree. `tinything.py` and that's it.
- **Under 200 lines.** Counting comments and blank lines. If it's growing past that, the project is over.
- **One run command.** `python tinything.py` produces output. No setup, no config files, no .env.
- **One artifact per run.** A printed table, a generated image, a piece of text, a sound file. One thing.
- **No dependencies you don't already have.** Stdlib + whatever's in your usual Python — no `pip install` for new tools.

That's it. The constraint is the point. Anything that grows out of these boundaries is a different project; park it.

---

## 25 one-screen project ideas

### MTG / Esoteric flavor

1. **Card oracle.** Pick a random MTG card from your alchemy_scryfall DB. Print the card text alongside one related hermetic axiom from EmeraldTablet/HERMETICDB. Run before each MTG game for the laughs.
   - *Prompt to start:* `Write a 100-line Python script that picks a random card from C:\Dev\alchemy_scryfall\<db> and a random concept from C:\Dev\EmeraldTablet\db\<db> and prints them paired. Plain text output.`

2. **Etymology generator.** Input: any English word. Output: 3 plausible (real-or-invented) etymologies in the style of OED. Have the AI generate; you grade.
   - *Prompt to start:* `Generate a script that takes a word as argv[1] and prints three OED-style etymologies. Two from real reference, one I write as a fake.`

3. **Daily hermetic axiom.** Generate one 1-sentence hermetic-sounding axiom per day, save to `axioms.txt`. Read at end of week for laughs.

4. **Mana-color personality test.** 10-question quiz that prints WUBRG color identity. Run with friends.

5. **MTG card → tarot card.** Input: MTG card name. Output: tarot equivalent with one-paragraph reading.

### Distant reading toys

6. **Word frequency over time in your own writing.** Point at `voicenotes/` or any text directory. Print top 20 words by month. ASCII bar chart.
   - *Prompt:* `Write a 150-line script that counts words in all .txt files in a dir, groups by file mtime month, and prints top-20 words per month with ASCII bars.`

7. **Self-quote miner.** Find the 5 most-quoted-by-you phrases in your own writing. ASCII output.

8. **Project name graph.** List all C:\Dev subdirectories, count files, sort by recency. Print as ASCII bar chart.

9. **Two-corpus diff.** Compare word distributions in any two corpora you have (e.g., GPT.txt vs your own writing). Print the words most distinctively in each.

10. **Lexicon shift detector.** Across a year of voice notes, which words appear in the second half but not the first? Vice versa?

### Game / simulation toys

11. **Two-dog physics sim.** Tiny ASCII grid. One dog moves toward bone. Other dog steals it. Print every tick. (Calibrating for DOGSGAME without committing.)

12. **Roguelike-in-100-lines.** Single screen, you (@), one monster (M), one stairs (>). Walk around. Whatever.

13. **MTG draft pick simulator.** Given a real or generated pack, "draft" one card based on a set of weighted rules. Print the pick + reasoning.

14. **Yard tile renderer.** ASCII-render the DOGSGAME yard from a hard-coded layout. Stop at rendering. No game logic.

15. **PKD novel mood-tracker.** Map each chapter of a PKD novel to a single emoji or color block. Print as a 2D grid.

### Audio toys (low-energy chiptune flavor)

16. **NES note-name converter.** Given an MIDI note number, print the NES register value, channel suggestion, and one historical NES song that uses it. Tiny but uses your existing NSFRIPPER knowledge.

17. **Chiptune name generator.** Output: random chiptune-band-style names. ("Toxic Lich on the Throne of TR808"). For laughs.

18. **WAV file inspector.** Print the WAV header of any file you point it at. Sample rate, bit depth, channels, length, RMS level. Stdlib only.

### Personal infrastructure micro-tools

19. **TODO grepper.** Walk C:\Dev, find every TODO/FIXME/HACK comment, print sorted by file age. Decide: real, dead, aspirational.

20. **Project freshness report.** For each subdirectory of C:\Dev, print last commit date and last file mtime. Color the cold ones.

21. **Stale memory finder.** Walk your `memory/` directory, flag any memory file not modified in 60+ days. Suggest review.

22. **Skill audit.** List all your slash commands. Print the description of each. Mark any whose description you no longer remember writing.

### Pure absurdity

23. **PKD oracle.** Random sentence generated from a Markov chain trained on PKD prose. (You can find PKD corpora online; cite where.) Print one sentence per day.

24. **Crockett the senior dog's daily affirmation.** Generate one ironic affirmation per day, in the voice of an arthritic 11-year-old toy-thieving dog.

25. **Maier-style emblem describer.** Input: any noun. Output: a fake Atalanta Fugiens emblem description (motto, image, epigram). Three lines max each.

---

## How to use this list

1. **Pick one when:** you want to code, you're tired, you have an hour.
2. **Don't elaborate.** If the project starts wanting a directory tree, kill it. Park the elaborated version for fresh-mode.
3. **Show one human OR don't.** The artifact is the point; sharing is optional.
4. **Save the file.** Even one-screen projects deserve a place to live. Drop them in `C:\Dev\onescreen/<name>.py`. After 12 of them, you have a folder of small interesting things.
5. **No dependencies upgrade.** If you find yourself wanting `pip install pandas`, kill the project.

---

## Why this category matters

These projects:
- Produce something runnable and *done* in one sitting (the rare experience your portfolio lacks)
- Teach you Python tricks at the small scale, where they're easier to internalize
- Convert tired-mode hours into discrete completed artifacts (even if private)
- Maintain your sense that *building is fun*, which is the actual fuel
- Build a folder of tiny weird tools that, in aggregate, become a portfolio of taste

You said: *"I'm having a million laughs."* Ten one-screen projects = ten micro-laughs you can revisit. The discipline of fitting a thing in one file is itself a teacher.

---

## Open questions for you

- Want a `C:\Dev\onescreen/` folder set up with a README that links these prompts? Easy.
- Want me to flesh out 5 of these into ready-to-paste full-spec prompts? Tell me which 5.
- Should this be a `/loop weekly` thing — "pick a one-screen idea, build it, post in here"?
- Are there tiny project categories I missed that fit you? (e.g., MarxistTradition flavor — "labor-time of my own commits"?)

Pick one tonight. 90 minutes max. Don't grow it.
