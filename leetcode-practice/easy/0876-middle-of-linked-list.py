# LeetCode 876. Middle of the Linked List — Easy
# https://leetcode.com/problems/middle-of-the-linked-list/
# Submission 2197286850 — Accepted, Python3
#
# My thinking: two pointers — one moves one step at a
# time, the other moves two. When the fast one reaches
# the end, the slow one is sitting in the middle.
# With an even number of nodes this gives the second
# middle node, which is what the problem asks for.

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
