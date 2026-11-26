# LeetCode 86. Partition List — Medium
# https://leetcode.com/problems/partition-list/
# Submission 2203963178 — Accepted, Python3
#
# My thinking: I walk the list once and split it into two chains —
# one for nodes smaller than x, one for nodes x or larger — keeping
# each node's original relative order inside its own chain, because
# I only ever append to the tail of the chain it belongs to. When the
# walk is done I join the small chain to the head of the large chain
# and cap the large chain's tail with None, so the last large node
# cannot still point back into the small chain and form a cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)
        before, after = before_head, after_head
        node = head
        while node:
            if node.val < x:
                before.next = node
                before = before.next
            else:
                after.next = node
                after = after.next
            node = node.next
        after.next = None
        before.next = after_head.next
        return before_head.next
