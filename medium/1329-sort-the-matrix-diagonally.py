# LeetCode 1329. Sort the Matrix Diagonally — Medium
# https://leetcode.com/problems/sort-the-matrix-diagonally/
# Submission 2199032609 — Accepted, Python3
#
# My thinking: cells on one diagonal share the
# same row-minus-column value. I gather each
# diagonal, sort it, and put the values back
# from the top.

from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        diagonals = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                diagonals[r - c].append(mat[r][c])
        for key in diagonals:
            diagonals[key].sort(reverse=True)
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = diagonals[r - c].pop()
        return mat
