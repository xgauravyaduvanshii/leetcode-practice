# LeetCode 98. Validate Binary Search Tree — Medium
# https://leetcode.com/problems/validate-binary-search-tree/
# Submission 2203975221 — Accepted, Python3
#
# My thinking: a tree is a valid binary search tree only when every
# node sits strictly between the limits handed down from its
# ancestors, not just next to its own parent. So I walk the tree
# carrying a low and a high bound: a node must be greater than low
# and less than high, then its left child inherits the same low with
# the node's value as its new high, and its right child inherits the
# node's value as its new low with the same high. An empty subtree is
# always valid, and if any node breaks its bounds the whole tree is
# invalid.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: "TreeNode") -> bool:
        def check(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return check(node.left, low, node.val) and check(
                node.right, node.val, high
            )

        return check(root, float("-inf"), float("inf"))
