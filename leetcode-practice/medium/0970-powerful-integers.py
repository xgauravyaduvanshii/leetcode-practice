# LeetCode 970. Powerful Integers — Medium
# https://leetcode.com/problems/powerful-integers/
# Submission 2198979332 — Accepted, Python3
#
# My thinking: I list every power of x and every
# power of y up to the bound — a base of one only
# ever gives one — then I take every pair whose
# sum still fits.

from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powers_x = [1]
        while powers_x[-1] * x <= bound and x != 1:
            powers_x.append(powers_x[-1] * x)
        powers_y = [1]
        while powers_y[-1] * y <= bound and y != 1:
            powers_y.append(powers_y[-1] * y)
        result = set()
        for a in powers_x:
            for b in powers_y:
                if a + b <= bound:
                    result.add(a + b)
        return list(result)
