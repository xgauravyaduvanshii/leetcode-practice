# LeetCode 19. Remove Nth Node From End of List — Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Submission 2203809186 — Accepted, Python3
#
# My thinking: I put a dummy node in front of the list so removing
# the head is no special case. I send a fast pointer n+1 steps ahead,
# then walk both pointers together until the fast one reaches the end;
# the slow pointer then sits just before the node to remove, and one
# link change drops it out.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: 'ListNode | None', n: int) -> 'ListNode | None':
        dummy = ListNode(0, head)
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        slow = dummy
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
