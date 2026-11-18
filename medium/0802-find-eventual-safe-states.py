# LeetCode 802. Find Eventual Safe States — Medium
# https://leetcode.com/problems/find-eventual-safe-states/
# Submission 2198942845 — Accepted, Python3
#
# My thinking: a node is safe when every road out
# of it leads to safe nodes. I walk the graph
# depth-first, marking nodes as I visit them — a
# node that leads back to a visiting node is in a
# cycle and never safe.

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = [0] * len(graph)  # 0 unvisited, 1 visiting, 2 safe

        def is_safe(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1
            for nxt in graph[node]:
                if not is_safe(nxt):
                    return False
            state[node] = 2
            return True

        return [node for node in range(len(graph)) if is_safe(node)]
