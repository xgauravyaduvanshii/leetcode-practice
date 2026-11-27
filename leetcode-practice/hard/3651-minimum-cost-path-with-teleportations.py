# LeetCode 3651. Minimum Cost Path with Teleportations — Hard
# https://leetcode.com/problems/minimum-cost-path-with-teleportations/
# Submission 2202930227 — Accepted, Python3
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # My thinking: I keep a table of the cheapest cost to
        # reach every cell with a given number of teleports used.
        # With no teleports it is the plain walk down/right, adding
        # the cell I step onto. One more teleport can land me on
        # any cell whose value is no bigger than the value of the
        # cell I teleport from, for free — so for each value I only
        # need the cheapest cost to reach any cell of that value
        # or higher, which is a suffix minimum over the values.
        # After landing I walk again, so each layer is one
        # teleport plus one plain walk, and I repeat it k times.
        m, n = len(grid), len(grid[0])
        INF = float("inf")
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        max_v = max(max(row) for row in grid)
        for _ in range(k):
            best = [INF] * (max_v + 1)
            for i in range(m):
                for j in range(n):
                    if dp[i][j] < best[grid[i][j]]:
                        best[grid[i][j]] = dp[i][j]
            suff = [INF] * (max_v + 2)
            for v in range(max_v, -1, -1):
                suff[v] = best[v] if best[v] < suff[v + 1] else suff[v + 1]
            ndp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    c = suff[grid[i][j]]
                    if i > 0:
                        c = min(c, ndp[i - 1][j] + grid[i][j])
                    if j > 0:
                        c = min(c, ndp[i][j - 1] + grid[i][j])
                    ndp[i][j] = c
            dp = ndp
        return dp[m - 1][n - 1]
