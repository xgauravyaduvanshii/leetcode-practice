-- 586. Customer Placing the Largest Number of Orders (Easy)
-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
-- Submission 2200111355 -- Accepted, MySQL
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
