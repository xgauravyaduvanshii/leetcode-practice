# LeetCode 83. Remove Duplicates from Sorted List — Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Submission 2197384319 — Accepted, Python3
#
# My thinking: the list is sorted, so any duplicates sit
# right next to each other. I walk along and whenever two
# neighbours match, I skip the second one.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sorted list, so duplicates sit next to each other — skip them in place.
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
