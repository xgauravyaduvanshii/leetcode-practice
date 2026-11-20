-- 1517. Find Users With Valid E-Mails (Easy)
-- https://leetcode.com/problems/find-users-with-valid-e-mails/
-- Submission 2200124480 -- Accepted, MySQL
-- NOTE: the first submission (2200122785) was Wrong Answer 27/29:
-- MySQL REGEXP is case-insensitive, so it matched "@leetcode.COM".
-- REGEXP BINARY fails with a charset error, so the fix keeps REGEXP
-- for the shape and adds a case-sensitive BINARY LIKE check for the
-- exact lowercase domain.
SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
    AND BINARY mail LIKE '%@leetcode.com';
