# LeetCode 304. Range Sum Query 2D - Immutable — Medium
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# Submission 2198736449 — Accepted, Python3
#
# My thinking: I build a prefix-sum table once, so
# any rectangle's sum is four lookups — the whole
# rectangle from the corner, minus the strips above
# and to the left, plus back the corner counted
# twice.

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            row_sum = 0
            for c in range(cols):
                row_sum += matrix[r][c]
                self.prefix[r + 1][c + 1] = self.prefix[r][c + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )
