# LeetCode 764. Largest Plus Sign — Medium
# https://leetcode.com/problems/largest-plus-sign/
# Submission 2198931029 — Accepted, Python3
#
# My thinking: a plus is as big as its shortest
# arm, so I count the clear run in each of the
# four directions for every cell and keep the
# smallest of the four.

from typing import List


class Solution:
    def largestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        blocked = set(map(tuple, mines))
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        for r in range(n):
            run = 0
            for c in range(n):
                run = 0 if (r, c) in blocked else run + 1
                left[r][c] = run
            run = 0
            for c in range(n - 1, -1, -1):
                run = 0 if (r, c) in blocked else run + 1
                right[r][c] = run
        for c in range(n):
            run = 0
            for r in range(n):
                run = 0 if (r, c) in blocked else run + 1
                up[r][c] = run
            run = 0
            for r in range(n - 1, -1, -1):
                run = 0 if (r, c) in blocked else run + 1
                down[r][c] = run
        best = 0
        for r in range(n):
            for c in range(n):
                best = max(best, min(left[r][c], right[r][c], up[r][c], down[r][c]))
        return best
