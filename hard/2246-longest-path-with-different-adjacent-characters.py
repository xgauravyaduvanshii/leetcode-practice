# LeetCode 2246. Longest Path With Different Adjacent Characters — Hard
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# Submission 2201636549 — Accepted, Python3
#
# My thinking: the best run through any
# node is its two longest downward runs
# from children wearing a different letter
# — I grow those bottom-up and keep the
# best join I ever see.

class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        ans = 1

        def dfs(u: int) -> int:
            nonlocal ans
            top1 = top2 = 0
            for v in children[u]:
                cur = dfs(v)
                if s[v] != s[u]:
                    if cur > top1:
                        top2 = top1
                        top1 = cur
                    elif cur > top2:
                        top2 = cur
            ans = max(ans, 1 + top1 + top2)
            return 1 + top1

        dfs(0)
        return ans
