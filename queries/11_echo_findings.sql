-- 11_echo_findings.sql
-- Surface OLD prompts that anticipate current topics ("echo findings").
-- The point: you wrote the seed of your present obsessions a long time ago.
-- Edit the LIKE clause to match what you're currently working on.
-- Default theme: alchemy / hermetic.

SELECT
  date(created_at) AS d,
  conversation_title,
  source_name,
  approx_words,
  substr(prompt_text, 1, 500) AS prompt_preview
FROM pa_prompts
WHERE
  (LOWER(prompt_text) LIKE '%alchem%'
    OR LOWER(prompt_text) LIKE '%hermet%'
    OR LOWER(prompt_text) LIKE '%maier%'
    OR LOWER(prompt_text) LIKE '%atalanta%')
  AND created_at IS NOT NULL
  AND created_at < '2025-06-01'
ORDER BY RANDOM()
LIMIT 5;
