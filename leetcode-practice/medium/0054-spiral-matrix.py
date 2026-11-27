# LeetCode 54. Spiral Matrix — Medium
# https://leetcode.com/problems/spiral-matrix/
# Submission 2201082099 — Accepted, Python3
#
# My thinking: I peel the grid one layer at a time —
# top row left to right, right side top to bottom,
# bottom row right to left, left side bottom to top
# — then move inward until nothing is left.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
        return result
