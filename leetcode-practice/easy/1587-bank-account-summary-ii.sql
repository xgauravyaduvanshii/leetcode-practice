-- 1587. Bank Account Summary II (Easy)
-- https://leetcode.com/problems/bank-account-summary-ii/
-- Submission 2200125689 -- Accepted, MySQL
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
