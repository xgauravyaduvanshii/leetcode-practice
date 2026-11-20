-- 181. Employees Earning More Than Their Managers (Easy)
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Submission 2200107637 -- Accepted, MySQL
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
