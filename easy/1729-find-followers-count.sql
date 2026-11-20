-- 1729. Find Followers Count (Easy)
-- https://leetcode.com/problems/find-followers-count/
-- Submission 2200128727 -- Accepted, MySQL
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
