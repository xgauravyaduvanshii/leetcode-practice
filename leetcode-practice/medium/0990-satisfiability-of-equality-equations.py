# LeetCode 990. Satisfiability of Equality Equations — Medium
# https://leetcode.com/problems/satisfiability-of-equality-equations/
# Submission 2198982711 — Accepted, Python3
#
# My thinking: I first merge every pair of
# letters that must be equal, then check that no
# pair that must differ ended up in the same
# group.

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        for eq in equations:
            if eq[1] == "=":
                union(ord(eq[0]) - 97, ord(eq[3]) - 97)
        for eq in equations:
            if eq[1] == "!":
                if find(ord(eq[0]) - 97) == find(ord(eq[3]) - 97):
                    return False
        return True
