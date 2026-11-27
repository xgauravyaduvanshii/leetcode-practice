# LeetCode 729. My Calendar I — Medium
# https://leetcode.com/problems/my-calendar-i/
# Submission 2198923048 — Accepted, Python3
#
# My thinking: a new booking is fine only when it
# does not overlap any booking already on the
# calendar. Two intervals overlap when each one
# starts before the other ends.

class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if start < e and s < end:
                return False
        self.bookings.append((start, end))
        return True
