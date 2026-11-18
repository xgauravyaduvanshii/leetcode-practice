# LeetCode 475. Heaters — Medium
# https://leetcode.com/problems/heaters/
# Submission 2198819147 — Accepted, Python3
#
# My thinking: for each house the nearest heater is
# one of the two around it in the sorted heater
# list, found with binary search. The radius has to
# cover the worst house, so I take the biggest of
# those nearest distances.

import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for house in houses:
            position = bisect.bisect_left(heaters, house)
            nearest = float("inf")
            if position < len(heaters):
                nearest = min(nearest, heaters[position] - house)
            if position > 0:
                nearest = min(nearest, house - heaters[position - 1])
            radius = max(radius, nearest)
        return radius
