# LeetCode 1664. Ways to Make a Fair Array — Medium
# https://leetcode.com/problems/ways-to-make-a-fair-array/
# Submission 2199906125 — Accepted, Python3
#
# My thinking: removing one element flips
# the parity of everything after it. I keep
# the even and odd sums on both sides and
# check each removal against them.

from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = sum(nums[0::2])
        total_odd = sum(nums[1::2])
        left_even = 0
        left_odd = 0
        count = 0
        for i, value in enumerate(nums):
            if i % 2 == 0:
                total_even -= value
            else:
                total_odd -= value
            if left_even + total_odd == left_odd + total_even:
                count += 1
            if i % 2 == 0:
                left_even += value
            else:
                left_odd += value
        return count
