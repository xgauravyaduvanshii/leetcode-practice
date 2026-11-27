# LeetCode 354. Russian Doll Envelopes — Hard
# https://leetcode.com/problems/russian-doll-envelopes/
# Submission 2198407934 — Accepted, Python3
#
# My thinking: I sort by width, and for equal widths
# I put the taller envelope first so two envelopes
# of the same width can never end up nested. Then
# the problem is just the longest strictly rising
# run of heights, which I build with binary search
# over the smallest possible tail for each length.

import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        tails = []
        for _, height in envelopes:
            pos = bisect.bisect_left(tails, height)
            if pos == len(tails):
                tails.append(height)
            else:
                tails[pos] = height
        return len(tails)
