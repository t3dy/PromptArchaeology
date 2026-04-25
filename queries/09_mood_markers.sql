-- 09_mood_markers.sql
-- Prompts carrying emotional markers: fatigue, frustration, excitement, humor, confusion.
-- Tracks affective valence over time as a proxy for relationship to the work.
-- Crude — these are surface markers, not real sentiment analysis.

SELECT
  date(created_at) AS d,
  conversation_title,
  CASE
    WHEN LOWER(prompt_text) LIKE '%ugh%'
      OR LOWER(prompt_text) LIKE '%frustrat%'
      OR LOWER(prompt_text) LIKE '%annoy%' THEN 'frustration'
    WHEN LOWER(prompt_text) LIKE '%love this%'
      OR LOWER(prompt_text) LIKE '%this is great%'
      OR LOWER(prompt_text) LIKE '%perfect!%'
      OR LOWER(prompt_text) LIKE '%amazing%' THEN 'excitement'
    WHEN LOWER(prompt_text) LIKE '%i''m tired%'
      OR LOWER(prompt_text) LIKE '%exhausted%'
      OR LOWER(prompt_text) LIKE '%can''t think%'
      OR LOWER(prompt_text) LIKE '%too tired%' THEN 'fatigue'
    WHEN LOWER(prompt_text) LIKE '%lol%'
      OR LOWER(prompt_text) LIKE '%haha%' THEN 'humor'
    WHEN LOWER(prompt_text) LIKE '%confused%'
      OR LOWER(prompt_text) LIKE '%stuck%'
      OR LOWER(prompt_text) LIKE '%don''t understand%' THEN 'confusion'
    ELSE 'unknown'
  END AS mood,
  approx_words,
  substr(prompt_text, 1, 240) AS preview
FROM pa_prompts
WHERE
     LOWER(prompt_text) LIKE '%ugh%'
  OR LOWER(prompt_text) LIKE '%frustrat%'
  OR LOWER(prompt_text) LIKE '%annoy%'
  OR LOWER(prompt_text) LIKE '%love this%'
  OR LOWER(prompt_text) LIKE '%this is great%'
  OR LOWER(prompt_text) LIKE '%perfect!%'
  OR LOWER(prompt_text) LIKE '%amazing%'
  OR LOWER(prompt_text) LIKE '%i''m tired%'
  OR LOWER(prompt_text) LIKE '%exhausted%'
  OR LOWER(prompt_text) LIKE '%can''t think%'
  OR LOWER(prompt_text) LIKE '%too tired%'
  OR LOWER(prompt_text) LIKE '%lol%'
  OR LOWER(prompt_text) LIKE '%haha%'
  OR LOWER(prompt_text) LIKE '%confused%'
  OR LOWER(prompt_text) LIKE '%stuck%'
  OR LOWER(prompt_text) LIKE '%don''t understand%'
ORDER BY created_at DESC
LIMIT 300;
