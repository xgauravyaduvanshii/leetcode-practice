# LeetCode 3123. Find Edges in Shortest Paths — Hard
# https://leetcode.com/problems/find-edges-in-shortest-paths/
# Submission 2202014347 — Accepted, Python3
#
# My thinking: an edge lies on a
# shortest path exactly when going
# through it from 0 and then on to
# n - 1 costs the same as the shortest
# distance. I run Dijkstra from both
# ends once and test every edge against
# that sum.

from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        import heapq
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        def dijkstra(src):
            INF = 10 ** 18
            dist = [INF] * n
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        d0 = dijkstra(0)
        d1 = dijkstra(n - 1)
        total = d0[n - 1]
        ans = []
        for a, b, w in edges:
            ok = (d0[a] + w + d1[b] == total) or (d0[b] + w + d1[a] == total)
            ans.append(ok)
        return ans
