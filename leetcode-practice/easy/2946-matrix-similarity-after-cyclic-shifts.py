# LeetCode 2946. Matrix Similarity After Cyclic Shifts — Easy
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
# Submission 2198703497 — Accepted, Python3
#
# My thinking: even rows shift left and odd rows
# shift right, k times. I apply the shift to each
# row and check whether it still matches the
# original — if every row does, the matrix is
# similar to itself.

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        cols = len(mat[0])
        k %= cols
        if k == 0:
            return True
        for row_index, row in enumerate(mat):
            if row_index % 2 == 0:
                shifted = row[k:] + row[:k]
            else:
                shifted = row[-k:] + row[:-k]
            if shifted != row:
                return False
        return True
