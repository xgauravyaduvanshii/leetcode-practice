# LeetCode 725. Split Linked List in Parts — Medium
# https://leetcode.com/problems/split-linked-list-in-parts/
# Submission 2198922625 — Accepted, Python3
#
# My thinking: I count the list first, then work
# out how big each part should be — the first
# parts get one extra node when the length does
# not divide evenly. Then I cut the list into
# those pieces.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        base, extra = divmod(length, k)
        parts = []
        current = head
        for _ in range(k):
            part_head = current
            size = base + (1 if extra > 0 else 0)
            extra -= 1 if extra > 0 else 0
            for _ in range(size - 1):
                if current:
                    current = current.next
            if current:
                nxt = current.next
                current.next = None
                current = nxt
            parts.append(part_head)
        return parts
