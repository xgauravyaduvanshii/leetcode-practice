# LeetCode 399. Evaluate Division — Medium
# https://leetcode.com/problems/evaluate-division/
# Submission 2198776903 — Accepted, Python3
#
# My thinking: the equations are edges in a graph,
# weighted by their ratio and its inverse. A query
# is a path between the two variables, and the
# answer is the product of the edge weights along
# it — or -1 when no path exists.

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def answer(a, b, seen):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            seen.add(a)
            for neighbor, weight in graph[a].items():
                if neighbor not in seen:
                    result = answer(neighbor, b, seen)
                    if result != -1.0:
                        return weight * result
            return -1.0

        return [answer(a, b, set()) for a, b in queries]
