# LeetCode 144. Binary Tree Preorder Traversal — Easy
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Submission 2197444957 — Accepted, Python3
#
# My thinking: preorder is root, then left, then right.
# With a stack I pop a node, write it down, then push
# its right child first and its left child second —
# that way the left one comes out first.

class Solution:
    def preorderTraversal(self, root) -> list[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
