# LeetCode 2089. Find Target Indices After Sorting Array — Easy
# https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Submission 2197612356 — Accepted, Python3
#
# My thinking: I sort the array first, then collect
# every index where the value equals the target.

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, x in enumerate(nums) if x == target]
