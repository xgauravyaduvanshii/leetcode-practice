# LeetCode 129. Sum Root to Leaf Numbers — Medium
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Submission 2204023442 — Accepted, Python3
#
# My thinking: Each root-to-leaf path spells out one number, digit
# by digit, so I walk the tree carrying the number built so far. At
# each node I extend it by one digit (multiply by 10 and add the
# node's value). When I reach a leaf, that completed number is one
# of the terms in the answer, so I add it to the total. Inner nodes
# contribute nothing themselves — they only pass their partial number
# down to their children. A depth-first walk visits each node once.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: 'TreeNode') -> int:
        total = 0

        def dfs(node, num):
            nonlocal total
            if node is None:
                return
            num = num * 10 + node.val
            if node.left is None and node.right is None:
                total += num
                return
            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)
        return total
