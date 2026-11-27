# LeetCode 589. N-ary Tree Preorder Traversal — Easy
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Submission 2197501777 — Accepted, Python3
#
# My thinking: preorder means I write the node down
# first, then visit each of its children in order,
# doing the same thing for each of them.

class Solution:
    def preorder(self, root) -> list[int]:
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return result
