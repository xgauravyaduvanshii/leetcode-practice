# 3643. Flip Square Submatrix Vertically (Easy)
# https://leetcode.com/problems/flip-square-submatrix-vertically/
# Submission 2200034751 — Accepted, Python3
from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # My thinking: inside the chosen square, the
        # top row swaps with the bottom row, the second
        # row with the second from the bottom, and so
        # on — everything outside the square stays
        # exactly where it is.
        for i in range(k // 2):
            top = x + i
            bottom = x + k - 1 - i
            for j in range(y, y + k):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
        return grid
