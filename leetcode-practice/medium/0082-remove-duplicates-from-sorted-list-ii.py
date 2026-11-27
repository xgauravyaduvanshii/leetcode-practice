# LeetCode 82. Remove Duplicates from Sorted List II — Medium
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Submission 2203959736 — Accepted, Python3
#
# My thinking: because the list is sorted, all copies of a value sit
# together, so I can spot a duplicate by looking at the next node's
# value. I use a dummy node in front of the head so that duplicates at
# the very start are handled the same as anywhere else. I walk with a
# pointer to the last node known to be clean: if the next node has a
# different value from the one after it, it is unique and I move on;
# otherwise I skip the whole run of equal values by jumping past every
# node with that value, without linking any of them in.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next:
            if prev.next.next and prev.next.val == prev.next.next.val:
                dup_val = prev.next.val
                while prev.next and prev.next.val == dup_val:
                    prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
