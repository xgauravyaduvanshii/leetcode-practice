# LeetCode 4073. Count Good Strings — Hard
# https://leetcode.com/problems/count-good-strings/
# Submission 2203681541 — Accepted, Python3
class Solution:
    def countGoodStrings(self, n: int) -> int:
        # My thinking: let a(n) be the number of good
        # strings of length n. A good string is either
        # a single repeated character of odd length, or
        # a split into two non-empty good parts whose
        # boundary characters differ. Counting the
        # splits by the length of the first part gives
        # the recurrence a(n) = a(n-1) + a(n-2), with
        # a(1) = 2 and a(2) = 2. That is twice the
        # Fibonacci sequence: a(n) = 2 * Fib(n). Since
        # n can be as large as 10^15, compute Fib(n)
        # in O(log n) with the fast-doubling identities
        # F(2k) = F(k) * (2*F(k+1) - F(k)) and
        # F(2k+1) = F(k)^2 + F(k+1)^2, all modulo
        # 10^9 + 7, and return twice F(n).
        MOD = 10 ** 9 + 7

        def fib_pair(k):
            if k == 0:
                return (0, 1)
            a, b = fib_pair(k >> 1)
            c = a * ((b * 2 - a) % MOD) % MOD
            d = (a * a + b * b) % MOD
            if k & 1:
                return (d, (c + d) % MOD)
            return (c, d)

        return (2 * fib_pair(n)[0]) % MOD
