# LeetCode 2203. Minimum Weighted Subgraph With the Required Paths — Hard
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
# Solved on LeetCode Nov 22, 2026 — Accepted, Python3 (repo file reconstructed
# and verified locally; the original submission id was not recorded).
#
# My thinking: the two routes can share their
# tail, so they meet at some junction — I
# measure the cheapest way into every
# junction from both starts and out to the
# destination, and the cheapest meeting
# point wins.

import heapq


class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        forward = [[] for _ in range(n)]
        reverse = [[] for _ in range(n)]
        for u, v, w in edges:
            forward[u].append((v, w))
            reverse[v].append((u, w))

        def dijkstra(start, graph):
            INF = float('inf')
            dist = [INF] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist

        d1 = dijkstra(src1, forward)
        d2 = dijkstra(src2, forward)
        d3 = dijkstra(dest, reverse)
        ans = min(d1[v] + d2[v] + d3[v] for v in range(n))
        return -1 if ans == float('inf') else ans
