# LeetCode 861. Score After Flipping Matrix — Medium
# https://leetcode.com/problems/score-after-flipping-matrix/
# Submission 2198957011 — Accepted, Python3
#
# My thinking: the first column is worth the
# most, so I flip every row that starts with 0.
# After that, each column is flipped on its own
# whenever that gives more ones.

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = rows * (1 << (cols - 1))
        for c in range(1, cols):
            ones = 0
            for r in range(rows):
                ones += grid[r][c] if grid[r][0] == 1 else 1 - grid[r][c]
            total += max(ones, rows - ones) * (1 << (cols - 1 - c))
        return total
