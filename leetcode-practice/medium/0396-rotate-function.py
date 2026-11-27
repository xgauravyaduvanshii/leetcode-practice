# LeetCode 396. Rotate Function — Medium
# https://leetcode.com/problems/rotate-function/
# Submission 2198774805 — Accepted, Python3
#
# My thinking: rotating the array shifts every
# index by one, so the value changes by a fixed
# amount — the total sum minus n times the element
# that wraps around. I walk all rotations with that
# update and keep the best.

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        value = sum(i * num for i, num in enumerate(nums))
        best = value
        for i in range(n - 1, 0, -1):
            value += total - n * nums[i]
            best = max(best, value)
        return best
