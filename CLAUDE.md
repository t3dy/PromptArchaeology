# CLAUDE.md — Promptarchaeology-Heldscalla

## Project overview
Read-only analytical layer over `C:\Dev\megabase\megabase.db`. Surfaces patterns in the user's own prompt history (~1.45M prompts, 5,271 conversations across 11 sources). Does NOT analyze assistant outputs.

## Mandatory rules

1. **Read-only.** Always open megabase.db with `mode=ro`. Never write to it. Never create/modify/migrate megabase tables. Views live in TEMP.
2. **Views, not copies.** Define analytical views in `schema/views.sql`. Do not duplicate rows into a local DB.
3. **Prompts only.** All queries filter to `role='user'`. Assistant outputs are explicitly excluded from primary analyses.
4. **Reports are markdown.** Query outputs land in `reports/YYYY-MM-DD_<query>.md`. Append-only history.
5. **No ingestion logic here.** If a new source needs ingestion, that's megabase's job.

## Where things live

- `schema/views.sql` — `pa_prompts` and `pa_cascades` TEMP views. Applied on every run.
- `queries/NN_name.sql` — one file per saved analysis.
- `tools/run.py` — runs a query by name, writes a report.
- `tools/chunk_cascade.py` — chunks a single conversation into prompt-only chunks.
- `reports/` — dated outputs. `reports/cascades/<slug>/` for chunked cascades.
- `fixtures/` — known prompts to validate views against (optional).

## When the user asks for analysis

1. Match request to an existing query in `queries/`. If matched, run it.
2. If no match, draft a new SQL file using views from `schema/views.sql`. Add it as `NN_descriptive_name.sql`.
3. Run, surface the report path, summarize the top finding in <100 words.
4. Never run a query that scans all 1.45M prompts without `LIMIT` or aggregation.

## When the user asks about a specific cascade

Use `tools/chunk_cascade.py <conversation_id>`. Do not try to dump 1000 pages into one file. Default chunk size is 50 prompts.

To find the conversation ID:
```sql
SELECT conversation_id, conversation_title, estimated_pages
FROM pa_cascades WHERE conversation_title LIKE '%<keyword>%';
```

## Adding a new query

Each `.sql` file should:
- Begin with a comment block: purpose, expected runtime, expected row count
- Use views from `schema/views.sql`, not raw megabase tables
- Include `LIMIT` on row-returning queries; aggregations don't need it
- Use `LOWER()` on text comparisons (the corpus is mixed case)

## Smoke test

`python tools/run.py 01_first_prompts` should produce a report with at least 100 rows.

## Megabase tables (for reference, do not modify)

- `sources` — 11 sources (chatgpt, chatgpt-md, llm_logs_html, llm_logs_pdf, claude, sms, facebook, twitter, etc.)
- `conversations` — 5,271 rows. Has `title`, `created_at`, `estimated_pages`.
- `messages` — 3,968,349 rows. Has `role` ('user'/'assistant'), `content`, `created_at`.
- `segments`, `segment_scores`, `prompt_catalog_entries`, `ideas`, `entities` — additional megabase analytical tables; do not depend on these for promptarchaeology queries unless explicitly asked.

## Style of output

When summarizing query results to the user:
- Lead with one observation, not a recap.
- If you noticed something genuinely surprising in the data, flag it.
- If the user asks "what does this mean about me," answer carefully — let the data speak first, your interpretation second.
