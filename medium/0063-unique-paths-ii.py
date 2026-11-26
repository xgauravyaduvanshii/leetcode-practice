# LeetCode 63. Unique Paths II — Medium
# https://leetcode.com/problems/unique-paths-ii/
# Submission 2203837663 — Accepted, Python3
#
# My thinking: I count the ways to reach each cell with dynamic
# programming: a cell's count is the sum of the counts from above and
# from the left, because every path arrives through one of those two.
# Obstacles get zero, the start cell gets one unless it is blocked,
# and I reuse a single row of counts since each row only needs the one
# above it.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c - 1]
        return dp[n - 1]
