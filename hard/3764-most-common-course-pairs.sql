-- LeetCode 3764. Most Common Course Pairs — Hard
-- https://leetcode.com/problems/most-common-course-pairs/
-- Submission 2203165484 — Accepted, MySQL
--
-- My thinking: a top performer is a student who finished
-- at least 5 courses with an average rating of 4 or more.
-- For each of them I order their courses by completion
-- date and take each consecutive pair with LEAD, then
-- count how often each pair occurs. I order by the count
-- descending, then by the two course names ascending
-- case-insensitively, so the order does not depend on
-- how the names were capitalised.
WITH top_users AS (
    SELECT user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(*) >= 5 AND AVG(course_rating) >= 4
),
sequenced AS (
    SELECT
        course_name,
        LEAD(course_name) OVER (
            PARTITION BY user_id
            ORDER BY completion_date
        ) AS next_course
    FROM course_completions
    WHERE user_id IN (SELECT user_id FROM top_users)
)
SELECT
    course_name AS first_course,
    next_course AS second_course,
    COUNT(*) AS transition_count
FROM sequenced
WHERE next_course IS NOT NULL
GROUP BY course_name, next_course
ORDER BY transition_count DESC, LOWER(first_course) ASC, LOWER(second_course) ASC;
