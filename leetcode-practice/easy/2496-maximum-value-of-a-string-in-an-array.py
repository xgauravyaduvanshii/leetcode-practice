# LeetCode 2496. Maximum Value of a String in an Array — Easy
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
# Submission 2197794021 — Accepted, Python3
#
# My thinking: a string made only of digits is worth
# its numeric value; any other string is worth its
# length. I take the biggest value over the array.

class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        best = 0
        for s in strs:
            if s.isdigit():
                best = max(best, int(s))
            else:
                best = max(best, len(s))
        return best
