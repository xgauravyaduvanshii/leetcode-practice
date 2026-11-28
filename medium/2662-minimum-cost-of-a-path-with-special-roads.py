# LeetCode 2662. Minimum Cost of a Path With Special Roads — Medium
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
# Submission 2205114516 — Accepted, Python3
#
# My thinking: only the start, the target and the special-road
# endpoints ever matter — between any two of them you just walk
# the Manhattan distance. Dijkstra over that small point set,
# with the special roads as extra directed edges, gives the
# cheapest route.
import heapq
import math
from collections import defaultdict


class Solution:
    def minimumCost(self, start: list[int], target: list[int],
                    specialRoads: list[list[int]]) -> int:
        points = [tuple(start), tuple(target)]
        roads = []
        for x1, y1, x2, y2, c in specialRoads:
            a, b = (x1, y1), (x2, y2)
            if a not in points:
                points.append(a)
            if b not in points:
                points.append(b)
            roads.append((a, b, c))
        idx = {p: i for i, p in enumerate(points)}
        road_from = defaultdict(list)
        for a, b, c in roads:
            road_from[idx[a]].append((idx[b], c))

        def manhattan(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])

        m = len(points)
        dist = [math.inf] * m
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            if u == 1:
                return d
            for v in range(m):
                if v == u:
                    continue
                nd = d + manhattan(points[u], points[v])
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
            for v, c in road_from[u]:
                nd = d + c
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist[1]
