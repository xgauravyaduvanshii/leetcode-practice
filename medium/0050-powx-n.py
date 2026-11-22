# LeetCode 50. Pow(x, n) — Medium
# https://leetcode.com/problems/powx-n/
# Submission 2201085780 — Accepted, Python3
#
# My thinking: I square the base and halve the exponent
# again and again — whenever the exponent is odd I fold
# the base into the answer — and a negative exponent
# just flips the result over.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result
