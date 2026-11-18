# LeetCode 474. Ones and Zeroes — Medium
# https://leetcode.com/problems/ones-and-zeroes/
# Submission 2198818261 — Accepted, Python3
#
# My thinking: each string costs some zeros and
# some ones, so this is a knapsack with two limits.
# I build up the best count for every budget of
# zeros and ones, string by string, working
# backwards so each string is used at most once.

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]
