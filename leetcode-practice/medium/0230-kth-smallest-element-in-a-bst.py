# LeetCode 230. Kth Smallest Element in a BST — Medium
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Submission 2198463402 — Accepted, Python3
#
# My thinking: an inorder walk of a BST visits the
# numbers in sorted order, so the kth number I meet
# is the answer. I walk it with a stack — always
# diving left first, then taking the node, then
# moving right — and stop as soon as I have counted
# k nodes.

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        return -1
