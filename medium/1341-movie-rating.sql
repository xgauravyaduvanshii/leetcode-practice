-- 1341. Movie Rating (Medium)
-- https://leetcode.com/problems/movie-rating/
-- Submission 2200846156 -- Accepted, MySQL
(SELECT name AS results
FROM Users
JOIN MovieRating ON Users.user_id = MovieRating.user_id
GROUP BY Users.user_id
ORDER BY COUNT(*) DESC, name ASC
LIMIT 1)
UNION ALL
(SELECT title AS results
FROM Movies
JOIN MovieRating ON Movies.movie_id = MovieRating.movie_id
WHERE created_at LIKE '2020-02%'
GROUP BY Movies.movie_id
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1);
