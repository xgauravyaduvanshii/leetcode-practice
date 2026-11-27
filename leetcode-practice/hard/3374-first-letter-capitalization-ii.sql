-- LeetCode 3374. First Letter Capitalization II — Hard
-- https://leetcode.com/problems/first-letter-capitalization-ii/
-- Submission 2202490023 — Accepted 15/15, MySQL
--
-- My thinking: walk the text one character at a time, carrying the output
-- built so far, the previous character and the start of the current word.
-- The word a character belongs to is the run of non-spaces from that start,
-- so I can test it directly: a word that starts with a non-letter is copied
-- unchanged; a word of two or more all-letter parts joined by hyphens gets
-- the first letter of each part (the word start, or right after a hyphen)
-- uppercased and the rest lowered; any other word gets its first letter
-- uppercased and the rest lowered.
WITH RECURSIVE chars AS (
    SELECT
        content_id,
        content_text,
        0 AS pos,
        CAST('' AS CHAR(1000)) AS built,
        ' ' AS prev_ch,
        1 AS ws
    FROM user_content
    UNION ALL
    SELECT
        content_id,
        content_text,
        pos + 1,
        CONCAT(built,
            CASE
                WHEN SUBSTRING(content_text, pos + 1, 1) = ' ' THEN ' '
                WHEN SUBSTRING(
                    CASE WHEN prev_ch = ' '
                         THEN SUBSTRING_INDEX(SUBSTRING(content_text, pos + 1), ' ', 1)
                         ELSE SUBSTRING_INDEX(SUBSTRING(content_text, ws), ' ', 1)
                    END, 1, 1) REGEXP '[A-Za-z]' = 0
                    THEN SUBSTRING(content_text, pos + 1, 1)
                WHEN (
                    CASE WHEN prev_ch = ' '
                         THEN SUBSTRING_INDEX(SUBSTRING(content_text, pos + 1), ' ', 1)
                         ELSE SUBSTRING_INDEX(SUBSTRING(content_text, ws), ' ', 1)
                    END) REGEXP '^[A-Za-z]+(-[A-Za-z]+)+$'
                    THEN CASE WHEN prev_ch IN (' ', '-')
                              THEN UPPER(SUBSTRING(content_text, pos + 1, 1))
                              ELSE LOWER(SUBSTRING(content_text, pos + 1, 1)) END
                WHEN prev_ch = ' ' THEN UPPER(SUBSTRING(content_text, pos + 1, 1))
                ELSE LOWER(SUBSTRING(content_text, pos + 1, 1))
            END),
        SUBSTRING(content_text, pos + 1, 1),
        CASE WHEN prev_ch = ' ' AND SUBSTRING(content_text, pos + 1, 1) <> ' '
             THEN pos + 1 ELSE ws END
    FROM chars
    WHERE pos < CHAR_LENGTH(content_text)
)
SELECT
    content_id,
    content_text AS original_text,
    built AS converted_text
FROM chars
WHERE pos = CHAR_LENGTH(content_text)
ORDER BY content_id;
