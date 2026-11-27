-- 196. Delete Duplicate Emails (Easy)
-- https://leetcode.com/problems/delete-duplicate-emails/
-- Submission 2200109014 -- Accepted, MySQL
DELETE p1
FROM Person p1
JOIN Person p2 ON p1.email = p2.email AND p1.id > p2.id;
