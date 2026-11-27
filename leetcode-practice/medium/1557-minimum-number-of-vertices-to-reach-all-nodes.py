# LeetCode 1557. Minimum Number of Vertices to Reach All Nodes — Medium
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# Submission 2199875760 — Accepted, Python3
#
# My thinking: a node with no incoming edge
# can only be reached by starting there. Every
# other node is reachable from one of those
# starts, so the answer is exactly the nodes
# with in-degree zero.

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_incoming = set()
        for _, b in edges:
            has_incoming.add(b)
        return [node for node in range(n) if node not in has_incoming]
