# LeetCode 2392. Build a Matrix With Conditions — Hard
# https://leetcode.com/problems/build-a-matrix-with-conditions/
# Submission 2201714849 — Accepted, Python3
#
# My thinking: rows and columns are two
# separate orderings — I sort each one on
# its own, and if either one ties itself
# in a knot there is no matrix at all.

from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def topo(conds):
            adj = [[] for _ in range(k + 1)]
            indeg = [0] * (k + 1)
            for a, b in conds:
                adj[a].append(b)
                indeg[b] += 1
            q = deque([v for v in range(1, k + 1) if indeg[v] == 0])
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            return order if len(order) == k else None

        rows = topo(rowConditions)
        cols = topo(colConditions)
        if rows is None or cols is None:
            return []
        rpos = {v: i for i, v in enumerate(rows)}
        cpos = {v: i for i, v in enumerate(cols)}
        mat = [[0] * k for _ in range(k)]
        for v in range(1, k + 1):
            mat[rpos[v]][cpos[v]] = v
        return mat
