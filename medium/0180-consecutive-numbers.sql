-- 180. Consecutive Numbers (Medium)
-- https://leetcode.com/problems/consecutive-numbers/
-- Submission 2200846779 -- Accepted, MySQL
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.Id = l2.Id - 1 AND l1.Num = l2.Num
JOIN Logs l3 ON l1.Id = l3.Id - 2 AND l1.Num = l3.Num;
