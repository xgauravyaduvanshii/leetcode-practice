# LeetCode 1317. Convert Integer to the Sum of Two No-Zero Integers — Easy
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Submission 2197570493 — Accepted, Python3
#
# My thinking: I try a = 1, 2, 3... and let b be
# whatever is left (n - a). The first pair where
# neither number contains a zero digit is the
# answer — and one always exists.

class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for a in range(1, n):
            b = n - a
            if "0" not in str(a) and "0" not in str(b):
                return [a, b]
        return []
