-- 178. Rank Scores (Medium)
-- https://leetcode.com/problems/rank-scores/
-- Submission 2200846636 -- Accepted, MySQL
SELECT score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
