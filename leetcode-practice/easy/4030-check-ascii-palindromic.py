# 4030. Check ASCII Palindromic (Easy)
# https://leetcode.com/problems/check-ascii-palindromic/
# Submission 2200098567 — Accepted, Python3
class Solution:
    def isPalindromic(self, s: str) -> bool:
        # My thinking: I write every letter as its
        # eight-bit ASCII code, join them into one
        # long binary string, and check whether it
        # reads the same backwards.
        b = "".join(format(ord(ch), "08b") for ch in s)
        return b == b[::-1]
