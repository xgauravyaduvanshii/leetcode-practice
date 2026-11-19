# LeetCode 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold — Medium
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# Submission 2199026300 — Accepted, Python3
#
# My thinking: a prefix-sum grid gives any
# square's sum in one step. I grow squares
# from each top-left corner and keep the
# biggest one that still fits the threshold.

from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
        best = 0
        for r in range(rows):
            for c in range(cols):
                for size in range(best + 1, min(rows - r, cols - c) + 1):
                    total = prefix[r + size][c + size] - prefix[r][c + size] - prefix[r + size][c] + prefix[r][c]
                    if total <= threshold:
                        best = size
                    else:
                        break
        return best
