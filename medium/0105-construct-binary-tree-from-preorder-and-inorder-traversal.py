# LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal — Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Submission 2203993309 — Accepted, Python3
#
# My thinking:
# Preorder always visits the root first, so the first preorder value is
# the root of the current subtree. Inorder lists that root somewhere in
# the middle: everything to its left belongs to the left subtree and
# everything to its right belongs to the right subtree.
# I keep a map from each value to its position in inorder, so I can find
# the root's split point in O(1) instead of scanning the list each time.
# I also keep a single index into preorder that walks forward as I build
# nodes: each recursive call takes the next preorder value as its root,
# then builds the left subtree from the inorder slice left of the root
# and the right subtree from the slice right of it. When a slice is
# empty, that child is None.
# Each node is created exactly once and each inorder lookup is O(1), so
# the whole build is O(n) time and O(n) space for the map plus the
# recursion stack.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {value: i for i, value in enumerate(inorder)}
        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            mid = inorder_index[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
