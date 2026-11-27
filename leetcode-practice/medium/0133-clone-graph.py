# LeetCode 133. Clone Graph — Medium
# https://leetcode.com/problems/clone-graph/
# Submission 2204033756 — Accepted, Python3
#
# My thinking: I walk the graph once with a depth-first search,
# remembering each original node and its clone in a map. When I
# first meet a node I make its clone, then I clone each neighbour
# the same way and link the clones together. The map stops me
# from cloning the same node twice, which is what breaks the
# cycles — a node I have already seen just returns its clone.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:
            return None
        old_to_new = {}

        def dfs(current):
            if current in old_to_new:
                return old_to_new[current]
            copy = Node(current.val)
            old_to_new[current] = copy
            for neighbour in current.neighbors:
                copy.neighbors.append(dfs(neighbour))
            return copy

        return dfs(node)
