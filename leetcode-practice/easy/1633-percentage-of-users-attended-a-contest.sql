-- 1633. Percentage of Users Attended a Contest (Easy)
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/
-- Submission 2200126107 -- Accepted, MySQL
SELECT contest_id,
    ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
