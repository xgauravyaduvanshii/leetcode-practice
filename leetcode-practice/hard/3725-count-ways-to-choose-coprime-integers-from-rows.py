# LeetCode 3725. Count Ways to Choose Coprime Integers from Rows — Hard
# https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/
# Submission 2203131727 — Accepted, Python3
from typing import List


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        # My thinking: the gcd of the chosen numbers is 1 exactly
        # when no prime divides all of them, so Mobius inversion
        # over the divisor d does the counting: for each d, count
        # the choices whose numbers are all multiples of d (a
        # product over the rows of the per-row multiple counts),
        # then add them up weighted by mu(d). Values are at most
        # 150, so a linear sieve gives mu up to 150 and each row's
        # multiple counts come from one frequency pass.
        MOD = 10 ** 9 + 7
        MAXV = 150
        mu = [0] * (MAXV + 1)
        mu[1] = 1
        primes = []
        is_comp = [False] * (MAXV + 1)
        for i in range(2, MAXV + 1):
            if not is_comp[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > MAXV:
                    break
                is_comp[i * p] = True
                if i % p == 0:
                    mu[i * p] = 0
                    break
                mu[i * p] = -mu[i]
        # Per row, how many entries are multiples of each d.
        row_mults = []
        for row in mat:
            freq = [0] * (MAXV + 1)
            for x in row:
                freq[x] += 1
            mult = [0] * (MAXV + 1)
            for d in range(1, MAXV + 1):
                s = 0
                for m in range(d, MAXV + 1, d):
                    s += freq[m]
                mult[d] = s
            row_mults.append(mult)
        ans = 0
        for d in range(1, MAXV + 1):
            if mu[d] == 0:
                continue
            prod = 1
            for mult in row_mults:
                prod = prod * mult[d] % MOD
                if prod == 0:
                    break
            ans = (ans + mu[d] * prod) % MOD
        return ans
