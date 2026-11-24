-- LeetCode 3554. Find Category Recommendation Pairs — Hard
-- https://leetcode.com/problems/find-category-recommendation-pairs/
-- MySQL submission 2202842041 — Accepted
--
-- My thinking: first I collapse each user's purchases to the
-- distinct categories they bought from. Then I pair those
-- categories up per user (a self-join on user_id, keeping
-- category1 < category2), count how many users each pair
-- shares, keep only the pairs with at least 3, and order by
-- that count descending, then the two category names.
WITH UserCategories AS (
    SELECT DISTINCT pp.user_id, pi.category
    FROM ProductPurchases pp
    JOIN ProductInfo pi ON pp.product_id = pi.product_id
)
SELECT
    a.category AS category1,
    b.category AS category2,
    COUNT(*) AS customer_count
FROM UserCategories a
JOIN UserCategories b
    ON a.user_id = b.user_id
    AND a.category < b.category
GROUP BY a.category, b.category
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC, category1 ASC, category2 ASC;
