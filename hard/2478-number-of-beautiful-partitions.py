# LeetCode 2478. Number of Beautiful Partitions — Hard
# https://leetcode.com/problems/number-of-beautiful-partitions/
# Submission 2201771002 — Accepted, Python3
#
# My thinking: a beautiful piece must
# start on a prime digit and end on a
# non-prime one, so for each end I only
# need the running total of ways to reach
# the prime starts that are far enough
# back — I keep that total as a prefix
# sum and sweep it across the pieces.

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        prime = set("2357")
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for j in range(1, k + 1):
            pref = 0
            for i in range(1, n + 1):
                a = i - minLength
                if a >= 0 and s[a] in prime:
                    pref = (pref + dp[a][j - 1]) % MOD
                if s[i - 1] not in prime:
                    dp[i][j] = pref
        return dp[n][k]
