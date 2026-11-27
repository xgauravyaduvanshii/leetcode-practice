-- 511. Game Play Analysis I (Easy)
-- https://leetcode.com/problems/game-play-analysis-i/
-- Submission 2200109928 -- Accepted, MySQL
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
