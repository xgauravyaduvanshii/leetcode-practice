# LeetCode 2642. Design Graph With Shortest Path Calculator — Hard
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
# Submission 2200907091 — Accepted, Python3
#
# My thinking: the graph only ever gains edges, so every
# query is a fresh Dijkstra run from the start node over
# the edges added so far.

import heapq


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = {node1: 0}
        heap = [(0, node1)]
        while heap:
            d, node = heapq.heappop(heap)
            if d != dist[node]:
                continue
            if node == node2:
                return d
            for nxt, w in self.graph[node]:
                if dist.get(nxt, float("inf")) > d + w:
                    dist[nxt] = d + w
                    heapq.heappush(heap, (dist[nxt], nxt))
        return -1
