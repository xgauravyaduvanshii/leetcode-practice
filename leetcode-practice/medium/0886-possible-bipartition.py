# LeetCode 886. Possible Bipartition — Medium
# https://leetcode.com/problems/possible-bipartition/
# Submission 2198962527 — Accepted, Python3
#
# My thinking: two people who dislike each other
# must sit in different groups, so I colour the
# dislike graph with two colours. If two
# neighbours ever share a colour, no split works.

from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colour = {}
        for start in range(1, n + 1):
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
