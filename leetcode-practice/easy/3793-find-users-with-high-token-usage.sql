-- 3793. Find Users with High Token Usage (Easy)
-- https://leetcode.com/problems/find-users-with-high-token-usage/
-- Submission 2200137934 -- Accepted, MySQL
-- NOTE: the candidate list called this problem "Unpivoted String",
-- but that title is wrong — the slug unpivoted-string 404s, and the
-- problem-list search by number showed 3793 is actually "Find Users
-- with High Token Usage" (same class of list error as 627 and 1817).
SELECT user_id, COUNT(*) AS prompt_count,
    ROUND(AVG(tokens), 2) AS avg_tokens
FROM prompts
GROUP BY user_id
HAVING COUNT(*) >= 3 AND MAX(tokens) > AVG(tokens)
ORDER BY avg_tokens DESC, user_id ASC;
