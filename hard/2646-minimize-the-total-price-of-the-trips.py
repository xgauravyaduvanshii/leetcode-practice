# LeetCode 2646. Minimize the Total Price of the Trips — Hard
# https://leetcode.com/problems/minimize-the-total-price-of-the-trips/
# Submission 2201857390 — Accepted, Python3
#
# My thinking: I count how many trips
# cross each node, then halving a node
# saves half its price times its trips
# — and since halved nodes may never sit
# side by side, I pick the best set the
# way you would rob houses on a tree.

import sys
sys.setrecursionlimit(300000)


class Solution:
    def minimumTotalPrice(self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = -2
        for u in order:
            for w in adj[u]:
                if parent[w] == -1:
                    parent[w] = u
                    depth[w] = depth[u] + 1
                    order.append(w)
        LOG = (n).bit_length()
        up = [[-1] * n for _ in range(LOG)]
        for i in range(n):
            up[0][i] = parent[i] if parent[i] >= 0 else i
        for j in range(1, LOG):
            for i in range(n):
                up[j][i] = up[j - 1][up[j - 1][i]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return parent[a]

        diff = [0] * n
        for u, v in trips:
            w = lca(u, v)
            diff[u] += 1
            diff[v] += 1
            diff[w] -= 1
            if parent[w] >= 0:
                diff[parent[w]] -= 1
        count = [0] * n
        for u in reversed(order):
            count[u] += diff[u]
            if parent[u] >= 0:
                count[parent[u]] += count[u]
        base = sum(price[i] * count[i] for i in range(n))
        # tree DP: dp0 = best saving below u when u is not halved,
        # dp1 = best saving when u is halved
        dp0 = [0] * n
        dp1 = [0] * n
        for u in reversed(order):
            save = (price[u] // 2) * count[u]
            s0 = 0
            s1 = save
            for w in adj[u]:
                if parent[w] == u:
                    s0 += max(dp0[w], dp1[w])
                    s1 += dp0[w]
            dp0[u] = s0
            dp1[u] = s1
        # the root itself may be halved too, so take the better of the two
        return base - max(dp0[0], dp1[0])
