# 3142. Check if Grid Satisfies Conditions (Easy)
# https://leetcode.com/problems/check-if-grid-satisfies-conditions/
# Submission 2199979400 — Accepted, Python3
from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        # My thinking: two rules — every column holds
        # one value all the way down, and neighbouring
        # columns hold different values. I check both
        # rules cell by cell.
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if r + 1 < rows and grid[r][c] != grid[r + 1][c]:
                    return False
                if c + 1 < cols and grid[r][c] == grid[r][c + 1]:
                    return False
        return True
