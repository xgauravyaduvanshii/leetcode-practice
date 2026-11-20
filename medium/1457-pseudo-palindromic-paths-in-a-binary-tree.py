# LeetCode 1457. Pseudo-Palindromic Paths in a Binary Tree — Medium
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# Submission 2199854312 — Accepted, Python3
#
# My thinking: a path can shuffle into a
# palindrome when at most one digit appears an
# odd number of times. I track the odd digits
# as bits in a mask — a leaf counts when the
# mask has at most one bit set.

from __future__ import annotations


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node, mask):
            if not node:
                return 0
            mask ^= 1 << node.val
            if not node.left and not node.right:
                return 1 if mask & (mask - 1) == 0 else 0
            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)
