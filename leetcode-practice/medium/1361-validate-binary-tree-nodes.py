# LeetCode 1361. Validate Binary Tree Nodes — Medium
# https://leetcode.com/problems/validate-binary-tree-nodes/
# Submission 2199038642 — Accepted, Python3
#
# My thinking: a valid tree has exactly one
# root, every other node has exactly one
# parent, and a walk from the root reaches
# every node once. Any break in those rules
# means it is not a tree.

from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        for node in range(n):
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    if parent[child] != -1:
                        return False
                    parent[child] = node
        roots = [i for i in range(n) if parent[i] == -1]
        if len(roots) != 1:
            return False
        seen = set()
        stack = [roots[0]]
        while stack:
            node = stack.pop()
            if node in seen:
                return False
            seen.add(node)
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    stack.append(child)
        return len(seen) == n
