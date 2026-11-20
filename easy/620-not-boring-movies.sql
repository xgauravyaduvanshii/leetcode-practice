-- 620. Not Boring Movies (Easy)
-- https://leetcode.com/problems/not-boring-movies/
-- Submission 2200114409 -- Accepted, MySQL
SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 = 1 AND description != 'boring'
ORDER BY rating DESC;
