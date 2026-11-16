# LeetCode 867. Transpose Matrix — Easy
# https://leetcode.com/problems/transpose-matrix/
# Submission 2197536393 — Accepted, Python3
#
# My thinking: transposing just swaps rows and
# columns — the element at row i, column j moves
# to row j, column i. So I build the new matrix
# column by column, reading down each column of
# the original.

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        return [[matrix[i][j] for i in range(m)] for j in range(n)]
