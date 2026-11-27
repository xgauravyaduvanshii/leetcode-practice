# 3633. Earliest Finish Time for Land and Water Rides I (Easy)
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
# Submission 2200033846 — Accepted, Python3
from typing import List


class Solution:
    def earliestFinishTime(self, landStart: List[int], landDuration: List[int], waterStart: List[int], waterDuration: List[int]) -> int:
        # My thinking: take the land ride that finishes
        # earliest. After that, each water ride can
        # start at its own start time or when the land
        # ride ends, whichever is later — the earliest
        # finish among them is the answer.
        land_finish = min(s + d for s, d in zip(landStart, landDuration))
        return min(max(ws, land_finish) + wd for ws, wd in zip(waterStart, waterDuration))
