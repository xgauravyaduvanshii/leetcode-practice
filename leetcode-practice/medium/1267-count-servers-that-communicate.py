# LeetCode 1267. Count Servers that Communicate — Medium
# https://leetcode.com/problems/count-servers-that-communicate/
# Submission 2199021875 — Accepted, Python3
#
# My thinking: a server can talk when another
# server shares its row or its column. I count
# the servers in every row and column first,
# then keep the ones that are not alone in
# both.

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(grid[r][c] for r in range(rows)) for c in range(cols)]
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_counts[r] > 1 or col_counts[c] > 1):
                    total += 1
        return total
