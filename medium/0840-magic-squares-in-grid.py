# LeetCode 840. Magic Squares In Grid — Medium
# https://leetcode.com/problems/magic-squares-in-grid/
# Submission 2198952256 — Accepted, Python3
#
# My thinking: a magic square must hold exactly
# the numbers 1 to 9, and every row, column and
# diagonal must add to the same total. I check
# each 3 by 3 window in the grid.

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r, c):
            values = [grid[r + dr][c + dc] for dr in range(3) for dc in range(3)]
            if sorted(values) != list(range(1, 10)):
                return False
            target = sum(grid[r][c:c + 3])
            for dr in range(3):
                if sum(grid[r + dr][c:c + 3]) != target:
                    return False
            for dc in range(3):
                if sum(grid[r + dr][c] for dr in range(3)) != target:
                    return False
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != target:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != target:
                return False
            return True

        rows, cols = len(grid), len(grid[0])
        return sum(is_magic(r, c) for r in range(rows - 2) for c in range(cols - 2))
