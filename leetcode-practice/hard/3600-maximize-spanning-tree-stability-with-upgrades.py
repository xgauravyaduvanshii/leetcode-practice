# LeetCode 3600. Maximize Spanning Tree Stability with Upgrades — Hard
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
# Submission 2202866485 — Accepted, Python3
from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # My thinking: first the must-edges have to be acyclic, and
        # the graph as a whole has to be connected, or the answer is
        # -1. For a target stability X, a must-edge is usable only
        # at its own strength, an optional edge is free when its
        # strength already reaches X and costs one upgrade when
        # doubling it does. I take the free edges first, then the
        # cheapest upgraded ones, and X works when the tree closes
        # with at most k upgrades. That test is monotone in X, so I
        # binary search the largest working X.
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        must = [e for e in edges if e[3] == 1]
        opt = [e for e in edges if e[3] == 0]
        for u, v, s, _ in must:
            if not union(u, v):
                return -1
        parent2 = list(range(n))
        rank2 = [0] * n

        def find2(x):
            while parent2[x] != x:
                parent2[x] = parent2[parent2[x]]
                x = parent2[x]
            return x

        def union2(a, b):
            ra, rb = find2(a), find2(b)
            if ra == rb:
                return False
            if rank2[ra] < rank2[rb]:
                ra, rb = rb, ra
            parent2[rb] = ra
            if rank2[ra] == rank2[rb]:
                rank2[ra] += 1
            return True

        comps = n
        for u, v, s, _ in edges:
            if union2(u, v):
                comps -= 1
        if comps > 1:
            return -1

        def feasible(X):
            par = list(range(n))
            rk = [0] * n

            def f(x):
                while par[x] != x:
                    par[x] = par[par[x]]
                    x = par[x]
                return x

            def un(a, b):
                ra, rb = f(a), f(b)
                if ra == rb:
                    return False
                if rk[ra] < rk[rb]:
                    ra, rb = rb, ra
                par[rb] = ra
                if rk[ra] == rk[rb]:
                    rk[ra] += 1
                return True

            for u, v, s, _ in must:
                if s < X:
                    return False
                un(u, v)
            used = 0
            upgrades = 0
            for u, v, s, _ in opt:
                if s >= X and f(u) != f(v):
                    un(u, v)
                    used += 1
            for u, v, s, _ in opt:
                if s < X and 2 * s >= X and f(u) != f(v):
                    un(u, v)
                    upgrades += 1
                    used += 1
            need = (n - 1) - len(must)
            if used < need or upgrades > k:
                return False
            root = f(0)
            return all(f(i) == root for i in range(n))

        lo, hi = 1, 2 * 10 ** 5 + 1
        best = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best
