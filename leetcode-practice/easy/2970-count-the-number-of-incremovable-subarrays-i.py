# LeetCode 2970. Count the Number of Incremovable Subarrays I — Easy
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
# Submission 2198705391 — Accepted, Python3
#
# My thinking: the array is tiny, so I try removing
# every possible subarray and check whether what is
# left is strictly increasing. Removing everything
# counts too — an empty array is increasing.

from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for start in range(n + 1):
            for end in range(start + 1, n + 1):
                remaining = nums[:start] + nums[end:]
                if all(
                    remaining[i] < remaining[i + 1]
                    for i in range(len(remaining) - 1)
                ):
                    count += 1
        return count
