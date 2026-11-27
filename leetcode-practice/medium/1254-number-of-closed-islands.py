# LeetCode 1254. Number of Closed Islands — Medium
# https://leetcode.com/problems/number-of-closed-islands/
# Submission 2199018869 — Accepted, Python3
#
# My thinking: I flood in from every border
# cell, which wipes out all the water that
# touches the edge. Whatever water is left
# sits in closed islands, one flood each.

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def flood(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 1:
                return
            grid[r][c] = 1
            flood(r + 1, c)
            flood(r - 1, c)
            flood(r, c + 1)
            flood(r, c - 1)

        for r in range(rows):
            flood(r, 0)
            flood(r, cols - 1)
        for c in range(cols):
            flood(0, c)
            flood(rows - 1, c)
        closed = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed += 1
                    flood(r, c)
        return closed
