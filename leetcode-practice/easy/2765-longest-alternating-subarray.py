# LeetCode 2765. Longest Alternating Subarray — Easy
# https://leetcode.com/problems/longest-alternating-subarray/
# Submission 2198360740 — Accepted, Python3
#
# My thinking: I only care about the gaps between
# neighbours, which must be +1, -1, +1, -1 and so
# on. I keep the length of the current alternating
# stretch and the last gap I saw. When the next gap
# is the same as the last one, a fresh stretch of
# two starts there instead; any other gap restarts
# the stretch completely.

from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        best = 1
        current = 1
        last_gap = 0
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i - 1]
            if gap == 1 and last_gap != 1:
                current += 1
                last_gap = 1
            elif gap == -1 and last_gap != -1:
                current += 1
                last_gap = -1
            elif gap == 1 or gap == -1:
                current = 2
                last_gap = gap
            else:
                current = 1
                last_gap = 0
            best = max(best, current)
        return best
