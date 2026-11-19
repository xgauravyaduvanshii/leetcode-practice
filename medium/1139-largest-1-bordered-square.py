# LeetCode 1139. Largest 1-Bordered Square — Medium
# https://leetcode.com/problems/largest-1-bordered-square/
# Submission 2199004459 — Accepted, Python3
#
# My thinking: for every cell I count how many
# ones run right and down from it. A square
# starting there works when its far edges have
# enough ones too, so I try the biggest size
# first and keep the best.

from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        right = [[0] * (cols + 1) for _ in range(rows)]
        down = [[0] * cols for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if grid[r][c] == 1:
                    right[r][c] = right[r][c + 1] + 1
                    down[r][c] = down[r + 1][c] + 1
        best = 0
        for r in range(rows):
            for c in range(cols):
                max_side = min(right[r][c], down[r][c])
                for side in range(max_side, best, -1):
                    if right[r + side - 1][c] >= side and down[r][c + side - 1] >= side:
                        best = side
                        break
        return best * best
