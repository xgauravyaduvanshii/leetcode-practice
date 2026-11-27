# LeetCode 504. Base 7 — Easy
# https://leetcode.com/problems/base-7/
# Submission 2197486221 — Accepted, Python3
#
# My thinking: same as converting to any base — keep
# taking the remainder when divided by 7 and divide
# down. I remember the sign first, work with the
# positive number, and put the minus back at the end.

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num > 0:
            digits.append(str(num % 7))
            num //= 7
        result = "".join(reversed(digits))
        return "-" + result if negative else result
