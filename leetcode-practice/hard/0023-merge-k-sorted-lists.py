# LeetCode 23. Merge k Sorted Lists — Hard
# https://leetcode.com/problems/merge-k-sorted-lists/
# Submission 2198362859 — Accepted, Python3
#
# My thinking: I keep the front node of every list
# in a small heap, so the smallest one is always on
# top. I take it off, attach it to the answer, and
# push the next node from that same list into the
# heap. The list number travels along so two nodes
# with the same value never get compared directly.

import heapq


class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        tail = dummy
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
