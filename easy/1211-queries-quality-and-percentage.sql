-- 1211. Queries Quality and Percentage (Easy)
-- https://leetcode.com/problems/queries-quality-and-percentage/
-- Submission 2200118785 -- Accepted, MySQL
SELECT query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
