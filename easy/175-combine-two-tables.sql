-- 175. Combine Two Tables (Easy)
-- https://leetcode.com/problems/combine-two-tables/
-- Submission 2200107235 -- Accepted, MySQL
SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;
