# LeetCode 1162. As Far from Land as Possible — Medium
# https://leetcode.com/problems/as-far-from-land-as-possible/
# Submission 2199008705 — Accepted, Python3
#
# My thinking: I flood outward from every land
# cell at once, one ring at a time. The last
# ring reached is the water cell farthest from
# any land.

from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
        if not queue or len(queue) == n * n:
            return -1
        distance = -1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
        return distance
