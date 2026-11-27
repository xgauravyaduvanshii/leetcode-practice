-- 176. Second Highest Salary (Easy)
-- https://leetcode.com/problems/second-highest-salary/
-- Submission 2201072942 -- Accepted, MySQL
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
