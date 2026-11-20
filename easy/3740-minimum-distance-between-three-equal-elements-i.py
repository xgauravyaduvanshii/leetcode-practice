# 3740. Minimum Distance Between Three Equal Elements I (Easy)
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
# Submission 2200058390 — Accepted, Python3
from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # My thinking: for three spots i, j and k in
        # order, the distance works out to twice the
        # gap from the first to the last. So for each
        # value I only need its closest three
        # appearances in a row.
        spots = defaultdict(list)
        for i, x in enumerate(nums):
            spots[x].append(i)
        best = None
        for idxs in spots.values():
            for t in range(len(idxs) - 2):
                gap = 2 * (idxs[t + 2] - idxs[t])
                if best is None or gap < best:
                    best = gap
        return -1 if best is None else best
