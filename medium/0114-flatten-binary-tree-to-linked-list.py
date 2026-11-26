# LeetCode 114. Flatten Binary Tree to Linked List — Medium
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Submission 2204001554 — Accepted, Python3
#
# My thinking: the flattened tree must read like a preorder walk of
# the original tree, with every node keeping only a right child. So I
# walk the tree in preorder with an explicit stack: I pop a node, push
# its right child first and then its left child (so the left child is
# popped next), and then I rewire the popped node — its left child
# becomes None and its right child becomes whatever is on top of the
# stack, which is exactly the next node in preorder. Because each node
# is pushed and popped once, every node ends up linked right after the
# node before it in preorder, and the last node's right child is None.
# An empty tree needs nothing done, and a single node is already flat.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: "TreeNode") -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            # The next node in preorder is now on top of the stack
            # (or there is no next node).
            node.left = None
            node.right = stack[-1] if stack else None
