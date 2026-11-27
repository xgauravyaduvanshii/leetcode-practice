# LeetCode 376. Wiggle Subsequence — Medium
# https://leetcode.com/problems/wiggle-subsequence/
# Submission 2198764070 — Accepted, Python3
#
# My thinking: I only track the length of the best
# wiggle run ending with an upward step and the best
# ending with a downward step. An upward step
# extends the downward run, a downward step extends
# the upward run, and equal neighbours change
# nothing.

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
