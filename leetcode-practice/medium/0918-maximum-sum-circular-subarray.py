# LeetCode 918. Maximum Sum Circular Subarray — Medium
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Submission 2198969342 — Accepted, Python3
#
# My thinking: the best wrap-around subarray is
# everything except the worst middle part. I
# find the best and worst ordinary subarrays in
# one pass — unless every number is negative,
# when the best ordinary one is the answer.

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        current_max = best = nums[0]
        current_min = worst = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)
            best = max(best, current_max)
            worst = min(worst, current_min)
        if best < 0:
            return best
        return max(best, total - worst)
