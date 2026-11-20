# LeetCode 1443. Minimum Time to Collect All Apples in a Tree — Medium
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
# Submission 2199852840 — Accepted, Python3
#
# My thinking: I walk the tree from the root.
# A branch costs its children's time plus two
# for the trip there and back — but only when
# an apple hides somewhere below it.

from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            time = 0
            for child in graph[node]:
                if child == parent:
                    continue
                child_time = dfs(child, node)
                if child_time > 0 or hasApple[child]:
                    time += child_time + 2
            return time

        return dfs(0, -1)
