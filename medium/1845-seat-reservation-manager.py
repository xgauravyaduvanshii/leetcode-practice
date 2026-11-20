# LeetCode 1845. Seat Reservation Manager — Medium
# https://leetcode.com/problems/seat-reservation-manager/
# Submission 2199946470 — Accepted, Python3
#
# My thinking: the smallest free seat is
# always the next one to hand out, and a
# returned seat just goes back into the pool.
# A min-heap does both jobs.

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.free = list(range(1, n + 1))
        heapq.heapify(self.free)

    def reserve(self) -> int:
        return heapq.heappop(self.free)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.free, seatNumber)
