# LeetCode 1509. Minimum Difference Between Largest and Smallest Value in Three Moves — Medium
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# Submission 2199866348 — Accepted, Python3
#
# My thinking: three moves can only remove
# three numbers from the ends. I sort and try
# all four ways of splitting the removals
# between the small end and the large end.

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[i + len(nums) - 4] - nums[i] for i in range(4))
