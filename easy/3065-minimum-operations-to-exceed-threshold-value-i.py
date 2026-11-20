# 3065. Minimum Operations to Exceed Threshold Value I (Easy)
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
# Submission 2199973125 — Accepted, Python3
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # My thinking: every number below the threshold
        # needs one operation to reach it, and numbers
        # already at or above it need none — so the
        # answer is just how many fall short.
        return sum(1 for num in nums if num < k)
