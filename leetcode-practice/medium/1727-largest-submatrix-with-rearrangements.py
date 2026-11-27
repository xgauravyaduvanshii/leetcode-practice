# LeetCode 1727. Largest Submatrix With Rearrangements — Medium
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/
# Submission 2199921832 — Accepted, Python3
#
# My thinking: I count the run of ones above
# each cell, then sort each row's heights —
# columns can be rearranged freely, so the
# best rectangle for a row is width times
# height over the sorted heights.

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == 1 else 0
            for width, height in enumerate(sorted(heights, reverse=True), 1):
                best = max(best, width * height)
        return best
