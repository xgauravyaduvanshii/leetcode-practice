# 3674. Minimum Operations to Equalize Array (Easy)
# https://leetcode.com/problems/minimum-operations-to-equalize-array/
# Submission 2200042144 — Accepted, Python3
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # My thinking: one operation can set every
        # element to any value at once. So if the array
        # is already all equal, nothing is needed —
        # otherwise a single operation fixes it.
        return 0 if len(set(nums)) == 1 else 1
