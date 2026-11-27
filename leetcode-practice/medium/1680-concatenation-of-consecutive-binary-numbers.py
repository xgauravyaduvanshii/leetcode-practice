# LeetCode 1680. Concatenation of Consecutive Binary Numbers — Medium
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# Submission 2199908383 — Accepted, Python3
#
# My thinking: I grow the answer one number
# at a time, shifting it left by the new
# number's bit length and adding the number.
# The bit length only grows at powers of two.

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        result = 0
        bits = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                bits += 1
            result = ((result << bits) | i) % mod
        return result
