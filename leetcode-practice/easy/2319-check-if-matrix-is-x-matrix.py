# LeetCode 2319. Check if Matrix Is X-Matrix — Easy
# https://leetcode.com/problems/check-if-matrix-is-x-matrix/
# Submission 2197622955 — Accepted, Python3
#
# My thinking: in an X-matrix the two diagonals must
# be non-zero and everything else zero. I check
# every cell against that rule.

class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False
        return True
