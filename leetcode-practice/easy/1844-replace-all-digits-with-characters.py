# LeetCode 1844. Replace All Digits with Characters — Easy
# https://leetcode.com/problems/replace-all-digits-with-characters/
# Submission 2197600774 — Accepted, Python3
#
# My thinking: every odd position holds a digit that
# says how far to shift the letter before it. I
# walk the odd positions, replace each digit with
# that shifted letter, and join everything back.

class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for i in range(1, len(chars), 2):
            chars[i] = chr(ord(chars[i - 1]) + int(chars[i]))
        return "".join(chars)
