-- 08_thousand_page_anatomy.sql
-- The really long cascades. Each is essentially a book-length conversation on one topic.
-- Use chunk_cascade.py <conversation_id> to break each into prompt-only readable chunks.
-- The 1000-page conversations are your highest-signal scholarly artifacts.

SELECT
  conversation_id,
  conversation_title,
  source_name,
  prompt_count,
  ROUND(estimated_pages, 1) AS pages,
  ROUND(avg_prompt_words, 1) AS avg_prompt_words,
  reactions_to_outputs,
  date(started) AS started,
  date(ended)   AS ended,
  CAST(julianday(ended) - julianday(started) AS INTEGER) AS span_days
FROM pa_cascades
WHERE estimated_pages >= 50
ORDER BY estimated_pages DESC
LIMIT 100;
