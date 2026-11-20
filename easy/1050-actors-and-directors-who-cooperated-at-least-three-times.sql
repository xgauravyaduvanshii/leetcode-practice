-- 1050. Actors and Directors Who Cooperated At Least Three Times (Easy)
-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
-- Submission 2200115515 -- Accepted, MySQL
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
