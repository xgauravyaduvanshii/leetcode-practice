# LeetCode 778. Swim in Rising Water — Hard
# https://leetcode.com/problems/swim-in-rising-water/
# Submission 2198675225 — Accepted, Python3
#
# My thinking: the water only rises, so the time a
# path needs is the highest square on it. I walk the
# grid with Dijkstra, where the cost of a square is
# the highest elevation met so far — the first time I
# reach the bottom-right corner, that cost is the
# smallest possible.

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        while heap:
            height, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return height
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(heap, (max(height, grid[nr][nc]), nr, nc))
        return -1
