# 4052. Cyclically Shift Rows and Columns (Easy)
# https://leetcode.com/problems/cyclically-shift-rows-and-columns/
# Submission 2200100283 — Accepted, Python3
class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        # My thinking: first I slide every row to the
        # left by its own amount, then I slide every
        # column of the result upward by its amount.
        after_rows = []
        for i in range(n):
            k = rowShift[i] % n
            after_rows.append(grid[i][k:] + grid[i][:k])
        result = [[0] * n for _ in range(n)]
        for j in range(n):
            k = colShift[j] % n
            col = [after_rows[i][j] for i in range(n)]
            col = col[k:] + col[:k]
            for i in range(n):
                result[i][j] = col[i]
        return result
