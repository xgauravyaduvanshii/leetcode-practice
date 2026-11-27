# LeetCode 2328. Number of Increasing Paths in a Grid — Hard
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# Submission 2201682110 — Accepted, Python3
#
# My thinking: every cell starts a path of
# its own and grows into each taller
# neighbour — I memoise how many paths
# each cell begins and add them all up.

MOD = 10 ** 9 + 7


class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            total = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    total = (total + dfs(ni, nj)) % MOD
            dp[i][j] = total
            return total

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD
        return ans
