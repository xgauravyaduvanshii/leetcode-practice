# LeetCode 559. Maximum Depth of N-ary Tree — Easy
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Submission 2197497157 — Accepted, Python3
#
# My thinking: same as a binary tree, but a node can
# have many children. The depth is 1 plus the
# biggest depth among all of its children — and a
# node with no children is depth 1.

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)
