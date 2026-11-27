# LeetCode 910. Smallest Range II — Medium
# https://leetcode.com/problems/smallest-range-ii/
# Submission 2198966810 — Accepted, Python3
#
# My thinking: after sorting, the split point is
# the only choice — everything up to it goes up
# by k and the rest goes down. I try every split
# and keep the smallest range I can make.

from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        best = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            best = min(best, high - low)
        return best
