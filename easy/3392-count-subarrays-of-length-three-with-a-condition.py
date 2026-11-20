# 3392. Count Subarrays of Length Three With a Condition (Easy)
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
# Submission 2200009814 — Accepted, Python3
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # My thinking: a triple counts when the first
        # and last add up to exactly half the middle
        # one — so I double their sum and compare it
        # with the middle value, avoiding fractions.
        return sum(
            1
            for i in range(len(nums) - 2)
            if 2 * (nums[i] + nums[i + 2]) == nums[i + 1]
        )
