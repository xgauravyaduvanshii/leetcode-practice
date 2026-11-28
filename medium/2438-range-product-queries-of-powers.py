# LeetCode 2438. Range Product Queries of Powers — Medium
# https://leetcode.com/problems/range-product-queries-of-powers/
# Submission 2204944539 — Accepted, Python3
#
# My thinking: the binary representation of n gives the powers of
# two directly, one per set bit. Prefix sums of their exponents turn
# each query's product into a single power of two, computed with
# modular exponentiation.
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        exponents = []
        bit = 0
        while n:
            if n & 1:
                exponents.append(bit)
            n >>= 1
            bit += 1
        pref = [0]
        for e in exponents:
            pref.append(pref[-1] + e)
        return [pow(2, pref[r + 1] - pref[l], MOD) for l, r in queries]
