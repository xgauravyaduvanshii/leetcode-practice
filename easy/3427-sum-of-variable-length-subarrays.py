# 3427. Sum of Variable Length Subarrays (Easy)
# https://leetcode.com/problems/sum-of-variable-length-subarrays/
# Submission 2200015113 — Accepted, Python3
from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # My thinking: for each spot I add up the
        # numbers from nums[i] steps back — or from the
        # start if that goes past it — up to the spot
        # itself. All those little sums added together
        # are the answer.
        total = 0
        for i, num in enumerate(nums):
            start = max(0, i - num)
            total += sum(nums[start:i + 1])
        return total
