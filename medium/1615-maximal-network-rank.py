# LeetCode 1615. Maximal Network Rank — Medium
# https://leetcode.com/problems/maximal-network-rank/
# Submission 2199892748 — Accepted, Python3
#
# My thinking: a pair's rank is just the two
# cities' road counts, minus one when they
# share a road. I try every pair and keep the
# best.

from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    rank -= 1
                best = max(best, rank)
        return best
