# LeetCode 3244. Shortest Distance After Road Addition Queries II — Hard
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
# Submission 2202127125 — Accepted, Python3
#
# My thinking: the chain edges alone give a
# distance of n - 1. Each query (u, v) can
# only help by skipping the chain nodes strictly
# between u and v. I keep a DSU "next alive"
# pointer, so each skipped node is removed once
# and the distance drops by 1 per removal.

from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        dist = n - 1
        ans = []
        for u, v in queries:
            x = find(u + 1)
            while x < v:
                dist -= 1
                parent[x] = find(x + 1)
                x = parent[x]
            ans.append(dist)
        return ans
