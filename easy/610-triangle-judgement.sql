-- 610. Triangle Judgement (Easy)
-- https://leetcode.com/problems/triangle-judgement/
-- Submission 2200113566 -- Accepted, MySQL
SELECT x, y, z,
    CASE WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle;
