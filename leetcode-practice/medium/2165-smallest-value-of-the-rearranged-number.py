# LeetCode 2165. Smallest Value of the Rearranged Number — Medium
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
# Submission 2204483057 — Accepted, Python3
#
# My thinking: for a positive number the smallest rearrangement sorts
# the digits ascending, except the first digit must not be zero — so I
# swap the smallest non-zero digit to the front. For a negative number
# the smallest value comes from the digits in descending order, making
# the magnitude as large as possible.
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        neg = num < 0
        digits = sorted(str(abs(num)))
        if neg:
            return -int(''.join(digits[::-1]))
        for i, ch in enumerate(digits):
            if ch != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
        return int(''.join(digits))
