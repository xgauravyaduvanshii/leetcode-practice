# LeetCode 1219. Path with Maximum Gold — Medium
# https://leetcode.com/problems/path-with-maximum-gold/
# Submission 2199013131 — Accepted, Python3
#
# My thinking: I try a walk from every gold
# cell, marking cells as I step on them so no
# cell is visited twice, and undoing the marks
# when I backtrack. The richest walk wins.

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        best = 0

        def walk(r, c, gold):
            nonlocal best
            best = max(best, gold)
            saved = grid[r][c]
            grid[r][c] = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    walk(nr, nc, gold + grid[nr][nc])
            grid[r][c] = saved

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    walk(r, c, grid[r][c])
        return best
