# LeetCode 1493. Longest Subarray of 1's After Deleting One Element — Medium
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Submission 2199863874 — Accepted, Python3
#
# My thinking: I slide a window holding at
# most one zero. Its length minus the one
# deleted element is the answer — even when
# the array is all ones, one still has to go.

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        best = 0
        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left)
        return best
