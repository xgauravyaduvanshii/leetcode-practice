# LeetCode 2251. Number of Flowers in Full Bloom — Hard
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/
# Submission 2201637845 — Accepted, Python3
#
# My thinking: a flower counts at a moment
# if it has opened but not yet closed — so
# I sort the openings and the closings and
# take opened minus closed for each arrival.

import bisect


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts = sorted(f[0] for f in flowers)
        ends = sorted(f[1] for f in flowers)
        ans = []
        for t in people:
            started = bisect.bisect_right(starts, t)
            ended = bisect.bisect_left(ends, t)
            ans.append(started - ended)
        return ans
