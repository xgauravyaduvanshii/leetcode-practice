-- 570. Managers with at Least 5 Direct Reports (Medium)
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Submission 2201059183 -- Accepted, MySQL
SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
);
