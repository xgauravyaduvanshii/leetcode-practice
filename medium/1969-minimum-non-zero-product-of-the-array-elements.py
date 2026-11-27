# LeetCode 1969. Minimum Non-Zero Product of the Array Elements — Medium
# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/
# Submission 2204353068 — Accepted, Python3
#
# My thinking: the array holds 1..2^p - 1, and I can swap any two bits
# in the same position across numbers, so each bit position can be
# rearranged freely. To minimise the product I want as many small
# numbers as possible: put a single 1 in the lowest bit of every number
# except one, which keeps all the remaining 1s. That leaves one factor
# of (2^p - 1) and (2^(p-1) - 1) factors of (2^p - 2), computed with
# modular exponentiation.
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10 ** 9 + 7
        return ((pow(2, p, MOD) - 1) * pow((pow(2, p, MOD) - 2) % MOD, pow(2, p - 1) - 1, MOD)) % MOD
