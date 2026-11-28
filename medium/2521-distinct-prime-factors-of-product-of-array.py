# LeetCode 2521. Distinct Prime Factors of Product of Array — Medium
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/
# Submission 2204982457 — Accepted, Python3
#
# My thinking: the distinct prime factors of the product are just
# the union of the prime factors of each number, so factor every
# number by trial division — 2 first, then odd divisors only — and
# count the primes collected.
class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        primes = set()
        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    primes.add(d)
                    while x % d == 0:
                        x //= d
                d += 1 if d == 2 else 2
            if x > 1:
                primes.add(x)
        return len(primes)
