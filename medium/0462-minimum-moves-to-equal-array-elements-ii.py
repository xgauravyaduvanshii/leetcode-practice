# LeetCode 462. Minimum Moves to Equal Array Elements II — Medium
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Submission 2198808294 — Accepted, Python3
#
# My thinking: the cheapest target is the median —
# moving it either way only adds distance. I sort,
# take the middle value, and add up how far every
# number has to travel.

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)
