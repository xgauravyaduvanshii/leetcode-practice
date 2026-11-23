# LeetCode 2603. Collect Coins in a Tree — Hard
# https://leetcode.com/problems/collect-coins-in-a-tree/
# Submission 2201847314 — Accepted, Python3
#
# My thinking: a branch with no coin
# is never worth entering, and a coin
# two steps away can be picked up from
# where I stand, so I trim the empty
# branches, then peel two layers off the
# edge — what is left is the road I must
# walk, there and back.

from collections import deque


class Solution:
    def collectTheCoins(self, coins: list[int], edges: list[list[int]]) -> int:
        n = len(coins)
        adj = [[] for _ in range(n)]
        deg = [0] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            deg[a] += 1
            deg[b] += 1
        removed = [False] * n
        # step 1: trim branches that hold no coin
        q = deque(i for i in range(n) if deg[i] == 1 and coins[i] == 0)
        while q:
            u = q.popleft()
            removed[u] = True
            for w in adj[u]:
                if not removed[w]:
                    deg[w] -= 1
                    if deg[w] == 1 and coins[w] == 0:
                        q.append(w)
        # step 2: peel two layers — coins within distance 2 are collected
        # from the core, so the outer layers need no visit
        for _ in range(2):
            leaves = [i for i in range(n) if not removed[i] and deg[i] <= 1]
            if not leaves:
                break
            for u in leaves:
                removed[u] = True
            for u in leaves:
                for w in adj[u]:
                    if not removed[w]:
                        deg[w] -= 1
        remaining = sum(1 for i in range(n) if not removed[i])
        if remaining <= 1:
            return 0
        return 2 * (remaining - 1)
