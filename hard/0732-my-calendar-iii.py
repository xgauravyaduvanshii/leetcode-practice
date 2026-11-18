# LeetCode 732. My Calendar III — Hard
# https://leetcode.com/problems/my-calendar-iii/
# Submission 2198669886 — Accepted, Python3
#
# My thinking: every booking is just a +1 at its start
# and a -1 at its end. Walking the timeline in order
# and keeping a running total tells me how many events
# overlap at any point, and the biggest total so far
# is the answer.

class MyCalendarThree:
    def __init__(self):
        self.timeline = {}

    def book(self, start: int, end: int) -> int:
        self.timeline[start] = self.timeline.get(start, 0) + 1
        self.timeline[end] = self.timeline.get(end, 0) - 1
        running = 0
        best = 0
        for time in sorted(self.timeline):
            running += self.timeline[time]
            best = max(best, running)
        return best
