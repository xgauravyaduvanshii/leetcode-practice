# LeetCode 2095. Delete the Middle Node of a Linked List — Medium
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Submission 2200970833 — Accepted, Python3
#
# My thinking: I walk two pointers — one twice as fast
# — so when the fast one reaches the end, the slow one
# sits just before the middle, and I skip that node.

class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
