# LeetCode 2594. Minimum Time to Repair Cars — Medium
# https://leetcode.com/problems/minimum-time-to-repair-cars/
# Submission 2205092424 — Accepted, Python3
#
# My thinking: binary-search the time. In t minutes a mechanic
# of rank r repairs floor(sqrt(t / r)) cars, so the total over
# all mechanics is monotone in t — find the smallest t that
# covers all the cars.
import math


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def can(t):
            total = 0
            for r in ranks:
                total += math.isqrt(t // r)
                if total >= cars:
                    return True
            return total >= cars

        lo, hi = 1, min(ranks) * cars * cars
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
