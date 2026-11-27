-- 1667. Fix Names in a Table (Easy)
-- https://leetcode.com/problems/fix-names-in-a-table/
-- Submission 2200126764 -- Accepted, MySQL
SELECT user_id,
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
