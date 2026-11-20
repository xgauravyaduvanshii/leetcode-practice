# 2639. Find the Width of Columns of a Grid (Easy)
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/
# Submission 2199969068 — Accepted, Python3
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # My thinking: a column is as wide as its widest
        # entry, and an entry's width is just how many
        # characters it takes to write it down — the
        # minus sign counts too.
        widths = []
        for col in range(len(grid[0])):
            widths.append(max(len(str(grid[row][col])) for row in range(len(grid))))
        return widths
