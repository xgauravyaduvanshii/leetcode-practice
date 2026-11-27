# LeetCode 1252. Cells with Odd Values in a Matrix — Easy
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
# Submission 2197564792 — Accepted, Python3
#
# My thinking: instead of building the whole matrix,
# I just count how many times each row and each
# column was incremented. A cell is odd exactly
# when its row count plus its column count is odd
# — so I count those cells directly.

class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        return sum((rows[i] + cols[j]) % 2 for i in range(m) for j in range(n))
