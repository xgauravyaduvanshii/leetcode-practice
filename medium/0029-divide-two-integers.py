# LeetCode 29. Divide Two Integers — Medium
# https://leetcode.com/problems/divide-two-integers/
# Submission 2203813070 — Accepted, Python3
#
# My thinking: I work with the absolute values and double the divisor
# by shifting left, finding the biggest doubled chunk that still fits
# into what is left of the dividend. Each chunk I take adds its power
# of two to the answer, then I keep going with the remainder. The sign
# goes on at the end, and the one overflow case (-2^31 divided by -1)
# is clamped to 2^31 - 1.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        while a >= b:
            chunk, multiple = b, 1
            while a >= (chunk << 1):
                chunk <<= 1
                multiple <<= 1
            a -= chunk
            quotient += multiple
        return -quotient if negative else quotient
