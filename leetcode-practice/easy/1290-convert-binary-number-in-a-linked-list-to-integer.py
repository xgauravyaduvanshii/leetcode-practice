# LeetCode 1290. Convert Binary Number in a Linked List to Integer — Easy
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Submission 2197567720 — Accepted, Python3
#
# My thinking: I walk the list from the head, building
# the number as I go — each step doubles what I
# have so far and adds the next bit. That is exactly
# how binary place values work.

class Solution:
    def getDecimalValue(self, head) -> int:
        result = 0
        while head:
            result = result * 2 + head.val
            head = head.next
        return result
