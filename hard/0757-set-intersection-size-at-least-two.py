# LeetCode 757. Set Intersection Size At Least Two — Hard
# https://leetcode.com/problems/set-intersection-size-at-least-two/
# Submission 2198673380 — Accepted, Python3
#
# My thinking: I handle the intervals in order of
# their right end, so every decision is final. For
# each interval I count how many points I already
# have inside it and top it up to two with the
# rightmost free points — the end, then the end
# minus one — which leaves the most room for the
# intervals still to come.

from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        picked = []
        for start, end in intervals:
            inside = [p for p in picked if start <= p <= end]
            if len(inside) >= 2:
                continue
            if len(inside) == 1:
                picked.append(end if inside[0] != end else end - 1)
            else:
                picked.append(end - 1)
                picked.append(end)
            picked.sort()
        return len(picked)
