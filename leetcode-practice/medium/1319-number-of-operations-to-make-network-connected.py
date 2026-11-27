# LeetCode 1319. Number of Operations to Make Network Connected — Medium
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# Submission 2199031461 — Accepted, Python3
#
# My thinking: with fewer cables than computers
# minus one, connecting everything is hopeless.
# Otherwise I join the cables with a union-find
# and count the separate groups — one cable
# per group minus one links them all.

from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        return len({find(i) for i in range(n)}) - 1
