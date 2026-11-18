# LeetCode 947. Most Stones Removed with Same Row or Column — Medium
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# Submission 2198973724 — Accepted, Python3
#
# My thinking: stones linked by a shared row or
# column form one group, and each group can be
# thinned down to a single stone. So the answer
# is the number of stones minus the number of
# groups, which I find with union-find.

from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for x, y in stones:
            union(("row", x), ("col", y))
        groups = {find(("row", x)) for x, y in stones}
        return len(stones) - len(groups)
