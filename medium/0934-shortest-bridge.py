# LeetCode 934. Shortest Bridge — Medium
# https://leetcode.com/problems/shortest-bridge/
# Submission 2198972542 — Accepted, Python3
#
# My thinking: I find the first island and mark
# it, then grow outward ring by ring over the
# water. The first ring that touches the second
# island is the shortest bridge.

from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first = None
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
            if first:
                break
        island = set()
        queue = deque([first])
        island.add(first)
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in island:
                    island.add((nr, nc))
                    queue.append((nr, nc))
        queue = deque([(r, c, 0) for r, c in island])
        seen = set(island)
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    if grid[nr][nc] == 1:
                        return dist
                    seen.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        return -1
