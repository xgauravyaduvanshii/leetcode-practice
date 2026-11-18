# LeetCode 1094. Car Pooling — Medium
# https://leetcode.com/problems/car-pooling/
# Submission 2198997841 — Accepted, Python3
#
# My thinking: I note every pickup and drop-off
# as a change in the number of riders, then sweep
# through the stops in order. If the riders ever
# pass the capacity, the trips cannot all run.

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for passengers, start, end in trips:
            stops[start] += passengers
            stops[end] -= passengers
        riding = 0
        for change in stops:
            riding += change
            if riding > capacity:
                return False
        return True
