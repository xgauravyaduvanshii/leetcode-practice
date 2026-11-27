# LeetCode 34. Find First and Last Position of Element in Sorted Array — Medium
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Submission 2201079114 — Accepted, Python3
#
# My thinking: I binary-search twice — once for the
# first spot the target could sit in, and once for the
# spot just past its last one.

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def leftmost(value):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < value:
                    left = mid + 1
                else:
                    right = mid
            return left
        first = leftmost(target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        return [first, leftmost(target + 1) - 1]
