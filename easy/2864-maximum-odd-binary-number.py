# LeetCode 2864. Maximum Odd Binary Number — Easy
# https://leetcode.com/problems/maximum-odd-binary-number/
# Submission 2198424631 — Accepted, Python3
#
# My thinking: the number must end in 1 to be odd,
# so one of the 1s is fixed at the end. To make the
# number as big as possible I put all the remaining
# 1s first, then all the 0s, then that final 1.

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = len(s) - ones
        return "1" * (ones - 1) + "0" * zeros + "1"
