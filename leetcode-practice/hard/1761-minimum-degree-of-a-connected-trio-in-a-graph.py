# LeetCode 1761. Minimum Degree of a Connected Trio in a Graph — Hard
# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
# Submission 2201148478 — Accepted, Python3
#
# My thinking: every trio sits on one of its three
# edges, so for each edge I look at the neighbours
# both ends share — each shared neighbour closes a
# trio, and its degree is the three degrees added
# up minus the six edges inside the trio.

class Solution:
    def minTrioDegree(self, n: int, edges: list[list[int]]) -> int:
        adj = [set() for _ in range(n + 1)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        best = float("inf")
        for u, v in edges:
            for w in adj[u] & adj[v]:
                best = min(best, len(adj[u]) + len(adj[v]) + len(adj[w]) - 6)
        return best if best != float("inf") else -1
