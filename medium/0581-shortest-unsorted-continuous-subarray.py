# LeetCode 581. Shortest Unsorted Continuous Subarray — Medium
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Submission 2198874515 — Accepted, Python3
#
# My thinking: scanning from the left, the last
# place where the running maximum drops marks the
# right end of the mess; scanning from the right,
# the first place where the running minimum rises
# marks the left end. Everything between them is
# the subarray to sort.

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = len(nums)
        right = -1
        highest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < highest:
                right = i
            else:
                highest = nums[i]
        lowest = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > lowest:
                left = i
            else:
                lowest = nums[i]
        return max(0, right - left + 1)
