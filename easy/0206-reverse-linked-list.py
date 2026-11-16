# LeetCode 206. Reverse Linked List — Easy
# https://leetcode.com/problems/reverse-linked-list/
# Submission 2197451802 — Accepted, Python3
#
# My thinking: I walk through the list one node at a
# time, and flip each node's arrow to point at the
# node before it instead of the next one. I keep a
# pointer to the previous node so I do not lose it,
# and at the end that previous pointer is the new head.

class Solution:
    def reverseList(self, head):
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
