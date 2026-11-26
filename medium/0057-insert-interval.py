# LeetCode 57. Insert Interval — Medium
# https://leetcode.com/problems/insert-interval/
# Submission 2203832298 — Accepted, Python3
#
# My thinking: I walk the intervals once, in three parts. First I copy
# every interval that ends before the new one starts. Then I merge the
# new interval with every interval it overlaps, stretching it to cover
# them all. Finally I copy the rest, which all start after the merged
# interval ends.

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
