# LeetCode 797. All Paths From Source to Target — Medium
# https://leetcode.com/problems/all-paths-from-source-to-target/
# Submission 2198942201 — Accepted, Python3
#
# My thinking: the graph has no cycles, so I can
# simply walk every road from node 0 to the last
# node, keeping the path I took and saving it
# whenever I arrive.

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []

        def walk(node, path):
            if node == target:
                result.append(path[:])
                return
            for nxt in graph[node]:
                path.append(nxt)
                walk(nxt, path)
                path.pop()

        walk(0, [0])
        return result
