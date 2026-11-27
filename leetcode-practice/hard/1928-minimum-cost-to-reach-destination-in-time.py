# LeetCode 1928. Minimum Cost to Reach Destination in Time — Hard
# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
# Submission 2201236969 — Accepted, Python3
#
# My thinking: I run Dijkstra ordered by the fee
# paid so far, and for each city I keep only the
# fastest arrival I have actually expanded — a
# slower arrival can never lead to a cheaper trip,
# because the faster one was popped earlier (so it
# also cost no more) and every later fee and time
# from there is the same.

import heapq

class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        INF = float("inf")
        best = [INF] * n
        heap = [(passingFees[0], 0, 0)]
        while heap:
            fee, time, u = heapq.heappop(heap)
            if u == n - 1:
                return fee
            if time >= best[u]:
                continue
            best[u] = time
            for v, t in graph[u]:
                nt = time + t
                if nt <= maxTime:
                    heapq.heappush(heap, (fee + passingFees[v], nt, v))
        return -1
