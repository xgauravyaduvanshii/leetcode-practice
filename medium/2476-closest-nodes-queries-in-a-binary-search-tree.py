# LeetCode 2476. Closest Nodes Queries in a Binary Search Tree — Medium
# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/
# Submission 2204967045 — Accepted, Python3
#
# My thinking: an inorder walk of a BST lists its values in sorted
# order. For each query, binary-search that list: an exact hit
# answers [q, q], otherwise the neighbours around the insertion
# point are the closest smaller and larger values, or -1 when one
# side does not exist.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect


class Solution:
    def closestNodes(self, root: TreeNode | None, queries: list[int]) -> list[list[int]]:
        vals = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            vals.append(node.val)
            node = node.right
        res = []
        n = len(vals)
        for q in queries:
            i = bisect.bisect_left(vals, q)
            if i < n and vals[i] == q:
                res.append([q, q])
            else:
                lo = vals[i - 1] if i > 0 else -1
                hi = vals[i] if i < n else -1
                res.append([lo, hi])
        return res
