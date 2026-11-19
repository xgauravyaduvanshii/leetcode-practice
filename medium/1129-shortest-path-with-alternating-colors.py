# LeetCode 1129. Shortest Path with Alternating Colors — Medium
# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Submission 2199003665 — Accepted, Python3
#
# My thinking: I search outward from node zero,
# remembering both the node and the colour of
# the edge I arrived on — each step must switch
# colour, and the first time I reach a node is
# the shortest way there.

from collections import deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]
        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)
        answer = [-1] * n
        answer[0] = 0
        queue = deque([(0, 0, 0), (0, 1, 0)])
        seen = {(0, 0), (0, 1)}
        while queue:
            node, color, steps = queue.popleft()
            for next_node in (blue[node] if color == 0 else red[node]):
                if (next_node, 1 - color) in seen:
                    continue
                seen.add((next_node, 1 - color))
                if answer[next_node] == -1:
                    answer[next_node] = steps + 1
                queue.append((next_node, 1 - color, steps + 1))
        return answer
