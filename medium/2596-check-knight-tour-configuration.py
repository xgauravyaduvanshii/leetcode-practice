# LeetCode 2596. Check Knight Tour Configuration — Medium
# https://leetcode.com/problems/check-knight-tour-configuration/
# Submission 2205094511 — Accepted, Python3
#
# My thinking: record where each number sits, then check the
# tour in order — it must start at (0, 0) with value 0, and
# every step from v to v+1 must be a knight's move, i.e. the
# row/col gaps are (1, 2) or (2, 1) in some order.
class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        pos = {}
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i, j)
        if pos[0] != (0, 0):
            return False
        for v in range(n * n - 1):
            r1, c1 = pos[v]
            r2, c2 = pos[v + 1]
            if (abs(r1 - r2), abs(c1 - c2)) not in ((1, 2), (2, 1)):
                return False
        return True
