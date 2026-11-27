# LeetCode 731. My Calendar II — Medium
# https://leetcode.com/problems/my-calendar-ii/
# Submission 2198923394 — Accepted, Python3
#
# My thinking: I keep the bookings and also every
# place where two of them overlap. A new booking
# is refused when it would touch one of those
# overlaps — that would make three at once.

class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and s < end:
                return False
        for s, e in self.bookings:
            if start < e and s < end:
                self.overlaps.append((max(start, s), min(end, e)))
        self.bookings.append((start, end))
        return True
