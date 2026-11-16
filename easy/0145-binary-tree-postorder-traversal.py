# LeetCode 145. Binary Tree Postorder Traversal — Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Submission 2197445474 — Accepted, Python3
#
# My thinking: postorder is left, right, then root.
# I do a root-right-left walk with a stack (the
# mirror image of preorder) and reverse the result
# at the end — that gives me left-right-root.

class Solution:
    def postorderTraversal(self, root) -> list[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
