# LeetCode 1786. Number of Restricted Paths From First to Last Node — Medium
# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# Submission 2199934585 — Accepted, Python3
#
# My thinking: a restricted path always walks
# toward the destination, so I first find
# every node's distance to the end with
# Dijkstra. Then I count paths from the start,
# visiting nodes in decreasing distance order
# and passing their counts downhill.

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = [float("inf")] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for neighbour, weight in graph[node]:
                if d + weight < dist[neighbour]:
                    dist[neighbour] = d + weight
                    heapq.heappush(heap, (dist[neighbour], neighbour))
        order = sorted(range(1, n + 1), key=lambda x: dist[x], reverse=True)
        ways = [0] * (n + 1)
        ways[1] = 1
        for node in order:
            for neighbour, _ in graph[node]:
                if dist[neighbour] < dist[node]:
                    ways[neighbour] = (ways[neighbour] + ways[node]) % mod
        return ways[n]
