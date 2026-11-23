# LeetCode 2322. Minimum Score After Removals on a Tree — Hard
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
# Submission 2201677325 — Accepted, Python3
#
# My thinking: cutting two edges leaves
# three pieces, and each piece is either a
# whole subtree or what is left of one — so
# I root the tree, take every subtree's
# xor, and try every pair of cuts.

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        sub = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = [0]

        def dfs(u, p):
            tin[u] = timer[0]
            timer[0] += 1
            x = nums[u]
            for v in adj[u]:
                if v != p:
                    x ^= dfs(v, u)
            sub[u] = x
            tout[u] = timer[0]
            timer[0] += 1
            return x

        total = dfs(0, -1)

        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        ans = float('inf')
        for u in range(1, n):
            for v in range(u + 1, n):
                if is_ancestor(u, v):
                    a, b, c = sub[v], sub[u] ^ sub[v], total ^ sub[u]
                elif is_ancestor(v, u):
                    a, b, c = sub[u], sub[v] ^ sub[u], total ^ sub[v]
                else:
                    a, b, c = sub[u], sub[v], total ^ sub[u] ^ sub[v]
                score = max(a, b, c) - min(a, b, c)
                if score < ans:
                    ans = score
        return ans
