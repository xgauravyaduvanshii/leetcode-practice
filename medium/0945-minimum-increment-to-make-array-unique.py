# LeetCode 945. Minimum Increment to Make Array Unique — Medium
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Submission 2198973271 — Accepted, Python3
#
# My thinking: after sorting, every number only
# needs to be bigger than the one before it. I
# walk along and lift any number that is not,
# counting each lift as one move.

from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                moves += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return moves
