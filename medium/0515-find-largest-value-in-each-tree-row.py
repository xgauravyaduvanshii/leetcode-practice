# LeetCode 515. Find Largest Value in Each Tree Row — Medium
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Submission 2198835952 — Accepted, Python3
#
# My thinking: I walk the tree one level at a time
# and keep the biggest value I see on each level.

from collections import deque
from typing import List


class Solution:
    def largestValues(self, root) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            largest = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                largest = max(largest, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(largest)
        return result
