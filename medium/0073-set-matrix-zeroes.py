# LeetCode 73. Set Matrix Zeroes — Medium
# https://leetcode.com/problems/set-matrix-zeroes/
# Submission 2201082617 — Accepted, Python3
#
# My thinking: I remember which rows and columns hold a
# zero in a first pass, then zero out exactly those rows
# and columns in a second pass.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = {r for r in range(len(matrix)) for c in range(len(matrix[0])) if matrix[r][c] == 0}
        cols = {c for r in range(len(matrix)) for c in range(len(matrix[0])) if matrix[r][c] == 0}
        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0
