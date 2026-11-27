# LeetCode 743. Network Delay Time — Medium
# https://leetcode.com/problems/network-delay-time/
# Submission 2198925448 — Accepted, Python3
#
# My thinking: the signal spreads like Dijkstra's
# algorithm — always from the node reached
# earliest so far. When every node has a time,
# the slowest one is the answer; if any node is
# never reached, there is no answer.

import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {k: 0}
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist.get(node, float("inf")):
                continue
            for neighbour, weight in graph[node]:
                arrival = time + weight
                if arrival < dist.get(neighbour, float("inf")):
                    dist[neighbour] = arrival
                    heapq.heappush(heap, (arrival, neighbour))
        return max(dist.values()) if len(dist) == n else -1
