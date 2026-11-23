# LeetCode 2608. Shortest Cycle in a Graph — Hard
# https://leetcode.com/problems/shortest-cycle-in-a-graph/
# Submission 2201848339 — Accepted, Python3
#
# My thinking: I walk out from every
# vertex in turn, and the first time a
# walk meets a vertex it has already
# reached by another road, the two roads
# together close a cycle — the shortest
# such meeting anywhere is the answer.

from collections import deque


class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        INF = float("inf")
        best = INF
        for s in range(n):
            dist = [-1] * n
            parent = [-1] * n
            dist[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v and parent[v] != u:
                        best = min(best, dist[u] + dist[v] + 1)
        return -1 if best == INF else best
