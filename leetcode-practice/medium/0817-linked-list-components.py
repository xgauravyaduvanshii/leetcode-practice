# LeetCode 817. Linked List Components — Medium
# https://leetcode.com/problems/linked-list-components/
# Submission 2198947108 — Accepted, Python3
#
# My thinking: I walk the list once. A component
# ends at a wanted node whose next node is not
# wanted — each such ending is one component.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        wanted = set(nums)
        components = 0
        node = head
        while node:
            if node.val in wanted and (not node.next or node.next.val not in wanted):
                components += 1
            node = node.next
        return components
