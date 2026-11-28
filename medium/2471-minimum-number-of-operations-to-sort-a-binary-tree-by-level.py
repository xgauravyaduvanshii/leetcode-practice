# LeetCode 2471. Minimum Number of Operations to Sort a Binary Tree by Level — Medium
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
# Submission 2204966134 — Accepted, Python3
#
# My thinking: levels are independent, so handle each on its own.
# Sorting one level by swaps takes as many swaps as the cycles in
# the permutation that sorts it have elements minus one each — count
# the cycles and add up over all levels.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minimumOperations(self, root: TreeNode | None) -> int:
        def min_swaps(arr):
            n = len(arr)
            idx = sorted(range(n), key=lambda i: arr[i])
            visited = [False] * n
            swaps = 0
            for i in range(n):
                if visited[i] or idx[i] == i:
                    continue
                cycle = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = idx[j]
                    cycle += 1
                swaps += cycle - 1
            return swaps

        total = 0
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            total += min_swaps(level)
        return total
