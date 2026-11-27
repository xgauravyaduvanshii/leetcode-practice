# LeetCode 695. Max Area of Island — Medium
# https://leetcode.com/problems/max-area-of-island/
# Submission 2198916037 — Accepted, Python3
#
# My thinking: every patch of land is an island, so
# I flood each unvisited land cell, mark it as I
# go so it is never counted twice, and keep the
# biggest flood.

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                area = 0
                stack = [(r, c)]
                grid[r][c] = 0
                while stack:
                    cr, cc = stack.pop()
                    area += 1
                    for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                best = max(best, area)
        return best
