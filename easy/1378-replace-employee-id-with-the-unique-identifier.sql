-- 1378. Replace Employee ID With The Unique Identifier (Easy)
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
-- Submission 2200120645 -- Accepted, MySQL
SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
