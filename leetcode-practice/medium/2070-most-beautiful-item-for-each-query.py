# LeetCode 2070. Most Beautiful Item for Each Query — Medium
# https://leetcode.com/problems/most-beautiful-item-for-each-query/
# Submission 2204396097 — Accepted, Python3
#
# My thinking: after sorting items by price, the best beauty available
# at any price is the running maximum of beauty so far. I store the
# sorted prices with their running best, then answer each query with
# a binary search for the most expensive item at or below the query
# price.
from bisect import bisect_right


class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        prices = []
        best = []
        cur = 0
        for p, b in items:
            cur = max(cur, b)
            prices.append(p)
            best.append(cur)
        ans = []
        for q in queries:
            i = bisect_right(prices, q) - 1
            ans.append(best[i] if i >= 0 else 0)
        return ans
