# LeetCode 2855. Minimum Right Shifts to Sort the Array — Easy
# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/
# Submission 2198422928 — Accepted, Python3
#
# My thinking: a rotated sorted array has exactly
# one place where a number is bigger than the next
# one. If there is no such drop the array is already
# sorted; if there is more than one it can never be
# sorted by shifting. Otherwise the shift count is
# how far the sorted part sits from the end — and
# the last number must also be no bigger than the
# first, or the rotation would not line up.

from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        drop = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if drop != -1:
                    return -1
                drop = i
        if drop == -1:
            return 0
        if nums[-1] > nums[0]:
            return -1
        return n - (drop + 1)
