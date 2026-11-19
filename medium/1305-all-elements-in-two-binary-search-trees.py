# LeetCode 1305. All Elements in Two Binary Search Trees — Medium
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Submission 2199027842 — Accepted, Python3
#
# My thinking: an in-order walk reads each
# search tree out in sorted order. I merge the
# two sorted lists the way you merge two
# sorted decks.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def collect(node, values):
            if node:
                collect(node.left, values)
                values.append(node.val)
                collect(node.right, values)

        first, second = [], []
        collect(root1, first)
        collect(root2, second)
        merged = []
        i = j = 0
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                merged.append(first[i])
                i += 1
            else:
                merged.append(second[j])
                j += 1
        return merged + first[i:] + second[j:]
