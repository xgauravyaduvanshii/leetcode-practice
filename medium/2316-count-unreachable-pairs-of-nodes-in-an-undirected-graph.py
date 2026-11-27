# LeetCode 2316. Count Unreachable Pairs of Nodes in an Undirected Graph — Medium
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
# Submission 2204678085 — Accepted, Python3
#
# My thinking: union-find groups the nodes into connected components.
# Two nodes are unreachable from each other exactly when they sit in
# different components, so I count pairs across components: walk the
# component sizes in any order, and for each component multiply its size
# by the number of nodes still unseen — every cross-component pair is
# counted exactly once.
class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        from collections import Counter
        sizes = Counter(find(i) for i in range(n))
        ans = 0
        remaining = n
        for sz in sizes.values():
            remaining -= sz
            ans += sz * remaining
        return ans
