# LeetCode 3873. Maximum Points Activated with One Addition — Hard
# https://leetcode.com/problems/maximum-points-activated-with-one-addition/
# Submission 2203331033 — Accepted, Python3
from typing import List


class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        # My thinking: activation spreads along shared x or y
        # coordinates, so the points split into connected
        # components where two points are linked when they
        # share an x or a y — a union-find over the points,
        # joining each point to the first point seen with its
        # x and with its y, finds them. Adding one point at
        # (X, Y) activates every point with x = X and every
        # point with y = Y, and then the whole components
        # those points belong to. All points sharing an x
        # (or a y) already sit in one component, so the new
        # point touches at most two components, and any two
        # components can be bridged this way: pick X from
        # one component's x-coordinates and Y from the
        # other's y-coordinates, and (X, Y) cannot already
        # be a point or the two components would be one.
        # The best play is therefore 1 (the new point) plus
        # the sizes of the two largest components.
        n = len(points)
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        by_x = {}
        by_y = {}
        for i, (x, y) in enumerate(points):
            if x in by_x:
                union(i, by_x[x])
            else:
                by_x[x] = i
            if y in by_y:
                union(i, by_y[y])
            else:
                by_y[y] = i

        comp = {}
        for i in range(n):
            root = find(i)
            comp[root] = comp.get(root, 0) + 1
        sizes = sorted(comp.values(), reverse=True)
        best1 = sizes[0] if sizes else 0
        best2 = sizes[1] if len(sizes) > 1 else 0
        return 1 + best1 + best2
