# LeetCode 1669. Merge In Between Linked Lists — Medium
# https://leetcode.com/problems/merge-in-between-linked-lists/
# Submission 2199906555 — Accepted, Python3
#
# My thinking: I find the node just before a
# and the node just after b, splice the second
# list in between, and stitch its tail to the
# rest of the first list.

from __future__ import annotations


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        for _ in range(a - 1):
            node = node.next
        before = node
        node = list1
        for _ in range(b):
            node = node.next
        after = node.next
        before.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = after
        return list1
