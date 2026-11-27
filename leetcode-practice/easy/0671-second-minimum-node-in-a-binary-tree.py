# LeetCode 671. Second Minimum Node In a Binary Tree — Easy
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Submission 2197512309 — Accepted, Python3
#
# My thinking: the root holds the smallest value in
# the whole tree. So I walk the tree looking for
# the smallest value that is bigger than the root's
# value. If I never find one, the answer is -1.

class Solution:
    def findSecondMinimumValue(self, root) -> int:
        smallest = root.val
        second = float('inf')

        def dfs(node):
            nonlocal second
            if not node:
                return
            if smallest < node.val < second:
                second = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return -1 if second == float('inf') else second
