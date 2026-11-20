-- 1757. Recyclable and Low Fat Products (Easy)
-- https://leetcode.com/problems/recyclable-and-low-fat-products/
-- Submission 2200129997 -- Accepted, MySQL
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
