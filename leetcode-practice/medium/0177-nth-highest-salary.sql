-- LeetCode 177. Nth Highest Salary — Medium
-- https://leetcode.com/problems/nth-highest-salary/
-- Submission 2204055310 — Accepted, MySQL
--
-- My thinking: distinct salaries sorted highest first
-- put the Nth highest at position N, so skip the first
-- N - 1 distinct salaries and take the next one. If
-- fewer than N distinct salaries exist, the query
-- returns no rows and the function returns NULL.
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N - 1
  );
END
