-- 1068. Product Sales Analysis I (Easy)
-- https://leetcode.com/problems/product-sales-analysis-i/
-- Submission 2200115889 -- Accepted, MySQL
SELECT product_name, year, price
FROM Sales
JOIN Product ON Sales.product_id = Product.product_id;
