# LeetCode 2760. Longest Even Odd Subarray With Threshold — Easy
# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/
# Submission 2198360198 — Accepted, Python3
#
# My thinking: a good stretch must start with an
# even number, stay under the threshold, and flip
# parity at every step. I walk through the array
# keeping the length of the current stretch. A
# number over the threshold breaks it, an odd
# number can only extend a stretch that is already
# going, and an even number either starts a fresh
# stretch or extends one that ended on an odd.

from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        best = 0
        current = 0
        for i, value in enumerate(nums):
            if value > threshold:
                current = 0
            elif value % 2 == 0:
                if current > 0 and nums[i - 1] % 2 == 1:
                    current += 1
                else:
                    current = 1
            else:
                if current > 0 and nums[i - 1] % 2 == 0:
                    current += 1
                else:
                    current = 0
            best = max(best, current)
        return best
