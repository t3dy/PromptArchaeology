# 20 Questions on Megabase

*The substrate. The unified corpus across 11 sources. 1.45M user prompts, 5,271 conversations. The ground without which Heldscalla is nothing.*

---

1. Megabase is built across **8 sessions** with **zero API cost**. Do you remember which session was the breakthrough? (The corpus knows.)

2. The **`ideas` table** has 30+ columns at this point — primary_class, dh_subtype, family_id, score_game, etc. Was the schema additive (you added when needed) or was there a moment of redesign? Audit the answer.

3. The **`segments` table** with `segment_scores` and `segment_type` — is this still actively used, or is it scaffolding from an earlier ambition?

4. **11 sources** ingested: chatgpt, chatgpt-md, claude, llm_logs_html, llm_logs_pdf, sms, facebook, gmail, twitter, google_chat, pkd_chats. Which has the **highest information density per prompt**? (Not volume — density.)

5. **gmail has zero conversations**. Why?

6. The **Twitter Timeline as one 6,246-page conversation** is a clever schema choice. Was it intentional, or did the ingester treat the timeline that way by default?

7. *"Personal Knowledge Archaeology System"* (PKAS) was the original framing. Promptarchaeology-Heldscalla now narrows that to prompts-only. **Should megabase rebrand to absorb both, or stay as-is and let the siblings specialize?**

8. The **`prompt_catalog_entries`** table has the columns `term`, `term_category`, `topic`. What's currently in `term_category`? (Open the DB; check.)

9. Megabase has been touched in **2026-02-23** prompts on database storytelling: *"What else can I do to improve the database and search it to map out my life."* That's a coach question disguised as a tech question.

10. The **`refine_names_local.py`** and **`apply_renames.py`** scripts imply a name-refinement subsystem. Is that still running, or has it stabilized?

11. **NotebookLM-py** (2026-03-02) — you scoped this. Did you ever integrate it with megabase, or is it still parked?

12. **Aldous's `gemini_segment_reader.py`** — when did Gemini join the corpus? Was the schema flex enough to hold it without changes?

13. The **`personal_census.json`** and **`personal_ranked.json`** files imply a ranking exercise was run. What was the question? What was the answer?

14. **"All my projects"** as a single megabase view: does that view exist, or only as a recurring opening prompt of yours? (E.g. 2026-03-14: *"All projects: Review progress on functionality improvements…"*.)

15. Promptarchaeology lives at `C:\Dev\promptarchaeology\` and queries megabase read-only. Is there a *symmetric* tool that could query megabase **for the assistant outputs only** — a "outputs-archaeology" sibling? **Probably not — but the symmetry is interesting.**

16. The **`hidden`** column on `ideas` and the **`limbo_reason`** column suggest a triage workflow. Is the triage queue actively maintained, or has limbo become permanent?

17. Megabase's **`schema.py`** is the ground truth. When you stand up the Marxist Knowledge Portal, will it inherit megabase's schema or build its own? **The right answer might be: inherit and never fork.**

18. The **`.spec`** file suggests a pyinstaller bundle. Did you ever ship megabase as a desktop app? Or was it always a local CLI?

19. If a friend asked *"so what does megabase do, in plain English"* — what's your one-sentence answer? **Practice it. The shape of the answer is its own diagnostic.**

20. Megabase is the **largest single thing you've built**. It's also the **least visible**. Should it stay invisible — pure substrate — or should there be a "megabase showroom" page somewhere?

---

*Megabase is the cathedral floor. Promptarchaeology is one chamber inside. Heldscalla rises one stone at a time.*
