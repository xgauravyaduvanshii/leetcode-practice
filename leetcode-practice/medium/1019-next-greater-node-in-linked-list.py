# LeetCode 1019. Next Greater Node In Linked List — Medium
# https://leetcode.com/problems/next-greater-node-in-linked-list/
# Submission 2198987278 — Accepted, Python3
#
# My thinking: I read the list into an array and
# scan it backwards, keeping a stack of values
# that are still waiting for something bigger.
# The top of the stack is each node's next
# greater value.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        result = [0] * len(values)
        stack = []
        for i in range(len(values) - 1, -1, -1):
            while stack and values[stack[-1]] <= values[i]:
                stack.pop()
            if stack:
                result[i] = values[stack[-1]]
            stack.append(i)
        return result
