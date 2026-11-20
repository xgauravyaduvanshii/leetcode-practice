# 3345. Smallest Divisible Digit Product I (Easy)
# https://leetcode.com/problems/smallest-divisible-digit-product-i/
# Submission 2200006794 — Accepted, Python3
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # My thinking: try numbers from n upward. A
        # number's digit product is the product of its
        # digits — if any digit is 0 the product is 0,
        # which is divisible by everything. The first
        # number whose product divides cleanly is the
        # answer.
        x = n
        while True:
            product = 1
            for d in str(x):
                product *= int(d)
            if product % t == 0:
                return x
            x += 1
