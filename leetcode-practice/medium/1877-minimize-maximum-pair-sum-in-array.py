# LeetCode 1877. Minimize Maximum Pair Sum in Array — Medium
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# Submission 2197602602 — Accepted, Python3
#
# My thinking: to keep the biggest pair sum as
# small as possible, I pair the smallest number
# with the largest one, the second smallest with
# the second largest, and so on. Sorting first and
# pairing the ends like that is optimal.

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[i] + nums[n - 1 - i] for i in range(n // 2))
