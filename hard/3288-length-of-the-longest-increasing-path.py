# LeetCode 3288. Length of the Longest Increasing Path — Hard
# https://leetcode.com/problems/length-of-the-longest-increasing-path/
# Submission 2202182373 — Accepted, Python3
#
# My thinking: any increasing path through
# coordinates[k] is an increasing chain before
# it plus one plus an increasing chain after
# it. The two sides are independent, and each
# side's longest chain is a plain LIS on the
# y-values after sorting by x (ties broken by
# y descending so equal x never chains).

from bisect import bisect_left
from typing import List


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        xk, yk = coordinates[k]

        def lis(pts):
            pts.sort(key=lambda p: (p[0], -p[1]))
            tails = []
            for _, y in pts:
                i = bisect_left(tails, y)
                if i == len(tails):
                    tails.append(y)
                else:
                    tails[i] = y
            return len(tails)

        before = [p for p in coordinates if p[0] < xk and p[1] < yk]
        after = [p for p in coordinates if p[0] > xk and p[1] > yk]
        return lis(before) + 1 + lis(after)
