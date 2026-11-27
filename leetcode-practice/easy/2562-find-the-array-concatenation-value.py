# LeetCode 2562. Find the Array Concatenation Value — Easy
# https://leetcode.com/problems/find-the-array-concatenation-value/
# Submission 2197802777 — Accepted, Python3
#
# My thinking: I take the first and last remaining
# numbers, join their digits into one number, and
# add it to the total. If one number is left in the
# middle, I add it as it is.

from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        i, j = 0, len(nums) - 1
        while i < j:
            total += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        if i == j:
            total += nums[i]
        return total
