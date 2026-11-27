# LeetCode 2093. Minimum Weighted Subgraph With the Required Paths — Hard
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
# Submission 2200905524 — Accepted, Python3
#
# My thinking: the cheapest shared route is two paths from
# the two starts meeting at some middle node, then one
# path on to the destination — so I run Dijkstra from
# both starts and backwards from the destination and
# take the best meeting point.

import heapq


class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        graph = [[] for _ in range(n)]
        reverse = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            reverse[v].append((u, w))

        def dijkstra(start: int, adj: list[list[tuple[int, int]]]) -> list[int]:
            dist = [float("inf")] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, node = heapq.heappop(heap)
                if d != dist[node]:
                    continue
                for nxt, w in adj[node]:
                    if dist[nxt] > d + w:
                        dist[nxt] = d + w
                        heapq.heappush(heap, (dist[nxt], nxt))
            return dist

        d1 = dijkstra(src1, graph)
        d2 = dijkstra(src2, graph)
        dd = dijkstra(dest, reverse)
        best = min(d1[i] + d2[i] + dd[i] for i in range(n))
        return -1 if best == float("inf") else best
