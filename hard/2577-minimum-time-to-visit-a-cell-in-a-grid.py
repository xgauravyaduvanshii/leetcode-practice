# LeetCode 2577. Minimum Time to Visit a Cell In a Grid — Hard
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
# Submission 2201828898 — Accepted, Python3
#
# My thinking: every step flips the
# parity of where I stand, so the
# earliest I can enter a cell is its
# opening time rounded up to my parity
# — I let Dijkstra carry the earliest
# arrival everywhere, and if both doors
# out of the start open too late there
# is no way in at all.

import heapq


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        # you must leave the start at t = 1; if every neighbour opens later,
        # there is nowhere to go and no way to wait
        if all(
            grid[nr][nc] > 1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            for nr, nc in [(0 + dr, 0 + dc)]
            if 0 <= nr < m and 0 <= nc < n
        ):
            return -1
        INF = float("inf")
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            t, r, c = heapq.heappop(pq)
            if t != dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return t
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nt = max(t + 1, grid[nr][nc])
                    if (nt - (nr + nc)) % 2:
                        nt += 1
                    if nt < dist[nr][nc]:
                        dist[nr][nc] = nt
                        heapq.heappush(pq, (nt, nr, nc))
        return -1
