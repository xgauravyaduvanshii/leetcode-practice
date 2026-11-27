-- 607. Sales Person (Easy)
-- https://leetcode.com/problems/sales-person/
-- Submission 2200113151 -- Accepted, MySQL
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    JOIN Company ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
);
