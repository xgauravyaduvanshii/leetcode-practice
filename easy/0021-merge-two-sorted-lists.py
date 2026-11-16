# LeetCode 21. Merge Two Sorted Lists — Easy
# https://leetcode.com/problems/merge-two-sorted-lists/
# Submission 2197279460 — Accepted, Python3
#
# My thinking: both lists are already sorted, so I just
# walk through them together and always pick the smaller
# front node. A dummy node at the start makes the code
# much simpler — I do not have to handle the first node
# as a special case.

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # one list is finished — attach whatever is left
        tail.next = list1 if list1 else list2
        return dummy.next
