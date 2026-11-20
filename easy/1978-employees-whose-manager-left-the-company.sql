-- 1978. Employees Whose Manager Left the Company (Easy)
-- https://leetcode.com/problems/employees-whose-manager-left-the-company/
-- Submission 2200133002 -- Accepted, MySQL
SELECT employee_id
FROM Employees
WHERE salary < 30000
    AND manager_id IS NOT NULL
    AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
