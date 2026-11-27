# LeetCode 2187. Minimum Time to Complete Trips — Medium
# https://leetcode.com/problems/minimum-time-to-complete-trips/
# Submission 2204494123 — Accepted, Python3
#
# My thinking: the number of trips finished by time T only grows with T,
# so the smallest T that reaches totalTrips is found by binary search.
# The search runs between 1 and the fastest bus alone doing all the
# trips, and I count trips at each midpoint, stopping early once the
# target is reached.
class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        lo, hi = 1, min(time) * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            trips = 0
            for t in time:
                trips += mid // t
                if trips >= totalTrips:
                    break
            if trips >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo
