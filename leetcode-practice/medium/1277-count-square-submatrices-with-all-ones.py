# LeetCode 1277. Count Square Submatrices with All Ones — Medium
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Submission 2199022649 — Accepted, Python3
#
# My thinking: each cell holds the size of the
# biggest all-ones square ending there — one
# more than the smallest of its top, left and
# diagonal neighbours. Adding those sizes up
# counts every square.

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        total = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1 and r > 0 and c > 0:
                    matrix[r][c] += min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                total += matrix[r][c]
        return total
