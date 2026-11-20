# 3423. Maximum Difference Between Adjacent Elements in a Circular Array (Easy)
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
# Submission 2200014787 — Accepted, Python3
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # My thinking: neighbours on a circle include
        # the last element next to the first. I check
        # every neighbouring pair and keep the biggest
        # gap between them.
        return max(
            abs(nums[i] - nums[(i + 1) % len(nums)]) for i in range(len(nums))
        )
