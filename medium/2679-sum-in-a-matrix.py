# LeetCode 2679. Sum in a Matrix — Medium
# https://leetcode.com/problems/sum-in-a-matrix/
# Submission 2197817396 — Accepted, Python3
#
# My thinking: sorting each row from largest to
# smallest lines up the values so each round takes
# the biggest remaining value of every row. I add
# up the biggest value of each column.

from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        total = 0
        for j in range(len(nums[0])):
            total += max(row[j] for row in nums)
        return total
