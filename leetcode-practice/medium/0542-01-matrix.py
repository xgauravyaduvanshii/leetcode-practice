# LeetCode 542. 01 Matrix — Medium
# https://leetcode.com/problems/01-matrix/
# Submission 2198860487 — Accepted, Python3
#
# My thinking: every zero is a starting point, so I
# spread out from all of them at once. The first
# time the wave reaches a cell, that is its nearest
# zero.

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1
        while queue:
            r, c = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        return mat
