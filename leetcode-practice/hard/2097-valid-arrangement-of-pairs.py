# LeetCode 2097. Valid Arrangement of Pairs — Hard
# https://leetcode.com/problems/valid-arrangement-of-pairs/
# Submission 2201571218 — Accepted, Python3
#
# My thinking: the pairs are the edges of a
# directed graph and the arrangement is a walk
# that uses every edge once, so I follow
# Hierholzer — always take an unused edge
# forward, and backtrack into the answer when
# a stop runs out of edges.

from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        for u, v in pairs:
            graph[u].append(v)
            outdeg[u] += 1
            indeg[v] += 1
        start = pairs[0][0]
        for u in list(graph):
            if outdeg[u] - indeg[u] == 1:
                start = u
                break
        stack = [start]
        path = []
        while stack:
            u = stack[-1]
            if graph[u]:
                stack.append(graph[u].pop())
            else:
                path.append(stack.pop())
        path.reverse()
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]
