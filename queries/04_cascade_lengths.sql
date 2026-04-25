-- 04_cascade_lengths.sql
-- Distribution of cascade lengths.
-- Long cascades = unstable framing or deep exploration.
-- Short cascades = operational, single-turn requests.

SELECT
  CASE
    WHEN prompt_count = 1 THEN '1 (one-shot)'
    WHEN prompt_count <= 3 THEN '02-03'
    WHEN prompt_count <= 10 THEN '04-10'
    WHEN prompt_count <= 30 THEN '11-30'
    WHEN prompt_count <= 100 THEN '031-100'
    WHEN prompt_count <= 300 THEN '101-300'
    WHEN prompt_count <= 1000 THEN '301-1000'
    ELSE '1000+'
  END AS bucket,
  COUNT(*)                   AS cascade_count,
  ROUND(AVG(estimated_pages), 1) AS avg_pages,
  ROUND(AVG(avg_prompt_words), 1) AS avg_prompt_words
FROM pa_cascades
GROUP BY bucket
ORDER BY MIN(prompt_count);
