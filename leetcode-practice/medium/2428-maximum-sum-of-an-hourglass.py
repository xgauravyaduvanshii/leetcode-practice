# LeetCode 2428. Maximum Sum of an Hourglass — Medium
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/
# Submission 2197782937 — Accepted, Python3
#
# My thinking: an hourglass is the top row of three
# cells, the middle cell of the next row, and the
# bottom row of three cells. I try every possible
# hourglass position and keep the biggest sum.

class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        best = 0
        for i in range(m - 2):
            for j in range(n - 2):
                s = (grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                     + grid[i + 1][j + 1]
                     + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2])
                best = max(best, s)
        return best
