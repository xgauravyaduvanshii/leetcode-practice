# LeetCode 2264. Largest 3-Same-Digit Number in String — Easy
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Submission 2197620730 — Accepted, Python3
#
# My thinking: I scan every window of three
# characters and keep the biggest one where all
# three digits are the same.

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i:i + 3] > best:
                    best = num[i:i + 3]
        return best
