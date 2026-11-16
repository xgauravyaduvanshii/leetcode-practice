# LeetCode 1022. Sum of Root To Leaf Binary Numbers — Easy
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Submission 2197551954 — Accepted, Python3
#
# My thinking: I walk down from the root carrying the
# binary number built so far — each step doubles
# it and adds the current node's bit. When I
# reach a leaf, that number is one root-to-leaf
# value, so I add it to the total.

class Solution:
    def sumRootToLeaf(self, root) -> int:
        total = 0

        def dfs(node, value):
            nonlocal total
            if not node:
                return
            value = value * 2 + node.val
            if not node.left and not node.right:
                total += value
                return
            dfs(node.left, value)
            dfs(node.right, value)

        dfs(root, 0)
        return total
