-- LeetCode 3832. Find Users with Persistent Behavior Patterns — Hard
-- https://leetcode.com/problems/find-users-with-persistent-behavior-patterns/
-- Submission 2203279173 — Accepted, MySQL
--
-- My thinking: a day only counts if the user did exactly
-- one action on it, so first drop every (user, date) with
-- more than one row. On the surviving days, consecutive
-- dates with the same action share the value of
-- date minus its row number, so grouping by that value
-- gives each unbroken same-action streak with its length
-- and its first and last day. Keep streaks of at least 5
-- days, then per user keep the longest one, breaking ties
-- by the lexicographically smallest action and then by
-- the latest start date.
WITH single_days AS (
    SELECT user_id, action_date, MAX(action) AS action
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
),
sequenced AS (
    SELECT
        user_id,
        action,
        action_date,
        DATE_SUB(action_date, INTERVAL ROW_NUMBER() OVER (
            PARTITION BY user_id, action
            ORDER BY action_date
        ) DAY) AS grp
    FROM single_days
),
streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM sequenced
    GROUP BY user_id, action, grp
    HAVING COUNT(*) >= 5
),
ranked AS (
    SELECT
        user_id,
        action,
        streak_length,
        start_date,
        end_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY streak_length DESC, action ASC, start_date DESC
        ) AS rn
    FROM streaks
)
SELECT user_id, action, streak_length, start_date, end_date
FROM ranked
WHERE rn = 1
ORDER BY streak_length DESC, user_id ASC;
