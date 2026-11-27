# LeetCode 171. Excel Sheet Column Number — Easy
# https://leetcode.com/problems/excel-sheet-column-number/
# Submission 2197448832 — Accepted, Python3
#
# My thinking: this is just base 26, except A is 1,
# not 0. I go through the letters left to right,
# multiply what I have so far by 26, and add the
# value of the next letter.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
