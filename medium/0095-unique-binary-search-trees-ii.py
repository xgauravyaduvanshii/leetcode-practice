# LeetCode 95. Unique Binary Search Trees II — Medium
# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Submission 2203978730 — Accepted, Python3
#
# My thinking:
# In a binary search tree the inorder traversal is sorted, so for the
# values 1..n the root must be some value i, every value smaller than i
# goes in the left subtree and every value larger than i goes in the
# right subtree.
# That splits the problem into two independent smaller problems: build
# all BSTs from the values below i, and all BSTs from the values above
# i. Every left tree pairs with every right tree to make a distinct
# overall tree with i as the root, so we take the cartesian product of
# the two lists.
# The recursion bottoms out when the range is empty: there is exactly
# one empty tree, represented by None, so a leaf node still gets one
# left and one right combination.
# We repeat this for every possible root i and collect all the trees.
# The count grows like the Catalan numbers, which is why the problem
# only asks for n up to 8.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(lo: int, hi: int) -> List[Optional[TreeNode]]:
            # Empty range: exactly one empty tree.
            if lo > hi:
                return [None]
            trees = []
            for root_val in range(lo, hi + 1):
                left_trees = build(lo, root_val - 1)
                right_trees = build(root_val + 1, hi)
                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(root_val, left, right))
            return trees

        return build(1, n)
