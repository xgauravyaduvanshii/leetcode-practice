# LeetCode 1808. Maximize Number of Nice Divisors — Hard
# https://leetcode.com/problems/maximize-number-of-nice-divisors/
# Submission 2201178266 — Accepted, Python3
#
# My thinking: the nice divisors multiply out as
# the product of the exponents, so I split the
# prime factors into threes — a leftover one is
# better spent as two twos than as a three and a
# one.

MOD = 10 ** 9 + 7

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors == 1:
            return 1
        q, r = divmod(primeFactors, 3)
        if r == 0:
            return pow(3, q, MOD)
        if r == 1:
            return pow(3, q - 1, MOD) * 4 % MOD
        return pow(3, q, MOD) * 2 % MOD
