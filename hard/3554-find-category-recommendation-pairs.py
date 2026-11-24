# LeetCode 3554. Find Category Recommendation Pairs — Hard
# https://leetcode.com/problems/find-category-recommendation-pairs/
# Pandas submission 2202841171 — Accepted
import pandas as pd


def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # My thinking: first I collapse each user's purchases to the
    # distinct categories they bought from. Then I pair those
    # categories up per user (a self-join on user_id, keeping
    # category1 < category2), count how many users each pair
    # shares, keep only the pairs with at least 3, and order by
    # that count descending, then the two category names.
    merged = product_purchases.merge(product_info, on="product_id")
    user_cats = merged[["user_id", "category"]].drop_duplicates()
    a = user_cats.rename(columns={"category": "category1"})
    b = user_cats.rename(columns={"category": "category2"})
    pairs = a.merge(b, on="user_id")
    pairs = pairs[pairs["category1"] < pairs["category2"]]
    result = pairs.groupby(["category1", "category2"]).size().reset_index(name="customer_count")
    result = result[result["customer_count"] >= 3]
    result = result.sort_values(
        ["customer_count", "category1", "category2"], ascending=[False, True, True]
    )
    return result[["category1", "category2", "customer_count"]]
