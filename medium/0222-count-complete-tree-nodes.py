# LeetCode 222. Count Complete Tree Nodes — Medium
# https://leetcode.com/problems/count-complete-tree-nodes/
# Submission 2198459169 — Accepted, Python3
#
# My thinking: a complete tree is only incomplete
# on its last level, so I compare the height down
# the left edge with the height down the right edge.
# When they match, the tree is perfect and its size
# is a power of two minus one. When they differ,
# the answer is one for the root plus the counts of
# the two sides, worked out the same way.

class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0

        def height(node, go_left: bool) -> int:
            h = 0
            while node:
                h += 1
                node = node.left if go_left else node.right
            return h

        left_h = height(root, True)
        right_h = height(root, False)
        if left_h == right_h:
            return (1 << left_h) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
