# LeetCode 3620. Network Recovery Pathways — Hard
# https://leetcode.com/problems/network-recovery-pathways/
# Submission 2202882743 — Accepted, Python3
from typing import List
from collections import deque


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # My thinking: the answer is the largest minimum edge cost
        # over valid paths, so I binary search that value. For a
        # trial value X I keep only edges costing at least X and
        # ask whether a path from 0 to n-1 through online nodes
        # costs at most k in total. Because the graph is a DAG, that
        # check is a single pass in topological order, which keeps
        # the whole search cheap.
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, c in edges:
            adj[u].append((v, c))
            indeg[v] += 1
        dq = deque([i for i in range(n) if indeg[i] == 0])
        topo = []
        while dq:
            u = dq.popleft()
            topo.append(u)
            for v, c in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    dq.append(v)
        costs = sorted({c for _, _, c in edges})
        INF = float("inf")

        def can(X):
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, c in adj[u]:
                    if c < X:
                        continue
                    if v != 0 and v != n - 1 and not online[v]:
                        continue
                    if dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c
            return dist[n - 1] <= k

        if not can(0):
            return -1
        lo, hi = 0, len(costs) - 1
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(costs[mid]):
                best = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return best
