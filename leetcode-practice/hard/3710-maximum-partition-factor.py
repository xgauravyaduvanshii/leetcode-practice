# LeetCode 3710. Maximum Partition Factor — Hard
# https://leetcode.com/problems/maximum-partition-factor/
# Submission 2203057391 — Accepted, Python3
from typing import List


class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        # My thinking: binary-search-free. A split has factor at
        # least D exactly when every pair closer than D lands in
        # different groups, i.e. when the graph joining pairs
        # with distance < D is bipartite. As D grows, edges join
        # in order of distance, so the best D is the distance of
        # the first edge that closes an odd cycle. I add the
        # edges shortest first with a parity union-find (each
        # component remembers which side each point is on); the
        # first edge whose ends are already forced onto the same
        # side is the answer. With two points the factor is 0
        # by definition.
        n = len(points)
        if n == 2:
            return 0
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                edges.append((abs(xi - xj) + abs(yi - yj), i, j))
        edges.sort()
        parent = list(range(n))
        parity = [0] * n

        def find(x):
            if parent[x] != x:
                root, p = find(parent[x])
                parity[x] ^= p
                parent[x] = root
            return parent[x], parity[x]

        for d, u, v in edges:
            ru, pu = find(u)
            rv, pv = find(v)
            if ru == rv:
                if pu == pv:
                    return d
            else:
                # Join the components so that u and v end up on
                # opposite sides: parity(ru -> rv) = pu ^ pv ^ 1.
                parent[ru] = rv
                parity[ru] = pu ^ pv ^ 1
        return edges[-1][0]
