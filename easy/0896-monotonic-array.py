# LeetCode 896. Monotonic Array — Easy
# https://leetcode.com/problems/monotonic-array/
# Submission 2197540107 — Accepted, Python3
#
# My thinking: an array is monotonic if it only goes
# up or only goes down. I track both possibilities
# at once — a rise kills "only decreasing", a fall
# kills "only increasing". If either one survives
# the whole walk, it is monotonic.

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
        return increasing or decreasing
