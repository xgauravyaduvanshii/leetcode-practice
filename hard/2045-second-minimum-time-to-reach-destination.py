# LeetCode 2045. Second Minimum Time to Reach Destination — Hard
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/
# Submission 2201557498 — Accepted, Python3
#
# My thinking: a red light only makes me wait
# for the next green, so I walk the graph keeping
# the two quickest distinct arrivals at every
# stop — the second one at the end is the answer.

import heapq


class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dist = [[] for _ in range(n + 1)]
        heap = [(0, 1)]
        while heap:
            t, u = heapq.heappop(heap)
            if len(dist[u]) == 2 and t >= dist[u][1]:
                continue
            if t in dist[u]:
                continue
            dist[u].append(t)
            dist[u].sort()
            if len(dist[u]) > 2:
                dist[u] = dist[u][:2]
            if u == n and len(dist[n]) == 2:
                return dist[n][1]
            # Wait for green if the light is red.
            if (t // change) % 2 == 1:
                depart = (t // change + 1) * change
            else:
                depart = t
            for v in graph[u]:
                heapq.heappush(heap, (depart + time, v))
        return -1
