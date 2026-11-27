# LeetCode 436. Find Right Interval — Medium
# https://leetcode.com/problems/find-right-interval/
# Submission 2198794261 — Accepted, Python3
#
# My thinking: I sort all the start points once,
# then for each interval I binary-search the first
# start that is not before its end. That start's
# original index is the answer, or -1 when there is
# none.

import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, i) for i, (start, _) in enumerate(intervals))
        start_values = [start for start, _ in starts]
        result = []
        for _, end in intervals:
            position = bisect.bisect_left(start_values, end)
            result.append(starts[position][1] if position < len(starts) else -1)
        return result
