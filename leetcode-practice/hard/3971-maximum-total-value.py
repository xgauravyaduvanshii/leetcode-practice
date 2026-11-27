# LeetCode 3971. Maximum Total Value — Hard
# https://leetcode.com/problems/maximum-total-value/
# Submission 2203490503 — Accepted, Python3
from typing import List


class Solution:
    def maxTotalValue(self, value: List[int], decay: List[int], m: int) -> int:
        # My thinking: every selection is one gain from the
        # arithmetic sequences value[i], value[i]-decay[i],
        # ... while they stay positive, and the best m
        # selections are simply the m largest gains. For a
        # threshold x, the count of gains of at least x and
        # their sum both follow from the arithmetic-series
        # formula, and both are monotone in x, so binary
        # search finds the largest threshold T whose count
        # reaches the number taken; then take every gain
        # above T and fill the rest with gains equal to T.
        # Only positive gains are ever taken, and the total
        # is returned modulo 10^9 + 7.
        MOD = 10 ** 9 + 7

        def count_at_least(x: int) -> int:
            total = 0
            for v, d in zip(value, decay):
                if v >= x:
                    total += (v - x) // d + 1
            return total

        def sum_at_least(x: int) -> int:
            total = 0
            for v, d in zip(value, decay):
                if v >= x:
                    c = (v - x) // d + 1
                    total += c * v - d * c * (c - 1) // 2
            return total

        take = min(m, count_at_least(1))
        if take == 0:
            return 0
        lo, hi = 1, max(value)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if count_at_least(mid) >= take:
                lo = mid
            else:
                hi = mid - 1
        threshold = lo
        total = sum_at_least(threshold + 1) + (take - count_at_least(threshold + 1)) * threshold
        return total % MOD
