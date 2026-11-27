# LeetCode 807. Max Increase to Keep City Skyline — Medium
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
# Submission 2198943129 — Accepted, Python3
#
# My thinking: a building can grow until it hits
# the tallest building in its row or in its
# column, whichever is lower. Adding up that
# headroom for every building gives the answer.

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        total = 0
        for r, row in enumerate(grid):
            for c, height in enumerate(row):
                total += min(row_max[r], col_max[c]) - height
        return total
