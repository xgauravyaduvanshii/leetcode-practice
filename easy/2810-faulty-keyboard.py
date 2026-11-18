# LeetCode 2810. Faulty Keyboard — Easy
# https://leetcode.com/problems/faulty-keyboard/
# Submission 2198414943 — Accepted, Python3
#
# My thinking: I type the string one character at a
# time. A normal character is simply added, and an
# 'i' reverses everything typed so far — the 'i'
# itself never appears in the result.

class Solution:
    def finalString(self, s: str) -> str:
        chars = []
        for ch in s:
            if ch == "i":
                chars.reverse()
            else:
                chars.append(ch)
        return "".join(chars)
