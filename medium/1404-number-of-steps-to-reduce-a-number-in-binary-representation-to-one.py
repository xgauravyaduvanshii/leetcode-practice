# LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to One — Medium
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Submission 2199050067 — Accepted, Python3
#
# My thinking: I scan the bits from the right,
# carrying a one whenever an odd step adds one.
# A zero bit costs one step, a one bit costs
# two — the final carry adds one more.

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry
            if bit % 2 == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
