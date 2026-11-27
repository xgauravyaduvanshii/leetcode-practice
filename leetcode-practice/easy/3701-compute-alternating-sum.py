# 3701. Compute Alternating Sum (Easy)
# https://leetcode.com/problems/compute-alternating-sum/
# Submission 2200044959 — Accepted, Python3
from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        # My thinking: add the numbers in even spots
        # and subtract the ones in odd spots.
        return sum(num if i % 2 == 0 else -num for i, num in enumerate(nums))
