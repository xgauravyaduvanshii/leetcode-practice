# LeetCode 590. N-ary Tree Postorder Traversal — Easy
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Submission 2197502245 — Accepted, Python3
#
# My thinking: postorder is the mirror of preorder —
# I visit all of a node's children first, and only
# write the node down after them.

class Solution:
    def postorder(self, root) -> list[int]:
        result = []

        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            result.append(node.val)

        dfs(root)
        return result
