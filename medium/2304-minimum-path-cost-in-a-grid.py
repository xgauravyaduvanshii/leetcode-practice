# LeetCode 2304. Minimum Path Cost in a Grid — Medium
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/
# Submission 2204660329 — Accepted, Python3
#
# My thinking: only the previous row matters, so I keep one DP row. The
# cost of stepping into cell (i, j) is the cell's own value plus the
# cheapest way to arrive there: min over k of dp[k] + moveCost[value of
# the cell above in column k][j]. Roll the row forward and take the
# minimum of the last row.
class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]
        for i in range(1, m):
            ndp = [0] * n
            for j in range(n):
                ndp[j] = grid[i][j] + min(dp[k] + moveCost[grid[i - 1][k]][j] for k in range(n))
            dp = ndp
        return min(dp)
