# LeetCode 3260. Find the Largest Palindrome Divisible by K — Hard
# https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/
# Submission 2202154888 — Accepted, Python3
#
# My thinking: only the first half of the
# palindrome is free — each of its digits
# contributes a known coefficient mod k (its
# two mirrored powers of 10, or one for the
# middle digit). I precompute, for each
# position, the set of remainders the suffix
# can still reach as a bitmask, then greedily
# pick the largest digit at each position that
# leaves a completable remainder.

from typing import List


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        h = (n + 1) // 2
        pow10 = [1 % k] * n
        for i in range(1, n):
            pow10[i] = (pow10[i - 1] * 10) % k
        coeff = [0] * h
        for i in range(h):
            if n % 2 == 1 and i == h - 1:
                coeff[i] = pow10[n - 1 - i]
            else:
                coeff[i] = (pow10[n - 1 - i] + pow10[i]) % k
        full = (1 << k) - 1
        suff = [0] * (h + 1)
        suff[h] = 1
        for i in range(h - 1, -1, -1):
            mask = 0
            nxt = suff[i + 1]
            c = coeff[i]
            seen = set()
            for d in range(10):
                shift = (d * c) % k
                if shift in seen:
                    continue
                seen.add(shift)
                if shift == 0:
                    rot = nxt
                else:
                    rot = ((nxt << shift) & full) | (nxt >> (k - shift))
                mask |= rot
            suff[i] = mask
        half = []
        acc = 0
        for i in range(h):
            lo = 1 if i == 0 else 0
            for d in range(9, lo - 1, -1):
                need = (-acc - d * coeff[i]) % k
                if (suff[i + 1] >> need) & 1:
                    half.append(str(d))
                    acc = (acc + d * coeff[i]) % k
                    break
        half_s = ''.join(half)
        if n % 2 == 1:
            return half_s + half_s[:-1][::-1]
        return half_s + half_s[::-1]
