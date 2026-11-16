# LeetCode 1827. Minimum Operations to Make the Array Increasing — Easy
# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
# Submission 2197600180 — Accepted, Python3
#
# My thinking: I go left to right and fix each
# position as I reach it. If a number is not bigger
# than the one before it, I bump it up to exactly
# one more than its neighbour — the cheapest fix —
# and count those bumps.

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                diff = nums[i - 1] - nums[i] + 1
                nums[i] += diff
                ops += diff
        return ops
