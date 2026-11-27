-- 182. Duplicate Emails (Easy)
-- https://leetcode.com/problems/duplicate-emails/
-- Submission 2200108075 -- Accepted, MySQL
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
