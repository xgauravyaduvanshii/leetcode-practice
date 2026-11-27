# LeetCode 2373. Largest Local Values in a Matrix — Easy
# https://leetcode.com/problems/largest-local-values-in-a-matrix/
# Submission 2197775531 — Accepted, Python3
#
# My thinking: each cell of the answer is the biggest
# number in the 3x3 window centred on that position.
# I slide the window over the whole grid and take
# the max of each window.

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
        return res
