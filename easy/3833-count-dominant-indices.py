# 3833. Count Dominant Indices (Easy)
# https://leetcode.com/problems/count-dominant-indices/
# Submission 2200070794 — Accepted, Python3
from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        # My thinking: I walk from the right keeping
        # the sum of everything seen so far. An index
        # is dominant when its value beats the average
        # of everything to its right — checked without
        # fractions by multiplying instead of dividing.
        count = 0
        suffix = 0
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1 and nums[i] * (len(nums) - 1 - i) > suffix:
                count += 1
            suffix += nums[i]
        return count
