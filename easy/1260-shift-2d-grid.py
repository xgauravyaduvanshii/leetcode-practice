# LeetCode 1260. Shift 2D Grid — Easy
# https://leetcode.com/problems/shift-2d-grid/
# Submission 2197565141 — Accepted, Python3
#
# My thinking: shifting the grid is easier if I
# flatten it into one row first — a shift just
# moves the last k elements to the front. Then I
# chop the flat list back into rows of the original
# width. (Shifting by k is the same as shifting by
# k mod the total number of cells.)

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        k %= m * n
        flat = flat[-k:] + flat[:-k]
        return [flat[i * n:(i + 1) * n] for i in range(m)]
