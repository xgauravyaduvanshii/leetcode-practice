# LeetCode 1365. How Many Numbers Are Smaller Than the Current Number — Easy
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Submission 2197573149 — Accepted, Python3
#
# My thinking: in a sorted copy of the array, the
# first position where a number appears tells me
# how many numbers are smaller than it. So I note
# that first position for each distinct value, then
# look it up for every number in the original order.

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        first_index = {}
        for i, num in enumerate(sorted_nums):
            if num not in first_index:
                first_index[num] = i
        return [first_index[num] for num in nums]
