# LeetCode 2684. Maximum Number of Moves in a Grid — Medium
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
# Submission 2205193104 — Accepted, Python3
#
# My thinking: work column by column from right to left. From a
# cell, the best onward move is one plus the best value among the
# three cells in the next column that are strictly larger (up,
# level, down); with no larger neighbour the cell is a dead end
# worth 0. The last column is all 0s, and the answer is the best
# value in the first column.
class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * m
        for c in range(n - 2, -1, -1):
            ndp = [0] * m
            for r in range(m):
                nxt = -1
                for nr in (r - 1, r, r + 1):
                    if 0 <= nr < m and grid[nr][c + 1] > grid[r][c]:
                        nxt = max(nxt, dp[nr])
                ndp[r] = 0 if nxt < 0 else nxt + 1
            dp = ndp
        return max(dp)
