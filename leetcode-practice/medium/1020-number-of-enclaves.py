# LeetCode 1020. Number of Enclaves — Medium
# https://leetcode.com/problems/number-of-enclaves/
# Submission 2198987448 — Accepted, Python3
#
# My thinking: any land that touches the border
# can escape, so I flood away all of it first.
# Whatever land is left is trapped inside, and I
# just count it.

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        stack = []
        for r in range(rows):
            for c in (0, cols - 1):
                if grid[r][c] == 1:
                    stack.append((r, c))
        for c in range(cols):
            for r in (0, rows - 1):
                if grid[r][c] == 1:
                    stack.append((r, c))
        while stack:
            r, c = stack.pop()
            if grid[r][c] == 0:
                continue
            grid[r][c] = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    stack.append((nr, nc))
        return sum(sum(row) for row in grid)
