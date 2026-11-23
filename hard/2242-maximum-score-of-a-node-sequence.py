# LeetCode 2242. Maximum Score of a Node Sequence — Hard
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/
# Submission 2201631372 — Accepted, Python3
#
# My thinking: a four-node run is really a
# middle edge with its best neighbours on
# each side — I keep each node's three
# highest-scoring neighbours and try every
# pairing across every middle edge.

class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        n = len(scores)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        top = []
        for u in range(n):
            neigh = sorted(adj[u], key=lambda v: scores[v], reverse=True)[:3]
            top.append(neigh)
        ans = -1
        for a, b in edges:
            for x in top[a]:
                if x == b:
                    continue
                for y in top[b]:
                    if y == a or y == x:
                        continue
                    ans = max(ans, scores[x] + scores[a] + scores[b] + scores[y])
        return ans
