# LeetCode 2406. Divide Intervals Into Minimum Number of Groups — Medium
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
# Submission 2204788709 — Accepted, Python3
#
# My thinking: turn each interval into two events — +1 at its start,
# -1 just past its end — and sweep them in order. The running count is
# how many intervals overlap at that point, and its peak is the number
# of groups needed (overlapping intervals must go in different groups).
class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort()
        cur = 0
        ans = 0
        for _, d in events:
            cur += d
            if cur > ans:
                ans = cur
        return ans
