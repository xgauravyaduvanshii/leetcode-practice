-- 619. Biggest Single Number (Easy)
-- https://leetcode.com/problems/biggest-single-number/
-- Submission 2200113990 -- Accepted, MySQL
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1
);
