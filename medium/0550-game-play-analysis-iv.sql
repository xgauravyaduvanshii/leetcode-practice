-- 550. Game Play Analysis IV (Medium)
-- https://leetcode.com/problems/game-play-analysis-iv/
-- Submission 2201062511 -- Accepted, MySQL
SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity
    GROUP BY player_id
);
