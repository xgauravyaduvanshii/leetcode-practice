# LeetCode 684. Redundant Connection — Medium
# https://leetcode.com/problems/redundant-connection/
# Submission 2198909756 — Accepted, Python3
#
# My thinking: a tree has no cycles, so the first
# edge that joins two nodes already connected is
# the extra one. I track the connections with a
# union-find structure.

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                return [u, v]
            parent[ru] = rv
        return []
