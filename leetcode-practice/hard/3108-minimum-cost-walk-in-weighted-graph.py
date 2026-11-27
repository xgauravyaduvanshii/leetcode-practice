# LeetCode 3108. Minimum Cost Walk in Weighted Graph — Hard
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
# Submission 2201996464 — Accepted, Python3
#
# My thinking: I union the edges with a
# disjoint set, keeping the bitwise AND
# of all edge weights in each component.
# Two vertices can walk together exactly
# when they share a component, and then
# the cheapest walk costs the
# component's AND; otherwise the answer
# is -1.

from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))
        comp_and = [-1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v, w in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                comp_and[ru] &= w
            else:
                parent[rv] = ru
                comp_and[ru] = comp_and[ru] & comp_and[rv] & w
        ans = []
        for s, t in query:
            rs, rt = find(s), find(t)
            if rs != rt:
                ans.append(-1)
            else:
                ans.append(comp_and[rs])
        return ans
