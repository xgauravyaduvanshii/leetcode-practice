# LeetCode 1339. Maximum Product of Splitted Binary Tree — Medium
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# Submission 2199035890 — Accepted, Python3
#
# My thinking: every subtree sum is a candidate
# for one side of the split. I collect the
# sums bottom-up with an explicit stack, then
# try each subtree against the rest of the tree.

from __future__ import annotations

from typing import Optional


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        sums = {}
        for node in reversed(order):
            sums[node] = node.val + sums.get(node.left, 0) + sums.get(node.right, 0)
        total = sums[root]
        best = 0
        for node in order:
            if node is not root:
                best = max(best, sums[node] * (total - sums[node]))
        return best % 1_000_000_007
