# LeetCode 1631. Path With Minimum Effort — Medium
# https://leetcode.com/problems/path-with-minimum-effort/
# Submission 2199899074 — Accepted, Python3
#
# My thinking: the effort of a path is its
# biggest single step. Dijkstra with that
# cost always expands the gentlest path first,
# so the first time I reach the end it is the
# answer.

import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        best = [[float("inf")] * cols for _ in range(rows)]
        best[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            effort, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return effort
            if effort > best[r][c]:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < best[nr][nc]:
                        best[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return best[rows - 1][cols - 1]
