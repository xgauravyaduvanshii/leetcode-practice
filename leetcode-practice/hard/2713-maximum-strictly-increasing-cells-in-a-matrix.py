# LeetCode 2713. Maximum Strictly Increasing Cells in a Matrix — Hard
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
# Submission 2201875822 — Accepted, Python3
#
# My thinking: a cell can only follow
# a strictly smaller one in its row or
# column, so I visit the cells in
# increasing order of value, each one
# reaching back to the best chain its
# row or column has seen so far — and
# cells of the same value are settled
# together, so none of them can borrow
# from another of its own kind.

from collections import defaultdict


class Solution:
    def maxIncreasingCells(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                cells[mat[i][j]].append((i, j))
        row_best = [0] * m
        col_best = [0] * n
        ans = 0
        for val in sorted(cells):
            group = cells[val]
            dps = []
            for i, j in group:
                d = 1 + max(row_best[i], col_best[j])
                dps.append(d)
                ans = max(ans, d)
            for (i, j), d in zip(group, dps):
                row_best[i] = max(row_best[i], d)
                col_best[j] = max(col_best[j], d)
        return ans
