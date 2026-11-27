# LeetCode 59. Spiral Matrix II — Medium
# https://leetcode.com/problems/spiral-matrix-ii/
# Submission 2203833901 — Accepted, Python3
#
# My thinking: I fill the square layer by layer, walking each layer
# in four straight runs — left to right across the top, top to bottom
# down the right side, right to left across the bottom, and bottom to
# top up the left side — writing the next number at each step. After a
# layer is done I shrink the borders by one and start the next layer.

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                matrix[top][c] = num
                num += 1
            top += 1
            for r in range(top, bottom + 1):
                matrix[r][right] = num
                num += 1
            right -= 1
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = num
                num += 1
            bottom -= 1
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = num
                num += 1
            left += 1
        return matrix
