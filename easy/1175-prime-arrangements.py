# LeetCode 1175. Prime Arrangements — Easy
# https://leetcode.com/problems/prime-arrangements/
# Submission 2197560704 — Accepted, Python3
#
# My thinking: primes can only sit on prime positions
# and composites on the rest. If there are p primes
# up to n, there are p! ways to arrange the primes
# and (n - p)! ways to arrange the rest — I
# multiply those two factorials (mod 1e9+7). I find
# the primes with a sieve.

import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        if n >= 1:
            is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        p = sum(is_prime)
        return math.factorial(p) * math.factorial(n - p) % MOD
