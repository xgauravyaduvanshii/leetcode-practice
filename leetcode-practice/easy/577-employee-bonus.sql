-- 577. Employee Bonus (Easy)
-- https://leetcode.com/problems/employee-bonus/
-- Submission 2200110408 -- Accepted, MySQL
SELECT name, bonus
FROM Employee
LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus IS NULL;
