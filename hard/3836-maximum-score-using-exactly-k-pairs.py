# LeetCode 3836. Maximum Score Using Exactly K Pairs — Hard
# https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/
# Submission 2203281385 — Accepted, Python3
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # My thinking: dp[t][i][j] is the best score using
        # exactly t pairs inside the first i entries of nums1
        # and the first j of nums2. Either skip nums1[i-1],
        # skip nums2[j-1], or take the pair (i-1, j-1) as the
        # last pair on top of the best t-1 pairs before it.
        # Impossible states stay at negative infinity, which
        # matters because products can be negative and taking
        # a bad pair can still beat leaving the count short.
        # The answer is dp[k][n][m].
        n, m = len(nums1), len(nums2)
        NEG = float("-inf")
        dp = [[[NEG] * (m + 1) for _ in range(n + 1)] for __ in range(k + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                dp[0][i][j] = 0
        for t in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    best = max(dp[t][i - 1][j], dp[t][i][j - 1])
                    prev = dp[t - 1][i - 1][j - 1]
                    if prev != NEG:
                        best = max(best, prev + nums1[i - 1] * nums2[j - 1])
                    dp[t][i][j] = best
        return dp[k][n][m]
