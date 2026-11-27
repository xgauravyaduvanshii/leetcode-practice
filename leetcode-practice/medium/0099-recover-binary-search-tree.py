# LeetCode 99. Recover Binary Search Tree — Medium
# https://leetcode.com/problems/recover-binary-search-tree/
# Submission 2203984804 — Accepted, Python3
#
# My thinking:
# An inorder walk of a correct binary search tree visits the values in
# increasing order. Exactly two nodes have been swapped, so the inorder
# sequence has one or two places where a value is bigger than the next
# one (a violation). The first node of the first violation and the
# second node of the last violation are the two swapped nodes.
# If there is only one violation, the two nodes next to it are the pair.
# I do a plain recursive inorder walk, remember the previous node, and
# record the first and second misplaced nodes as I go. At the end I
# swap their values back, which fixes the tree without changing its
# shape. The walk visits each node once.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                    self.second = node
                else:
                    self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
