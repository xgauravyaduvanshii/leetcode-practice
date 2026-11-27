# LeetCode 162. Find Peak Element — Medium
# https://leetcode.com/problems/find-peak-element/
# Submission 2200999955 — Accepted, Python3
#
# My thinking: I compare the middle with its right
# neighbour — if it is smaller, a peak must be on the
# right; otherwise one is on the left, including the
# middle itself.

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
