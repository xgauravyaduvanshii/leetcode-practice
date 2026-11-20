# LeetCode 1695. Maximum Erasure Value — Medium
# https://leetcode.com/problems/maximum-erasure-value/
# Submission 2199913962 — Accepted, Python3
#
# My thinking: the best subarray has no
# repeats, so I slide a window and drop from
# the left whenever a value repeats, tracking
# the biggest window sum I see.

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        current = 0
        best = 0
        for right, value in enumerate(nums):
            while value in seen:
                seen.remove(nums[left])
                current -= nums[left]
                left += 1
            seen.add(value)
            current += value
            best = max(best, current)
        return best
