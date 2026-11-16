# LeetCode 653. Two Sum IV - Input is a BST — Easy
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Submission 2197510139 — Accepted, Python3
#
# My thinking: an inorder walk of a BST gives me the
# values already sorted. Then it is the classic two
# pointers — one at each end, moving inwards until
# the pair adds up to k.

class Solution:
    def findTarget(self, root, k: int) -> bool:
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        left, right = 0, len(values) - 1
        while left < right:
            total = values[left] + values[right]
            if total == k:
                return True
            if total < k:
                left += 1
            else:
                right -= 1
        return False
