# LeetCode 94. Binary Tree Inorder Traversal — Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Submission 2197385717 — Accepted, Python3
#
# My thinking: inorder means left, then the node itself,
# then right. I do it with a stack instead of recursion:
# push left children until there are none, then visit the
# top of the stack and move to its right child.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative inorder with an explicit stack: go left, visit, go right.
        result = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
