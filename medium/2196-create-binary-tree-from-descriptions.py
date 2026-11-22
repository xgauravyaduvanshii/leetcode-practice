# LeetCode 2196. Create Binary Tree From Descriptions — Medium
# https://leetcode.com/problems/create-binary-tree-from-descriptions/
# Submission 2200921972 — Accepted, Python3
#
# My thinking: every description names a parent, a child
# and a side, so I build all the nodes first, link each
# child to its parent, and return the one node that is
# never anyone's child.

from __future__ import annotations

from typing import Optional


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            if is_left:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
            children.add(child_val)
        for val, node in nodes.items():
            if val not in children:
                return node
        return None
