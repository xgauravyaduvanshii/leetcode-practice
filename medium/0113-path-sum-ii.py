# LeetCode 113. Path Sum II — Medium
# https://leetcode.com/problems/path-sum-ii/
# Submission 2203995287 — Accepted, Python3
#
# My thinking:
# Walk the tree from the root down, carrying the path so far and the
# amount of the target sum still left to reach. At each node, subtract
# its value from the remaining sum and add the node to the current path.
# A path only counts when it ends at a leaf (a node with no children)
# and the remaining sum is exactly zero at that leaf.
# If the node is a leaf and the sum is not zero, this path is a dead
# end, so drop it. Otherwise keep going into both children, then remove
# the node from the path before returning (backtracking) so the other
# branches reuse the same path list. This visits every root-to-leaf
# path once, in O(n) time.

from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(node: Optional["TreeNode"], remaining: int) -> None:
            if node is None:
                return
            path.append(node.val)
            remaining -= node.val
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(list(path))
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            path.pop()

        dfs(root, targetSum)
        return result
