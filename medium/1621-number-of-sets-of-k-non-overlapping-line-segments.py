# LeetCode 1621. Number of Sets of K Non-Overlapping Line Segments — Medium
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
# Submission 2199894007 — Accepted, Python3
#
# My thinking: I count ways using the first i
# points. Either point i is unused, or it ends
# a segment starting at some earlier point —
# and the segments before it must fit inside
# that start. Prefix sums keep the count fast.

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        prefix = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (dp[i - 1][j] + prefix[i - 1][j - 1]) % mod
            for j in range(k + 1):
                prefix[i][j] = (prefix[i - 1][j] + dp[i][j]) % mod
        return dp[n][k]
