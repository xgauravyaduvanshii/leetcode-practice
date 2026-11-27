# LeetCode 2503. Maximum Number of Points From Grid Queries — Hard
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
# Submission 2201783889 — Accepted, Python3
#
# My thinking: a query can only ever
# reach cells smaller than itself, so I
# sort the queries and grow one frontier
# with a min-heap — each cell is claimed
# the first time the heap's smallest wall
# drops below the query, and the running
# count answers every query in order.

import heapq


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        m, n = len(grid), len(grid[0])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        seen = [[False] * n for _ in range(m)]
        heap = [(grid[0][0], 0, 0)]
        seen[0][0] = True
        points = 0
        for qi in order:
            q = queries[qi]
            while heap and heap[0][0] < q:
                _, r, c = heapq.heappop(heap)
                points += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not seen[nr][nc]:
                        seen[nr][nc] = True
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            ans[qi] = points
        return ans
