# LeetCode 2435. Paths in Matrix Whose Sum Is Divisible by K — Hard
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
# Submission 2201739257 — Accepted, Python3
#
# My thinking: only the remainder of the
# running sum matters — I carry, for each
# cell, how many ways reach it with each
# remainder, and pass them down and right.

MOD = 10 ** 9 + 7


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = grid[i][j] % k
                for r in range(k):
                    ways = 0
                    if i > 0:
                        ways += dp[i - 1][j][(r - v) % k]
                    if j > 0:
                        ways += dp[i][j - 1][(r - v) % k]
                    dp[i][j][r] = ways % MOD
        return dp[m - 1][n - 1][0]
