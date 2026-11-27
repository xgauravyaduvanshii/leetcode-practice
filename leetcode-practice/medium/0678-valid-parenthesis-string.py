# LeetCode 678. Valid Parenthesis String — Medium
# https://leetcode.com/problems/valid-parenthesis-string/
# Submission 2198909284 — Accepted, Python3
#
# My thinking: a star can be an open bracket, a
# close bracket, or nothing, so instead of one
# balance I keep a range — the fewest and the most
# open brackets the string could have so far. The
# string works when zero stays inside that range.

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                low -= 1
                high -= 1
            else:  # "*"
                low -= 1
                high += 1
            low = max(low, 0)
            if high < 0:
                return False
        return low == 0
