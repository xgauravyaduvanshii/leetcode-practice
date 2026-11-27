# LeetCode 3373. Maximize the Number of Target Nodes After Connecting Trees II — Hard
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
# Submission 2202430043 — Accepted, Python3
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # My thinking: in a tree, two nodes are at even distance exactly
        # when they share a side of the bipartition, so I 2-colour both
        # trees. Connecting i to any node j of tree 2 adds the tree-2 nodes
        # of the opposite colour to j, which is most when j has the minority
        # colour — so tree 2 always contributes max(cnt2[0], cnt2[1]).
        # Tree 1 contributes the nodes sharing i's colour.
        def colour_counts(n, edges):
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            colour = [-1] * n
            colour[0] = 0
            stack = [0]
            cnt = [0, 0]
            while stack:
                u = stack.pop()
                cnt[colour[u]] += 1
                for v in adj[u]:
                    if colour[v] == -1:
                        colour[v] = colour[u] ^ 1
                        stack.append(v)
            return colour, cnt

        n = len(edges1) + 1
        m = len(edges2) + 1
        colour1, cnt1 = colour_counts(n, edges1)
        _, cnt2 = colour_counts(m, edges2)
        best2 = max(cnt2)
        return [cnt1[colour1[i]] + best2 for i in range(n)]
