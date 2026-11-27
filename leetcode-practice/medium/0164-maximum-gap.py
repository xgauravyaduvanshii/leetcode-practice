# LeetCode 164. Maximum Gap — Medium
# https://leetcode.com/problems/maximum-gap/
# Submission 2198432501 — Accepted, Python3
#
# My thinking: once the numbers are sorted, the
# biggest gap can only sit between two neighbours
# — any wider pair has a neighbour gap inside it
# that is at most as big. So I sort and scan the
# neighbours once, keeping the largest difference.

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        return max(b - a for a, b in zip(nums, nums[1:]))
