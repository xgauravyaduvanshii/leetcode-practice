# LeetCode 3686. Number of Stable Subsequences — Hard
# https://leetcode.com/problems/number-of-stable-subsequences/
# Submission 2203039730 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        # My thinking: a subsequence is stable unless it ever
        # holds three in a row of the same parity, so all I need
        # to remember about a subsequence's tail is its parity
        # and whether its current run is 1 or 2 long. For each
        # new number I either start a fresh subsequence with it,
        # extend any subsequence ending in the opposite parity
        # (its run goes back to 1), or extend one ending in the
        # same parity with run 1 (its run becomes 2) — a run-2
        # tail can never grow, so three in a row never forms.
        dp = [[0, 0, 0], [0, 0, 0]]
        for x in nums:
            q = x & 1
            add1 = (1 + dp[1 - q][1] + dp[1 - q][2]) % MOD
            add2 = dp[q][1]
            dp[q][1] = (dp[q][1] + add1) % MOD
            dp[q][2] = (dp[q][2] + add2) % MOD
        return (dp[0][1] + dp[0][2] + dp[1][1] + dp[1][2]) % MOD
