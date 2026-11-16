# LeetCode 766. Toeplitz Matrix — Easy
# https://leetcode.com/problems/toeplitz-matrix/
# Submission 2197526157 — Accepted, Python3
#
# My thinking: in a Toeplitz matrix every diagonal
# has the same value. That just means every cell
# has to equal the cell diagonally up and to its
# left — so I check that for every cell except the
# first row and first column.

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
