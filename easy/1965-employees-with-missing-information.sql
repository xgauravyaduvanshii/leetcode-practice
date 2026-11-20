-- 1965. Employees With Missing Information (Easy)
-- https://leetcode.com/problems/employees-with-missing-information/
-- Submission 2200132104 -- Accepted, MySQL
SELECT employee_id FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
