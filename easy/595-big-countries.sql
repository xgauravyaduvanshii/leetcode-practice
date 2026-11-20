-- 595. Big Countries (Easy)
-- https://leetcode.com/problems/big-countries/
-- Submission 2200112290 -- Accepted, MySQL
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
