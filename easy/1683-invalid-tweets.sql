-- 1683. Invalid Tweets (Easy)
-- https://leetcode.com/problems/invalid-tweets/
-- Submission 2200127147 -- Accepted, MySQL
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
