# LeetCode 1201. Ugly Number III — Medium
# https://leetcode.com/problems/ugly-number-iii/
# Submission 2199011978 — Accepted, Python3
#
# My thinking: I count how many numbers up to x
# are divisible by a, b or c — inclusion and
# exclusion with their least common multiples.
# That count grows steadily, so I binary search
# the smallest x whose count reaches n.

import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)

        def count(x):
            return x // a + x // b + x // c - x // ab - x // ac - x // bc + x // abc

        lo, hi = 1, n * min(a, b, c)
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
