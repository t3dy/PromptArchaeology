-- 03_what_im_actually.sql
-- "What I'm actually trying to do is..." — the real-goal reveals.
-- Usually appears around prompt 5-10 of a long conversation, after AI outputs
-- have surfaced what you DON'T want by contrast. These are gold-tier sentences:
-- the moment you finally articulate the underlying goal in your most lucid voice.

SELECT
  date(created_at) AS d,
  source_name,
  conversation_title,
  substr(prompt_text, 1, 600) AS prompt_preview
FROM pa_prompts
WHERE
     LOWER(prompt_text) LIKE '%what i''m actually%'
  OR LOWER(prompt_text) LIKE '%what i really mean%'
  OR LOWER(prompt_text) LIKE '%what i really want%'
  OR LOWER(prompt_text) LIKE '%let me reconsider%'
  OR LOWER(prompt_text) LIKE '%the thing is%'
  OR LOWER(prompt_text) LIKE '%i think what%i''m%'
  OR LOWER(prompt_text) LIKE '%i should clarify%'
  OR LOWER(prompt_text) LIKE '%let me clarify%'
  OR LOWER(prompt_text) LIKE '%my real goal%'
  OR LOWER(prompt_text) LIKE '%what i actually want%'
  OR LOWER(prompt_text) LIKE '%let me back up%'
ORDER BY created_at DESC;
