# LeetCode 2440. Create Components With Same Value — Hard
# https://leetcode.com/problems/create-components-with-same-value/
# Submission 2201741745 — Accepted, Python3
#
# My thinking: every piece must add up to
# the same total, so that total has to
# divide the whole sum — I try the
# smallest divisors first, and for each
# one I cut off every subtree that already
# adds up to it, keeping the cut that
# makes the most pieces.

import sys
sys.setrecursionlimit(30000)


class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        total = sum(nums)

        def can(target):
            count = [0]

            def dfs(u, parent):
                s = nums[u]
                for w in adj[u]:
                    if w == parent:
                        continue
                    sub = dfs(w, u)
                    if sub == -1:
                        return -1
                    s += sub
                if s == target:
                    count[0] += 1
                    return 0
                if s > target:
                    return -1
                return s

            if dfs(0, -1) != 0:
                return -1
            return count[0] - 1

        divisors = [d for d in range(1, total + 1) if total % d == 0]
        for target in divisors:
            res = can(target)
            if res != -1:
                return res
        return 0
