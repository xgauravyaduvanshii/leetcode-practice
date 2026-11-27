# LeetCode 109. Convert Sorted List to Binary Search Tree — Medium
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Submission 2203998538 — Accepted, Python3
#
# My thinking: the list is already sorted, so the middle element is
# the natural root of a height-balanced tree — everything smaller
# belongs on the left and everything bigger on the right. I first
# copy the linked list into an array so I can reach the middle of
# any slice in constant time, then build recursively: pick the middle
# value as the root, build the left subtree from the values before
# it and the right subtree from the values after it, and stop when a
# slice is empty. Because each root splits its slice in half, the
# tree comes out height-balanced, and an in-order walk of the tree
# gives back the original sorted list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: "ListNode") -> "TreeNode":
        nums = []
        node = head
        while node is not None:
            nums.append(node.val)
            node = node.next

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(nums) - 1)
