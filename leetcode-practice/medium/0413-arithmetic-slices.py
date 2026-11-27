# LeetCode 413. Arithmetic Slices — Medium
# https://leetcode.com/problems/arithmetic-slices/
# Submission 2198783264 — Accepted, Python3
#
# My thinking: I walk the array keeping the length
# of the current run with the same step. Every time
# the step continues, the run grows by one, and
# that adds one new slice ending here for each
# earlier starting point in the run.

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        run = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                run += 1
                total += run
            else:
                run = 0
        return total
