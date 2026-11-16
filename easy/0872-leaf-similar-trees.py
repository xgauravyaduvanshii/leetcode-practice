# LeetCode 872. Leaf-Similar Trees — Easy
# https://leetcode.com/problems/leaf-similar-trees/
# Submission 2197537196 — Accepted, Python3
#
# My thinking: two trees are leaf-similar if their
# leaves read the same left to right. I collect
# the leaves of each tree in order — a node with
# no children is a leaf, otherwise I take the
# left leaves then the right leaves — and compare
# the two lists.

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return leaves(node.left) + leaves(node.right)
        return leaves(root1) == leaves(root2)
