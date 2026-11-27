# LeetCode 2661. First Completely Painted Row or Column — Medium
# https://leetcode.com/problems/first-completely-painted-row-or-column/
# Submission 2197814414 — Accepted, Python3
#
# My thinking: I remember where each value sits in
# the matrix. Then I walk through the painting
# order, counting how many cells of each row and
# column are painted, and stop as soon as a row or
# a column is fully painted.

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)
        rows = [0] * m
        cols = [0] * n
        for idx, v in enumerate(arr):
            i, j = pos[v]
            rows[i] += 1
            cols[j] += 1
            if rows[i] == n or cols[j] == m:
                return idx
        return -1
