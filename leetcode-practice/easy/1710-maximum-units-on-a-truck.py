# LeetCode 1710. Maximum Units on a Truck — Easy
# https://leetcode.com/problems/maximum-units-on-a-truck/
# Submission 2197594877 — Accepted, Python3
#
# My thinking: I load the box types with the most
# units per box first — that is always best. I
# take as many boxes of each type as fit in the
# truck, and stop when the truck is full.

class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0
        for count, units in boxTypes:
            take = min(count, truckSize)
            total += take * units
            truckSize -= take
            if truckSize == 0:
                break
        return total
