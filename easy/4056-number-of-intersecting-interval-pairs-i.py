# 4056. Number of Intersecting Interval Pairs I (Easy)
# https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/
# Submission 2200100690 — Accepted, Python3
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        # My thinking: two closed intervals meet when
        # the later start is no bigger than the
        # earlier end — even a shared endpoint counts.
        # I check every pair.
        ans = 0
        n = len(intervals)
        for i in range(n):
            for j in range(i + 1, n):
                if max(intervals[i][0], intervals[j][0]) <= min(intervals[i][1], intervals[j][1]):
                    ans += 1
        return ans
