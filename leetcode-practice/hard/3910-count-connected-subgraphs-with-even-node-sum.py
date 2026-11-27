# LeetCode 3910. Count Connected Subgraphs with Even Node Sum — Hard
# https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/
# Submission 2203377522 — Accepted, Python3
from typing import List


class Solution:
    def evenSumSubgraphs(self, nums: List[int], edges: List[List[int]]) -> int:
        # My thinking: n is at most 13, so there are only
        # 8191 non-empty subsets — enumerate them all. A
        # subset has an even sum exactly when it holds an
        # even number of 1-valued nodes, which is a single
        # parity check on the subset masked with the
        # 1-valued nodes. A subset is connected when a
        # flood fill from its lowest set bit, walking only
        # to neighbours inside the subset, reaches every
        # node of the subset. Count the subsets that pass
        # both tests.
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ones = 0
        for i, v in enumerate(nums):
            if v:
                ones |= 1 << i
        ans = 0
        for mask in range(1, 1 << n):
            if (mask & ones).bit_count() % 2:
                continue
            start = (mask & -mask).bit_length() - 1
            seen = 1 << start
            stack = [start]
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if (mask >> w) & 1 and not (seen >> w) & 1:
                        seen |= 1 << w
                        stack.append(w)
            if seen == mask:
                ans += 1
        return ans
