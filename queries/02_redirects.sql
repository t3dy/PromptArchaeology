-- 02_redirects.sql
-- Prompts where you pushed back on an AI output: "no, actually I want..."
-- These are your real-time corrections — your highest-signal value statements.
-- Each redirect is a moment where output failed to match desire and you said so.

SELECT
  date(created_at) AS d,
  source_name,
  conversation_title,
  approx_words,
  substr(prompt_text, 1, 400) AS prompt_preview
FROM pa_prompts
WHERE reacts_to_output = 1
  AND (
       LOWER(prompt_text) LIKE 'no,%'
    OR LOWER(prompt_text) LIKE 'no.%'
    OR LOWER(prompt_text) LIKE 'no %'
    OR LOWER(prompt_text) LIKE 'actually %'
    OR LOWER(prompt_text) LIKE 'actually,%'
    OR LOWER(prompt_text) LIKE 'wait,%'
    OR LOWER(prompt_text) LIKE 'wait %'
    OR LOWER(prompt_text) LIKE 'i don''t want%'
    OR LOWER(prompt_text) LIKE 'i didn''t %'
    OR LOWER(prompt_text) LIKE 'that''s not what%'
    OR LOWER(prompt_text) LIKE 'not quite %'
    OR LOWER(prompt_text) LIKE 'hmm %'
    OR LOWER(prompt_text) LIKE 'hmm,%'
    OR LOWER(prompt_text) LIKE 'stop %'
  )
ORDER BY created_at DESC
LIMIT 300;
