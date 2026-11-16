# LeetCode 203. Remove Linked List Elements — Easy
# https://leetcode.com/problems/remove-linked-list-elements/
# Submission 2197450433 — Accepted, Python3
#
# My thinking: a dummy node in front of the head makes
# this much easier — then even the first node can be
# removed the same way as the rest. I walk along, and
# whenever the next node's value matches, I skip over
# it; otherwise I move forward.

class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode(0, head)
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
