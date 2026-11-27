# LeetCode 213. House Robber II — Medium
# https://leetcode.com/problems/house-robber-ii/
# Submission 2198454681 — Accepted, Python3
#
# My thinking: the houses form a circle, so the
# first and last houses cannot both be robbed. I
# solve the straight-line version twice — once
# skipping the first house and once skipping the
# last — and take the better of the two. The
# straight-line version keeps only the best haul
# up to the previous two houses.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses: List[int]) -> int:
            prev2 = prev1 = 0
            for num in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
