# LeetCode 685. Redundant Connection II — Hard
# https://leetcode.com/problems/redundant-connection-ii/
# Submission 2198667752 — Accepted, Python3
#
# My thinking: a valid rooted tree has one parent per
# node and no cycle, so the extra edge is one of two
# things. If some node has two parents, I try dropping
# the second one — if what is left has no cycle, that
# is the answer, otherwise the first one is. If no
# node has two parents, the answer is the edge that
# closes the cycle.

from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find_cycle(skip):
            parent = {}

            def find(x):
                parent.setdefault(x, x)
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            for i, (u, v) in enumerate(edges):
                if i == skip:
                    continue
                if find(u) == find(v):
                    return [u, v]
                parent[find(u)] = find(v)
            return None

        seen = {}
        first = second = None
        for i, (u, v) in enumerate(edges):
            if v in seen:
                first = seen[v]
                second = i
                break
            seen[v] = i

        if second is None:
            return find_cycle(-1)
        if find_cycle(second) is None:
            return edges[second]
        return edges[first]
