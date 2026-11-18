# LeetCode 199. Binary Tree Right Side View — Medium
# https://leetcode.com/problems/binary-tree-right-side-view/
# Submission 2198444314 — Accepted, Python3
#
# My thinking: I walk the tree level by level. At
# each level the rightmost node is the one seen
# from the right side, so I note the last node of
# every level before moving on to its children.

from collections import deque
from typing import List


class Solution:
    def rightSideView(self, root) -> List[int]:
        if not root:
            return []
        view = []
        queue = deque([root])
        while queue:
            view.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return view
