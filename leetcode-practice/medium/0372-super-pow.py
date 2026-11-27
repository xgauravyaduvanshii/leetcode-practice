# LeetCode 372. Super Pow — Medium
# https://leetcode.com/problems/super-pow/
# Submission 2198759307 — Accepted, Python3
#
# My thinking: the exponent arrives digit by digit,
# so I build the answer the same way — each new
# digit raises the answer so far to the tenth power
# and multiplies in one more power of a. Everything
# stays modulo 1337, so the numbers never grow.

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = 1
        for digit in b:
            result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
        return result
