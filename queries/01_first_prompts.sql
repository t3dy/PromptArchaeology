-- 01_first_prompts.sql
-- The first user message of every conversation, chronologically.
-- These are pre-influence: what you walked in wanting before AI shaped framing.
-- Expected: ~5,271 total. Limit to 200 most recent by default.

SELECT
  date(created_at)     AS d,
  source_name,
  conversation_title,
  approx_words,
  ROUND(estimated_pages, 1) AS pages,
  substr(prompt_text, 1, 280) AS prompt_preview
FROM pa_prompts
WHERE is_first_in_conversation = 1
  AND created_at IS NOT NULL AND created_at != ''
ORDER BY created_at DESC
LIMIT 200;
