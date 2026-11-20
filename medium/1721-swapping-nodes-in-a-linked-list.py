# LeetCode 1721. Swapping Nodes in a Linked List — Medium
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Submission 2199920682 — Accepted, Python3
#
# My thinking: the k-th node from the front
# is easy to reach, and the k-th from the back
# is the same distance behind the tail. I
# walk both pointers together, then swap the
# two values.

from __future__ import annotations


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = head
        for _ in range(k - 1):
            first = first.next
        second = head
        runner = first
        while runner.next:
            runner = runner.next
            second = second.next
        first.val, second.val = second.val, first.val
        return head
