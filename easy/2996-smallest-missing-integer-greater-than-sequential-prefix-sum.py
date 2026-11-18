# LeetCode 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum — Easy
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# Submission 2198713755 — Accepted, Python3
#
# My thinking: I add up the sequential run at the
# start — 1, 2, 3 and so on — and then look for the
# smallest number at or above that sum that does not
# appear anywhere in the array.

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
        seen = set(nums)
        missing = prefix_sum
        while missing in seen:
            missing += 1
        return missing
