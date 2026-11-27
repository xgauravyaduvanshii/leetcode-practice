-- 183. Customers Who Never Order (Easy)
-- https://leetcode.com/problems/customers-who-never-order/
-- Submission 2200108580 -- Accepted, MySQL
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders);
