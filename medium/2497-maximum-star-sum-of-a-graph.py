# LeetCode 2497. Maximum Star Sum of a Graph — Medium
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/
# Submission 2204973482 — Accepted, Python3
#
# My thinking: a star is a centre plus up to k of its neighbours.
# Only positive neighbours ever help, so for each node take its
# value plus its k largest positive neighbour values. The best
# centre wins — a single node alone is always a valid star, so the
# answer is at least the largest node value.
class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(vals[v])
            adj[v].append(vals[u])
        res = float("-inf")
        for u in range(n):
            neigh = [x for x in adj[u] if x > 0]
            neigh.sort(reverse=True)
            res = max(res, vals[u] + sum(neigh[:k]))
        return res
