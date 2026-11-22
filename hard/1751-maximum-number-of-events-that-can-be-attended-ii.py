# LeetCode 1751. Maximum Number of Events That Can Be Attended II — Hard
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
# Submission 2201139691 — Accepted, Python3
#
# My thinking: I sort the events by start time and
# walk backwards keeping, for each number of events
# I may still attend, the best value from here on —
# taking an event jumps straight to the first event
# that starts after it ends.

from bisect import bisect_right

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort(key=lambda e: e[0])
        n = len(events)
        starts = [e[0] for e in events]
        nxt = [bisect_right(starts, events[i][1], i + 1) for i in range(n)]
        prev = [0] * (n + 1)
        for _ in range(k):
            curr = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                curr[i] = max(curr[i + 1], events[i][2] + prev[nxt[i]])
            prev = curr
        return prev[0]
