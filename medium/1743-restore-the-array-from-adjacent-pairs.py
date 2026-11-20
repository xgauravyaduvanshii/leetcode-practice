# LeetCode 1743. Restore the Array From Adjacent Pairs — Medium
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
# Submission 2199926383 — Accepted, Python3
#
# My thinking: the array is a path — its two
# ends are the only values with one neighbour.
# I start at an end and walk the path, never
# stepping back.

from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        start = next(node for node, neighbours in graph.items() if len(neighbours) == 1)
        result = [start]
        previous = None
        current = start
        while len(result) < len(adjacentPairs) + 1:
            for neighbour in graph[current]:
                if neighbour != previous:
                    result.append(neighbour)
                    previous, current = current, neighbour
                    break
        return result
