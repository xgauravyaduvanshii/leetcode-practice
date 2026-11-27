# LeetCode 328. Odd Even Linked List — Medium
# https://leetcode.com/problems/odd-even-linked-list/
# Submission 2198747439 — Accepted, Python3
#
# My thinking: I walk the list with two pointers,
# one gathering the odd positions and one the even
# positions, each skipping ahead by two. When the
# walk ends I join the odd chain onto the head of
# the even chain.

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
