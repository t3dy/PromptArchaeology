-- 06_obsession_lines.sql
-- Theme tracking by month. Add or remove keyword columns to track other interests.
-- Each integer is "how many user-prompts that month mentioned the term family."
-- Plot the columns as lines over months and you have a visual of your obsessions.

SELECT
  strftime('%Y-%m', created_at) AS month,
  COUNT(*) AS total_prompts,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%alchem%' OR LOWER(prompt_text) LIKE '%hermet%' THEN 1 ELSE 0 END) AS alchemy_hermetic,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%pkd%' OR LOWER(prompt_text) LIKE '%philip k%' OR LOWER(prompt_text) LIKE '% dick %' THEN 1 ELSE 0 END) AS pkd,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%nes %' OR LOWER(prompt_text) LIKE '%nsf%' OR LOWER(prompt_text) LIKE '%chiptune%' THEN 1 ELSE 0 END) AS nes_chiptune,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '% mtg %' OR LOWER(prompt_text) LIKE '%magic the gathering%' OR LOWER(prompt_text) LIKE '%commander deck%' THEN 1 ELSE 0 END) AS mtg,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%marx%' OR LOWER(prompt_text) LIKE '%capital%' THEN 1 ELSE 0 END) AS marxism,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%shakespear%' THEN 1 ELSE 0 END) AS shakespeare,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%maier%' OR LOWER(prompt_text) LIKE '%atalanta%' OR LOWER(prompt_text) LIKE '%hypnerotomach%' THEN 1 ELSE 0 END) AS scholarly_texts,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%dog%' OR LOWER(prompt_text) LIKE '%okie%' OR LOWER(prompt_text) LIKE '%attila%' OR LOWER(prompt_text) LIKE '%crockett%' THEN 1 ELSE 0 END) AS dogs,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%reaper%' OR LOWER(prompt_text) LIKE '%jsfx%' OR LOWER(prompt_text) LIKE '%midi%' THEN 1 ELSE 0 END) AS audio_tooling,
  SUM(CASE WHEN LOWER(prompt_text) LIKE '%sqlite%' OR LOWER(prompt_text) LIKE '%database%' THEN 1 ELSE 0 END) AS databases
FROM pa_prompts
WHERE created_at IS NOT NULL AND created_at != ''
GROUP BY month
ORDER BY month;
