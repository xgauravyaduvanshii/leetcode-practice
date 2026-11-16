# LeetCode 2309. Greatest English Letter in Upper and Lower Case — Easy
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
# Submission 2197622651 — Accepted, Python3
#
# My thinking: I check the letters from Z down to A
# and take the first one that appears in both its
# upper and lower case forms in the string.

class Solution:
    def greatestLetter(self, s: str) -> str:
        for c in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
            if c in s and c.lower() in s:
                return c
        return ""
