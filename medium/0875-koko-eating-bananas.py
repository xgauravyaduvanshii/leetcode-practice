# LeetCode 875. Koko Eating Bananas — Medium
# https://leetcode.com/problems/koko-eating-bananas/
# Submission 2198961174 — Accepted, Python3
#
# My thinking: the hours needed shrink as the
# speed grows, so the smallest speed that fits
# in time is found with a binary search between
# one banana an hour and the biggest pile.

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(speed):
            return sum((pile + speed - 1) // speed for pile in piles)

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if hours(mid) <= h:
                high = mid
            else:
                low = mid + 1
        return low
