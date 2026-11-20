# LeetCode 1504. Count Submatrices With All Ones — Medium
# https://leetcode.com/problems/count-submatrices-with-all-ones/
# Submission 2199865669 — Accepted, Python3
#
# My thinking: I build column heights row by
# row. For each cell I look left, tracking the
# shortest height so far — every step left adds
# that many submatrices ending here.

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        heights = [0] * cols
        total = 0
        for r in range(rows):
            for c in range(cols):
                heights[c] = heights[c] + 1 if mat[r][c] == 1 else 0
            for c in range(cols):
                if heights[c] == 0:
                    continue
                min_height = heights[c]
                for left in range(c, -1, -1):
                    if heights[left] == 0:
                        break
                    min_height = min(min_height, heights[left])
                    total += min_height
        return total
