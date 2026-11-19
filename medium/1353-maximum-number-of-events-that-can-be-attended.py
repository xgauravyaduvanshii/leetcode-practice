# LeetCode 1353. Maximum Number of Events That Can Be Attended — Medium
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# Submission 2199037707 — Accepted, Python3
#
# My thinking: day by day, I attend the event
# that ends soonest among those that have
# started. A min-heap of end days keeps that
# choice cheap, and expired events drop out.

import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        day = 0
        i = 0
        attended = 0
        ends = []
        while i < len(events) or ends:
            if not ends:
                day = max(day, events[i][0])
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(ends, events[i][1])
                i += 1
            heapq.heappop(ends)
            attended += 1
            day += 1
            while ends and ends[0] < day:
                heapq.heappop(ends)
        return attended
