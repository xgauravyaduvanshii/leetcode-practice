# LeetCode 64. Minimum Path Sum — Medium
# https://leetcode.com/problems/minimum-path-sum/
# Submission 2203839573 — Accepted, Python3
#
# My thinking: I fill the grid with the cheapest cost to reach each
# cell, which is the cell's own value plus the cheaper of the costs
# from above and from the left. The first row and column only have one
# way in, so they just accumulate. I reuse one row of costs, updating
# it left to right, and the last cell holds the answer.

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[c] = grid[r][c]
                elif r == 0:
                    dp[c] = dp[c - 1] + grid[r][c]
                elif c == 0:
                    dp[c] = dp[c] + grid[r][c]
                else:
                    dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
        return dp[n - 1]
