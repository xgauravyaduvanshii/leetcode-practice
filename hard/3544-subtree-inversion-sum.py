# LeetCode 3544. Subtree Inversion Sum — Hard
# https://leetcode.com/problems/subtree-inversion-sum/
# Submission 2202821653 — Accepted, Python3
from typing import List


class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        # My thinking: inverting a node flips the sign of its whole
        # subtree, so a node's final sign is the parity of the
        # inverted nodes on the path from the root to it. Two inverted
        # nodes on one root-to-leaf path must be at least k apart, so
        # for each node I keep the distance to the nearest inverted
        # ancestor (capped at k, where k means far enough or none)
        # and the parity of inverted ancestors. Not inverting passes
        # the distance down plus one; inverting is only allowed when
        # the distance is already k, resets it to 1 below, and flips
        # the parity. The children are independent once those two
        # numbers are fixed, so a bottom-up pass over the tree fills
        # the table.
        n = len(nums)
        children = [[] for _ in range(n)]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = -2
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    children[u].append(v)
                    stack.append(v)
        NEG = float("-inf")
        f = [None] * n
        for u in reversed(order):
            S = [[0] * (k + 1) for _ in range(2)]
            for c in children[u]:
                fc = f[c]
                for d in range(1, k + 1):
                    fcd = fc[d]
                    S[0][d] += fcd[0]
                    S[1][d] += fcd[1]
            fu = [[NEG] * 2 for _ in range(k + 1)]
            for d in range(1, k + 1):
                for p in (0, 1):
                    sign = 1 if p == 0 else -1
                    best = nums[u] * sign + S[p][min(d + 1, k)]
                    if d == k:
                        best = max(best, nums[u] * (-sign) + S[1 - p][1])
                    fu[d][p] = best
            f[u] = fu
        return f[0][k][0]
