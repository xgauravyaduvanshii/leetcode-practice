# LeetCode 1171. Remove Zero Sum Consecutive Nodes from Linked List — Medium
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# Submission 2199009124 — Accepted, Python3
#
# My thinking: I record the running sum at each
# node. When a sum repeats, everything between
# the two nodes adds to zero, so I skip straight
# from the first to the last.

from __future__ import annotations

from typing import Optional


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix = 0
        last_seen = {0: dummy}
        node = head
        while node:
            prefix += node.val
            last_seen[prefix] = node
            node = node.next
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            node.next = last_seen[prefix].next
            node = node.next
        return dummy.next
