# LeetCode 48. Rotate Image — Medium
# https://leetcode.com/problems/rotate-image/
# Submission 2203827688 — Accepted, Python3
#
# My thinking: rotating the square 90 degrees clockwise is the same as
# flipping it over its main diagonal and then reversing each row. Both
# steps work in place, so I only swap elements and never allocate a
# second matrix.

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()
