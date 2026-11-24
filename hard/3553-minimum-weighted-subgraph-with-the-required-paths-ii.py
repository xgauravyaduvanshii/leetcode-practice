# LeetCode 3553. Minimum Weighted Subgraph With the Required Paths II — Hard
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/
# Submission 2202839412 — Accepted, Python3
from typing import List


class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # My thinking: the cheapest subtree that reaches dest from
        # both sources is the union of the two paths to dest, which
        # is the smallest subtree spanning all three nodes. Its
        # weight is half the sum of the three pairwise distances —
        # each edge of that subtree is counted in exactly two of
        # them. Distances come from root distances and binary-lifted
        # lowest common ancestors.
        n = max(max(u, v) for u, v, _ in edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        LOG = 18
        up = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist = [0] * n
        parent = [-1] * n
        order = [0]
        parent[0] = -2
        for u in order:
            for v, w in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    up[0][v] = u
                    order.append(v)
        up[0][0] = 0
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        def d(u, v):
            w = lca(u, v)
            return dist[u] + dist[v] - 2 * dist[w]

        return [(d(s1, s2) + d(s2, dest) + d(s1, dest)) // 2 for s1, s2, dest in queries]
