# LeetCode 2192. All Ancestors of a Node in a Directed Acyclic Graph — Medium
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
# Submission 2204495298 — Accepted, Python3
#
# My thinking: a node's ancestors are its direct parents plus their
# ancestors, so I build the reverse graph and walk backwards from each
# node with a stack, collecting every reachable node once. Sorting the
# collected set gives the ancestors in increasing order.
class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        rev = [[] for _ in range(n)]
        for u, v in edges:
            rev[v].append(u)
        ans = []
        for i in range(n):
            seen = set()
            stack = list(rev[i])
            while stack:
                u = stack.pop()
                if u in seen:
                    continue
                seen.add(u)
                stack.extend(rev[u])
            ans.append(sorted(seen))
        return ans
