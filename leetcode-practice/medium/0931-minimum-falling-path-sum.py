# LeetCode 931. Minimum Falling Path Sum — Medium
# https://leetcode.com/problems/minimum-falling-path-sum/
# Submission 2198972114 — Accepted, Python3
#
# My thinking: each cell's cheapest path down
# comes from the three cells above it. I walk
# the rows top to bottom, adding each cell's
# cheapest entry cost, and take the smallest
# value in the last row.

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for row in range(1, n):
            for col in range(n):
                best = matrix[row - 1][col]
                if col > 0:
                    best = min(best, matrix[row - 1][col - 1])
                if col < n - 1:
                    best = min(best, matrix[row - 1][col + 1])
                matrix[row][col] += best
        return min(matrix[-1])
