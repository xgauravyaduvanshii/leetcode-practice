# LeetCode 1342. Number of Steps to Reduce a Number to Zero — Easy
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Submission 2197286554 — Accepted, Python3
#
# My thinking: just follow the rules until the number
# hits zero. Even number — divide by 2. Odd number —
# subtract 1. Count every step along the way.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps
