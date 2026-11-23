# LeetCode 2276. Count Integers in Intervals — Hard
# https://leetcode.com/problems/count-integers-in-intervals/
# Submission 2201650958 — Accepted, Python3
#
# My thinking: the covered integers are a
# row of disjoint stretches — each new
# interval just swallows every stretch it
# touches and the total is the sum of what
# is left standing.

import bisect


class CountIntervals:
    def __init__(self):
        self.intervals = []
        self.total = 0

    def add(self, left: int, right: int) -> None:
        intervals = self.intervals
        i = bisect.bisect_left(intervals, left, key=lambda iv: iv[0])
        if i > 0 and intervals[i - 1][1] >= left - 1:
            i -= 1
        new_l, new_r = left, right
        j = i
        while j < len(intervals) and intervals[j][0] <= new_r + 1:
            new_l = min(new_l, intervals[j][0])
            new_r = max(new_r, intervals[j][1])
            self.total -= intervals[j][1] - intervals[j][0] + 1
            j += 1
        del intervals[i:j]
        intervals.insert(i, [new_l, new_r])
        self.total += new_r - new_l + 1

    def count(self) -> int:
        return self.total
