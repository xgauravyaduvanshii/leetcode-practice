# 3402. Minimum Operations to Make Columns Strictly Increasing (Easy)
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/
# Submission 2200013465 — Accepted, Python3
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # My thinking: walk down each column, making
        # every cell at least one bigger than the cell
        # above it. Whatever I add up is the number of
        # operations.
        ops = 0
        for col in range(len(grid[0])):
            for row in range(1, len(grid)):
                if grid[row][col] <= grid[row - 1][col]:
                    need = grid[row - 1][col] + 1 - grid[row][col]
                    ops += need
                    grid[row][col] += need
        return ops
