# LeetCode 1775. Equal Sum Arrays With Minimum Number of Operations — Medium
# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
# Submission 2199933080 — Accepted, Python3
#
# My thinking: I only ever need to shrink the
# bigger sum. Every change buys a fixed gain,
# so I take the biggest gains first until the
# gap closes — or give up if even all of them
# are not enough.

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        total1 = sum(nums1)
        total2 = sum(nums2)
        if total1 == total2:
            return 0
        if total1 < total2:
            nums1, nums2 = nums2, nums1
            total1, total2 = total2, total1
        diff = total1 - total2
        gains = sorted([value - 1 for value in nums1] + [6 - value for value in nums2], reverse=True)
        operations = 0
        for gain in gains:
            diff -= gain
            operations += 1
            if diff <= 0:
                return operations
        return -1
