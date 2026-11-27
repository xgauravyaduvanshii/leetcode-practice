# LeetCode 1091. Shortest Path in Binary Matrix — Medium
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Submission 2198997519 — Accepted, Python3
#
# My thinking: I walk out from the top-left
# corner one ring at a time, in all eight
# directions. The first time I reach the
# bottom-right corner is the shortest path.

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        while queue:
            r, c, steps = queue.popleft()
            if r == n - 1 and c == n - 1:
                return steps
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc, steps + 1))
        return -1
