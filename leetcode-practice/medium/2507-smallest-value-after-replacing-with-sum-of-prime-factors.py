# LeetCode 2507. Smallest Value After Replacing With Sum of Prime Factors — Medium
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
# Submission 2197795269 — Accepted, Python3
#
# My thinking: I replace the number with the sum of
# its prime factors, counting repeats. I repeat
# until the number stops changing — that happens
# when it is prime, since a prime's only prime
# factor is itself.

class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_sum(x):
            s = 0
            d = 2
            while d * d <= x:
                while x % d == 0:
                    s += d
                    x //= d
                d += 1
            if x > 1:
                s += x
            return s
        while True:
            m = prime_sum(n)
            if m == n:
                return n
            n = m
