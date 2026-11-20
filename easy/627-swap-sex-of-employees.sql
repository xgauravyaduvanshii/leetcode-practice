-- 627. Swap Sex of Employees (Easy)
-- https://leetcode.com/problems/swap-sex-of-employees/
-- Submission 2200115058 -- Accepted, MySQL
-- NOTE: LeetCode renamed this problem from "Swap Salary" to
-- "Swap Sex of Employees"; the slug is swap-sex-of-employees.
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END;
