# LeetCode 2824. Count Pairs Whose Sum is Less than Target — Easy
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
# Submission 2198416716 — Accepted, Python3
#
# My thinking: I sort the numbers and take one from
# each end. If the pair is already under the target,
# every number between the left pointer and the
# right one pairs with the left one too, so I count
# them all and move the left pointer on. Otherwise
# the pair is too big and the right pointer moves
# in.

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
