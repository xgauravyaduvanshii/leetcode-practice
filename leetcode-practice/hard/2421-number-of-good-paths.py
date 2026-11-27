# LeetCode 2421. Number of Good Paths — Hard
# https://leetcode.com/problems/number-of-good-paths/
# Submission 2201727758 — Accepted, Python3
#
# My thinking: a good path never climbs
# above its endpoints' value, so I wake
# the nodes up from the smallest value
# upward, joining each to its waking
# neighbours — when a value's nodes wake,
# the ones already joined in one piece
# make that many good pairs.

from collections import defaultdict


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        by_val = defaultdict(list)
        for i, v in enumerate(vals):
            by_val[v].append(i)
        active = [False] * n
        ans = n
        for v in sorted(by_val):
            for u in by_val[v]:
                active[u] = True
                for w in adj[u]:
                    if active[w]:
                        union(u, w)
            groups = defaultdict(int)
            for u in by_val[v]:
                groups[find(u)] += 1
            for cnt in groups.values():
                ans += cnt * (cnt - 1) // 2
        return ans
