-- 584. Find Customer Referee (Easy)
-- https://leetcode.com/problems/find-customer-referee/
-- Submission 2200110961 -- Accepted, MySQL
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
