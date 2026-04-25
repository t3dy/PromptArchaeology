-- 10_random_pull.sql
-- Pull one random substantive prompt from the corpus.
-- Use as a coach-mode discussion seed: "what was this about?"
-- Filtered to prompts with >30 words to skew toward something with substance.

SELECT
  date(created_at) AS d,
  conversation_title,
  source_name,
  approx_words,
  prompt_text
FROM pa_prompts
WHERE created_at IS NOT NULL AND created_at != ''
  AND approx_words > 30
ORDER BY RANDOM()
LIMIT 1;
