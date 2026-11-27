# LeetCode 2. Add Two Numbers — Medium
# https://leetcode.com/problems/add-two-numbers/
# Submission 2201088973 — Accepted, Python3
#
# My thinking: I add the two lists digit by digit from
# the front, carrying the tens forward, and keep going
# while either list or the carry has anything left.

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            current.next = ListNode(digit)
            current = current.next
        return dummy.next
