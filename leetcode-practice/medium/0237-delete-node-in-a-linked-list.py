# LeetCode 237. Delete Node in a Linked List — Medium
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Submission 2198723990 — Accepted, Python3
#
# My thinking: I cannot reach the node before this
# one, so I do not remove the node itself — I copy
# the next node's value into it and skip over the
# next node. The list then reads exactly as if this
# node had been deleted.

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
