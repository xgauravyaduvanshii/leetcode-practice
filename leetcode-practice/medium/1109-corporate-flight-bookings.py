# LeetCode 1109. Corporate Flight Bookings — Medium
# https://leetcode.com/problems/corporate-flight-bookings/
# Submission 2199000692 — Accepted, Python3
#
# My thinking: each booking adds seats from its
# first flight and takes them away after its
# last. One sweep through those changes gives
# the seats on every flight.

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats
        result = []
        running = 0
        for i in range(n):
            running += diff[i]
            result.append(running)
        return result
