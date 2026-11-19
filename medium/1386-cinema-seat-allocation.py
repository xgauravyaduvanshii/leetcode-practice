# LeetCode 1386. Cinema Seat Allocation — Medium
# https://leetcode.com/problems/cinema-seat-allocation/
# Submission 2199044728 — Accepted, Python3
#
# My thinking: rows with no reservations fit
# two families each. For the rest I check the
# three possible blocks of four — left, middle
# and right — and count what fits.

from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row].add(seat)
        families = 2 * (n - len(rows))
        for seats in rows.values():
            left = not ({2, 3, 4, 5} & seats)
            middle = not ({4, 5, 6, 7} & seats)
            right = not ({6, 7, 8, 9} & seats)
            if left and right:
                families += 2
            elif left or middle or right:
                families += 1
        return families
