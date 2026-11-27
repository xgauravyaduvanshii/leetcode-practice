# LeetCode 1838. Frequency of the Most Frequent Element — Medium
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
# Submission 2199945904 — Accepted, Python3
#
# My thinking: after sorting, any window can
# be raised to its biggest element if the
# operations it needs fit the budget. I slide
# the window, keeping the cheapest one that
# still fits.

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        best = 1
        for right in range(len(nums)):
            total += nums[right]
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best
