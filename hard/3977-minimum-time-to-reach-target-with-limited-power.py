# LeetCode 3977. Minimum Time to Reach Target With Limited Power — Hard
# https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/
# Submission 2203492778 — Accepted, Python3
import heapq
from typing import List


class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        # My thinking: a state is a node together with the
        # power left on arrival, and from it you may leave
        # only when the power covers the node's cost, paying
        # that cost and the edge time. Time strictly grows
        # along every edge, so Dijkstra over these states,
        # ordered by time and breaking ties by more
        # remaining power, settles each state once; the
        # first time the target is popped it has the
        # smallest time and, among those, the most power
        # left. A single label per node would be wrong: a
        # slower arrival with more power can still continue
        # where a faster, drained one cannot.
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
        INF = float("inf")
        dist = [[INF] * (power + 1) for _ in range(n)]
        dist[source][power] = 0
        pq = [(0, -power, source, power)]
        while pq:
            time, negp, u, p = heapq.heappop(pq)
            if time != dist[u][p]:
                continue
            if u == target:
                return [time, p]
            if p < cost[u]:
                continue
            for v, t in adj[u]:
                np = p - cost[u]
                nt = time + t
                if nt < dist[v][np]:
                    dist[v][np] = nt
                    heapq.heappush(pq, (nt, -np, v, np))
        return [-1, -1]
