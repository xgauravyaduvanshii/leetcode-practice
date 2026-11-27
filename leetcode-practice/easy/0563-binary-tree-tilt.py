# LeetCode 563. Binary Tree Tilt — Easy
# https://leetcode.com/problems/binary-tree-tilt/
# Submission 2197498288 — Accepted, Python3
#
# My thinking: the tilt of a node is how different
# its left and right subtree sums are. As I walk
# the tree adding up each subtree, I add each
# node's tilt to a running total — that total is
# the answer.

class Solution:
    def findTilt(self, root) -> int:
        self.tilt = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.tilt += abs(left - right)
            return node.val + left + right

        dfs(root)
        return self.tilt
