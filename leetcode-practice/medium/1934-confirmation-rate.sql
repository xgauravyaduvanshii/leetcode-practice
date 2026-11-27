-- 1934. Confirmation Rate (Medium)
-- https://leetcode.com/problems/confirmation-rate/
-- Submission 2201059984 -- Accepted, MySQL
SELECT s.user_id, ROUND(IFNULL(AVG(c.action = 'confirmed'), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id;
