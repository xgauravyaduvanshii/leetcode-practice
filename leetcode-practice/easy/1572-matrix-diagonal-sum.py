# LeetCode 1572. Matrix Diagonal Sum — Easy
# https://leetcode.com/problems/matrix-diagonal-sum/
# Submission 2197586574 — Accepted, Python3
#
# My thinking: I add up both diagonals — row i
# contributes the element at (i, i) and the one at
# (i, n-1-i). In an odd-sized matrix the middle
# element sits on both diagonals, so I subtract it
# once to avoid counting it twice.

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n - 1 - i]
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
        return total
