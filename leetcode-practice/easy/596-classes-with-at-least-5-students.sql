-- 596. Classes With at Least 5 Students (Easy)
-- https://leetcode.com/problems/classes-with-at-least-5-students/
-- Submission 2200112702 -- Accepted, MySQL
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
