# LeetCode 540. Single Element in a Sorted Array — Medium
# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Submission 2198859804 — Accepted, Python3
#
# My thinking: before the single element, pairs
# start on even positions; after it, they start on
# odd ones. A binary search on that shift finds the
# one element without a partner.

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
