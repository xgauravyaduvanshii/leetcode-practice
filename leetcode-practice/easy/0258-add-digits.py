# LeetCode 258. Add Digits — Easy
# https://leetcode.com/problems/add-digits/
# Submission 2197458540 — Accepted, Python3
#
# My thinking: adding digits over and over always
# ends at the digital root. That follows a simple
# pattern: 0 stays 0, and for anything else the
# answer is 1 + (num - 1) % 9.

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
