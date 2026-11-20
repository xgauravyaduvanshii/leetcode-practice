# 3033. Modify the Matrix (Easy)
# https://leetcode.com/problems/modify-the-matrix/
# Submission 2199970073 — Accepted, Python3
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[int]:
        # My thinking: a -1 takes the biggest value in
        # its column. I work out each column's biggest
        # value once, then fill every -1 with its own
        # column's best.
        rows = len(matrix)
        cols = len(matrix[0])
        col_max = [max(matrix[r][c] for r in range(rows)) for c in range(cols)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == -1:
                    matrix[r][c] = col_max[c]
        return matrix
