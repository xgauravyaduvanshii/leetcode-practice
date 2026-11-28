# LeetCode 2583. Kth Largest Sum in a Binary Tree — Medium
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
# Submission 2205086340 — Accepted, Python3
#
# My thinking: one BFS pass collects each level's sum; the
# k-th largest of those sums is the answer, or -1 when there
# are fewer than k levels.
from collections import deque


class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        level_sums = []
        q = deque([root])
        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sums.append(s)
        if len(level_sums) < k:
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k - 1]
