# LeetCode 1766. Tree of Coprimes — Hard
# https://leetcode.com/problems/tree-of-coprimes/
# Submission 2201152169 — Accepted, Python3
#
# My thinking: walking down from the root, I keep
# for every value the deepest node on the path that
# carries it — a node's answer is the deepest such
# node whose value is coprime with its own, and I
# restore the old entry when I walk back up.

from math import gcd

class Solution:
    def getCoprimes(self, nums: list[int], edges: list[list[int]]) -> list[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        coprime = [[] for _ in range(51)]
        for a in range(1, 51):
            for b in range(1, 51):
                if gcd(a, b) == 1:
                    coprime[a].append(b)
        ans = [-1] * n
        deepest = [(-1, -1)] * 51
        stack = [(0, -1, 0, True, None)]
        while stack:
            u, parent, depth, entering, prev = stack.pop()
            if entering:
                best_depth = -1
                best_node = -1
                for v in coprime[nums[u]]:
                    d, node = deepest[v]
                    if d > best_depth:
                        best_depth, best_node = d, node
                ans[u] = best_node
                prev = deepest[nums[u]]
                deepest[nums[u]] = (depth, u)
                stack.append((u, parent, depth, False, prev))
                for w in adj[u]:
                    if w != parent:
                        stack.append((w, u, depth + 1, True, None))
            else:
                deepest[nums[u]] = prev
        return ans
