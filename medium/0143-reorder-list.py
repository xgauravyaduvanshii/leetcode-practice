# LeetCode 143. Reorder List — Medium
# https://leetcode.com/problems/reorder-list/
# Submission 2204044479 — Accepted, Python3
#
# My thinking: I split the list in half with a slow and a fast pointer,
# so the slow pointer ends at the middle. I reverse the second half in
# place, then weave the two halves together one node at a time — first
# half, then reversed second half, and so on — until the second half
# runs out. This reorders the list in place, using only O(1) extra
# memory and one pass for each step.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: 'ListNode | None') -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find the middle of the list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half.
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge the two halves alternately.
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
