-- 1045. Customers Who Bought All Products (Easy)
-- https://leetcode.com/problems/customers-who-bought-all-products/
-- Submission 2200844614 -- Accepted, MySQL
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
