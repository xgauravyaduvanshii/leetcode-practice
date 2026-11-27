# LeetCode 400. Nth Digit — Medium
# https://leetcode.com/problems/nth-digit/
# Submission 2198777547 — Accepted, Python3
#
# My thinking: I skip whole blocks of numbers by
# digit length — 9 one-digit numbers, 90 two-digit
# ones, and so on — until I reach the block holding
# the nth digit. Then I pick the exact number and
# the exact digit inside it.

class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
        number = 10 ** (digits - 1) + (n - 1) // digits
        return int(str(number)[(n - 1) % digits])
