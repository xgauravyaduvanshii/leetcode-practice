# LeetCode 3272. Find the Count of Good Integers — Hard
# https://leetcode.com/problems/find-the-count-of-good-integers/
# Submission 2202171004 — Accepted, Python3
#
# My thinking: a "good" integer's digits can be
# rearranged into a palindrome divisible by k.
# I build every palindrome of length n from its
# first half, keep the ones divisible by k, and
# group them by their digit-count signature —
# palindromes with the same signature share the
# same rearrangement count. For each signature I
# count all permutations minus the ones with a
# leading zero, using factorials.

from math import factorial
from typing import List


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half_len = (n + 1) // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len
        seen = set()
        for half in range(start, end):
            s = str(half)
            if n % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]
            if int(pal) % k != 0:
                continue
            cnt = [0] * 10
            for ch in pal:
                cnt[int(ch)] += 1
            seen.add(tuple(cnt))
        total = 0
        fact_n = factorial(n)
        fact_n1 = factorial(n - 1) if n > 1 else 1
        for cnt in seen:
            perms = fact_n
            for c in cnt:
                perms //= factorial(c)
            if cnt[0] > 0:
                lead_zero = fact_n1
                lead_zero //= factorial(cnt[0] - 1)
                for c in cnt[1:]:
                    lead_zero //= factorial(c)
                perms -= lead_zero
            total += perms
        return total
