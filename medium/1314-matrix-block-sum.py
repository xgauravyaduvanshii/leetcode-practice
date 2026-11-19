# LeetCode 1314. Matrix Block Sum — Medium
# https://leetcode.com/problems/matrix-block-sum/
# Submission 2199028914 — Accepted, Python3
#
# My thinking: a prefix-sum grid turns every
# block into one rectangle sum. I clamp each
# block to the grid's edges and read its sum
# straight from the prefix sums.

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
        result = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                top = max(0, r - k)
                left = max(0, c - k)
                bottom = min(rows, r + k + 1)
                right = min(cols, c + k + 1)
                result[r][c] = prefix[bottom][right] - prefix[top][right] - prefix[bottom][left] + prefix[top][left]
        return result
