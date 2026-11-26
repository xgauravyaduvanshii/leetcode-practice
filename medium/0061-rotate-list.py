# LeetCode 61. Rotate List — Medium
# https://leetcode.com/problems/rotate-list/
# Submission 2203836123 — Accepted, Python3
#
# My thinking: rotating by k is the same as rotating by k modulo the
# length, so I first measure the length and close the list into a ring
# by pointing the tail at the head. The new tail is length - k - 1
# steps from the head; I walk there, take the next node as the new
# head, and break the ring.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: 'ListNode | None', k: int) -> 'ListNode | None':
        if head is None or head.next is None or k == 0:
            return head
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        tail.next = head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
