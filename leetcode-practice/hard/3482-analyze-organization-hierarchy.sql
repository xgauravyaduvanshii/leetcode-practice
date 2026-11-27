-- LeetCode 3482. Analyze Organization Hierarchy — Hard
-- https://leetcode.com/problems/analyze-organization-hierarchy/
-- Submission 2202674684 — Accepted 11/11, MySQL
--
-- My thinking: the Hierarchy walk starts at the CEO and follows manager
-- links down, adding one to the level at each step. The Subtree walk
-- starts every employee as their own root and follows the same links down,
-- so it holds every descendant of every employee together with their
-- salary. A manager's team size is their descendant count minus
-- themselves, and their budget is the salary sum over that same set. The
-- answer is ordered by level, then by budget from large to small, then by
-- name.
WITH RECURSIVE Hierarchy AS (
    SELECT employee_id, employee_name, manager_id, salary, 1 AS level
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.employee_name, e.manager_id, e.salary, h.level + 1
    FROM Employees e
    JOIN Hierarchy h ON e.manager_id = h.employee_id
),
Subtree AS (
    SELECT employee_id AS root_id, employee_id AS emp_id, salary
    FROM Employees
    UNION ALL
    SELECT s.root_id, e.employee_id, e.salary
    FROM Subtree s
    JOIN Employees e ON e.manager_id = s.emp_id
)
SELECT
    h.employee_id,
    h.employee_name,
    h.level,
    (SELECT COUNT(*) - 1 FROM Subtree s WHERE s.root_id = h.employee_id) AS team_size,
    (SELECT SUM(salary) FROM Subtree s WHERE s.root_id = h.employee_id) AS budget
FROM Hierarchy h
ORDER BY h.level ASC, budget DESC, h.employee_name ASC;
