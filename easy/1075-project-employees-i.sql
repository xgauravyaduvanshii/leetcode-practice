-- 1075. Project Employees I (Easy)
-- https://leetcode.com/problems/project-employees-i/
-- Submission 2200116290 -- Accepted, MySQL
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project
JOIN Employee ON Project.employee_id = Employee.employee_id
GROUP BY project_id;
