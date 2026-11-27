# LeetCode 1685. Sum of Absolute Differences in a Sorted Array — Medium
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
# Submission 2199909699 — Accepted, Python3
#
# My thinking: the array is sorted, so every
# element's total is its distance to the
# smaller ones plus its distance to the bigger
# ones. Prefix sums give me both sides in one
# pass.

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        result = []
        for i, value in enumerate(nums):
            right_sum = total - left_sum - value
            result.append(value * i - left_sum + right_sum - value * (len(nums) - i - 1))
            left_sum += value
        return result
