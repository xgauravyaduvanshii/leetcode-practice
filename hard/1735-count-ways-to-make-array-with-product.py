# LeetCode 1735. Count Ways to Make Array With Product — Hard
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# Submission 2201124844 — Accepted, Python3
#
# My thinking: each prime power in k has to be split
# across the n slots, and splitting e identical copies
# into n slots is a stars-and-bars count — I multiply
# those counts, one prime at a time, modulo 1e9+7.

MOD = 10 ** 9 + 7

class Solution:
    def waysToFillArray(self, queries: list[list[int]]) -> list[int]:
        max_n = max(n for n, _ in queries)
        max_k = max(k for _, k in queries)
        N = max_n + 20
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (N + 1)
        inv_fact[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        spf = list(range(max_k + 1))
        for i in range(2, int(max_k ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_k + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        def prime_exponents(k):
            exps = []
            while k > 1:
                p = spf[k]
                e = 0
                while k % p == 0:
                    k //= p
                    e += 1
                exps.append(e)
            return exps
        answer = []
        for n, k in queries:
            ways = 1
            for e in prime_exponents(k):
                ways = ways * comb(n + e - 1, e) % MOD
            answer.append(ways)
        return answer
