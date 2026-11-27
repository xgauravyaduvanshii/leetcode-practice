# LeetCode 3887. Incremental Even-Weighted Cycle Queries — Hard
# https://leetcode.com/problems/incremental-even-weighted-cycle-queries/
# Submission 2203349066 — Accepted, Python3
from typing import List


class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        # My thinking: adding an edge creates a new cycle only
        # when its ends are already connected, and every other
        # cycle keeps its weight, so only the new cycle can
        # break the all-even invariant. Its weight is the new
        # edge's weight plus the weight of any path between
        # its ends, so I need path parities in the graph so
        # far. A union-find with xor-to-root keeps exactly
        # that: two vertices are connected when they share a
        # root, and the parity between them is the xor of
        # their xors to the root. A disconnected edge is
        # always added and joins the two sets with the xor
        # that makes the edge's weight consistent; a
        # connected edge is added exactly when its weight
        # matches the existing parity, and then it changes
        # nothing, since it is consistent with every path
        # already there.
        parent = list(range(n))
        xr = [0] * n

        def find(x):
            if parent[x] == x:
                return x, 0
            path = []
            while parent[x] != x:
                path.append(x)
                x = parent[x]
            root = x
            suf = 0
            for node in reversed(path):
                suf ^= xr[node]
                xr[node] = suf
                parent[node] = root
            return root, xr[path[0]]

        ans = 0
        for u, v, w in edges:
            ru, xu = find(u)
            rv, xv = find(v)
            if ru != rv:
                parent[ru] = rv
                xr[ru] = xu ^ xv ^ w
                ans += 1
            elif xu ^ xv == w:
                ans += 1
        return ans
