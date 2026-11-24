# LeetCode 3615. Longest Palindromic Path in Graph — Hard
# https://leetcode.com/problems/longest-palindromic-path-in-graph/
# Submission 2202874940 — Accepted, Python3
from typing import List
from collections import defaultdict


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        # My thinking: with at most 14 nodes I keep, for every set
        # of visited nodes, the pairs of endpoints of palindromic
        # paths using exactly that set. A single node is a
        # palindrome of length 1, and an edge whose ends share a
        # label is one of length 2. From any such path I grow it by
        # one node at each end, but only when the two new labels
        # match. I process the sets in increasing size so every
        # extension is itself extended later; the answer is the
        # largest set that holds a palindrome.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = defaultdict(set)
        for u in range(n):
            dp[1 << u].add((u, u))
        for u, v in edges:
            if label[u] == label[v]:
                dp[(1 << u) | (1 << v)].add((u, v))
                dp[(1 << u) | (1 << v)].add((v, u))
        best = 1 if n >= 1 else 0
        for pc in range(1, n + 1):
            for mask in range(1 << n):
                if bin(mask).count("1") != pc:
                    continue
                if mask not in dp:
                    continue
                if pc > best:
                    best = pc
                for (u, v) in list(dp[mask]):
                    for a in adj[u]:
                        if mask & (1 << a):
                            continue
                        for b in adj[v]:
                            if mask & (1 << b) or a == b:
                                continue
                            if label[a] == label[b]:
                                dp[mask | (1 << a) | (1 << b)].add((a, b))
        for mask in dp:
            pc = bin(mask).count("1")
            if pc > best:
                best = pc
        return best
