# LeetCode 847. Shortest Path Visiting All Nodes — Hard
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# Submission 2198682890 — Accepted, Python3
#
# My thinking: the state is not just where I am but
# which nodes I have already visited, so I search
# over (node, visited-mask) pairs. Starting from
# every node at once, the first time any state has
# all bits set, its step count is the shortest path
# that visits everything.

from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full = (1 << n) - 1
        queue = deque()
        seen = set()
        for start in range(n):
            queue.append((start, 1 << start, 0))
            seen.add((start, 1 << start))
        while queue:
            node, mask, steps = queue.popleft()
            if mask == full:
                return steps
            for nxt in graph[node]:
                new_mask = mask | (1 << nxt)
                if (nxt, new_mask) not in seen:
                    seen.add((nxt, new_mask))
                    queue.append((nxt, new_mask, steps + 1))
        return -1
