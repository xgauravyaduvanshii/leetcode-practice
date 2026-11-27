# LeetCode 2054. Two Best Non-Overlapping Events — Medium
# https://leetcode.com/problems/two-best-non-overlapping-events/
# Submission 2204385372 — Accepted, Python3
#
# My thinking: sort the events by start time and build a suffix array
# of the best value from each position onward. For each event I take
# it alone, then binary-search the first event starting after it ends
# and add the best suffix value from there. The maximum over all
# events is the answer.
from bisect import bisect_right


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort()
        starts = [e[0] for e in events]
        n = len(events)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i + 1], events[i][2])
        ans = 0
        for s, e, v in events:
            ans = max(ans, v)
            j = bisect_right(starts, e)
            if j < n:
                ans = max(ans, v + suffix[j])
        return ans
