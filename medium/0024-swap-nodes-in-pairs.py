# LeetCode 24. Swap Nodes in Pairs — Medium
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Submission 2203811353 — Accepted, Python3
#
# My thinking: I walk the list two nodes at a time with a dummy node
# in front, so the head swap needs no special case. For each pair I
# point the previous node at the second node, the second node back at
# the first, and the first node at whatever comes after the pair, then
# move on to the next pair.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: 'ListNode | None') -> 'ListNode | None':
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        return dummy.next
