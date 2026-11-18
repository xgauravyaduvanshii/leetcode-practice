# LeetCode 853. Car Fleet — Medium
# https://leetcode.com/problems/car-fleet/
# Submission 2198955849 — Accepted, Python3
#
# My thinking: I look at the cars from the front
# back. A car joins the fleet ahead of it when it
# arrives no later than that fleet — otherwise it
# forms a fleet of its own.

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        slowest = 0.0
        for pos, spd in sorted(zip(position, speed), reverse=True):
            arrival = (target - pos) / spd
            if arrival > slowest:
                fleets += 1
                slowest = arrival
        return fleets
