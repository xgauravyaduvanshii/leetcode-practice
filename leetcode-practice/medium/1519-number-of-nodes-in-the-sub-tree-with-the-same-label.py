# LeetCode 1519. Number of Nodes in the Sub-Tree With the Same Label — Medium
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
# Submission 2199868432 — Accepted, Python3
#
# My thinking: one depth-first walk returns the
# letter counts of each subtree. A node's answer
# is just the count of its own letter in the
# counts its children handed up.

from collections import defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        answer = [0] * n

        def dfs(node, parent):
            counts = [0] * 26
            counts[ord(labels[node]) - ord("a")] = 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_counts = dfs(neighbor, node)
                for i in range(26):
                    counts[i] += child_counts[i]
            answer[node] = counts[ord(labels[node]) - ord("a")]
            return counts

        dfs(0, -1)
        return answer
