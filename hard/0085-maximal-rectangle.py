# LeetCode 85. Maximal Rectangle — Hard
# https://leetcode.com/problems/maximal-rectangle/
# Submission 2198383044 — Accepted, Python3
#
# My thinking: I turn every row into a histogram —
# each column's height is how many 1s stand in a
# row above it, resetting to zero on a 0. Then each
# row is the largest-rectangle-in-histogram problem:
# a rising stack measures every bar's widest stretch.
# The best rectangle over all rows is the answer.

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        best = 0
        for row in matrix:
            for j, cell in enumerate(row):
                heights[j] = heights[j] + 1 if cell == "1" else 0
            stack = []
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    left = stack[-1] + 1 if stack else 0
                    best = max(best, height * (i - left))
                stack.append(i)
        return best
