# LeetCode 513. Find Bottom Left Tree Value — Medium
# https://leetcode.com/problems/find-bottom-left-tree-value/
# Submission 2198835046 — Accepted, Python3
#
# My thinking: a level-by-level walk reaches the
# deepest row last, and the first node I see on
# each row is its leftmost one. The leftmost node
# of the final row is the answer.

from collections import deque


class Solution:
    def findBottomLeftValue(self, root) -> int:
        queue = deque([root])
        leftmost = root.val
        while queue:
            leftmost = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftmost
