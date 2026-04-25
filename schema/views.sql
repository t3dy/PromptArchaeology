-- promptarchaeology TEMP views over megabase.db (read-only).
-- Applied on every connection in tools/run.py. Lives in TEMP database, so works
-- even when main connection is mode=ro.
--
-- Conventions:
--   pa_prompts   — one row per user message; includes context flags
--   pa_cascades  — one row per conversation; aggregates over user messages

DROP VIEW IF EXISTS temp.pa_prompts;
DROP VIEW IF EXISTS temp.pa_cascades;

CREATE TEMP VIEW pa_prompts AS
SELECT
  m.id              AS message_id,
  m.conversation_id,
  c.title           AS conversation_title,
  s.name            AS source_name,
  m.created_at,
  m.content         AS prompt_text,
  m.char_count,
  -- crude word count via space-counting; fine for distant reading
  CASE
    WHEN m.content IS NULL OR m.content = '' THEN 0
    ELSE LENGTH(m.content) - LENGTH(REPLACE(m.content, ' ', '')) + 1
  END AS approx_words,
  -- first user message in the conversation? (pre-influence)
  CASE WHEN m.id = (
    SELECT MIN(m2.id) FROM messages m2
    WHERE m2.conversation_id = m.conversation_id AND m2.role = 'user'
  ) THEN 1 ELSE 0 END AS is_first_in_conversation,
  -- did the AI speak before this prompt? if yes, this prompt is reacting to output
  CASE WHEN EXISTS (
    SELECT 1 FROM messages m2
    WHERE m2.conversation_id = m.conversation_id
      AND m2.role = 'assistant'
      AND m2.id < m.id
  ) THEN 1 ELSE 0 END AS reacts_to_output,
  c.estimated_pages
FROM messages m
JOIN conversations c ON c.id = m.conversation_id
JOIN sources s       ON s.id = c.source_id
WHERE m.role = 'user';

CREATE TEMP VIEW pa_cascades AS
SELECT
  conversation_id,
  conversation_title,
  source_name,
  estimated_pages,
  COUNT(*)                AS prompt_count,
  MIN(created_at)         AS started,
  MAX(created_at)         AS ended,
  AVG(approx_words)       AS avg_prompt_words,
  SUM(reacts_to_output)   AS reactions_to_outputs
FROM pa_prompts
GROUP BY conversation_id, conversation_title, source_name, estimated_pages;
