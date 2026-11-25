-- LeetCode 3673. Find Zombie Sessions — Hard
-- https://leetcode.com/problems/find-zombie-sessions/
-- Submission 2203032111 — Accepted, MySQL
--
-- My thinking: I group the events by session (and user),
-- then measure each session: whole minutes from its first
-- to its last event, how many scrolls, clicks and purchases
-- it has. A zombie session lasts more than 30 minutes, has
-- at least 5 scrolls, fewer than 0.20 clicks per scroll, and
-- no purchase at all. I order by scroll count descending,
-- then session id ascending.
SELECT
    session_id,
    user_id,
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS session_duration_minutes,
    SUM(event_type = 'scroll') AS scroll_count
FROM app_events
GROUP BY session_id, user_id
HAVING session_duration_minutes > 30
    AND scroll_count >= 5
    AND SUM(event_type = 'click') / scroll_count < 0.20
    AND SUM(event_type = 'purchase') = 0
ORDER BY scroll_count DESC, session_id ASC;
