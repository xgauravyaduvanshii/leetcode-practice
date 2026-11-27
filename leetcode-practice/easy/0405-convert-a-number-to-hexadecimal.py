# LeetCode 405. Convert a Number to Hexadecimal — Easy
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Submission 2197472375 — Accepted, Python3
#
# My thinking: I build the hex string from the end
# backwards — each step takes the remainder when
# divided by 16 and looks up its hex digit. A
# negative number is treated as its 32-bit
# two's-complement value, so I add 2^32 first.

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        digits = "0123456789abcdef"
        result = ""
        while num > 0:
            result = digits[num % 16] + result
            num //= 16
        return result
