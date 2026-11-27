# LeetCode 2581. Count Number of Possible Root Nodes — Hard
# https://leetcode.com/problems/count-number-of-possible-root-nodes/
# Submission 2201831802 — Accepted, Python3
#
# My thinking: I root the tree once and
# count the guesses that already point
# the right way, then I walk the root
# across each edge — only the guesses on
# that edge can flip, so every other
# root's count follows for free.

import sys
from collections import Counter
sys.setrecursionlimit(300000)


class Solution:
    def rootCount(self, edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        # guesses may repeat: count each occurrence, it counts that many times
        guess_count = Counter(map(tuple, guesses))
        parent = [-1] * n
        order = [0]
        parent[0] = -2
        for u in order:
            for w in adj[u]:
                if parent[w] == -1:
                    parent[w] = u
                    order.append(w)
        # correct guesses when rooted at 0: (u, v) is right when u is v's parent
        cnt = [0] * n
        c0 = 0
        for u, v in guesses:
            if parent[v] == u:
                c0 += 1
        cnt[0] = c0
        for u in order:
            for w in adj[u]:
                if parent[w] == u:
                    # moving the root from u down to w flips only the guesses
                    # on the edge (u, w), each occurrence counting separately
                    c = cnt[u] - guess_count.get((u, w), 0) + guess_count.get((w, u), 0)
                    cnt[w] = c
        return sum(1 for c in cnt if c >= k)
