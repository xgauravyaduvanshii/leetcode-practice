# LeetCode 1909. Remove One Element to Make the Array Strictly Increasing — Easy
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
# Submission 2197604113 — Accepted, Python3
#
# My thinking: I try removing each element in turn
# and check whether what is left is strictly
# increasing. If any single removal works, the
# answer is true.

class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        def strictly_increasing(arr):
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
        for i in range(len(nums)):
            if strictly_increasing(nums[:i] + nums[i + 1:]):
                return True
        return False
