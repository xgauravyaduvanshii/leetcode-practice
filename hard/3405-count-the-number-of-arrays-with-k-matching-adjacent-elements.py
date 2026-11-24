# LeetCode 3405. Count the Number of Arrays with K Matching Adjacent Elements — Hard
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/
# Submission 2202511161 — Accepted 809/809, Python3


class Solution:
    def countArrays(self, n: int, m: int, k: int) -> int:
        # My thinking: pick which k of the n - 1 adjacent slots are
        # the matching ones — C(n - 1, k) ways. Then the first element
        # has m choices, each matching slot is forced to repeat the
        # previous value, and each of the other n - 1 - k slots has
        # m - 1 choices (anything but the previous value). Multiply
        # the three counts, all modulo 1_000_000_007.
        mod = 10 ** 9 + 7
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % mod
        inv_fact = [1] * n
        inv_fact[n - 1] = pow(fact[n - 1], mod - 2, mod)
        for i in range(n - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % mod

        def comb(a: int, b: int) -> int:
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % mod * inv_fact[a - b] % mod

        return comb(n - 1, k) * m % mod * pow(m - 1, n - 1 - k, mod) % mod
