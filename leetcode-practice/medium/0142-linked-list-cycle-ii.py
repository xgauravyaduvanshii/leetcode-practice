# LeetCode 142. Linked List Cycle II — Medium
# https://leetcode.com/problems/linked-list-cycle-ii/
# Submission 2204042192 — Accepted, Python3
#
# My thinking: I use Floyd's two-pointer trick in two phases. First,
# a slow pointer moving one step and a fast pointer moving two steps
# will meet inside the cycle if there is one — the fast pointer laps
# the slow one, so no meeting means no cycle and I return None. Once
# they meet, I send a second pointer back to the head and walk it and
# the slow pointer one step at a time; they meet exactly at the node
# where the cycle begins, because the distance from the head to the
# cycle start equals the distance from the meeting point around the
# cycle to the start. This needs no extra memory and one pass.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: 'ListNode | None') -> 'ListNode | None':
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                entry = head
                while entry is not slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
