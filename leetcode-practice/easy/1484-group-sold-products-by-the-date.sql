-- 1484. Group Sold Products By The Date (Easy)
-- https://leetcode.com/problems/group-sold-products-by-the-date/
-- Submission 2200121986 -- Accepted, MySQL
SELECT sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
