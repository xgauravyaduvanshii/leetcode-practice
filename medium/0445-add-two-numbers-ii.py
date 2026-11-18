# LeetCode 445. Add Two Numbers II — Medium
# https://leetcode.com/problems/add-two-numbers-ii/
# Submission 2198797103 — Accepted, Python3
#
# My thinking: the digits come most-significant
# first, so I push both lists onto stacks and add
# from the back, carrying tens forward. Each new
# result digit is built in front of the answer.

class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None
        while stack1 or stack2 or carry:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            node = ListNode(total % 10)
            node.next = head
            head = node
            carry = total // 10
        return head
