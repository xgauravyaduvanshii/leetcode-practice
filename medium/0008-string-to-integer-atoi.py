# LeetCode 8. String to Integer (atoi) — Medium
# https://leetcode.com/problems/string-to-integer-atoi/
# Submission 2203801353 — Accepted, Python3
#
# My thinking: I skip leading spaces, read an optional sign, then
# collect digits until a non-digit shows up. I build the number digit
# by digit, clamping it to the 32-bit signed range as I go, so a huge
# input can never overflow past the limits.

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1
        value = 0
        while i < n and s[i].isdigit():
            value = value * 10 + int(s[i])
            i += 1
        value *= sign
        return max(-2**31, min(2**31 - 1, value))
