# LeetCode 124. Binary Tree Maximum Path Sum — Hard
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Submission 2198386033 — Accepted, Python3
#
# My thinking: for every node I ask each child for
# the best path going down from it, ignoring a child
# that would only drag the sum down. A path through
# this node can use both children plus the node
# itself, and that is a candidate for the overall
# best. What I pass back up is only the better of
# the two children plus the node, because a path
# going up can only take one side.

class Solution:
    def maxPathSum(self, root) -> int:
        best = float("-inf")

        def gain(node):
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return best
