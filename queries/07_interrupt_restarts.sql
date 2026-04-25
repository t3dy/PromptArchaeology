-- 07_interrupt_restarts.sql
-- Interrupt-and-restart pattern: a new conversation began within ~10 minutes
-- of another conversation's last prompt. Often signals "halfway through I realized
-- the framing was wrong; let me restart." May also just mean "context-window full."
--
-- Note: requires reasonable created_at on messages. May be slow on full corpus.
-- Limited to most recent 100.

WITH conv_bounds AS (
  SELECT
    conversation_id,
    conversation_title,
    source_name,
    MIN(created_at) AS started,
    MAX(created_at) AS ended
  FROM pa_prompts
  WHERE created_at IS NOT NULL AND created_at != ''
  GROUP BY conversation_id, conversation_title, source_name
)
SELECT
  date(a.ended) AS d,
  a.source_name        AS first_source,
  a.conversation_title AS first_title,
  b.conversation_title AS next_title,
  CAST((julianday(b.started) - julianday(a.ended)) * 24 * 60 AS INTEGER) AS minutes_gap
FROM conv_bounds a
JOIN conv_bounds b
  ON b.started > a.ended
 AND a.source_name = b.source_name
 AND (julianday(b.started) - julianday(a.ended)) * 24 * 60 < 10
 AND a.conversation_id != b.conversation_id
ORDER BY a.ended DESC
LIMIT 100;
