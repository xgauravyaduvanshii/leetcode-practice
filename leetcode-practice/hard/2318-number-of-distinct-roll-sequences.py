# LeetCode 2318. Number of Distinct Roll Sequences — Hard
# https://leetcode.com/problems/number-of-distinct-roll-sequences/
# Submission 2201674093 — Accepted, Python3
#
# My thinking: only the last two rolls
# matter — the next one must be coprime
# with the last and different from both —
# so I count how many ways each pair of
# last rolls can arise and grow them.

import math

MOD = 10 ** 9 + 7


class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6
        dp = [[0] * 7 for _ in range(7)]
        for a in range(1, 7):
            for b in range(1, 7):
                if a != b and math.gcd(a, b) == 1:
                    dp[a][b] = 1
        for _ in range(3, n + 1):
            ndp = [[0] * 7 for _ in range(7)]
            for a in range(1, 7):
                for b in range(1, 7):
                    if dp[a][b] == 0:
                        continue
                    for c in range(1, 7):
                        if c != a and c != b and math.gcd(b, c) == 1:
                            ndp[b][c] = (ndp[b][c] + dp[a][b]) % MOD
            dp = ndp
        total = 0
        for a in range(1, 7):
            for b in range(1, 7):
                total = (total + dp[a][b]) % MOD
        return total
