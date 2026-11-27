# 3678. Smallest Absent Positive Greater Than Average (Easy)
# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/
# Submission 2200042474 — Accepted, Python3
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        # My thinking: the answer must be bigger than
        # the average and missing from the array. I
        # start just above the average and walk upward
        # until I find a positive number that is not
        # there.
        present = set(nums)
        avg = sum(nums) / len(nums)
        x = max(1, int(avg) + 1)
        while x in present:
            x += 1
        return x
