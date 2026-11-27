# LeetCode 2487. Remove Nodes From Linked List — Medium
# https://leetcode.com/problems/remove-nodes-from-linked-list/
# Submission 2197792675 — Accepted, Python3
#
# My thinking: a node survives only when no bigger
# node comes after it. I reverse the list, keep a
# node when it is at least as big as the biggest
# value seen so far, and reverse the kept nodes back
# into their original order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        dummy = ListNode(0)
        tail = dummy
        maxv = 0
        cur = prev
        while cur:
            if cur.val >= maxv:
                maxv = cur.val
                tail.next = cur
                tail = cur
            cur = cur.next
        tail.next = None
        prev = None
        cur = dummy.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
