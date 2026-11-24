# LeetCode 3559. Number of Ways to Assign Edge Weights II — Hard
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
# Submission 2202843298 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # My thinking: on a path of L edges, giving an edge weight 1
        # or 2, the total is odd exactly when the number of 1s is
        # odd — the 2s contribute an even amount. Summing the
        # binomial coefficients over the odd counts gives 2^(L-1)
        # (and 0 when the path is empty). So each query only needs
        # the length of the path, which I get from depths and a
        # binary-lifted lowest common ancestor.
        n = max(max(u, v) for u, v in edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = 18
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        order = [1]
        parent[1] = -1
        for u in order:
            for v in adj[u]:
                if parent[v] == 0:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    up[0][v] = u
                    order.append(v)
        up[0][1] = 1
        for k in range(1, LOG):
            for i in range(1, n + 1):
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

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            L = depth[u] + depth[v] - 2 * depth[lca(u, v)]
            ans.append(pow(2, L - 1, MOD))
        return ans
