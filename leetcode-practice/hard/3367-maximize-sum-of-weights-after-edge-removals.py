# LeetCode 3367. Maximize Sum of Weights after Edge Removals — Hard
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/
# Submission 2202427216 — Accepted, Python3
from typing import List


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        # My thinking: root the tree at 0. For each node I decide which
        # child edges to keep: keeping edge (u,v) gains w + dp1(v) - dp0(v)
        # over dropping it, where dp0/dp1 are the best sums in v's subtree
        # with v's parent edge dropped/taken. A node keeps at most k child
        # edges (k-1 if its own parent edge is kept), so I take the largest
        # positive gains up to that limit. I process nodes bottom-up with an
        # explicit stack to avoid recursion limits.
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        parent = [-1] * n
        parent[0] = -2
        order = [0]
        for u in order:
            for v, w in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    order.append(v)
        dp0 = [0] * n
        dp1 = [0] * n
        for u in reversed(order):
            gains = []
            base = 0
            for v, w in adj[u]:
                if parent[v] == u:
                    base += dp0[v]
                    gains.append(w + dp1[v] - dp0[v])
            gains.sort(reverse=True)
            s0 = base
            take = 0
            for g in gains:
                if take >= k or g <= 0:
                    break
                s0 += g
                take += 1
            dp0[u] = s0
            s1 = base
            take = 0
            for g in gains:
                if take >= k - 1 or g <= 0:
                    break
                s1 += g
                take += 1
            dp1[u] = s1
        return dp0[0]
