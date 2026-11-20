# LeetCode 1514. Path with Maximum Probability — Medium
# https://leetcode.com/problems/path-with-maximum-probability/
# Submission 2199867086 — Accepted, Python3
#
# My thinking: this is Dijkstra with
# multiplication instead of addition — the most
# likely path to each node wins, and a max-heap
# always expands the best unfinished path.

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))
        best = [0.0] * n
        best[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob
            if node == end_node:
                return prob
            if prob < best[node]:
                continue
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > best[neighbor]:
                    best[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))
        return 0.0
