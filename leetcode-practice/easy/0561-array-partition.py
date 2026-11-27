# LeetCode 561. Array Partition — Easy
# https://leetcode.com/problems/array-partition/
# Submission 2197497804 — Accepted, Python3
#
# My thinking: to make the sum of the smaller number
# in each pair as big as possible, I sort the array
# and pair neighbours together. Then the smaller
# one of each pair is every second number starting
# from the first.

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])
