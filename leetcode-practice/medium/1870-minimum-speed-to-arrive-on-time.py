# 1870. Minimum Speed to Arrive on Time (Medium)
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
# Submission 2199952179 — Accepted, Python3
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # My thinking: every train except the last takes a
        # whole number of hours (the wait is rounded up),
        # so even at infinite speed the trip needs at
        # least len(dist) - 1 hours. If hour is not above
        # that, it is impossible. Otherwise the travel
        # time only shrinks as speed grows, so binary
        # search finds the slowest speed that still fits.
        n = len(dist)
        if hour <= n - 1:
            return -1

        def travel_time(speed: int) -> float:
            total = 0
            for d in dist[:-1]:
                total += -(-d // speed)
            return total + dist[-1] / speed

        low, high = 1, 10 ** 7
        while low < high:
            mid = (low + high) // 2
            if travel_time(mid) <= hour:
                high = mid
            else:
                low = mid + 1
        return low
