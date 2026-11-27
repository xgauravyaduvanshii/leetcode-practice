-- LeetCode 3617. Find Students with Study Spiral Pattern — Hard
-- https://leetcode.com/problems/find-students-with-study-spiral-pattern/
-- Submission 2202877222 — Accepted, MySQL
--
-- My thinking: for each student I read the sessions in date
-- order. The cycle length is fixed by the first subject: it is
-- the distance to its next appearance. A student qualifies
-- when that length is at least 3, the sessions run for at
-- least two full cycles, the subjects repeat with that period,
-- the subjects in one cycle are all different, and no two
-- consecutive sessions are more than 2 days apart. The total
-- hours are the sum over the student's sessions, ordered by
-- cycle length then hours, both descending.
WITH numbered AS (
    SELECT student_id, subject, session_date, hours_studied,
           ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY session_date, session_id) AS rn,
           COUNT(*) OVER (PARTITION BY student_id) AS cnt,
           LAG(session_date) OVER (PARTITION BY student_id ORDER BY session_date, session_id) AS prev_date
    FROM study_sessions
),
gap_check AS (
    SELECT student_id,
           MAX(CASE WHEN prev_date IS NOT NULL AND DATEDIFF(session_date, prev_date) > 2 THEN 1 ELSE 0 END) AS has_bad_gap
    FROM numbered
    GROUP BY student_id
),
first_subj AS (
    SELECT student_id, subject FROM numbered WHERE rn = 1
),
second_occ AS (
    SELECT n.student_id, MIN(n.rn) AS second_rn
    FROM numbered n
    JOIN first_subj f ON n.student_id = f.student_id AND n.subject = f.subject
    WHERE n.rn > 1
    GROUP BY n.student_id
),
cycle_len AS (
    SELECT student_id, second_rn - 1 AS L FROM second_occ
),
period_check AS (
    SELECT c.student_id, c.L,
           MIN(CASE WHEN a.subject = b.subject THEN 1 ELSE 0 END) AS period_ok
    FROM cycle_len c
    JOIN numbered a ON a.student_id = c.student_id
    JOIN numbered b ON b.student_id = c.student_id AND b.rn = a.rn + c.L
    JOIN (SELECT student_id, MAX(cnt) AS cnt FROM numbered GROUP BY student_id) t
      ON t.student_id = c.student_id
    WHERE a.rn <= t.cnt - c.L
    GROUP BY c.student_id, c.L
),
distinct_check AS (
    SELECT c.student_id, c.L, COUNT(DISTINCT n.subject) AS distinct_count
    FROM cycle_len c
    JOIN numbered n ON n.student_id = c.student_id AND n.rn <= c.L
    GROUP BY c.student_id, c.L
),
valid AS (
    SELECT c.student_id, c.L
    FROM cycle_len c
    JOIN gap_check g ON g.student_id = c.student_id AND g.has_bad_gap = 0
    JOIN period_check p ON p.student_id = c.student_id AND p.period_ok = 1
    JOIN distinct_check d ON d.student_id = c.student_id AND d.distinct_count = c.L
    JOIN (SELECT student_id, MAX(cnt) AS cnt FROM numbered GROUP BY student_id) t
      ON t.student_id = c.student_id
    WHERE c.L >= 3 AND t.cnt >= 2 * c.L
)
SELECT st.student_id, st.student_name, st.major, v.L AS cycle_length,
       (SELECT SUM(hours_studied) FROM numbered WHERE student_id = v.student_id) AS total_study_hours
FROM valid v
JOIN students st ON st.student_id = v.student_id
ORDER BY cycle_length DESC, total_study_hours DESC;
