-- 1084. Sales Analysis III (Easy)
-- https://leetcode.com/problems/sales-analysis-iii/
-- Submission 2200117172 -- Accepted, MySQL
SELECT product_id, product_name
FROM Product
WHERE product_id IN (
    SELECT product_id FROM Sales
    GROUP BY product_id
    HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'
);
