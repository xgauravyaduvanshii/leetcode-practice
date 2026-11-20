-- 3436. Find Valid Emails (Easy)
-- https://leetcode.com/problems/find-valid-emails/
-- Submission 2200134320 -- Accepted, MySQL
-- NOTE: same case-sensitivity lesson as 1517 — MySQL REGEXP is
-- case-insensitive, so the shape check is paired with a case-sensitive
-- BINARY LIKE check for the lowercase ".com" ending.
SELECT user_id, email
FROM Users
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+\\.com$'
    AND BINARY email LIKE '%.com'
ORDER BY user_id;
