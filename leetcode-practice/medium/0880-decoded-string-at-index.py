# LeetCode 880. Decoded String at Index — Medium
# https://leetcode.com/problems/decoded-string-at-index/
# Submission 2198961741 — Accepted, Python3
#
# My thinking: I first work out how long the
# decoded string would be, then walk backwards
# through the code, shrinking the size and the
# index together until I land on the letter I
# need — without ever building the string.

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1
        for ch in reversed(s):
            k %= size
            if k == 0 and ch.isalpha():
                return ch
            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1
        return ""
