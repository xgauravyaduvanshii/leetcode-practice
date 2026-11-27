# LeetCode 204. Count Primes — Medium
# https://leetcode.com/problems/count-primes/
# Submission 2198447353 — Accepted, Python3
#
# My thinking: I use the sieve of Eratosthenes —
# every number starts out marked prime, and for
# each prime I cross out its multiples starting
# from its square. Anything still marked at the
# end is prime, and I count those below n.

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)
