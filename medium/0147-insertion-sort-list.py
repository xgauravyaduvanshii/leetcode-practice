# LeetCode 147. Insertion Sort List — Medium
# https://leetcode.com/problems/insertion-sort-list/
# Submission 2200869781 — Accepted, Python3
#
# My thinking: I keep a sorted part of the list behind a
# dummy head and take the nodes one by one from the
# unsorted part, sliding each one into its right place
# in the sorted part before moving on.

class Solution:
    def insertionSortList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        dummy = ListNode(0)
        current = head
        while current:
            previous = dummy
            while previous.next and previous.next.val < current.val:
                previous = previous.next
            next_node = current.next
            current.next = previous.next
            previous.next = current
            current = next_node
        return dummy.next
