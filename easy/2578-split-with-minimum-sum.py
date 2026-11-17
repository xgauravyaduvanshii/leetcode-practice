# LeetCode 2578. Split With Minimum Sum — Easy
# https://leetcode.com/problems/split-with-minimum-sum/
# Submission 2197805965 — Accepted, Python3
#
# My thinking: I sort the digits and deal them
# alternately into two numbers — smallest digits
# first, so both numbers stay as small as possible.
# Their sum is the minimum possible.

class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        num1 = []
        num2 = []
        for i, d in enumerate(digits):
            if i % 2 == 0:
                num1.append(d)
            else:
                num2.append(d)
        return int(''.join(num1)) + int(''.join(num2))
