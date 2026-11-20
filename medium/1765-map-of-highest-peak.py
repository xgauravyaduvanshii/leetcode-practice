# LeetCode 1765. Map of Highest Peak — Medium
# https://leetcode.com/problems/map-of-highest-peak/
# Submission 2199929416 — Accepted, Python3
#
# My thinking: water is height zero, and every
# other cell is one higher than its lowest
# neighbour. A breadth-first walk out from all
# the water at once fills every height exactly.

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    queue.append((nr, nc))
        return height
