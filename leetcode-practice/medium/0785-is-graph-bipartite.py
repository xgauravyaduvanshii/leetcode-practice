# LeetCode 785. Is Graph Bipartite? — Medium
# https://leetcode.com/problems/is-graph-bipartite/
# Submission 2198936848 — Accepted, Python3
#
# My thinking: two colours are enough when every
# edge joins opposite colours. I colour each
# connected part with a breadth-first search, and
# if I ever find two neighbours with the same
# colour, the graph cannot be split.

from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colour = {}
        for start in range(len(graph)):
            if start in colour:
                continue
            colour[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if neighbour not in colour:
                        colour[neighbour] = 1 - colour[node]
                        queue.append(neighbour)
                    elif colour[neighbour] == colour[node]:
                        return False
        return True
