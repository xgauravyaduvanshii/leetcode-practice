# LeetCode 2710. Remove Trailing Zeros From a String — Easy
# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
# Submission 2197820054 — Accepted, Python3
#
# My thinking: the trailing zeros are just the zeros
# at the end of the string, so I strip them off.

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')
