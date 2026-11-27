# LeetCode 498. Diagonal Traverse — Medium
# https://leetcode.com/problems/diagonal-traverse/
# Submission 2198832376 — Accepted, Python3
#
# My thinking: cells on the same diagonal share the
# same row-plus-column sum. I walk the diagonals in
# order, going up on even ones and down on odd ones,
# staying inside the matrix.

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        result = []
        for diagonal in range(rows + cols - 1):
            if diagonal % 2 == 0:
                r = min(diagonal, rows - 1)
                c = diagonal - r
                while r >= 0 and c < cols:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                c = min(diagonal, cols - 1)
                r = diagonal - c
                while c >= 0 and r < rows:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1
        return result
