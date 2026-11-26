# LeetCode 3864. Minimum Cost to Partition a Binary String — Hard
# https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/
# Submission 2203322582 — Accepted, Python3
from functools import lru_cache


class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        # My thinking: a split only ever cuts an even-length
        # segment into two equal halves, so every segment
        # that can appear is [l, l + L) with L in n, n/2,
        # n/4, ... — only O(n) such segments exist, arranged
        # as a binary tree. dp(l, L) is the cheapest cost of
        # partitioning that segment: either keep it whole,
        # costing flatCost when it holds no '1' and
        # L * X * encCost for X ones otherwise, or, when L
        # is even, split it and add the two halves. Prefix
        # sums give each segment's one-count in O(1), and
        # memoisation makes the whole tree O(n).
        n = len(s)
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (ch == "1")

        @lru_cache(maxsize=None)
        def dp(l: int, ln: int) -> int:
            ones = pref[l + ln] - pref[l]
            leaf = flatCost if ones == 0 else ln * ones * encCost
            best = leaf
            if ln % 2 == 0:
                h = ln // 2
                best = min(best, dp(l, h) + dp(l + h, h))
            return best

        return dp(0, n)
