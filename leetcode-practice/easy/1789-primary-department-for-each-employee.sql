-- 1789. Primary Department for Each Employee (Easy)
-- https://leetcode.com/problems/primary-department-for-each-employee/
-- Submission 2200130421 -- Accepted, MySQL
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id IN (
       SELECT employee_id FROM Employee
       GROUP BY employee_id
       HAVING COUNT(*) = 1
   );
