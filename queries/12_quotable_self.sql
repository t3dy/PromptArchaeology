-- 12_quotable_self.sql
-- Surface short, declarative, possibly quotable user prompts.
-- "I think X..." / "the real question is..." / "what matters is..."
-- Useful as raw material for an essay, a journal entry, or a quiet ego boost.

SELECT
  date(created_at) AS d,
  conversation_title,
  approx_words,
  prompt_text
FROM pa_prompts
WHERE approx_words BETWEEN 8 AND 35
  AND (
       LOWER(prompt_text) LIKE 'i think %'
    OR LOWER(prompt_text) LIKE 'the real %'
    OR LOWER(prompt_text) LIKE 'the question is %'
    OR LOWER(prompt_text) LIKE 'what matters is %'
    OR LOWER(prompt_text) LIKE 'my whole point %'
    OR LOWER(prompt_text) LIKE 'the thing about %'
    OR LOWER(prompt_text) LIKE 'i actually believe %'
    OR LOWER(prompt_text) LIKE 'the way i see it %'
  )
ORDER BY RANDOM()
LIMIT 30;
