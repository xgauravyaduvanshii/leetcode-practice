# LeetCode 1584. Min Cost to Connect All Points — Medium
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Submission 2199885138 — Accepted, Python3
#
# My thinking: this is a minimum spanning
# tree on Manhattan distances. Prim's method
# grows it one cheapest edge at a time from
# the points already connected.

import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        total = 0
        connected = 0
        while connected < n:
            cost, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            total += cost
            connected += 1
            x1, y1 = points[node]
            for other in range(n):
                if not visited[other]:
                    x2, y2 = points[other]
                    heapq.heappush(heap, (abs(x1 - x2) + abs(y1 - y2), other))
        return total
