# LeetCode 310. Minimum Height Trees — Medium
# https://leetcode.com/problems/minimum-height-trees/
# Submission 2198739121 — Accepted, Python3
#
# My thinking: the best roots sit in the middle of
# the tree, so I peel off the leaves layer by layer
# — like trimming a tree from the outside in — until
# one or two nodes are left. Those are the roots
# with the smallest height.

from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        neighbors = [set() for _ in range(n)]
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
        leaves = deque(i for i in range(n) if len(neighbors[i]) == 1)
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    leaves.append(neighbor)
        return list(leaves)
