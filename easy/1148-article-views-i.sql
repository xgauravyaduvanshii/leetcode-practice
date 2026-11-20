-- 1148. Article Views I (Easy)
-- https://leetcode.com/problems/article-views-i/
-- Submission 2200118046 -- Accepted, MySQL
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
