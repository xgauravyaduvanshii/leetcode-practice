# LeetCode 1658. Minimum Operations to Reduce X to Zero — Medium
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Submission 2199902498 — Accepted, Python3
#
# My thinking: removing from the ends to reach
# x leaves the longest middle subarray that
# sums to the rest. I find that longest window
# with a sliding window and subtract its length.

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        left = 0
        current = 0
        longest = -1
        for right, value in enumerate(nums):
            current += value
            while current > target:
                current -= nums[left]
                left += 1
            if current == target:
                longest = max(longest, right - left + 1)
        return len(nums) - longest if longest != -1 else -1
